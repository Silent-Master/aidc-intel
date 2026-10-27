import os
import json
import xml.etree.ElementTree as ET
from datetime import datetime, timezone

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(ROOT_DIR, "data")

def generate_ics():
    """Generate RFC 5545 iCalendar anchors.ics file."""
    index_file = os.path.join(DATA_DIR, "index.json")
    if not os.path.exists(index_file):
        return
    with open(index_file, "r", encoding="utf-8") as f:
        days = json.load(f).get("days", [])
    
    events = []
    for day in days:
        day_path = os.path.join(DATA_DIR, f"{day}.json")
        if not os.path.exists(day_path):
            continue
        try:
            with open(day_path, "r", encoding="utf-8") as f:
                d = json.load(f)
            anchors = d.get("s7_timeline_ics", [])
            for a in anchors:
                events.append({
                    "date": a.get("date", day),
                    "title": a.get("event_title", "AIDC 关键时间锚点"),
                    "entity": a.get("entity", "AIDC 核心供应链"),
                    "note": a.get("reminder_note", ""),
                    "pub_date": day
                })
        except Exception:
            pass

    ics_lines = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//AIDC Supply Chain Intelligence Hub//CN",
        "CALSCALE:GREGORIAN",
        "METHOD:PUBLISH",
        "X-WR-CALNAME:AIDC 智算供应链时间锚点日历",
        "X-WR-TIMEZONE:Asia/Shanghai",
        "X-WR-CALDESC:每天早报发布后自动更新，汇聚 AIDC 财报、芯片量产、新机柜出货、行业峰会等确定性时间锚点"
    ]

    now_stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")

    for i, ev in enumerate(events):
        d_str = ev["date"].replace("-", "")
        uid = f"aidc-{d_str}-{i}@aidc-intel"
        title = ev["title"].replace(",", "\\,").replace(";", "\\;")
        desc = f"【关联主体】{ev['entity']}\\n【关注要点】{ev['note']}".replace(",", "\\,").replace(";", "\\;")
        ics_lines.extend([
            "BEGIN:VEVENT",
            f"UID:{uid}",
            f"DTSTAMP:{now_stamp}",
            f"DTSTART;VALUE=DATE:{d_str}",
            f"SUMMARY:[AIDC锚点] {title}",
            f"DESCRIPTION:{desc}",
            "STATUS:CONFIRMED",
            "TRANSP:TRANSPARENT",
            "BEGIN:VALARM",
            "TRIGGER:-PT15H",
            "ACTION:DISPLAY",
            f"DESCRIPTION:提前1天提醒：{title}",
            "END:VALARM",
            "END:VEVENT"
        ])

    ics_lines.append("END:VCALENDAR")

    out_path = os.path.join(ROOT_DIR, "anchors.ics")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\r\n".join(ics_lines) + "\r\n")
    print(f"Updated anchors.ics with {len(events)} events.")


def generate_rss():
    """Generate RSS 2.0 feed.xml."""
    index_file = os.path.join(DATA_DIR, "index.json")
    if not os.path.exists(index_file):
        return
    with open(index_file, "r", encoding="utf-8") as f:
        days = json.load(f).get("days", [])
    
    rss = ET.Element("rss", version="2.0", attrib={"xmlns:atom": "http://www.w3.org/2005/Atom"})
    channel = ET.SubElement(rss, "channel")

    ET.SubElement(channel, "title").text = "AIDC 智算中心供应链情报"
    ET.SubElement(channel, "link").text = "https://nohho.github.io/aidc-intel/"
    ET.SubElement(channel, "description").text = "AI 数据中心物理基建、算力机柜、供电配电、高速互连、液冷温控每日供应链情报。面向采购、供应链管理及硬件工程团队。"
    ET.SubElement(channel, "language").text = "zh-CN"
    ET.SubElement(channel, "lastBuildDate").text = datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S GMT")

    atom_link = ET.SubElement(channel, "atom:link")
    atom_link.set("href", "https://nohho.github.io/aidc-intel/feed.xml")
    atom_link.set("rel", "self")
    atom_link.set("type", "application/rss+xml")

    # Add items from last 14 days in reverse
    for day in reversed(days[-14:]):
        day_path = os.path.join(DATA_DIR, f"{day}.json")
        if not os.path.exists(day_path):
            continue
        try:
            with open(day_path, "r", encoding="utf-8") as f:
                d = json.load(f)
            report = d.get("daily_report", {})
            headlines = d.get("s2_headlines", [])
            alerts = d.get("s6_alerts", [])

            item = ET.SubElement(channel, "item")
            ET.SubElement(item, "title").text = f"【AIDC情报 {day}】{report.get('headline', '')[:100]}"
            item_link = f"https://nohho.github.io/aidc-intel/#date={day}"
            ET.SubElement(item, "link").text = item_link
            ET.SubElement(item, "guid", isPermaLink="true").text = item_link
            
            # Formulate rich HTML summary
            desc_parts = [
                f"<p><strong>头条快讯：</strong>{report.get('headline', '')}</p>",
                "<h4>核心头条拆解：</h4>"
            ]
            for h in headlines:
                desc_parts.append(f"<p><strong>{h.get('title', '')}</strong><br>{h.get('summary', '')}</p>")
            
            if alerts:
                desc_parts.append("<h4>齐套预警与采购建议：</h4><ul>")
                for a in alerts[:4]:
                    desc_parts.append(f"<li>[{a.get('risk_level')}] {a.get('material')}: {a.get('action_recommendation')} (交期: {a.get('lead_time_status')})</li>")
                desc_parts.append("</ul>")

            ET.SubElement(item, "description").text = "".join(desc_parts)

            dt = datetime.strptime(day, "%Y-%m-%d")
            ET.SubElement(item, "pubDate").text = dt.strftime("%a, %d %b %Y 00:30:00 GMT")
        except Exception:
            pass

    tree = ET.ElementTree(rss)
    ET.indent(tree, space="  ", level=0)
    out_path = os.path.join(ROOT_DIR, "feed.xml")
    tree.write(out_path, encoding="utf-8", xml_declaration=True)
    print("Updated feed.xml.")


def generate_sitemap():
    """Generate sitemap.xml."""
    index_file = os.path.join(DATA_DIR, "index.json")
    if not os.path.exists(index_file):
        return
    with open(index_file, "r", encoding="utf-8") as f:
        days = json.load(f).get("days", [])

    urlset = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")

    # Main page
    main_url = ET.SubElement(urlset, "url")
    ET.SubElement(main_url, "loc").text = "https://nohho.github.io/aidc-intel/"
    ET.SubElement(main_url, "changefreq").text = "daily"
    ET.SubElement(main_url, "priority").text = "1.0"
    if days:
        ET.SubElement(main_url, "lastmod").text = days[-1]

    for day in reversed(days):
        day_url = ET.SubElement(urlset, "url")
        ET.SubElement(day_url, "loc").text = f"https://nohho.github.io/aidc-intel/#date={day}"
        ET.SubElement(day_url, "changefreq").text = "never"
        ET.SubElement(day_url, "priority").text = "0.8"
        ET.SubElement(day_url, "lastmod").text = day

    tree = ET.ElementTree(urlset)
    ET.indent(tree, space="  ", level=0)
    out_path = os.path.join(ROOT_DIR, "sitemap.xml")
    tree.write(out_path, encoding="utf-8", xml_declaration=True)
    print("Updated sitemap.xml.")


if __name__ == "__main__":
    generate_ics()
    generate_rss()
    generate_sitemap()
