from homeassistant.components.sensor import SensorEntity, SensorDeviceClass
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, ServiceCall
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.event import async_track_time_change
from homeassistant.helpers.restore_state import RestoreEntity
from .const import DOMAIN, UPDATE_LUNAR_SERVICE
from .calculator import LunarCalculator

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback):
    """Set up the Lunar Sensor based on a config entry."""
    lunar_calculator = LunarCalculator()
    lunar_data = lunar_calculator.get_current_lunar_info()
    async_add_entities([LunarSensor(lunar_data)], True)
    # 注册手动更新服务
    hass.services.async_register(DOMAIN, UPDATE_LUNAR_SERVICE, async_update_lunar_sensor, schema=UPDATE_LUNAR_SERVICE_SCHEMA)

async def async_update_lunar_sensor(service: ServiceCall):
    """Service to manually update the lunar sensor."""
    entity_id = service.data.get('entity_id')
    if entity_id:
        entity = hass.states.get(entity_id)
        if entity is not None and entity.domain == 'sensor':
            # 这里需要根据实际情况调用实体的更新逻辑
            # 由于我们还没有实现传感器的实体ID获取，这里仅示意
            pass

class LunarSensor(SensorEntity, RestoreEntity):
    def __init__(self, lunar_data):
        super().__init__()
        self._attr_name = "Lunar Date"
        self._attr_device_class = SensorDeviceClass.DATE  # 可选，根据需要设置设备类别
        self._lunar_data = lunar_data
        self._attr_native_value = lunar_data["Lunar"]
        self._update_scheduled = False  # 用于跟踪是否已计划更新

    async def async_added_to_hass(self):
        """Run when entity about to be added to Home Assistant."""
        await super().async_added_to_hass()
        # 每天自动更新一次
        async_track_time_change(self.hass, self._update_daily, hour=0, minute=0, second=0)

    @property
    def extra_state_attributes(self):
        """Return the state attributes."""
        return {
            "Week": self._lunar_data["Week"],
            "NianGanZhi": self._lunar_data["NianGanZhi"],
            "YueGanZhi": self._lunar_data["YueGanZhi"],
            "RiGanZhi": self._lunar_data["RiGanZhi"],
            "RiLu": self._lunar_data["RiLu"],
            "JieQi": self._lunar_data["JieQi"],
            "DongFangXingXiu": self._lunar_data["DongFangXingXiu"],
            "PengZuGan": self._lunar_data["PengZuGan"],
            "PengZuZhi": self._lunar_data["PengZuZhi"],
            "XiShen": self._lunar_data["XiShen"],
            "YangGui": self._lunar_data["YangGui"],
            "YinGui": self._lunar_data["YinGui"],
            "FuShen": self._lunar_data["FuShen"],
            "CaiShen": self._lunar_data["CaiShen"],
            "TaiShen": self._lunar_data["TaiShen"],
            "ChongSha": self._lunar_data["ChongSha"],
            "WuXingNaYin": self._lunar_data["WuXingNaYin"],
            "WuXingRi": self._lunar_data["WuXingRi"],
            "BaZi": self._lunar_data["BaZi"],
            "Yi": self._lunar_data["Yi"],
            "Ji": self._lunar_data["Ji"],
            "JiShen": self._lunar_data["JiShen"],
            "XiongShen": self._lunar_data["XiongShen"],
            "YueXiang": self._lunar_data["YueXiang"],
          # "JiaQi": self._lunar_data["JiaQi"],
            "ShiChen": self._lunar_data.get("ShiChen", "未知"),
        }

    async def _update_daily(self, now):
        """Daily update at midnight."""
        await self.async_update_ha_state(True)

    async def async_update(self):
        """Update the sensor."""
        lunar_calculator = LunarCalculator()
        new_lunar_data = lunar_calculator.get_current_lunar_info()
        if new_lunar_data != self._lunar_data:
            self._lunar_data = new_lunar_data
            self.async_schedule_update_ha_state()
