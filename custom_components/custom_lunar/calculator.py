from datetime import datetime
from .Lunar import Lunar  # 引入自定义的农历计算库
from .Holiday import HolidayUtil  # 引入自定义的节日查询库

class LunarCalculator:
    def __init__(self):
        pass
    
    def get_current_lunar_info(self):
        """
        获取当前日期的农历信息并格式化输出。
        """
        now = datetime.now()
        
        # 使用Lunar库计算农历日期
        lunar_date = Lunar.fromDate(now)
        
        # 获取当天的农历年月日等信息
        lyear = lunar_date.getYearShengXiaoByLiChun()
        lmonth = lunar_date.getMonthInChinese()
        lday = lunar_date.getDayInChinese()
        time_ganzhi = lunar_date.getTimeInGanZhi()
        week = lunar_date.getWeekInChinese()
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
        chong_sha = f"冲{lunar_date.getDayChongDesc()} 煞{lunar_date.getDaySha()}"
        win_xing_na_year = lunar_date.getYearNaYin()
        wuxing_na_month = lunar_date.getMonthNaYin()
        wuxing_na_day = lunar_date.getDayNaYin()
        wu_xing_zhi_xing = f"{wuxing_na_day} {lunar_date.getZhiXing()}"
        ba_zi = lunar_date.getEightChar().toString()
        yi = lunar_date.getDayYi()
        ji = lunar_date.getDayJi()
        ji_shen = lunar_date.getDayJiShen()
        xiong_shen = lunar_date.getDayXiongSha()
        yue_xiang = lunar_date.getYueXiang()
        
        # 使用HolidayUtil库获取节日信息
        year = now.year
        month = now.month
        day = now.day
        get_holiday = HolidayUtil.getHoliday(year, month, day)
        
        # 组合输出信息
        lunar_data = {
            "Lunar": f"农历{lmonth}月{lday}",
            "Week": f"星期{week}",
            "NianGanZhi": f"{tian_gan_year}{lyear}年",
            "YueGanZhi": f"{tian_gan_month}月",
            "RiGanZhi": f"{tian_gan_day}日",
            "RiLu": day_lu,
            "JieQi": jie_qi._p.name if hasattr(jie_qi, '_p') else "",
            "DongFangXingXiu": f"{gong}方{xiu}{zheng}{animal}-{xin_luck}",
            "PengZuGan": peng_zu_gan,
            "PengZuZhi": peng_zu_zhi,
            "XiShen": xi_shen,
            "YangGui": yang_gui,
            "YinGui": yin_gui,
            "FuShen": fu_shen,
            "CaiShen": cai_shen,
            "TaiShen": tai_shen,
            "ChongSha": chong_sha,
            "WuXingNaYin": f"{win_xing_na_year} {wuxing_na_month} {wuxing_na_day}",
            "WuXingRi": wu_xing_zhi_xing + "执位",
            "BaZi": ba_zi,
            "Yi": "、".join(yi) if isinstance(yi, list) else yi,
            "Ji": "、".join(ji) if isinstance(ji, list) else ji,
            "JiShen": "、".join(ji_shen) if isinstance(ji_shen, list) else ji_shen,
            "XiongShen": "、".join(xiong_shen) if isinstance(xiong_shen, list) else xiong_shen,
            "YueXiang": f"{yue_xiang}月",
            "JiaQi": get_holiday._p.name if get_holiday else "工作日",
        }
        
        return lunar_data
