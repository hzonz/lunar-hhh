# custom_components/custom_lunar/__init__.py

import asyncio
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import Config, HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady
from homeassistant.helpers.entity_component import EntityComponent
from .const import DOMAIN, PLATFORMS
from .sensor import CustomLunarSensor

async def async_setup(hass: HomeAssistant, config: Config):
    """Set up the custom_lunar component."""
    # Initialize the component even if no config entry is present
    hass.data.setdefault(DOMAIN, {})
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up this integration using UI."""
    # Ensure the component is set up
    if not hass.data.get(DOMAIN):
        await async_setup(hass, {})

    component = EntityComponent(_LOGGER, DOMAIN, hass, SCAN_INTERVAL=None)
    await component.async_setup_entry(entry)

    # Setup the sensor platform
    hass.async_create_task(async_setup_sensor_platform(hass, entry))
    return True

async def async_setup_sensor_platform(hass: HomeAssistant, entry: ConfigEntry):
    """Set up the sensor platform."""
    await asyncio.gather(
        hass.config_entries.async_forward_entry_setup(entry, "sensor"),
    )

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Unload a config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)
    return unload_ok

# The following line is important for Home Assistant to discover your platforms
PLATFORMS = ["sensor"]
