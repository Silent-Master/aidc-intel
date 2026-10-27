# AIDC 每日自动化检索词矩阵（Data Feeding Layer）

为保障每日 AIDC 供应链早报具有最高鲜活度与事实密度，前置爬虫、新闻聚合器或搜索 API（如 Google News RSS, Tavily, Perplexity API, Bing Search）可配置以下 5 组检索词定时抓取过去 24~48 小时内的中英文资讯：

---

### 1. 供电、配电与备用电源组（Power & Grid Infrastructure）
```text
# 英文检索流
"AI data center" AND ("transformer" OR "switchgear" OR "diesel generator" OR "gas turbine") AND ("lead time" OR "shortage" OR "backlog" OR "capacity")
"Vertiv" OR "Eaton" OR "Schneider Electric" OR "Delta Electronics" OR "Cummins" OR "Caterpillar" data center power OR BBU OR HVDC

# 中文检索流
数据中心 (变压器 OR 柴油发电机 OR 服务器电源 OR BBU OR 超级电容 OR 高压直流) (产能 OR 交期 OR 招标 OR 扩产 OR 锁单)
(金盘科技 OR 伊戈尔 OR 麦格米特 OR 科华数据 OR 特变电工) 数据中心 电源 OR 变压器
```

---

### 2. 光互连与高速铜连接组（Optical & Copper Interconnect）
```text
# 英文检索流
"800G" OR "1.6T" OR "optical transceiver" OR "EML laser" OR "InP" OR "CPO" OR "silicon photonics" supply chain OR capacity OR shortage
"Amphenol" OR "Credo" OR "Coherent" OR "Lumentum" OR "Fabrinet" AEC OR DAC cable OR optical transceiver

# 中文检索流
光模块 (800G OR 1.6T OR 硅光 OR EML芯片 OR 磷化铟 OR 高速铜缆 OR 安费诺) (产能 OR 排产 OR 缺货 OR 良率 OR 交付)
(中际旭创 OR 新易盛 OR 天孚通信 OR 沃尔核材 OR 立讯精密) 800G OR 1.6T OR 高速铜缆
```

---

### 3. 算力机柜、PCB 上游材料与 ODM 组（Rack, PCB & ODM）
```text
# 英文检索流
"Foxconn" OR "Quanta" OR "Wiwynn" OR "Supermicro" AI server rack yield OR shipment OR backlog
"Low-Dk" OR "fiberglass cloth" OR "Nittobo" OR "CCL" OR "HDI PCB" AI server shortage OR expansion

# 中文检索流
AI服务器 (整机柜 OR 工业富联 OR 广达 OR 纬颖 OR 超微) (良率 OR 出货 OR 爬坡 OR 积压)
(覆铜板 OR 玻纤布 OR 高多层PCB OR Low-Dk OR 石英布) (沪电股份 OR 胜宏科技 OR 生益科技 OR 台光电子) 产能 OR 涨价 OR 缺货
```

---

### 4. 智算液冷与温控组（Liquid Cooling & Thermal Management）
```text
# 英文检索流
"liquid cooling" OR "CDU" OR "cold plate" OR "UQD" OR "manifold" AI data center supply chain OR leak OR capacity
"Boyd" OR "CoolIT" OR "nVent" OR "AVC" OR "Auras" liquid cooling capacity OR order

# 中文检索流
智算中心 液冷 (CDU OR 冷板 OR 快接头 OR 分水歧管 OR 钎焊板换) (产能 OR 导入 OR 认证 OR 漏液 OR 交期)
(英维克 OR 奇鋐 OR 双鸿 OR 高澜股份 OR 同飞股份 OR Cooler Master) 液冷 订单 OR 出货
```

---

### 5. 云厂商 CapEx、电网与贸易合规组（CapEx, Grid & Compliance）
```text
# 英文检索流
"hyperscaler" OR "Microsoft" OR "Meta" OR "Google" OR "AWS" data center CapEx OR power queue OR nuclear PPA
AI data center tariff OR "Section 301" OR "export control" OR Mexico facility supply chain

# 中文检索流
智算中心 OR 算力中心 (招标 OR 能耗指标 OR 绿电直供 OR 核电PPA OR 并网排队)
AI服务器 (关税 OR 墨西哥工厂 OR 泰国工厂 OR 原产地审查 OR 实体清单)
```
