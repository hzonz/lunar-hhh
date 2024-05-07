import datetime
import logging
import homeassistant.helpers.config_validation as cv
import voluptuous as vol
from homeassistant.const import CONF_NAME
from homeassistant.helpers.entity import Entity
from .lunar_calculator.Lunar import Lunar
from .lunar_calculator.Holiday import Holiday

async def async_setup(hass, config):
    """Set up the Lunar Calendar component."""
    async def handle_get_lunar_info(service):
        """Handle the get lunar info service."""
        now = datetime.datetime.now()
        lunar = Lunar()
        lunar_date = lunar.getLunar(now)
        holiday = Holiday().getHoliday(now.year, now.month, now.day)
        eight_char_string = str(lunar_date.getEightChar())

        response_data = {
            "LYear": lunar_date.getYearShengXiaoByLiChun(),
            "LMonth": lunar_date.getMonthInChinese(),
            "LDay": lunar_date.getDayInChinese(),
            "TimeInGanZhi": lunar_date.getTimeInGanZhi(),
            "Week": lunar_date.getWeekInChinese(),
            "LJie": lunar_date.getOtherFestivals(),  # 其他节日
            "TianGanYear": lunar_date.getYearInGanZhiExact(),
            "TianGanMonth": lunar_date.getMonthInGanZhiExact(),
            "TianGanDay": lunar_date.getDayInGanZhiExact(),
            "DayLu": lunar_date.getDayLu(),
            "JieQi": lunar_date.getPrevJieQi(True),  # 前一个节气
            "Xiu": lunar_date.getXiu(),
            "Animal": lunar_date.getAnimal(),
            "XinLuck": lunar_date.getXiuLuck(),
            "Zheng": lunar_date.getZheng(),
            "Gong": lunar_date.getGong(),
            "PengZuGan": lunar_date.getPengZuGan(),
            "PengZuZhi": lunar_date.getPengZuZhi(),
            "XiShen": lunar_date.getDayPositionXiDesc(),
            "YangGui": lunar_date.getDayPositionYangGuiDesc(),
            "YinGui": lunar_date.getDayPositionYinGuiDesc(),
            "FuShen": lunar_date.getDayPositionFuDesc(),
            "CaiShen": lunar_date.getDayPositionCaiDesc(),
            "TaiShen": lunar_date.getDayPositionTai(),
            "ChongSha": '冲' + lunar_date.getDayChongDesc() + ' 煞' + lunar_date.getDaySha(),
            "WinXingNaYear": lunar_date.getYearNaYin(),
            "WuxingNaMonth": lunar_date.getMonthNaYin(),
            "WuxingNaDay": lunar_date.getDayNaYin(),
            "WuXingZhiXing": lunar_date.getDayNaYin() + ' ' + lunar_date.getZhiXing(),
            "BaZi": eight_char_string,
            "Yi": lunar_date.getDayYi(),
            "Ji": lunar_date.getDayJi(),
            "JiShen": lunar_date.getDayJiShen(),
            "XiongShen": lunar_date.getDayXiongSha(),
            "YueXiang": lunar_date.getYueXiang(),
            "HolidayUtil": {
                "JiaQi": holiday
            }
        }

        _LOGGER.info("Lunar info: %s", response_data)

        # Call the service to send the data to Home Assistant
        await hass.services.async_call("custom_lunar", "lunar_info_updated", response_data)

    async def async_update_lunar_info_service(call):
        """Update lunar info service."""
        await handle_get_lunar_info(None)

    # Register the service
    hass.services.async_register(DOMAIN, "get_lunar_info", handle_get_lunar_info)

    # Set up a recurring call to update lunar info
    update_interval = datetime.timedelta(hours=1)
    hass.helpers.event.async_track_time_interval(async_update_lunar_info_service, update_interval)

    return True
