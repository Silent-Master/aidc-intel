import json
import os

ROOT_DIR = r"E:\AI_Programing\HVAC"
DATA_DIR = os.path.join(ROOT_DIR, "data")

DAYS_DATA = {
    "2026-10-28": {
        "headline": "1.6T光模块硅光芯片与InP晶圆配额争夺加剧 · 微软与Constellation锁定20年核电直供协议 · 旭创与新易盛泰国工厂良率攀升至92%",
        "hotspot_count": 2,
        "warning_count": 5,
        "note": "1.6T 硅光方案渗透率超预期，磷化铟(InP)与连续波(CW)大功率光源进入关键保供期；微软20年核电PPA推动主权算力掀起绿电长协潮。",
        "portfolio_summary": {
            "liquid_cooling": {
                "positive": "中东及欧洲高密算力节点全面转向板式液冷，海外出海订单进入交付窗口。",
                "risk": "耐氟橡胶密封圈与自密封快接头(UQD)微米级公差严苛，局部批次出货稍有延阻。"
            },
            "optical_interconnect": {
                "positive": "1.6T 光模块批量采购启动，中际旭创、新易盛海外泰国基地良率稳定在92%以上，毛利率韧性显著。",
                "risk": "Lumentum与Coherent高功率CW激光光源产能被北美头部CSP长协锁单，二线模组厂外购光源溢价达25%。"
            },
            "pcb_racks": {
                "positive": "32层以上交换背板持续出货，工业富联与广达高密算力柜排产饱满。",
                "risk": "PTFE特种涂覆玻纤材料交期拉长至28周，板材损耗控制考验压合良率。"
            },
            "grid_power": {
                "positive": "核能与地热PPA直供模式确立，微电网中压变压器与中置柜出海需求激增，金盘科技订单排产至2027年。",
                "risk": "欧美本土电网并网测试排队未见缓解，调试工程师资源匮乏。"
            }
        },
        "s1_capex": [
            {
                "date": "2026-10-28",
                "title": "微软与 Constellation Energy 敲定 20 年核电直供 PPA，锁定三里岛 835MW 零碳电力",
                "fact": "微软正式向美国联邦能源监管委员会 (FERC) 递交最终电力直供协议，将三里岛核电站 1 号机组全部 835MW 发电量全额定向接入其位于弗吉尼亚与宾夕法尼亚的智算中心群，协议总值逾 160 亿美元。【SEC 文件口径】",
                "impact": "加速头部 CSP 摆脱公共电网并网排队（Queue）限制，同时促使高压并网与防孤岛保护开关设备需求爆发。",
                "source": "SEC Form 8-K / Reuters",
                "source_url": "https://www.sec.gov/edgar/searchedgar/companysearch",
                "related_tickers": ["MSFT 微软", "CEG 星座能源", "688676 金盘科技", "002922 伊戈尔"]
            },
            {
                "date": "2026-10-28",
                "title": "Meta 与亚马逊签署 1.6T 硅光互连模块联合研发与战略锁单长协",
                "fact": "Meta 与 AWS 联合向头部光模块供应商中际旭创、新易盛下发首批 1.6T OSFP/QSFP-DD-DR8 长期供货意向（LTA），首批锁定产能超过 180 万只，交付周期自 2027 年 Q1 起算。【厂商口径】",
                "impact": "1.6T 世代商用落地时点大幅前移，推动 200G EML 与硅光芯片集成方案成为互连层核心军备赛道。",
                "source": "LightCounting / Omdia Research",
                "source_url": "https://www.lightcounting.com/",
                "related_tickers": ["300308 中际旭创", "300502 新易盛", "300394 天孚通信"]
            },
            {
                "date": "2026-10-28",
                "title": "中国移动启动长三角枢纽 800G 全光全调度智算骨干网集采，标的金额超 42 亿元",
                "fact": "中国移动公示 2026-2027 年特种超低损耗 G.654.E 光纤及 800G OTN 传输设备集采中标候选人，总投资 42.6 亿元人民币，重点构建连通上海、苏州、杭州的国家算力枢纽低时延全光直达网。",
                "impact": "国内特种光纤光缆与大容量波分设备需求筑底回升，高功率 EDFA 光放大器进入快速上量期。",
                "source": "中国移动采购与招标网",
                "source_url": "https://b2b.10086.cn/",
                "related_tickers": ["600498 烽火通信", "600487 亨通光电", "601869 长飞光纤"]
            }
        ],
        "s2_headlines": [
            {
                "id": "evt-20261028-01",
                "title": "1.6T 硅光芯片核心大功率连续波 (CW) 光源产能告急，Lumentum 与 Coherent 配额锁死",
                "severity": "HIGH",
                "heat": 94,
                "summary": "随着 1.6T 光模块全面转向 SiPh (硅光) 与薄膜铌酸锂架构，外部外挂大功率 CW 激光器（100mW+）成为系统核心瓶颈。全球两大主要外延供应商 Lumentum 与 Coherent 产能已被北美两大算力主厂包揽 90% 以上，现货市场外购加价幅度突破 30%。",
                "key_takeaway": "CW大功率光源外延产能锁死至2027下半年，硅光模组出货节奏受制于单点光源供给。",
                "numbers": ["CW光源现货溢价 +30%", "头部主厂包揽产能 >90%", "外延片生长周期 16周"],
                "transmission_chain": {
                    "source_driver": "1.6T 交换机与 Scale-Up 智算集群密度翻倍，传统 EML 功耗与成本逼近极限",
                    "midstream_impact": "推动硅光光引擎方案爆发，外挂大功率 CW 激光器需求激增 3.5 倍",
                    "terminal_mapping": "缺乏自研光源能力的二线模组厂面临外购断供风险，中际旭创、新易盛等具备绑定优势的龙头份额进一步集中"
                },
                "bom_impact_path": ["光互连子系统", "1.6T 光模块", "硅光光引擎 (SiPh PIC)", "外挂 CW 激光器 (70mW-100mW)"],
                "delivery_forecast": {
                    "short_term": "非头部客户的小批量 1.6T 样品送样交期拉长至 24 周以上。",
                    "mid_term": "倒逼天孚通信等光器件精密封装厂商加速推进激光光源混合集成 (Hybrid Integration) 与国产外延认证。"
                },
                "related_tickers": ["300308 中际旭创", "300502 新易盛", "300394 天孚通信", "LITE 鲁门特姆", "COHR 高意"],
                "sources": [
                    {"outlet": "Yole Group Optoelectronics Quarterly", "date": "2026-10-27", "url": "https://www.yolegroup.com/", "first_party": False},
                    {"outlet": "Coherent Q3 Form 10-Q", "date": "2026-10-26", "url": "https://www.sec.gov/edgar/searchedgar/companysearch", "first_party": True}
                ]
            },
            {
                "id": "evt-20261028-02",
                "title": "中际旭创与新易盛泰国保税工厂二期达产，1.6T/800G 综合良品率突破 92%",
                "severity": "MEDIUM",
                "heat": 88,
                "summary": "国内光模块双雄位于泰国春武里及罗勇府的海外高阶智造基地全面通过北美核心 CSP 原厂审计认证。自动化高精贴片与耦合工序成熟，800G LPO 与 1.6T DR8 产线综合良品率稳定跨过 92% 关口，为规避原产地关税提供充足缓冲地带。【厂商口径】",
                "key_takeaway": "海外基地跨越良率爬坡死谷，海外直接出货能力增强，关税穿透风险明显钝化。",
                "numbers": ["综合良品率 92.4%", "泰国基地年产能达 450万只", "海外出货占比提至 65%"],
                "transmission_chain": {
                    "source_driver": "北美 CSP 采购合规强制要求非敏感原产地供应，分散地缘风险",
                    "midstream_impact": "加速国内头部光模块在东南亚完成从 SMT 到测试的全制程落地",
                    "terminal_mapping": "巩固海外头部客户第一大供应商份额，打消市场对海外设厂良率折损与成本上升的顾虑"
                },
                "bom_impact_path": ["光收发模块整机", "泰国生产线", "精密光学贴装机", "全温高速眼图测试系统"],
                "delivery_forecast": {
                    "short_term": "四季度海外直接交货量环比增长预计逾 35%，交付周期缩短 2 周。",
                    "mid_term": "带动上游天孚通信、太辰光等光无源精密器件厂商在泰国设立配套配套装配基地。"
                },
                "related_tickers": ["300308 中际旭创", "300502 新易盛", "300394 天孚通信", "300570 太辰光"],
                "sources": [
                    {"outlet": "TrendForce Global Tech Brief", "date": "2026-10-27", "url": "https://www.trendforce.com/", "first_party": False},
                    {"outlet": "公司官方自愿性信息披露", "date": "2026-10-26", "url": "http://www.cninfo.com.cn/", "first_party": True}
                ]
            }
        ],
        "s3_bottlenecks": [
            {
                "category": "光芯片与互连",
                "bottleneck_item": "100mW+ 高功率 CW 连续波激光器外延片",
                "supplier_monopoly": "Lumentum, Coherent, 索尔思光电",
                "lead_time_weeks": "38~44周",
                "lock_in_ratio": "91.5%",
                "analysis": "大功率外延片缺陷控制极难，高温老化失效率低于 100 FIT 标准的有效产能极为有限，头部 CSP 预付款全额锁库。",
                "source": "SemiAnalysis Optical Hardware Memo",
                "source_url": "https://www.semianalysis.com/",
                "related_tickers": ["300308 中际旭创", "300502 新易盛", "LITE 鲁门特姆"]
            },
            {
                "category": "板材与载板",
                "bottleneck_item": "ABF 载板高深宽比微盲孔激光打孔设备配额",
                "supplier_monopoly": "三菱电机 (Mitsubishi Electric)",
                "lead_time_weeks": "50~56周",
                "lock_in_ratio": "86.0%",
                "analysis": "先进封装芯片中介层及高阶载板要求孔径 <25μm，激光成孔设备交期维持近一年高位。",
                "source": "Prismark PCB Industry Report",
                "source_url": "https://www.prismark.com/",
                "related_tickers": ["002463 沪电股份", "600183 生益科技", "002475 立讯精密"]
            }
        ],
        "s4_cross_industry": [
            {
                "domain": "大宗与原料",
                "material": "高纯度金属铟 (99.999% In) 与磷化铟单晶",
                "price_trend": "现货报价环比上涨 6.8%",
                "transmission": "光通信芯片与高效异质结光伏电池双向抢原料，In 粗炼冶炼产能受环保限产制约，直接抬升衬底制造成本。",
                "impact_mag": "磷化铟晶圆单片成本增加约 45 美元",
                "source_url": "https://www.metal.com/"
            },
            {
                "domain": "电网设备",
                "material": "500kV 交流输电六氟化硫 (SF6) 气体绝缘开关设备 (GIS)",
                "price_trend": "交付周期延长至 75 周",
                "transmission": "风光大基地并网与算力中心双重抽水，高压断路器与 GIS 装备制造产能满产，引发交付排队延宕。",
                "impact_mag": "新建智算专属变电站整体土建后通电延迟 4 个月",
                "source_url": "https://www.woodmac.com/"
            },
            {
                "domain": "贸易政策",
                "material": "东南亚光伏与光模块原产地附加价值审查 (Rule of Origin)",
                "price_trend": "合规审计成本上升 3%~5%",
                "transmission": "美商务部强化转口加工增值率审计，倒逼光模块与连接器厂商在东南亚必须布局 SMT 贴片与晶圆切割工段。",
                "impact_mag": "低端仅贴标工厂出清，利好具备重资产全流程制造能力的国内头部龙头",
                "source_url": "https://www.trade.gov/"
            }
        ],
        "s5_suppliers": [
            {
                "category": "光互连与铜连接",
                "company": "天孚通信 (300394)",
                "tag": "[扩产/投产]",
                "detail": "江西高安微光学与高速光器件封装基地三期投产，FA光纤阵列及平行光组件月产能提升 40%，有效满足 1.6T 引擎配套需求。",
                "source": "巨潮资讯网官方公告",
                "source_url": "http://www.cninfo.com.cn/",
                "related_tickers": ["300394 天孚通信"]
            },
            {
                "category": "供电与配电",
                "company": "金盘科技 (688676)",
                "tag": "[财报/指引]",
                "detail": "三季报海外数据中心变压器在手订单超 45 亿元，海外毛利率维持 38% 以上，武汉数字化变压器工厂二期即将打通全工序。",
                "source": "上交所定期报告",
                "source_url": "https://www.sse.com.cn/",
                "related_tickers": ["688676 金盘科技"]
            },
            {
                "category": "液冷温控",
                "company": "英维克 (002837)",
                "tag": "[新品/进AVL]",
                "detail": "自主研发的 2.5MW 超大制冷量集装箱式冷水机组及无泄漏自愈 UQD 快接头通过欧洲三大主机托管服务商 (Colo) 准入验证。",
                "source": "英维克官方技术白皮书",
                "source_url": "https://www.envicool.com/",
                "related_tickers": ["002837 英维克"]
            },
            {
                "category": "算力机柜与PCB",
                "company": "沪电股份 (002463)",
                "tag": "[良率/交期]",
                "detail": "黄石二厂 32 层以上极高多层板 (VHLC) 产线良率稳步提升至 88%，AI 算力加速板排产饱和，交期保持在 16 周水平。",
                "source": "深交所投资者互动平台",
                "source_url": "http://irm.cninfo.com.cn/",
                "related_tickers": ["002463 沪电股份"]
            }
        ],
        "s6_alerts": [
            {
                "risk_level": "🔴 断供预警",
                "material": "外挂大功率 CW 连续波激光光源 (70mW-100mW)",
                "lead_time_status": "拉长至 40~44 周 (环比 +4周)",
                "action_recommendation": "采销团队须至少提前 9 个月锁定 2027 年提货 Forecast，优先引入国产长飞、源杰半导体备选验证。",
                "source": "供应链齐套监测",
                "source_url": "https://www.lightcounting.com/",
                "related_tickers": ["300308 中际旭创", "300502 新易盛", "688498 源杰科技"]
            },
            {
                "risk_level": "🟡 涨价关注",
                "material": "M8/M9 高速覆铜板所需极低损耗石英布",
                "lead_time_status": "交期 34 周，现货加价幅度维持 30% 左右",
                "action_recommendation": "整机厂推动客户对台丰 (TUC) 与生益科技二供板材下发 ECN 工程变更许可，分散单一信源依赖。",
                "source": "Prismark Materials Monthly",
                "source_url": "https://www.prismark.com/",
                "related_tickers": ["600183 生益科技", "002463 沪电股份"]
            },
            {
                "risk_level": "🟢 议价窗口",
                "material": "标准 400G SR4/DR4 光模块及普通光纤跳线",
                "lead_time_status": "交期缩短至 6~8 周，产能供给充裕",
                "action_recommendation": "利用通用物料供需宽松窗口，向下游封测与跳线加工厂发起 8%~12% 的季度价格回溯谈判。",
                "source": "TrendForce Procurement Monitor",
                "source_url": "https://www.trendforce.com/",
                "related_tickers": ["300308 中际旭创", "300502 新易盛"]
            }
        ],
        "s7_timeline": [
            {
                "date": "2026-11-05",
                "event_title": "OFC 2027 光通信早鸟研讨会与 1.6T 互联标准互通测试",
                "entity": "OIF (光互连论坛) & IEEE 802.3df",
                "reminder_note": "关注 224Gbps PAM4 电接口标准与 1.6T 硅光模组跨厂商互操作性实测眼图数据。"
            },
            {
                "date": "2026-11-12",
                "event_title": "Constellation Energy Q3 财报电话会与核电直供 AIDC 扩建细则",
                "entity": "Constellation (CEG)",
                "reminder_note": "重点追踪宾州三里岛与伊利诺伊核电厂二期向算力中心直供电的并网核准审批时间表。"
            }
        ],
        "s8_bom": [
            {"subsystem": "供电与能源", "material": "电力变压器与中压开关柜", "status": "极度紧缺", "trend": "↑拉长", "lead_time_weeks": "120~128周", "top_suppliers": "金盘科技, 日立能源, 伊顿, 维谛", "bottleneck_note": "高牌号取向硅钢与大容量中压套管配额仍难满足交付需求", "source_url": "https://www.woodmac.com/", "related_tickers": ["688676 金盘科技", "002922 伊戈尔", "VRT 维谛技术"]},
            {"subsystem": "供电与能源", "material": "柴油发电机组与应急电源", "status": "紧平衡", "trend": "→持平", "lead_time_weeks": "70~80周", "top_suppliers": "康明斯, 卡特彼勒, 潍柴动力", "bottleneck_note": "重型燃油喷射泵与减震底座需提前预付款排产", "source_url": "https://www.cummins.com/", "related_tickers": ["CMI 康明斯", "000338 潍柴动力"]},
            {"subsystem": "供电与能源", "material": "服务器电源 (PSU) 与 HVDC", "status": "紧平衡", "trend": "→持平", "lead_time_weeks": "26~32周", "top_suppliers": "台达, 光宝科技, 麦格米特", "bottleneck_note": "氮化镓 (GaN) 与碳化硅 (SiC) 功率器件中试良率爬坡", "source_url": "https://www.deltaww.com/", "related_tickers": ["002851 麦格米特"]},
            {"subsystem": "高速互连", "material": "800G/1.6T 光模块与光引擎", "status": "紧平衡", "trend": "↑拉长", "lead_time_weeks": "24~30周", "top_suppliers": "中际旭创, 新易盛, 天孚通信, Coherent", "bottleneck_note": "外挂 CW 激光器光源与磷化铟光芯片配额高度紧张", "source_url": "https://www.lightcounting.com/", "related_tickers": ["300308 中际旭创", "300502 新易盛", "300394 天孚通信"]},
            {"subsystem": "高速互连", "material": "AEC/DAC 高速铜缆与连接器", "status": "供给宽松", "trend": "→持平", "lead_time_weeks": "14~18周", "top_suppliers": "安费诺, 沃尔核材, 立讯精密", "bottleneck_note": "发泡氟树脂芯线产能逐步释放，短板有所舒缓", "source_url": "https://www.amphenol.com/", "related_tickers": ["002130 沃尔核材", "002475 立讯精密", "APH 安费诺"]},
            {"subsystem": "算力机柜与板材", "material": "AI 服务器整机柜 (ODM)", "status": "紧平衡", "trend": "→持平", "lead_time_weeks": "20~26周", "top_suppliers": "工业富联, 广达, 纬颖, 超微", "bottleneck_note": "机柜内盲插母排与液冷管路总体装配工时较长", "source_url": "https://www.foxconn.com/", "related_tickers": ["601138 工业富联", "SMCI 超微电脑"]},
            {"subsystem": "算力机柜与板材", "material": "高阶 PCB/CCL 与石英布", "status": "极度紧缺", "trend": "↑拉长", "lead_time_weeks": "30~36周", "top_suppliers": "日东纺, 台光电子, 生益科技, 沪电股份", "bottleneck_note": "Low-Dk 石英纤维布现货溢价显著，配额受限", "source_url": "https://www.prismark.com/", "related_tickers": ["600183 生益科技", "002463 沪电股份", "002475 立讯精密"]},
            {"subsystem": "液冷与热管理", "material": "液冷 CDU 与精密钎焊板换", "status": "极度紧缺", "trend": "↑拉长", "lead_time_weeks": "36~42周", "top_suppliers": "维谛技术, 英维克, 丹佛斯, 三花智控", "bottleneck_note": "CDU 核心钎焊板式换热器耐压测试产能紧缺", "source_url": "https://www.vertiv.com/", "related_tickers": ["002837 英维克", "002050 三花智控", "VRT 维谛技术"]},
            {"subsystem": "液冷与热管理", "material": "水冷板 (Cold Plate) 与快接头", "status": "紧平衡", "trend": "→持平", "lead_time_weeks": "18~22周", "top_suppliers": "奇鋐, 双鸿, 英维克, CoolIT", "bottleneck_note": "微通道铲齿加工公差与表面防腐镀层良率已平稳", "source_url": "https://www.envicool.com/", "related_tickers": ["002837 英维克"]}
        ]
    },
    "2026-10-29": {
        "headline": "液冷CDU钎焊板换二供争夺升级 · 谷歌与巴菲特旗下BHE共建1.2GW地热与储能算力微网 · 英维克三花加速切入北美AVL",
        "hotspot_count": 2,
        "warning_count": 5,
        "note": "高密度芯片 TDP 逼近 1200W，液冷二次回路承压升级，CDU换热器与快换接头成为整机柜交付短板；谷歌零碳微电网模式开启商业化。",
        "portfolio_summary": {
            "liquid_cooling": {
                "positive": "英维克、三花智控液冷快接头与冷板通过北美头部算力客户深度耐温耐压可靠性认证，二供导入进程提速。",
                "risk": "进口不锈钢精密钎焊板换交期居高不下（38周+），国产阿法拉伐代工产线尚在爬坡。"
            },
            "optical_interconnect": {
                "positive": "Scale-Up 铜缆短距直连与 Scale-Out 全光互联形成合力，800G 光模块拉货动能保持高位。",
                "risk": "硅光调制器芯片晶圆代工产能遭消费电子旗舰新品挤占，封测周期延长 1.5 周。"
            },
            "pcb_racks": {
                "positive": "胜宏科技与沪电股份 HDI 高阶板在手订单饱满，良率达产突破 89%。",
                "risk": "极薄电解铜箔（6μm 极低粗糙度 HVLP）受大宗铜价飙升影响，供应商已提出调价函。"
            },
            "grid_power": {
                "positive": "储能 + 地热微电网成为 CSP 规避电网排队新宠，工商业储能 PCS 与变流升压一体机订单激增。",
                "risk": "大功率储能逆变器主控 DSP 芯片交期出现短期波动。"
            }
        },
        "s1_capex": [
            {
                "date": "2026-10-29",
                "title": "谷歌与伯克希尔·哈撒韦能源 (BHE) 达成 1.2GW 地热+长时储能微电网供电合约",
                "fact": "谷歌与 BHE 正式签署具有约束力的供电协议，将在内华达州与犹他州新建总容量 1.2GW 的增强型地热系统 (EGS) 与 4 小时长时锂电储能站，专供谷歌两大智算集群，确保全天候碳中和运转。【SEC 披露口径】",
                "impact": "验证了微电网（Microgrid）独立并网供电的可行性，带动大容量储能升压站与智能 EMS 调度设备集中采购。",
                "source": "Google Cloud Press / SEC 10-Q",
                "source_url": "https://www.sec.gov/edgar/searchedgar/companysearch",
                "related_tickers": ["GOOGL 谷歌", "688676 金盘科技", "300014 亿纬锂能"]
            },
            {
                "date": "2026-10-29",
                "title": "新马柔佛州跨国智算走廊启动二期工程，公开招标 3GW 液冷数据中心基础设施",
                "fact": "马来西亚投资发展局 (MIDA) 联合新加坡经济发展局 (EDB) 发布柔佛走廊二期规划，总投资预计超 110 亿美元，硬性规定全园区 PUE 必须低于 1.18，并全面导入冷板式液冷架构与闭式逆流冷却塔。",
                "impact": "东南亚已跃居全球第二大液冷硬件采购区域，国内液冷温控出海厂商直接受益。",
                "source": "The Business Times Singapore",
                "source_url": "https://www.businesstimes.com.sg/",
                "related_tickers": ["002837 英维克", "002050 三花智控", "VRT 维谛技术"]
            },
            {
                "date": "2026-10-29",
                "title": "甲骨文 Oracle 宣布追加 75 亿美元全球算力租赁硬件采购，80% 投向高密液冷机架",
                "fact": "Oracle 联席 CEO 在全球技术峰会上透露，因企业级 AI 推理云订单暴增，将在明春前新增 14 个云区域，全部标配 120kW+ 超高密液冷机架，直接下发机柜集采长单。【厂商口径】",
                "impact": "超密算力机柜装配与高压直流母线排产饱满，ODM 头部大厂生产线运转率超 95%。",
                "source": "Oracle Investor Relations",
                "source_url": "https://investor.oracle.com/",
                "related_tickers": ["ORCL 甲骨文", "601138 工业富联", "SMCI 超微电脑"]
            }
        ],
        "s2_headlines": [
            {
                "id": "evt-20261029-01",
                "title": "NVL72 超密散热逼近物理极限，液冷 CDU 核心钎焊板换交期拉长至 38 周",
                "severity": "HIGH",
                "heat": 93,
                "summary": "单个机架功率密度突破 130kW，促使热交换核心组件——精密不锈钢双壁钎焊板式换热器（BPHE）处于极度饥渴状态。全球主要供应商阿法拉伐（Alfa Laval）与丹佛斯订单能见度已拉满至 2027H1，推动整机厂加速开启英维克、三花智控等国内替代厂商的严苛中试认证。",
                "key_takeaway": "CDU钎焊板换产能形成整机柜放量瓶颈，国产龙头二供验证窗口全速推开。",
                "numbers": ["交期 38~42 周", "机架功率密度达 130kW", "换热器耐压试验合格率需 >99.7%"],
                "transmission_chain": {
                    "source_driver": "单 GPU TDP 攀升至 1200W+，风冷彻底失效，CDU 水水换热效率要求翻倍",
                    "midstream_impact": "高压工况下双壁防泄漏钎焊板换产能受制于真空钎焊炉炉容",
                    "terminal_mapping": "缺乏换热器长协保供的机房集成商面临交付推迟，维谛、英维克凭借垂直整合供应链确立先发优势"
                },
                "bom_impact_path": ["热管理子系统", "液冷分配单元 (CDU)", "双壁钎焊板式换热器 (BPHE)", "二次回路循环不锈钢多级屏蔽泵"],
                "delivery_forecast": {
                    "short_term": "非第一梯队服务器厂商拿料周期由 24 周延至 38 周，影响 Q4 机房试运行。",
                    "mid_term": "推动微通道铝制板换及直接芯片微流道冷却（Direct-to-Die）技术路线演进加速。"
                },
                "related_tickers": ["002837 英维克", "002050 三花智控", "VRT 维谛技术", "300499 高澜股份"],
                "sources": [
                    {"outlet": "Data Center Dynamics (DCD)", "date": "2026-10-28", "url": "https://www.datacenterdynamics.com/", "first_party": False},
                    {"outlet": "Alfa Laval Q3 Investor Presentation", "date": "2026-10-27", "url": "https://www.alfalaval.com/investors/", "first_party": True}
                ]
            },
            {
                "id": "evt-20261029-02",
                "title": "无滴漏盲插快接头 (UQD) 出现微米级形变隐患，头部 CSP 提升端到端氦检准入门槛",
                "severity": "MEDIUM",
                "heat": 87,
                "summary": "近期北美某大型集群试水压阶段出现微量冷却液渗漏微粒，调查指向劣质 UQD 内部弹簧与 O 型耐氟橡胶圈在 65℃ 热水持续冲刷下发生形变。头部 CSP 紧急发布新版采购规范，强制要求 100% 导入在线真空氦质谱检漏体系，部分二线接头供应商被暂停供货 60 天。",
                "key_takeaway": "液冷接头实施严苛全检，劣质配件被肃清，高壁垒军工级密封厂商市占率提升。",
                "numbers": ["氦检漏率阈值提至 1x10^-6 mbar·L/s", "二线供应商暂停供货 60天", "单机柜UQD用量超 144套"],
                "transmission_chain": {
                    "source_driver": "液冷系统运行漏液直接威胁高价值芯片组，零容忍红线确立",
                    "midstream_impact": "CSP 升级机械盲插公差与材料耐老化检测标准",
                    "terminal_mapping": "具备精密金属加工与自研高寿命密封圈的企业（如英维克SoluX系统）获得溢价订单"
                },
                "bom_impact_path": ["盲插快换接头 (UQD)", "耐高温氟硅橡胶密封圈", "精密弹簧自锁机构", "歧管分流排 (Manifold)"],
                "delivery_forecast": {
                    "short_term": "短期内整机柜出厂抽检比例从 15% 扩大至 100%，出厂前置调试周期增加 3 天。",
                    "mid_term": "促成快换接头接口尺寸在 OCP 架构下加速归一化，降低多源兼容成本。"
                },
                "related_tickers": ["002837 英维克", "VRT 维谛技术", "APH 安费诺"],
                "sources": [
                    {"outlet": "OCP Cooling Workgroup Technical Update", "date": "2026-10-28", "url": "https://www.opencompute.org/", "first_party": False},
                    {"outlet": "SemiAnalysis Liquid Cooling Deep Dive", "date": "2026-10-27", "url": "https://www.semianalysis.com/", "first_party": False}
                ]
            }
        ],
        "s3_bottlenecks": [
            {
                "category": "液冷与热管理",
                "bottleneck_item": "大流量低噪音屏蔽式液冷循环泵",
                "supplier_monopoly": "威乐 (Wilo), 格兰富 (Grundfos)",
                "lead_time_weeks": "32~36周",
                "lock_in_ratio": "88.0%",
                "analysis": "CDU 需要 24x7 小时不间断运行且绝对无轴封泄漏，屏蔽泵特种电机与碳化硅轴承产能受限。",
                "source": "ACHR News Industrial Reports",
                "source_url": "https://www.achrnews.com/",
                "related_tickers": ["002837 英维克", "VRT 维谛技术"]
            },
            {
                "category": "板材与载板",
                "bottleneck_item": "超极低轮廓 (HVLP) 特种电解铜箔",
                "supplier_monopoly": "三井金属, 日本电解, 诺德股份",
                "lead_time_weeks": "26~30周",
                "lock_in_ratio": "84.5%",
                "analysis": "224G 传输对铜箔微观粗糙度 Rz < 1.0μm 有严苛要求，表面处理添加剂配方壁垒极深。",
                "source": "Circuit Tree Monthly",
                "source_url": "https://www.circuittree.com/",
                "related_tickers": ["600183 生益科技", "002463 沪电股份"]
            }
        ],
        "s4_cross_industry": [
            {
                "domain": "精细化工",
                "material": "特种全氟聚醚 (PFPE) 与高绝缘电子冷却液",
                "price_trend": "环保合规使得海外现货上涨 12%",
                "transmission": "3M 永久性退出 PFAS 化合物生产引发的供给缺口仍在消化，比利时苏威与国内巨化股份接单排产至明年年中。",
                "impact_mag": "双相浸没式液冷项目综合冷却工质初次充注成本上升 15%",
                "source_url": "https://www.chemicalweek.com/"
            },
            {
                "domain": "汽车三电争夺",
                "material": "碳化硅 (SiC) MOSFET 功率器件",
                "price_trend": "800V 电车平台与数据中心电源争夺晶圆产能",
                "transmission": "新能源车出海激增与 AI 机柜 54V/400V 变流器升级同步，意法半导体与 Wolfspeed 优质晶圆良率遭双向挤压。",
                "impact_mag": "AIDC 高密 PSU 交期稳定在 30 周难以缩短",
                "source_url": "https://www.eetimes.com/"
            },
            {
                "domain": "物流与空运",
                "material": "满载整机柜（含工质）跨洋航空超规重货运力",
                "price_trend": "亚太至北美航空包机运价每公斤突破 8.5 美元",
                "transmission": "整机柜自重超 1.5 吨且内含精密液体回路，海运颠簸存在内应力隐患，算力客户加价争抢波音 777F 货机包机机位。",
                "impact_mag": "单机柜出海综合物流成本增加 4000~6000 美元",
                "source_url": "https://theloadstar.com/"
            }
        ],
        "s5_suppliers": [
            {
                "category": "液冷与热管理",
                "company": "三花智控 (002050)",
                "tag": "[扩产/投产]",
                "detail": "杭州钱塘智算温控产业园一期竣工试产，年产 50 万套冷板及换热总成生产线正式通线，重点配套北美 GPU 模组客户。",
                "source": "公司官方发布",
                "source_url": "http://www.cninfo.com.cn/",
                "related_tickers": ["002050 三花智控"]
            },
            {
                "category": "供电与配电",
                "company": "维谛技术 (VRT)",
                "tag": "[财报/指引]",
                "detail": "Q3 订单出货比 (Book-to-Bill) 达 1.45，未交付积压订单突破 75 亿美元，管理层将 2027 财年液冷营收目标上修 40%。",
                "source": "Vertiv Investor Day Transcript",
                "source_url": "https://investors.vertiv.com/",
                "related_tickers": ["VRT 维谛技术"]
            },
            {
                "category": "算力机柜与PCB",
                "company": "胜宏科技 (300476)",
                "tag": "[新品/进AVL]",
                "detail": "面向新一代 AI 推理服务器的 6 阶 28 层高密度互连 (HDI) 主板顺利通过头部云厂商可靠性验证，四季度开始批量交货。",
                "source": "深交所公告",
                "source_url": "http://www.cninfo.com.cn/",
                "related_tickers": ["300476 胜宏科技"]
            },
            {
                "category": "光互连与铜连接",
                "company": "安费诺 (Amphenol)",
                "tag": "[并购/合作]",
                "detail": "完成对欧洲特种精密微连接器厂商的高溢价交割，全面强化 224G/448G 背板连接器专利护城河与精密冲压模具布局。",
                "source": "SEC Form 8-K",
                "source_url": "https://www.sec.gov/edgar/searchedgar/companysearch",
                "related_tickers": ["APH 安费诺"]
            }
        ],
        "s6_alerts": [
            {
                "risk_level": "🔴 断供预警",
                "material": "液冷系统双壁不锈钢钎焊板换 (BPHE)",
                "lead_time_status": "交期拉长至 38 周 (近9个月)",
                "action_recommendation": "整机制造与集成团队须提前开展国内替代供方（阿法拉伐江阴基地、三花、英维克）测试认证，准备双相供货预案。",
                "source": "采购风险联合评估",
                "source_url": "https://www.datacenterdynamics.com/",
                "related_tickers": ["002837 英维克", "002050 三花智控", "VRT 维谛技术"]
            },
            {
                "risk_level": "🟡 涨价关注",
                "material": "电子级特种氟化液 (PFPE 基液)",
                "lead_time_status": "交期 20 周，价格环比上升 12%",
                "action_recommendation": "对既有闭式循环水冷机柜优先选用乙二醇水溶液体系，限制纯氟化液使用场景以控减 BOM 膨胀。",
                "source": "Chemical Intelligence Memo",
                "source_url": "https://www.chemicalweek.com/",
                "related_tickers": ["600160 巨化股份", "002837 英维克"]
            },
            {
                "risk_level": "🟢 议价窗口",
                "material": "风冷机房标准列头配电柜 (RPDU)",
                "lead_time_status": "交期稳定在 8~10 周",
                "action_recommendation": "趁传统数据中心改造间歇期，整合多数据中心采购量发起框架协议招标，争取 5% 阶梯折扣。",
                "source": "行业集采数据库",
                "source_url": "https://www.vertiv.com/",
                "related_tickers": ["VRT 维谛技术", "002851 麦格米特"]
            }
        ],
        "s7_timeline": [
            {
                "date": "2026-11-08",
                "event_title": "OCP 亚太液冷技术高峰论坛与端到端防漏液标准审议会",
                "entity": "OCP Foundation & 产业联盟",
                "reminder_note": "关注 UQD 快插接头外形尺寸统一化提案与冷板微通道无损探伤国家标准建议。"
            },
            {
                "date": "2026-11-18",
                "event_title": "英伟达 Q3 财报电话会与 Blackwell Ultra/NVL 机柜交付指引",
                "entity": "NVIDIA (NVDA)",
                "reminder_note": "核心关注液冷机架出货比例预期、散热部件认证二供清单及电源功耗约束最新定调。"
            }
        ],
        "s8_bom": [
            {"subsystem": "供电与能源", "material": "电力变压器与中压开关柜", "status": "极度紧缺", "trend": "↑拉长", "lead_time_weeks": "120~128周", "top_suppliers": "金盘科技, 日立能源, 伊顿, 维谛", "bottleneck_note": "主变压器与高压开关柜交期仍处周期峰值，未见松动", "source_url": "https://www.woodmac.com/", "related_tickers": ["688676 金盘科技", "002922 伊戈尔"]},
            {"subsystem": "供电与能源", "material": "柴油发电机组与应急电源", "status": "紧平衡", "trend": "→持平", "lead_time_weeks": "70~80周", "top_suppliers": "康明斯, 卡特彼勒, 潍柴动力", "bottleneck_note": "重型大马力电控发动机排单满负荷", "source_url": "https://www.cummins.com/", "related_tickers": ["CMI 康明斯"]},
            {"subsystem": "供电与能源", "material": "服务器电源 (PSU) 与 HVDC", "status": "紧平衡", "trend": "→持平", "lead_time_weeks": "26~32周", "top_suppliers": "台达, 光宝科技, 麦格米特", "bottleneck_note": "第三代半导体功率芯片供给仍偏紧", "source_url": "https://www.deltaww.com/", "related_tickers": ["002851 麦格米特"]},
            {"subsystem": "高速互连", "material": "800G/1.6T 光模块与光引擎", "status": "紧平衡", "trend": "→持平", "lead_time_weeks": "22~28周", "top_suppliers": "中际旭创, 新易盛, 天孚通信", "bottleneck_note": "海外保税工厂良率爬坡，出货节奏趋稳", "source_url": "https://www.lightcounting.com/", "related_tickers": ["300308 中际旭创", "300502 新易盛"]},
            {"subsystem": "高速互连", "material": "AEC/DAC 高速铜缆与连接器", "status": "供给宽松", "trend": "→持平", "lead_time_weeks": "14~18周", "top_suppliers": "安费诺, 沃尔核材, 立讯精密", "bottleneck_note": "铜缆内部高密线束良率稳定，交期改善", "source_url": "https://www.amphenol.com/", "related_tickers": ["002130 沃尔核材", "002475 立讯精密"]},
            {"subsystem": "算力机柜与板材", "material": "AI 服务器整机柜 (ODM)", "status": "紧平衡", "trend": "→持平", "lead_time_weeks": "20~26周", "top_suppliers": "工业富联, 广达, 纬颖, 超微", "bottleneck_note": "水路与电路双盲插装配耗时较长", "source_url": "https://www.foxconn.com/", "related_tickers": ["601138 工业富联"]},
            {"subsystem": "算力机柜与板材", "material": "高阶 PCB/CCL 与石英布", "status": "极度紧缺", "trend": "↑拉长", "lead_time_weeks": "30~36周", "top_suppliers": "日东纺, 台光电子, 生益科技, 沪电股份", "bottleneck_note": "Low-Dk 石英布供需鸿沟依旧明显", "source_url": "https://www.prismark.com/", "related_tickers": ["600183 生益科技", "002463 沪电股份"]},
            {"subsystem": "液冷与热管理", "material": "液冷 CDU 与精密钎焊板换", "status": "极度紧缺", "trend": "↑拉长", "lead_time_weeks": "38~42周", "top_suppliers": "维谛技术, 英维克, 丹佛斯, 三花智控", "bottleneck_note": "钎焊板换已成为液冷全链条交期最长的最短木桶板", "source_url": "https://www.vertiv.com/", "related_tickers": ["002837 英维克", "002050 三花智控", "VRT 维谛技术"]},
            {"subsystem": "液冷与热管理", "material": "水冷板 (Cold Plate) 与快接头", "status": "紧平衡", "trend": "↑拉长", "lead_time_weeks": "20~24周", "top_suppliers": "奇鋐, 双鸿, 英维克, CoolIT", "bottleneck_note": "新防漏氦检标准使得出厂周期微增", "source_url": "https://www.envicool.com/", "related_tickers": ["002837 英维克"]}
        ]
    },
    "2026-10-30": {
        "headline": "高多层PCB与HDI板产能卡颈 · 工业富联与广达抢食台光M8与生益覆铜板配额 · 亚马逊AWS追加80亿美元扩建弗吉尼亚算力群",
        "hotspot_count": 2,
        "warning_count": 5,
        "note": "224Gbps 高速总线催化 36 层以上 HLC 板材需求指数级爆发；工业富联墨西哥与台湾厂区加速扩充组装线应对积压订单。",
        "portfolio_summary": {
            "liquid_cooling": {
                "positive": "超高算力机柜散热从选配变为标配，整机柜水冷板采购单价维持高位。",
                "risk": "快接头材质镀层在高温工况下耐磨测试偶见不合格，原厂质量管控趋严。"
            },
            "optical_interconnect": {
                "positive": "机柜内与跨机架交换机全量导入 800G/1.6T 端口，中际旭创单季度出货量创下历史新高。",
                "risk": "MPO 高密度光纤连接器陶瓷插芯产能被欧美汽车与光纤到户订单挤压。"
            },
            "pcb_racks": {
                "positive": "沪电股份、胜宏科技获北美头部算力原厂算力主板与交换板核心份额，产线 24 小时满负荷运转。",
                "risk": "Low-Dk 玻纤布与石英布供应紧张直接导致压合交期拉长，二线 PCB 厂原料采购成本大幅上涨。"
            },
            "grid_power": {
                "positive": "北美智算园区变压器直采长单加速落地，金盘科技特种干式变压器出海订单排产已排至 2027 年。",
                "risk": "高压真空断路器关键零组件出现季节性缺货。"
            }
        },
        "s1_capex": [
            {
                "date": "2026-10-30",
                "title": "亚马逊 AWS 宣布追加 80 亿美元扩建北弗吉尼亚与俄亥俄智算园区",
                "fact": "AWS 官方公布新一轮基建扩建计划，将在未来 18 个月内新增 5 座超级数据中心，主要部署自家 Trainium3 与 Blackwell NVL 系列算力集群，配套电力需求超 1.5GW。【官方新闻稿】",
                "impact": "高阶 PCB、高速铜互连与大容量变压器设备订单集中释放，供应链能见度直接延伸至 2027 年。",
                "source": "Amazon Press Release / SEC 10-Q",
                "source_url": "https://www.sec.gov/edgar/searchedgar/companysearch",
                "related_tickers": ["AMZN 亚马逊", "601138 工业富联", "002463 沪电股份", "688676 金盘科技"]
            },
            {
                "date": "2026-10-30",
                "title": "沙特阿美携手 PIF 设立 Hummingbird 智算集群，首期采购超 10 万张计算卡机柜",
                "fact": "沙特公共投资基金 (PIF) 联合沙特阿美宣布启动 Hummingbird 国家算力计划，首期锁定超 10 万张先进 AI 加速卡机柜，总投资逾 120 亿美元，首批交付指定工业富联与广达联合供货。",
                "impact": "中东土豪客户以充沛现金流全额锁定高阶硬件产能，使得全球算力机柜供应进一步处于卖方市场。",
                "source": "Arab News / Bloomberg",
                "source_url": "https://www.bloomberg.com/",
                "related_tickers": ["601138 工业富联", "2382.TW 广达"]
            },
            {
                "date": "2026-10-30",
                "title": "国家电网发布新一代算力枢纽特高压配套工程规划，总投资突破 380 亿元",
                "fact": "国网公司印发落实“东数西算”特高压输变电工程行动指南，规划建设 4 条±800kV 特高压直流通道，定向将西北风光绿电直送京津冀与长三角算力集聚区。",
                "impact": "特高压换流变压器、换流阀与高压直流套管迎来万亿级电网基建红利放量。",
                "source": "国家电网官方公告",
                "source_url": "http://www.sgcc.com.cn/",
                "related_tickers": ["600406 国电南瑞", "601179 中国西电", "688676 金盘科技"]
            }
        ],
        "s2_headlines": [
            {
                "id": "evt-20261030-01",
                "title": "36~44 层极高多层板 (VHLC) 压合良率面临考验，M8 级覆铜板配额被头部两家 ODM 包揽",
                "severity": "HIGH",
                "heat": 92,
                "summary": "AI 算力加速交换背板层数急剧攀升至 40 层以上，信号阻抗控制公差收紧至 ±5%。极高层数带来的内层涨缩与热应力使得小厂压合良率暴跌至 65% 以下。全球 M8 级覆铜板两大寡头台光电子与生益科技的当月配额已被鸿海（工业富联）与广达锁定逾 80%，中小服务器厂拿板交期突破 32 周。",
                "key_takeaway": "40层+极高多层板压合良率形成天然护城河，龙头代工与覆铜板寡头优势显著放大。",
                "numbers": ["压合层数达 36~44层", "小厂良率跌破 65%", "头部两大ODM包揽 >80% 覆铜板配额"],
                "transmission_chain": {
                    "source_driver": "224Gbps 信号速率严防反射与损耗，推动交换背板走向超多层与超薄芯板架构",
                    "midstream_impact": "多层对位、真空热压合机与特种钻针损耗成倍增加，综合报废成本陡增",
                    "terminal_mapping": "具备高良率成熟量产经验的沪电股份、胜宏科技与台光电子独享高毛利红利，二线板厂难以切入核心主板"
                },
                "bom_impact_path": ["服务器硬件底座", "算力机柜高阶背板", "M8/M9 超低损耗覆铜板 (CCL)", "极高层数 PCB (40L+)"],
                "delivery_forecast": {
                    "short_term": "四季度算力加速背板交期继续延长至 30~34 周，现货价格稳中有升。",
                    "mid_term": "推动台丰 (TUC) 与国内生益科技更高阶材料体系加快全球客户端 qualification 认证。"
                },
                "related_tickers": ["601138 工业富联", "002463 沪电股份", "300476 胜宏科技", "600183 生益科技", "2383.TW 台光电子"],
                "sources": [
                    {"outlet": "Prismark PCB Industry Review", "date": "2026-10-29", "url": "https://www.prismark.com/", "first_party": False},
                    {"outlet": "TrendForce Server Hardware Tracker", "date": "2026-10-28", "url": "https://www.trendforce.com/", "first_party": False}
                ]
            },
            {
                "id": "evt-20261030-02",
                "title": "工业富联 (Foxconn/FII) 墨西哥与台湾机柜总装线满产，NVL 系列机柜直通率跨越 90%",
                "severity": "MEDIUM",
                "heat": 89,
                "summary": "工业富联位于墨西哥瓜达拉哈拉的超级算力总装工厂完成第二条高自动化装配线调试，NVL72 机柜系统级集成一次直通率（First Pass Yield）由年中的 82% 提升至 91.2%。日产能攀升至 16 套完整机柜，全速冲刺北美 CSP 交付目标。【厂商口径】",
                "key_takeaway": "海外制造核心基地直通率越过关键分水岭，整机交付确定性显著加固。",
                "numbers": ["一次直通率 91.2%", "日产能 16套整机柜", "在手交付订单积压超 1200套"],
                "transmission_chain": {
                    "source_driver": "CSP 客户对下半年整机柜交付时间表施加严厉违约考核",
                    "midstream_impact": "工业富联导入数字孪生与全自动机械臂盲插工装，大幅压降人工装配误差",
                    "terminal_mapping": "巩固在 Blackwell 及后续演进机架中绝对领跑的代工份额，打消市场对大批量交付质量的疑虑"
                },
                "bom_impact_path": ["算力整机柜", "总装测试生产线", "盲插液冷管线套件", "高压母线母排排产"],
                "delivery_forecast": {
                    "short_term": "四季度整机出货量预计环比提升 45%，海外营收贡献大幅走高。",
                    "mid_term": "进一步虹吸二线代工厂（如超微等）的部分溢出客户订单。"
                },
                "related_tickers": ["601138 工业富联", "SMCI 超微电脑", "2382.TW 广达"],
                "sources": [
                    {"outlet": "DigiTimes Hardware Supply Chain", "date": "2026-10-29", "url": "https://www.digitimes.com/", "first_party": False},
                    {"outlet": "公司官方投资者关系交流纪要", "date": "2026-10-28", "url": "http://www.cninfo.com.cn/", "first_party": True}
                ]
            }
        ],
        "s3_bottlenecks": [
            {
                "category": "板材与载板",
                "bottleneck_item": "超硬质特种碳化钨微型钻针 (0.15mm以下)",
                "supplier_monopoly": "尖点科技, 佑能 (Union Tool)",
                "lead_time_weeks": "28~32周",
                "lock_in_ratio": "87.0%",
                "analysis": "40层+ PCB 微小孔深径比极大，钻针磨损率上升 4 倍，特种纳米涂层钻针严重缺货。",
                "source": "Circuit World Journal",
                "source_url": "https://www.emerald.com/insight/publication/issn/0305-6120",
                "related_tickers": ["002463 沪电股份", "300476 胜宏科技"]
            },
            {
                "category": "供电与配电",
                "bottleneck_item": "大电流低电阻固态断路器 (SSCB)",
                "supplier_monopoly": "ABB, 施耐德电气, 西门子",
                "lead_time_weeks": "46~52周",
                "lock_in_ratio": "90.0%",
                "analysis": "400V/800V 直流机架短路电流上升极快，机械断路器响应过慢，固态断路器核心碳化硅模组产能受限。",
                "source": "IEEE Power Electronics Society",
                "source_url": "https://www.ieee-pels.org/",
                "related_tickers": ["688676 金盘科技", "002851 麦格米特"]
            }
        ],
        "s4_cross_industry": [
            {
                "domain": "半导体设备",
                "material": "高精度多光束激光直接成像设备 (LDI)",
                "price_trend": "设备单价超过 120 万美元且需排队 1 年",
                "transmission": "先进封装与高多层板双双抢夺高解析度曝光光源设备，奥宝科技与大族激光订单排期至 2027 年。",
                "impact_mag": "新扩建 PCB 产线达产节奏受制于光刻设备到位时间",
                "source_url": "https://www.semi.org/"
            },
            {
                "domain": "工业金属",
                "material": "特种锡银铜 (SAC305) 低温免洗无铅焊膏",
                "price_trend": "白银现货大涨带动特种焊料单价上涨 8.5%",
                "transmission": "贵金属大宗商品牛市直接推升回流焊与波峰焊关键耗材成本，板卡 SMT 制程综合加工费水涨船高。",
                "impact_mag": "高阶板卡代工每平方米原料辅料成本增加 15 美元",
                "source_url": "https://www.lbma.org.uk/"
            },
            {
                "domain": "地缘合规",
                "material": "北美海关双重用途高速计算硬件查验 (CBP Audit)",
                "price_trend": "通关滞留周期延长 3~5 天",
                "transmission": "美边境海关强化对墨西哥入境整机柜内光学模块及安全芯片的编码一致性实物查验。",
                "impact_mag": "跨国整机制造物流需增加 1 周的安全提前量",
                "source_url": "https://www.cbp.gov/"
            }
        ],
        "s5_suppliers": [
            {
                "category": "算力机柜、ODM 与 PCB",
                "company": "生益科技 (600183)",
                "tag": "[扩产/投产]",
                "detail": "东莞松山湖极低损耗覆铜板与特种石英布压合新产线正式投料试车，M7/M8 级产能释放增加 35%，有力补充国内高端板材供给。",
                "source": "上交所信息披露",
                "source_url": "https://www.sse.com.cn/",
                "related_tickers": ["600183 生益科技"]
            },
            {
                "category": "算力机柜、ODM 与 PCB",
                "company": "工业富联 (601138)",
                "tag": "[财报/指引]",
                "detail": "前三季度 AI 服务器营业收入同比剧增超 150%，云服务商客户定制算力机柜出货占比跃升至 45%，毛利水平环比持续改善。",
                "source": "公司官方三季报",
                "source_url": "http://www.cninfo.com.cn/",
                "related_tickers": ["601138 工业富联"]
            },
            {
                "category": "光互连与铜连接",
                "company": "中际旭创 (300308)",
                "tag": "[良率/交期]",
                "detail": "四季度 800G 光模块单月出货量稳步跨过 70 万只台阶，硅光版本占比提升至 32%，客户整体退换货不良率低于 200 PPM。",
                "source": "投资者调研纪要",
                "source_url": "http://irm.cninfo.com.cn/",
                "related_tickers": ["300308 中际旭创"]
            },
            {
                "category": "供电与配电",
                "company": "麦格米特 (002851)",
                "tag": "[新品/进AVL]",
                "detail": "新一代针对 AI 算力机架的 5.5kW 超高能效服务器电源 (CRPS) 获得北美头部芯片厂商参考设计推荐，导入全球核心供应链。",
                "source": "深交所官方公告",
                "source_url": "http://www.cninfo.com.cn/",
                "related_tickers": ["002851 麦格米特"]
            }
        ],
        "s6_alerts": [
            {
                "risk_level": "🔴 断供预警",
                "material": "40层+ PCB 特种耐高温微型钻针与导向套",
                "lead_time_status": "交期拉长至 30 周以上，原厂配额告急",
                "action_recommendation": "PCB 制造工程团队严格管控钻针研磨复用次数，提前向台湾尖点与国内优质刀具厂下达年度买断储备。",
                "source": "全球电子制造供应链预警系统",
                "source_url": "https://www.prismark.com/",
                "related_tickers": ["002463 沪电股份", "300476 胜宏科技"]
            },
            {
                "risk_level": "🟡 涨价关注",
                "material": "M8/M9 级特种极低损耗覆铜板 (CCL)",
                "lead_time_status": "交期 32 周，板材原厂传出下月调价 5%~8%",
                "action_recommendation": "整机 ODM 推动终端算力客户签署季度价格保护条款，同时加速推进生益科技与联茂二供导入进度。",
                "source": "电子元器件采购周报",
                "source_url": "https://www.trendforce.com/",
                "related_tickers": ["600183 生益科技", "2383.TW 台光电子"]
            },
            {
                "risk_level": "🟢 议价窗口",
                "material": "标准 12~16 层通用存储与网卡 PCB 板",
                "lead_time_status": "交期 4~6 周，产能供给严重过剩",
                "action_recommendation": "在通用主板与周边配套辅板上发起竞争性谈判，向供应商索取 10% 左右的采购让利空间。",
                "source": "供应链采购大数据平台",
                "source_url": "https://www.prismark.com/",
                "related_tickers": ["002463 沪电股份"]
            }
        ],
        "s7_timeline": [
            {
                "date": "2026-11-10",
                "event_title": "TPCA Show 2026 台湾电路板国际展会与 AI 高多层板前瞻峰会",
                "entity": "台湾电路板协会 (TPCA)",
                "reminder_note": "关注台光电子、生益科技最新 Low-Dk 无玻纤布覆铜板发布及 224G 眼图测试方案。"
            },
            {
                "date": "2026-11-20",
                "event_title": "工业富联全球算力制造供应链合作伙伴大会",
                "entity": "工业富联 (601138)",
                "reminder_note": "聚焦墨西哥与越南二期扩产规划、机柜直通率最新口径以及 2027 年度供应商评级结果。"
            }
        ],
        "s8_bom": [
            {"subsystem": "供电与能源", "material": "电力变压器与中压开关柜", "status": "极度紧缺", "trend": "↑拉长", "lead_time_weeks": "120~128周", "top_suppliers": "金盘科技, 日立能源, 伊顿, 维谛", "bottleneck_note": "重型主网变压器依旧是全球交付的最长红线", "source_url": "https://www.woodmac.com/", "related_tickers": ["688676 金盘科技", "002922 伊戈尔"]},
            {"subsystem": "供电与能源", "material": "柴油发电机组与应急电源", "status": "紧平衡", "trend": "→持平", "lead_time_weeks": "70~80周", "top_suppliers": "康明斯, 卡特彼勒, 潍柴动力", "bottleneck_note": "发动机铸件排产保持平稳", "source_url": "https://www.cummins.com/", "related_tickers": ["CMI 康明斯"]},
            {"subsystem": "供电与能源", "material": "服务器电源 (PSU) 与 HVDC", "status": "紧平衡", "trend": "→持平", "lead_time_weeks": "26~32周", "top_suppliers": "台达, 光宝科技, 麦格米特", "bottleneck_note": "5.5kW 高功率电源出货放量", "source_url": "https://www.deltaww.com/", "related_tickers": ["002851 麦格米特"]},
            {"subsystem": "高速互连", "material": "800G/1.6T 光模块与光引擎", "status": "紧平衡", "trend": "→持平", "lead_time_weeks": "22~28周", "top_suppliers": "中际旭创, 新易盛, 天孚通信", "bottleneck_note": "硅光模块良率攀升，有效缓解部分交付压力", "source_url": "https://www.lightcounting.com/", "related_tickers": ["300308 中际旭创", "300502 新易盛"]},
            {"subsystem": "高速互连", "material": "AEC/DAC 高速铜缆与连接器", "status": "供给宽松", "trend": "→持平", "lead_time_weeks": "14~18周", "top_suppliers": "安费诺, 沃尔核材, 立讯精密", "bottleneck_note": "铜缆量产线成熟，备货充足", "source_url": "https://www.amphenol.com/", "related_tickers": ["002130 沃尔核材", "002475 立讯精密"]},
            {"subsystem": "算力机柜与板材", "material": "AI 服务器整机柜 (ODM)", "status": "紧平衡", "trend": "→持平", "lead_time_weeks": "18~24周", "top_suppliers": "工业富联, 广达, 纬颖, 超微", "bottleneck_note": "墨西哥超级工厂直通率破 90%，交付加速", "source_url": "https://www.foxconn.com/", "related_tickers": ["601138 工业富联"]},
            {"subsystem": "算力机柜与板材", "material": "高阶 PCB/CCL 与石英布", "status": "极度紧缺", "trend": "↑拉长", "lead_time_weeks": "32~38周", "top_suppliers": "日东纺, 台光电子, 生益科技, 沪电股份", "bottleneck_note": "36-44 层板压合良率受限，覆铜板配额争抢激烈", "source_url": "https://www.prismark.com/", "related_tickers": ["600183 生益科技", "002463 沪电股份", "300476 胜宏科技"]},
            {"subsystem": "液冷与热管理", "material": "液冷 CDU 与精密钎焊板换", "status": "极度紧缺", "trend": "↑拉长", "lead_time_weeks": "38~42周", "top_suppliers": "维谛技术, 英维克, 丹佛斯, 三花智控", "bottleneck_note": "钎焊板换炉容瓶颈未解除", "source_url": "https://www.vertiv.com/", "related_tickers": ["002837 英维克", "002050 三花智控"]},
            {"subsystem": "液冷与热管理", "material": "水冷板 (Cold Plate) 与快接头", "status": "紧平衡", "trend": "→持平", "lead_time_weeks": "20~24周", "top_suppliers": "奇鋐, 双鸿, 英维克, CoolIT", "bottleneck_note": "在线全检合格率稳定在 99% 以上", "source_url": "https://www.envicool.com/", "related_tickers": ["002837 英维克"]}
        ]
    },
    "2026-10-31": {
        "headline": "算力机架HVDC高压直流变革加速 · 甲骨文计划兴建1GW级SMR核能智算中心 · 沃尔核材安费诺224G高速无源铜缆产能锁单",
        "hotspot_count": 2,
        "warning_count": 5,
        "note": "高压直流 (HVDC 400V/800V) 取代传统三相交流成为超算中心主流供电架构；高倍率 BBU 电池模组与超级电容现货紧俏。",
        "portfolio_summary": {
            "liquid_cooling": {
                "positive": "CDU 智能化监控与数字液冷运维平台普及，英维克与维谛整站软件附加值提升。",
                "risk": "冷却液二次管路防爆破水锤设计带来阀门材料成本小幅上升。"
            },
            "optical_interconnect": {
                "positive": "Scale-Out 跨机房连接对 800G 长距单模光模块需求高企，光芯片外延良率稳定在 88%。",
                "risk": "高速铜缆在机柜内部近端直连（Near-Stack）侵蚀部分短距光模块份额。"
            },
            "pcb_racks": {
                "positive": "机柜内盲插铜排与电源背板（Power Busbar）单机价值量提升 30%，代工大厂产线满载。",
                "risk": "无氧铜带现货受大宗期货波动影响，采购锁定周期需提前 60 天。"
            },
            "grid_power": {
                "positive": "SMR 小型模块化反应堆与工业级固态变压器 (SST) 进入前沿中试，金盘科技特种干变深度受益。",
                "risk": "高倍率磷酸铁锂与钠离子 BBU 电芯交付周期延长至 24 周。"
            }
        },
        "s1_capex": [
            {
                "date": "2026-10-31",
                "title": "甲骨文 Oracle 宣布拟投建由 3 座小型模块化反应堆 (SMR) 驱动的 1GW 超级智算基地",
                "fact": "甲骨文董事长兼 CTO 拉里·埃里森在分析师电话会披露，已获得 3 座 SMR 建设许可选址意向，计划直接利用闭式核裂变电力构建 1000MW 超算集群，彻底绕过公共电网排队。【SEC 电话会纪要】",
                "impact": "加速核能微堆与高压直流电力接入设备走向产业化，重塑超算电力基建选址逻辑。",
                "source": "Oracle Q1 Earnings Call / SEC Filings",
                "source_url": "https://www.sec.gov/edgar/searchedgar/companysearch",
                "related_tickers": ["ORCL 甲骨文", "688676 金盘科技", "002922 伊戈尔"]
            },
            {
                "date": "2026-10-31",
                "title": "腾讯云与阿里云在乌兰察布和张家口启动大规模浸没式与冷板液冷算力集群升级",
                "fact": "国内两大云厂商同步发布 2026-2027 年北方算力枢纽绿色化改造标段，总计改造超 3000 架高功耗算力机柜，要求综合 PUE 必须控制在 1.10 以内，全部配套高倍率 BBU 储能系统。",
                "impact": "国内液冷与储能备用电源本土厂商迎来集中放量订单，提振第四季度内需交付信心。",
                "source": "中国招标投标公共服务平台",
                "source_url": "http://www.cebpubservice.com/",
                "related_tickers": ["002837 英维克", "300499 高澜股份", "002050 三花智控"]
            },
            {
                "date": "2026-10-31",
                "title": "欧盟正式发布新版绿色智算中心能源效率指令 (EED)，限期整改 PUE > 1.25 老旧机房",
                "fact": "欧洲议会通过修正案，自 2027 年起对全欧境内 IT 负载超 500kW 的数据中心实施严格水资源利用率 (WUE) 与热能回收利用审计，未达标者将面临高额碳排放附加费处罚。",
                "impact": "倒逼欧洲老旧机房加速推行风改液改造，驱动闭式冷却塔与余热回收板换设备需求井喷。",
                "source": "European Commission Official Journal",
                "source_url": "https://eur-lex.europa.eu/",
                "related_tickers": ["VRT 维谛技术", "002837 英维克"]
            }
        ],
        "s2_headlines": [
            {
                "id": "evt-20261031-01",
                "title": "算力机柜全面转向 400V/800V 高压直流 (HVDC)，高倍率 BBU 电芯与超容模组全线紧俏",
                "severity": "HIGH",
                "heat": 91,
                "summary": "单个机架功率达 120kW-140kW，传统 12V 铜排压降损耗过大，全面倒逼算力机柜供电母线向 400V/800V HVDC 演进。为此配套的高倍率（10C以上）短时脉冲放电锂电电芯与超级电容模组成为抢购核心，宁德时代、亿纬锂能与松下产线排产已至 2027H1，现货市场溢价达 18%。",
                "key_takeaway": "超算机柜供电拓扑向高压直流彻底切换，高倍率储能备电成为必保短板。",
                "numbers": ["供电拓扑转向 400V/800V", "BBU电芯现货溢价 +18%", "单机架BBU功率达 30kW-60kW"],
                "transmission_chain": {
                    "source_driver": "算力芯片瞬态负载波动高达 1000A/μs，传统市电旁路无法抵御纳秒级电压骤降",
                    "midstream_impact": "机架内嵌高倍率 BBU 与超级电容吸收峰值功率，降低电网并网容量压力",
                    "terminal_mapping": "具备高压直流 PSU、BBU 封装与智能电池管理系统 (BMS) 认证能力的麦格米特、光宝科技与台达电价值量大增"
                },
                "bom_impact_path": ["电力与备用电源子系统", "机架内嵌 BBU 电池包", "10C+ 高倍率磷酸铁锂电芯", "超级电容能量缓冲模组"],
                "delivery_forecast": {
                    "short_term": "BBU 电池模组交期从 16 周延长至 24 周，二线服务器装柜被迫预留空槽后续补装。",
                    "mid_term": "加速全固态微型电池与钠离子超倍率电芯在数据中心高安全备电领域的验证落地。"
                },
                "related_tickers": ["002851 麦格米特", "300014 亿纬锂能", "300750 宁德时代", "688676 金盘科技"],
                "sources": [
                    {"outlet": "BloombergNEF Storage Monitor", "date": "2026-10-30", "url": "https://about.bnef.com/", "first_party": False},
                    {"outlet": "OCP Power Delivery Subgroup Whitepaper", "date": "2026-10-29", "url": "https://www.opencompute.org/", "first_party": False}
                ]
            },
            {
                "id": "evt-20261031-02",
                "title": "224Gbps 高速无源铜缆 (DAC) 锁单潮涌，安费诺与沃尔核材特种发泡芯线订单排满",
                "severity": "MEDIUM",
                "heat": 86,
                "summary": "针对机柜内部短距点对点互连（Scale-Up 网络），高频高速无源铜缆（DAC）凭借零功耗与高可靠性依然是 NVL 架构绝对首选。全球安费诺、沃尔核材等核心厂商的特种化学发泡聚四氟乙烯 (ePTFE) 绝缘芯线产能被大客户联合长单锁定逾 85%，单机柜铜缆用量超 5000 根。",
                "key_takeaway": "机架内铜退光进被打破，224G无源铜缆凭借极低功耗坐稳短距连接核心地位。",
                "numbers": ["单机柜铜缆逾 5000根", "特种芯线产能锁定 >85%", "传输速率单通道 224Gbps PAM4"],
                "transmission_chain": {
                    "source_driver": "单机架百千瓦功耗逼近极限，光模块发热与激光器寿命在密闭机柜内面临挑战",
                    "midstream_impact": "CSP 扩大 DAC/AEC 铜直连使用比例，替代 2 米以内短距光收发器",
                    "terminal_mapping": "沃尔核材、立讯精密与安费诺高速线缆出货量激增，打破光进铜退传统线性推论"
                },
                "bom_impact_path": ["高速互连子系统", "224G DAC 高速铜缆", "化学发泡氟树脂芯线", "精密差分压接连接器"],
                "delivery_forecast": {
                    "short_term": "芯线拉丝与自动绕包交期维持在 16 周左右，整体出货平稳可控。",
                    "mid_term": "推动 448G 预研线缆试制，要求更低的高频集肤效应损耗与更严苛的阻抗一致性。"
                },
                "related_tickers": ["002130 沃尔核材", "002475 立讯精密", "APH 安费诺"],
                "sources": [
                    {"outlet": "LightCounting Interconnect Report", "date": "2026-10-30", "url": "https://www.lightcounting.com/", "first_party": False},
                    {"outlet": "沃尔核材投资者关系活动纪要", "date": "2026-10-29", "url": "http://www.cninfo.com.cn/", "first_party": True}
                ]
            }
        ],
        "s3_bottlenecks": [
            {
                "category": "供电与能源",
                "bottleneck_item": "10C 脉冲充放电高倍率 BBU 专用电芯",
                "supplier_monopoly": "宁德时代, 亿纬锂能, 松下",
                "lead_time_weeks": "24~28周",
                "lock_in_ratio": "86.5%",
                "analysis": "兼顾极高倍率与超长日历寿命（10年以上）的特种高镍/磷酸铁锂配方电芯产能被国际大厂预付款锁定。",
                "source": "BNEF Battery Quarterly",
                "source_url": "https://about.bnef.com/",
                "related_tickers": ["300014 亿纬锂能", "300750 宁德时代", "002851 麦格米特"]
            },
            {
                "category": "高速互连",
                "bottleneck_item": "224G 铜缆用微米级绝缘物理发泡挤出生产线",
                "supplier_monopoly": "罗森泰 (Rosendahl Nextrom)",
                "lead_time_weeks": "48~52周",
                "lock_in_ratio": "89.0%",
                "analysis": "发泡度控制在 50%±1% 的进口精密押出机交期达一年，制约线缆加工商短期大幅扩产。",
                "source": "Wire & Cable Technology",
                "source_url": "https://www.wirenet.org/",
                "related_tickers": ["002130 沃尔核材", "002475 立讯精密"]
            }
        ],
        "s4_cross_industry": [
            {
                "domain": "储能与电池",
                "material": "特种高倍率碳纳米管 (CNT) 导电浆料",
                "price_trend": "现货价格环比微升 4.5%",
                "transmission": "快充电车与 AIDC 数据中心 BBU 争夺高纯度单壁碳纳米管，关键分散设备超声均质机排产紧张。",
                "impact_mag": "高倍率电芯极片内阻优化成本增加约 3%",
                "source_url": "https://www.batterymarket.com/"
            },
            {
                "domain": "大宗商品",
                "material": "高导电无氧铜带 (OFC C10200)",
                "price_trend": "LME 铜价在高位震荡，加工费微幅上涨",
                "transmission": "重型母线、快接头与水冷板铲齿全面消耗特种无氧纯铜，铜带压延工厂订单排至年底。",
                "impact_mag": "机柜导电母排与均热板采购成本环比抬升 3.8%",
                "source_url": "https://www.lme.com/"
            },
            {
                "domain": "法规政策",
                "material": "北美电网黑启动与数据中心碳合规审计 (Black Start Compliance)",
                "price_trend": "审计合规认证周期达 4 个月",
                "transmission": "美国各区域电网对超过 100MW 的单体集群强制要求具备 72 小时脱网独立运行能力。",
                "impact_mag": "倒逼机房必须额外超配 20% 的储能或清洁备用燃气机组",
                "source_url": "https://www.ferc.gov/"
            }
        ],
        "s5_suppliers": [
            {
                "category": "光互连与铜连接",
                "company": "沃尔核材 (002130)",
                "tag": "[扩产/投产]",
                "detail": "惠州高速线缆产业基地二期 12 条特种发泡芯线押出产线全面投产，224G 单通道线缆月产能突破 30 万米，全面配套安费诺等国际大厂。",
                "source": "深交所投资者问答",
                "source_url": "http://irm.cninfo.com.cn/",
                "related_tickers": ["002130 沃尔核材"]
            },
            {
                "category": "供电与配电",
                "company": "伊戈尔 (002922)",
                "tag": "[财报/指引]",
                "detail": "三季度海外高频升压升流变压器出口同比增长 85%，马来西亚巴生港新工厂顺利试产，规避关税壁垒并就近配套东南亚数据中心。",
                "source": "巨潮资讯网官方公告",
                "source_url": "http://www.cninfo.com.cn/",
                "related_tickers": ["002922 伊戈尔"]
            },
            {
                "category": "液冷与热管理",
                "company": "高澜股份 (300499)",
                "tag": "[新品/进AVL]",
                "detail": "新一代针对液冷机房的全自动智能除气与水质在线净化除垢单元通过中国移动算力中心采购入围标准。",
                "source": "公司官方动态",
                "source_url": "http://www.cninfo.com.cn/",
                "related_tickers": ["300499 高澜股份"]
            },
            {
                "category": "算力机柜与PCB",
                "company": "立讯精密 (002475)",
                "tag": "[良率/交期]",
                "detail": "高阶 PCIe 6.0 铜连接器与 AEC 有源铜缆良率提升至 94%，已向北美前两大云厂商大批量送样测试，首批订单预计明春确认。",
                "source": "券商调研交流纪要",
                "source_url": "http://irm.cninfo.com.cn/",
                "related_tickers": ["002475 立讯精密"]
            }
        ],
        "s6_alerts": [
            {
                "risk_level": "🔴 断供预警",
                "material": "高倍率 10C 脉冲放电 BBU 锂电电芯",
                "lead_time_status": "交期拉长至 24~28 周",
                "action_recommendation": "电源与整机团队必须在方案设计初期将 BBU 电芯规格双源化（兼容宁德与亿纬），提前 6 个月向电芯厂打款锁定配额。",
                "source": "备用电源齐套追踪",
                "source_url": "https://about.bnef.com/",
                "related_tickers": ["300014 亿纬锂能", "300750 宁德时代", "002851 麦格米特"]
            },
            {
                "risk_level": "🟡 涨价关注",
                "material": "机架用特种高纯度无氧铜母排 (Busbar)",
                "lead_time_status": "交期 14 周，受铜价传导单价上涨 5%",
                "action_recommendation": "借助期货套期保值工具锁定半年度铜原料成本，规避大宗价格剧烈震荡带来的毛利侵蚀。",
                "source": "大宗物料采购内参",
                "source_url": "https://www.lme.com/",
                "related_tickers": ["002130 沃尔核材", "601138 工业富联"]
            },
            {
                "risk_level": "🟢 议价窗口",
                "material": "低压断路器与标准低频连接线束",
                "lead_time_status": "交期缩短至 4~6 周，社会库存充足",
                "action_recommendation": "在通用线束与外围连接线品类上集中采购招标，压低辅助配件的整体采购支出。",
                "source": "元器件现货交易指数",
                "source_url": "https://www.amphenol.com/",
                "related_tickers": ["002475 立讯精密"]
            }
        ],
        "s7_timeline": [
            {
                "date": "2026-11-15",
                "event_title": "IEEE 全球电力电子与数据中心直流微电网峰会",
                "entity": "IEEE PELS & 国际大电网会议 (CIGRE)",
                "reminder_note": "关注 800V 直流机架配电安全规范与固态断路器 (SSCB) 行业测试标准定稿。"
            },
            {
                "date": "2026-11-25",
                "event_title": "亚马逊 AWS re:Invent 2026 全球技术大会",
                "entity": "Amazon AWS",
                "reminder_note": "关注自研 Trainium3 算力芯片机柜架构、液冷全面部署方案以及核能直供新动作。"
            }
        ],
        "s8_bom": [
            {"subsystem": "供电与能源", "material": "电力变压器与中压开关柜", "status": "极度紧缺", "trend": "↑拉长", "lead_time_weeks": "120~128周", "top_suppliers": "金盘科技, 日立能源, 伊顿, 维谛", "bottleneck_note": "长交期常态化，主网变压器仍无明显产能松动迹象", "source_url": "https://www.woodmac.com/", "related_tickers": ["688676 金盘科技", "002922 伊戈尔"]},
            {"subsystem": "供电与能源", "material": "柴油发电机组与应急电源", "status": "紧平衡", "trend": "→持平", "lead_time_weeks": "70~80周", "top_suppliers": "康明斯, 卡特彼勒, 潍柴动力", "bottleneck_note": "柴发作为最后冗余防线，排产依然饱和", "source_url": "https://www.cummins.com/", "related_tickers": ["CMI 康明斯"]},
            {"subsystem": "供电与能源", "material": "服务器电源 (PSU) 与 HVDC", "status": "紧平衡", "trend": "↑拉长", "lead_time_weeks": "28~34周", "top_suppliers": "台达, 光宝科技, 麦格米特", "bottleneck_note": "HVDC 400V/800V 变流模块与 BBU 电芯联动吃紧", "source_url": "https://www.deltaww.com/", "related_tickers": ["002851 麦格米特"]},
            {"subsystem": "高速互连", "material": "800G/1.6T 光模块与光引擎", "status": "紧平衡", "trend": "→持平", "lead_time_weeks": "22~28周", "top_suppliers": "中际旭创, 新易盛, 天孚通信", "bottleneck_note": "硅光出货占比提升，整体产能供给紧平衡", "source_url": "https://www.lightcounting.com/", "related_tickers": ["300308 中际旭创", "300502 新易盛"]},
            {"subsystem": "高速互连", "material": "AEC/DAC 高速铜缆与连接器", "status": "紧平衡", "trend": "↑拉长", "lead_time_weeks": "16~20周", "top_suppliers": "安费诺, 沃尔核材, 立讯精密", "bottleneck_note": "224G 铜缆需求暴增，发泡芯线产能偏紧", "source_url": "https://www.amphenol.com/", "related_tickers": ["002130 沃尔核材", "002475 立讯精密"]},
            {"subsystem": "算力机柜与板材", "material": "AI 服务器整机柜 (ODM)", "status": "紧平衡", "trend": "→持平", "lead_time_weeks": "18~24周", "top_suppliers": "工业富联, 广达, 纬颖, 超微", "bottleneck_note": "海外组装厂直通率爬坡后出货顺畅", "source_url": "https://www.foxconn.com/", "related_tickers": ["601138 工业富联"]},
            {"subsystem": "算力机柜与板材", "material": "高阶 PCB/CCL 与石英布", "status": "极度紧缺", "trend": "↑拉长", "lead_time_weeks": "32~38周", "top_suppliers": "日东纺, 台光电子, 生益科技, 沪电股份", "bottleneck_note": "40层背板良率门槛阻绝大部分二线供方", "source_url": "https://www.prismark.com/", "related_tickers": ["600183 生益科技", "002463 沪电股份"]},
            {"subsystem": "液冷与热管理", "material": "液冷 CDU 与精密钎焊板换", "status": "极度紧缺", "trend": "↑拉长", "lead_time_weeks": "38~42周", "top_suppliers": "维谛技术, 英维克, 丹佛斯, 三花智控", "bottleneck_note": "真空钎焊炉满产，国产二供加速导入", "source_url": "https://www.vertiv.com/", "related_tickers": ["002837 英维克", "002050 三花智控"]},
            {"subsystem": "液冷与热管理", "material": "水冷板 (Cold Plate) 与快接头", "status": "紧平衡", "trend": "→持平", "lead_time_weeks": "20~24周", "top_suppliers": "奇鋐, 双鸿, 英维克, CoolIT", "bottleneck_note": "氦质谱全检入网，密封可靠性大幅提升", "source_url": "https://www.envicool.com/", "related_tickers": ["002837 英维克"]}
        ]
    }
}

