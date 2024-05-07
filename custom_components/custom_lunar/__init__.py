# custom_components/custom_lunar/__init__.py

import asyncio
from datetime import timedelta
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import Config, HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady
from homeassistant.helpers.event import async_track_time_interval
from .const import DOMAIN, PLATFORMS, DEFAULT_UPDATE_INTERVAL
from .sensor import CustomLunarSensor

# This function is called when Home Assistant starts
async def async_setup(hass: HomeAssistant, config: Config):
    """Set up this integration using YAML."""
    hass.data.setdefault(DOMAIN, {})
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up this integration using UI."""
    await async_setup_platforms(hass, entry)
    return True

async def async_setup_platforms(hass: HomeAssistant, entry: ConfigEntry):
    """Set up the sensor platform."""
    await asyncio.gather(
        hass.config_entries.async_forward_entry_setup(entry, "sensor"),
    )

async def async_migrate_entry(hass, config_entry):
    """Migrate old entry."""
    # Implement migration logic if needed (e.g., when updating from an older version)
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Handle removal of an entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)
    return unload_ok

async def async_reload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Reload the config entry."""
    await async_unload_entry(hass, entry)
    await async_setup_entry(hass, entry)

def update_lunar_sensors(hass, now):
    """Function to update lunar sensors."""
    entities = hass.data[DOMAIN].get("entities", [])
    for entity in entities:
        hass.async_create_task(entity.async_manual_update())

async def async_schedule_updates(hass, entry):
    """Schedule periodic updates."""
    interval = timedelta(seconds=entry.options.get("update_interval", DEFAULT_UPDATE_INTERVAL))
    update_listener = async_track_time_interval(hass, lambda now: update_lunar_sensors(hass, now), interval)
    hass.data[DOMAIN][entry.entry_id]["update_listener"] = update_listener

async def async_remove_updates(hass, entry):
    """Remove scheduled updates."""
    update_listener = hass.data[DOMAIN][entry.entry_id]["update_listener"]
    update_listener()

async def async_update_options(hass: HomeAssistant, entry: ConfigEntry):
    """Update options."""
    await async_remove_updates(hass, entry)
    await async_schedule_updates(hass, entry)

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up the Custom Lunar component from a config entry."""
    await async_schedule_updates(hass, entry)
    hass.async_create_task(async_setup_platforms(hass, entry))
    entry.async_on_unload(entry.add_update_listener(async_update_options))
    return True
