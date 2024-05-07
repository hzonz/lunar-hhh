# custom_components/custom_lunar/calculator.py

from datetime import datetime
from .lunar_calculator.Lunar import Lunar
from .lunar_calculator.HolidayUtil import HolidayUtil

def calculate_lunar_and_holiday_data():
    """
    Calculate and format lunar date and holiday information.
    Returns a dictionary with lunar details and holiday information.
    """
    # 获取当前日期
    current_date = datetime.now()

    # 创建Lunar对象并获取农历信息
    lunar_date = Lunar.fromDate(current_date)
    
    # 获取农历年生肖、月份、日期等信息
    lyear = lunar_date.getYearShengXiaoByLiChun()
    lmonth = lunar_date.getMonthInChinese()
    lday = lunar_date.getDayInChinese()
    time_ganzhi = lunar_date.getTimeInGanZhi()
    week_chinese = lunar_date.getWeekInChinese()
    ljie = lunar_date.getOtherFestivals()
    tian_gan_year = lunar_date.getYearInGanZhiExact()
    tian_gan_month = lunar_date.getMonthInGanZhiExact()
    tian_gan_day = lunar_date.getDayInGanZhiExact()
    day_lu = lunar_date.getDayLu()
    jie_qi = lunar_date.getPrevJieQi(True)
    xiu = lunar_date.getXiu()
    animal = lunar_date.getAnimal()
    xin_luck = lunar_date.getXiuLuck()
    zheng = lunar_date.getZheng()
    gong = lunar_date.getGong()
    peng_zu_gan = lunar_date.getPengZuGan()
    peng_zu_zhi = lunar_date.getPengZuZhi()
    xi_shen = lunar_date.getDayPositionXiDesc()
    yang_gui = lunar_date.getDayPositionYangGuiDesc()
    yin_gui = lunar_date.getDayPositionYinGuiDesc()
    fu_shen = lunar_date.getDayPositionFuDesc()
    cai_shen = lunar_date.getDayPositionCaiDesc()
    tai_shen = lunar_date.getDayPositionTai()
    chong_sha = '冲' + lunar_date.getDayChongDesc() + ' 煞' + lunar_date.getDaySha()
    win_xing_na_year = lunar_date.getYearNaYin()
    wuxing_na_month = lunar_date.getMonthNaYin()
    wuxing_na_day = lunar_date.getDayNaYin()
    wuxing_zhi_xing = lunar_date.getDayNaYin() + ' ' + lunar_date.getZhiXing()
    ba_zi = lunar_date.getEightChar().toString()
    yi = lunar_date.getDayYi()
    ji = lunar_date.getDayJi()
    ji_shen = lunar_date.getDayJiShen()
    xiong_shen = lunar_date.getDayXiongSha()
    yue_xiang = lunar_date.getYueXiang()

    # 获取节日信息
    year = current_date.year
    month = str(current_date.month)
    day = str(current_date.day)
    holiday = HolidayUtil.getHoliday(year, month, day)
    
    # 整理数据
    lunar_info = {
        "LYear": lyear,
        "LMonth": lmonth,
        "LDay": lday,
        "TimeInGanZhi": time_ganzhi,
        "Week": week_chinese,
        "LJie": ljie,
        "TianGanYear": tian_gan_year,
        "TianGanMonth": tian_gan_month,
        "TianGanDay": tian_gan_day,
        "DayLu": day_lu,
        "JieQi": jie_qi,
        "Xiu": xiu,
        "Animal": animal,
        "XinLuck": xin_luck,
        "Zheng": zheng,
        "Gong": gong,
        "PengZuGan": peng_zu_gan,
        "PengZuZhi": peng_zu_zhi,
        "XiShen": xi_shen,
        "YangGui": yang_gui,
        "YinGui": yin_gui,
        "FuShen": fu_shen,
        "CaiShen": cai_shen,
        "TaiShen": tai_shen,
        "ChongSha": chong_sha,
        "WinXingNaYear": win_xing_na_year,
        "WuxingNaMonth": wuxing_na_month,
        "WuxingNaDay": wuxing_na_day,
        "WuXingZhiXing": wuxing_zhi_xing,
        "BaZi": ba_zi,
        "Yi": yi,
        "Ji": ji,
        "JiShen": ji_shen,
        "XiongShen": xiong_shen,
        "YueXiang": yue_xiang,
    }
    
    # 组织最终返回数据
    response_data = {
        "Lunar": lunar_info,
        "HolidayUtil": {
            "JiaQi": holiday,
        },
    }
    
    return response_data