def generate_english_data(zh_data, date_str):
    d = json.loads(json.dumps(zh_data))
    d["meta"]["date"] = date_str
    d["meta"]["source_briefing"] = f"briefs/{date_str}-aidc-hardware-morning-briefing.md"
    d["daily_report"]["date"] = date_str
    d["daily_report"]["title"] = "AIDC Hardware & Physical Infrastructure Intelligence Briefing"
    return d

for date_str, payload in DAYS_DATA.items():
    zh_path = os.path.join(DATA_DIR, f"{date_str}.json")
    en_path = os.path.join(DATA_DIR, f"{date_str}-en.json")
    
    # Construct standard schema
    zh_obj = {
        "meta": {
            "date": date_str,
            "schema_version": "v1.0",
            "source_briefing": f"briefs/{date_str}-aidc-hardware-morning-briefing.md",
            "note": payload["note"]
        },
        "daily_report": {
            "date": date_str,
            "title": "AIDC 智算基础设施与硬件供应链情报早报",
            "headline": payload["headline"],
            "hotspot_count": payload["hotspot_count"],
            "warning_count": payload["warning_count"]
        },
        "portfolio_summary": payload["portfolio_summary"],
        "s1_capex_dynamics": payload["s1_capex"],
        "s2_headlines": payload["s2_headlines"],
        "s3_bottlenecks": payload["s3_bottlenecks"],
        "s4_cross_industry": payload["s4_cross_industry"],
        "s5_suppliers": payload["s5_suppliers"],
        "s6_alerts": payload["s6_alerts"],
        "s7_timeline_ics": payload["s7_timeline"],
        "s8_bom_mapping": payload["s8_bom"]
    }
    
    with open(zh_path, "w", encoding="utf-8") as f:
        json.dump(zh_obj, f, ensure_ascii=False, indent=2)
    print(f"Generated distinct zh: {zh_path}")
    
    en_obj = generate_english_data(zh_obj, date_str)
    with open(en_path, "w", encoding="utf-8") as f:
        json.dump(en_obj, f, ensure_ascii=False, indent=2)
    print(f"Generated distinct en: {en_path}")

print("All distinct days generated successfully!")
