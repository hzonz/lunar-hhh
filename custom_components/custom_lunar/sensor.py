# custom_components/custom_lunar/sensor.py

from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity import DeviceInfo
from .const import DOMAIN, CONF_NAME
from .calculator import calculate_lunar_and_holiday_data  # 假设这是计算农历和节日数据的函数

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities):
    """Set up the lunar sensor based on a config entry."""
    name = entry.data.get(CONF_NAME)
    async_add_entities([CustomLunarSensor(hass, entry, name)])

class CustomLunarSensor(SensorEntity):
    def __init__(self, hass, entry, name):
        self.hass = hass
        self._entry = entry
        self._name = name
        self._state = None
        self._attributes = {}

    @property
    def unique_id(self):
        """Return a unique ID to use for this entity."""
        return f"{DOMAIN}_{self._entry.entry_id}_sensor"

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def native_value(self):
        """Return the state of the sensor."""
        # 假设calculate_lunar_and_holiday_data已提供完整的数据字典
        if self._state is None:
            self.update_lunar_data()
        return self._state.get('Lunar', '')

    @property
    def icon(self):
        """Return the icon to use in the frontend."""
        return "mdi:calendar"

    @property
    def extra_state_attributes(self):
        """Return the state attributes."""
        if not self._attributes:
            self.update_lunar_data()
        return self._attributes

    def update_lunar_data(self):
        """Fetch and update lunar and holiday data."""
        calculated_data = calculate_lunar_and_holiday_data()  # 调用计算函数
        if calculated_data:
            self._state = calculated_data.get('Lunar', '')
            # 移除 'Lunar' 项，因为它是传感器的 native_value
            formatted_data = calculated_data.copy()
            formatted_data.pop('Lunar', None)
            self._attributes = formatted_data

    async def async_update(self):
        """Update the sensor."""
        self.update_lunar_data()

    @property
    def device_info(self):
        """Return device information about this entity."""
        return DeviceInfo(identifiers={(DOMAIN, self.unique_id)}, name=self.name)


    async def async_manual_update(self):
    """Perform a manual update of the sensor's data."""
    self.update_lunar_data()
    self.async_write_ha_state()  # Notify Home Assistant of the state change
