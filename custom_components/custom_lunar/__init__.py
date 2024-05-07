"""The Lunar Calendar integration."""
from __future__ import annotations

import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.typing import ConfigType

from .const import (
    CONF_SCAN_INTERVAL,
    DEFAULT_SCAN_INTERVAL,
    DOMAIN,
    PLATFORMS,
    SERVICE_REFRESH,
    SERVICE_SCHEMA_REFRESH,
)
from .sensor import LunarSensor

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Lunar Calendar from a config entry."""
    hass.data.setdefault(DOMAIN, {})
    
    # Load configuration options
    scan_interval = entry.options.get(CONF_SCAN_INTERVAL, DEFAULT_SCAN_INTERVAL)
    
    # Setup sensor platform
    hass.async_create_task(
        hass.config_entries.async_forward_entry_setup(entry, Platform.SENSOR)
    )
    
    # Register service to refresh lunar data
    hass.services.async_register(
        DOMAIN, SERVICE_REFRESH, async_refresh_lunar_data, schema=SERVICE_SCHEMA_REFRESH
    )
    
    # Store options in hass.data for future reference or use
    hass.data[DOMAIN][entry.entry_id] = {
        "scan_interval": scan_interval,
    }

    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)
    return unload_ok

async def async_migrate_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool:
    """Migrate old entry."""
    _LOGGER.debug("Migrating from version %s", config_entry.version)
    # Implement migration logic here if needed
    config_entry.version = LATEST_VERSION  # Replace with actual latest version constant
    hass.config_entries.async_update_entry(config_entry)
    return True

async def async_refresh_lunar_data(hass: HomeAssistant, service_call: ServiceCall) -> None:
    """Handle the refresh lunar data service call."""
    # Here you would implement logic to refresh all or specific lunar sensors' data
    # For simplicity, let's assume we have a function to refresh all sensors
    # You need to implement this function based on your architecture
    await hass.async_add_executor_job(refresh_all_sensors)

def refresh_all_sensors():
    """Placeholder function to refresh all lunar sensors."""
    # Implement logic to refresh sensors here, if applicable
    # This is a placeholder and needs to be replaced with actual logic
    pass

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the Lunar Calendar component."""
    hass.data.setdefault(DOMAIN, {})
    return True

PLATFORMS = [Platform.SENSOR]
