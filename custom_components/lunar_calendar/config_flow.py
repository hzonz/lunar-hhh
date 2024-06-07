from __future__ import annotations
import logging
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback
import homeassistant.helpers.config_validation as cv
from .const import DOMAIN, CONF_SCAN_INTERVAL, DEFAULT_SCAN_INTERVAL

_LOGGER = logging.getLogger(__name__)

STEP_USER_DATA_SCHEMA = vol.Schema({
    vol.Optional(CONF_SCAN_INTERVAL, default=str(DEFAULT_SCAN_INTERVAL)): cv.time_period_str,
})

@callback
def async_get_options_flow(config_entry):
    """Handle an options flow for this integration."""
    return OptionsFlowHandler(config_entry)

class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Lunar Calendar."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        _LOGGER.debug("Starting user step for Lunar Calendar config flow.")
        errors = {}

        if user_input is not None:
            _LOGGER.debug("User input received: %s", user_input)
            return self.async_create_entry(title="农历日历", data=user_input)

        return self.async_show_form(
            step_id="user", data_schema=STEP_USER_DATA_SCHEMA, errors=errors
        )

class OptionsFlowHandler(config_entries.OptionsFlow):
    """Handle options flow for the component."""
    
    def __init__(self, config_entry):
        """Initialize options flow."""
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        """Manage options."""
        _LOGGER.debug("Starting options flow for Lunar Calendar config entry: %s", self.config_entry.entry_id)
        if user_input is not None:
            _LOGGER.debug("User input for options: %s", user_input)
            return self.async_create_entry(title="", data=user_input)

        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema({
                vol.Optional(CONF_SCAN_INTERVAL, default=str(self.config_entry.options.get(CONF_SCAN_INTERVAL, DEFAULT_SCAN_INTERVAL))): cv.time_period_str,
            }),
        )
