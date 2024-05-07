from lunar_calculator.Lunar import Lunar
from lunar_calculator.Holiday import HolidayUtil

def calculate_lunar_and_holiday():
    # 获取当前日期
    current_date = Lunar.fromDate(Lunar.getDate())
    
    # 获取农历信息
    lunar_data = {
        "LYear": current_date.getYearShengXiaoByLiChun(),
        "LMonth": current_date.getMonthInChinese(),
        "LDay": current_date.getDayInChinese(),
        "TimeInGanZhi": current_date.getTimeInGanZhi(),
        "Week": current_date.getWeekInChinese(),
        "LJie": current_date.getOtherFestivals(),
        "TianGanYear": current_date.getYearInGanZhiExact(),
        "TianGanMonth": current_date.getMonthInGanZhiExact(),
        "TianGanDay": current_date.getDayInGanZhiExact(),
        "DayLu": current_date.getDayLu(),
        "JieQi": current_date.getPrevJieQi(True),
        "Xiu": current_date.getXiu(),
        "Animal": current_date.getAnimal(),
        "XinLuck": current_date.getXiuLuck(),
        "Zheng": current_date.getZheng(),
        "Gong": current_date.getGong(),
        "PengZuGan": current_date.getPengZuGan(),
        "PengZuZhi": current_date.getPengZuZhi(),
        "XiShen": current_date.getDayPositionXiDesc(),
        "YangGui": current_date.getDayPositionYangGuiDesc(),
        "YinGui": current_date.getDayPositionYinGuiDesc(),
        "FuShen": current_date.getDayPositionFuDesc(),
        "CaiShen": current_date.getDayPositionCaiDesc(),
        "TaiShen": current_date.getDayPositionTai(),
        "ChongSha": '冲' + current_date.getDayChongDesc() + ' 煞' + current_date.getDaySha(),
        "WinXingNaYear": current_date.getYearNaYin(),
        "WuxingNaMonth": current_date.getMonthNaYin(),
        "WuxingNaDay": current_date.getDayNaYin(),
        "WuXingZhiXing": current_date.getDayNaYin() + ' ' + current_date.getZhiXing(),
        "BaZi": current_date.getEightChar().toString(),
        "Yi": current_date.getDayYi(),
        "Ji": current_date.getDayJi(),
        "JiShen": current_date.getDayJiShen(),
        "XiongShen": current_date.getDayXiongSha(),
        "YueXiang": current_date.getYueXiang(),
    }
    
    # 获取节日信息
    current_year = current_date.getYear()
    current_month = current_date.getMonth()
    current_day = current_date.getDay()
    holiday = HolidayUtil.getHoliday(current_year, current_month, current_day)
    
    return lunar_data, holiday
