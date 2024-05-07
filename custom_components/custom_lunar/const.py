# custom_components/custom_lunar/const.py

"""Constants for the Custom Lunar Calendar component."""

# Component domain
DOMAIN = "custom_lunar"

# Configuration constants
CONF_NAME = "lunar custom"  # 名称配置项，如果需要的话
CONF_UPDATE_INTERVAL = "update_interval"  # 更新间隔配置项，单位秒

# Default values
DEFAULT_NAME = "农历"
DEFAULT_UPDATE_INTERVAL = 7200  # 默认每天更新一次，即24小时

# Platforms within the component
PLATFORMS = ["sensor"]

# Sensor specific constants
SENSOR_TYPE_LUNAR_DATE = "lunar_date"
SENSOR_ICON = "mdi:calendar"

# Miscellaneous constants
SCAN_INTERVAL = DEFAULT_UPDATE_INTERVAL  # 传感器的刷新间隔，这里与默认更新间隔保持一致
