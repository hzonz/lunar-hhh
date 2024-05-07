# custom_components/custom_lunar/lunar_date.py

def format_lunar_and_holiday_data(calculated_data):
    """
    Formats and organizes the calculated lunar and holiday data into a structured output.

    :param calculated_data: A dictionary containing raw lunar and holiday data.
    :return: A formatted dictionary ready for output.
    """
    lunar_data = calculated_data['Lunar']
    holiday_data = calculated_data['HolidayUtil']['JiaQi']

    # 分离数据中的每个字段并格式化
    lunar_output = f"农历{ lunar_data['LMonth']}月{ lunar_data['LDay']}"
    xingqi_output = f"星期{lunar_data['Week']}"
    nian_tian_gan_output = f"{lunar_data['TianGanYear']}年{ lunar_data['LYear']}"
    yue_tian_gan_output = f"{lunar_data['TianGanMonth']}月"
    ri_tian_gan_output = f"{lunar_data['TianGanDay']}日"
    xing_xiu_output = f"{lunar_data['Gong']}方{ lunar_data['Xiu']} {lunar_data['Zheng']} {lunar_data['Animal']}-{ lunar_data['XinLuck']}"
    wuxing_output = f"{ lunar_data['WuXingZhiXing']}执位"
    wuxing_nayin_output = f"{ lunar_data['WinXingNaYear']} {lunar_data['WuxingNaMonth']} {lunar_data['WuxingNaDay']}"
    yue_output = f"{ lunar_data['YueXiang']}月"

    # 处理宜忌等列表数据
    yi_string = '，'.join(lunar_data['Yi'])
    ji_string = '，'.join(lunar_data['Ji'])
    ji_shen_string = '，'.join(lunar_data['JiShen'])
    xiong_shen_string = '，'.join(lunar_data['XiongShen'])

    # 判断假期
    jia_qi_output = "工作日" if holiday_data is None else holiday_data._p.name or "工作日"

    # 构建输出对象
    output_msg = {
        "Lunar": lunar_output,
        "Week": xingqi_output,
        "NianGanZhi": nian_tian_gan_output,
        "YueGanZhi": yue_tian_gan_output,
        "RiGanZhi": ri_tian_gan_output,
        "RiLu": lunar_data['DayLu'],
        "JieQi": lunar_data['JieQi']._p.name if lunar_data['JieQi'] else "",
        "DongFangXingXiu": xing_xiu_output,
        "PengZuGan": lunar_data['PengZuGan'],
        "PengZuZhi": lunar_data['PengZuZhi'],
        "XiShen": lunar_data['XiShen'],
        "YangGui": lunar_data['YangGui'],
        "YinGui": lunar_data['YinGui'],
        "FuShen": lunar_data['FuShen'],
        "CaiShen": lunar_data['CaiShen'],
        "TaiShen": lunar_data['TaiShen'],
        "ChongSha": lunar_data['ChongSha'],
        "WuXingNaYin": wuxing_nayin_output,
        "WuXingRi": wuxing_output,
        "BaZi": lunar_data['BaZi'],
        "Yi": yi_string,
        "Ji": ji_string,
        "JiShen": ji_shen_string,
        "XiongShen": xiong_shen_string,
        "YueXiang": yue_output,
        "JiaQi": jia_qi_output
    }

    return output_msg
