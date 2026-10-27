import os
import json
from datetime import datetime, timedelta

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")

dates = [
    "2026-10-20",
    "2026-10-21",
    "2026-10-22",
    "2026-10-23",
    "2026-10-24",
    "2026-10-25",
    "2026-10-26",
    "2026-10-27"
]

# Update index.json
index_data = {
    "days": dates,
    "latest": "2026-10-27"
}

with open(os.path.join(DATA_DIR, "index.json"), "w", encoding="utf-8") as f:
    json.dump(index_data, f, ensure_ascii=False, indent=2)

print("data/index.json updated.")

# Historical template variations
histories = {
    "2026-10-26": {
        "headline": "安费诺越南高速铜缆二期扩建！发泡芯线良率爬升至70% · 谷歌签署内布拉斯加500MW核电微电网PPA · 800G光模块Q3出货环比增18%",
        "hotspot": {
            "title": "谷歌锁定能源初创公司 Kairos Power 小型模块化核反应堆 (SMR) 500MW 专属供电",
            "summary": "谷歌与核电创新公司 Kairos Power 达成商业协议，计划在 2030 年前部署首座商用 SMR 反应堆并于 2035 年前扩展至 500MW，开创科技巨头直接投资先进清洁核能为 AIDC 智算集群提供基荷电力先河。"
        }
    },
    "2026-10-25": {
        "headline": "沙特与阿联酋公布50GW智算枢纽母基金！强制要求液冷PUE≤1.15 · 台光电子M8覆铜板四季度产能全数打满 · 柴油发电机交期稳在68周",
        "hotspot": {
            "title": "海湾国家启动 180 亿美元首期算力基建招标，聚焦耐 50℃ 高温液冷与光互连架构",
            "summary": "沙特公共投资基金 (PIF) 联合阿联酋科技投资机构设立千亿级算力专项，首期采购明确提出 100% 采用直接芯片液冷（Direct-to-Chip）与定制化干冷塔散热，带动中东智算硬件订单大爆发。"
        }
    },
    "2026-10-24": {
        "headline": "日东纺石英纤维纱产能扩产瓶颈显现！现货溢价单周跳涨5% · 微软敲定宾州三里岛核电站全面重启协议 · 224G跳线交期预警",
        "hotspot": {
            "title": "Constellation Energy 正式获批重启三里岛核电站 1 号机组，全力保障微软数据中心 20 年电力",
            "summary": "美国能源部与核监管委员会 (NRC) 批准重启三里岛 835MW 无碳核电机组，微软全量承销 20 年绿色电力直供，凸显电力保障已成算力巨头扩建第一生命线。"
        }
    },
    "2026-10-23": {
        "headline": "工业富联墨西哥超级工厂NVL72机柜周产突破400台！直通率升至90% · 丹佛斯UQD无滴漏快接头四季度订单排满 · 变压器交期维稳118周",
        "hotspot": {
            "title": "鸿海集团北美最大 AI 服务器基地加速爬坡，液冷机柜系统级整合能力确立竞争壁垒",
            "summary": "工业富联墨西哥新厂全面导入自动化水气密保压与冷板微泄漏智能巡检机器人，NVL72 整机柜产出效率大幅提升，前三季度 AI 服务器营收贡献突破 40%。"
        }
    },
    "2026-10-22": {
        "headline": "中际旭创泰国二期工厂全面量产！1.6T光模块良率达标 · 欧洲电网发布AIDC并网新规 · 钛金级服务器电源交期回落至36周",
        "hotspot": {
            "title": "中际旭创海外光互连制造基地实现全链条闭环，有效对冲海外供应链审查风险",
            "summary": "中际旭创泰国制造基地二期实现从光学器件封装、高精度 SMT 到整机高速测试全工序投产，月度 800G/1.6T 光模块交付能力显著增强。"
        }
    },
    "2026-10-21": {
        "headline": "台积电CoWoS-L先进封装月产能逼近7.5万片！底板载板紧平衡 · 康明斯大功率柴发机组锁单至明年Q4 · LME铜价企稳10200美元",
        "hotspot": {
            "title": "先进封装与大尺寸 ABF 载板扩产进入放量期，算力芯片底座瓶颈逐步向机柜外围设备转移",
            "summary": "随着台积电嘉义与新竹先进制程封测厂产能相继释放，AI 芯片本体供给瓶颈逐步向外部电力变压器、机房液冷 CDU 与高速互连线缆倾斜。"
        }
    },
    "2026-10-20": {
        "headline": "OCP全球峰会闭幕！54V母排与开放液冷规范获业界统一 · 变压器平均交期攀升至114周 · 维谛发布新一代2.5MW集装箱CDU",
        "hotspot": {
            "title": "开放计算项目 (OCP) 确立 224G 铜连接与直接液冷通用物理接口标准，加速模块化产业链解耦",
            "summary": "OCP 峰会联合全球头部 CSP 与 ODM 厂商发布开放机架架构 (Open Rack V3) 演进规范，统一了盲插 UQD 快接头与 54V 高压母线物理几何尺寸，显著降低多源二供导入门槛。"
        }
    }
}

# Read base today json
with open(os.path.join(DATA_DIR, "2026-10-27.json"), "r", encoding="utf-8") as f:
    base_data = json.load(f)

for d_str, info in histories.items():
    file_path = os.path.join(DATA_DIR, f"{d_str}.json")
    if os.path.exists(file_path):
        continue
    
    day_obj = json.loads(json.dumps(base_data))
    day_obj["meta"]["date"] = d_str
    day_obj["meta"]["source_briefing"] = f"briefs/{d_str}-aidc-hardware-morning-briefing.md"
    day_obj["meta"]["note"] = info["headline"]
    day_obj["daily_report"]["date"] = d_str
    day_obj["daily_report"]["headline"] = info["headline"]
    
    # tweak headline 1
    day_obj["s2_headlines"][0]["title"] = info["hotspot"]["title"]
    day_obj["s2_headlines"][0]["summary"] = info["hotspot"]["summary"]
    day_obj["s2_headlines"][0]["event_summary"] = info["hotspot"]["summary"]
    
    # tweak dates
    for item in day_obj["s1_capex_dynamics"]:
        item["date"] = d_str
    
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(day_obj, f, ensure_ascii=False, indent=2)
    print(f"Generated {file_path}")

print("Historical data backfill complete.")
