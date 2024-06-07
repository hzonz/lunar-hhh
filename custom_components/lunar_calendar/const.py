from datetime import timedelta

# Component Domain
DOMAIN = "lunar_calendar"

# Default configuration options
DEFAULT_SCAN_INTERVAL = timedelta(hours=1)  # 默认扫描间隔为1小时

# Configuration options
CONF_SCAN_INTERVAL = "scan_interval"

# Platforms
PLATFORMS = ["sensor"]
