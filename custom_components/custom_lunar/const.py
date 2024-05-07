"""
Constants for the Lunar Calendar custom component.
"""

import voluptuous as vol
from datetime import timedelta

# Component Domain
DOMAIN = "lunar_calendar"

# Default configuration options
DEFAULT_SCAN_INTERVAL = timedelta(hours=1)  # 默认扫描间隔为1小时
CONF_CUSTOM_NAME = "custom_name"  # 自定义组件名称配置项
DEFAULT_CUSTOM_NAME = "农历日期"  # 自定义名称的默认值

# Services
SERVICE_REFRESH = "refresh_lunar_data"
SERVICE_SCHEMA_REFRESH = vol.Schema({})

# Icons
ICON_CALENDAR = "mdi:calendar"

# Configuration options
CONF_SCAN_INTERVAL = "scan_interval"


# Sensor attribute keys
ATTR_WEEK = "week"
ATTR_LUNAR_YEAR = "lunar_year"
ATTR_LUNAR_MONTH = "lunar_month"
ATTR_LUNAR_DAY = "lunar_day"
# ... 其他属性键，根据需要添加

# Additional constants as needed
# ...

# Platforms
PLATFORMS = ["sensor"]

# Services
UPDATE_LUNAR_SERVICE = "update_lunar_data"
