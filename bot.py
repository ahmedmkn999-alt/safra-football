import feedparser

def get_news():
    # سحب أخبار يلا كورة وفي الجول
    sources = {'يلا كورة': 'https://www.yallakora.com/News/rss', 'في الجول': 'https://www.filgoal.com/section/rss?sectionid=1'}
    all_news = ""
    for name, url in sources.items():
        feed = feedparser.parse(url)
        for entry in feed.entries[:5]:
            all_news += f'<div style="background:#1a1a1a; margin:10px; padding:15px; border-radius:10px; border-right:5px solid #ccff00;">'
            all_news += f'<h3 style="color:#ccff00;">{entry.title}</h3>'
            all_news += f'<a href="{entry.link}" style="color:#fff; text-decoration:none; font-weight:bold;">إقرأ المزيد في {name}</a></div>'
    return all_news

def update():
    news = get_news()
    # الجدول مع التصميم في ملف واحد
    html = f"""
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>صافرة - SAFRA</title>
    </head>
    <body style="background:#000; color:#fff; font-family:sans-serif; margin:0; padding:0;">
        <header style="background:#ccff00; color:#000; padding:20px; text-align:center;">
            <h1>صافرة - SAFRA</h1>
            <nav><a href="live.html" style="color:#000; font-weight:bold;">بث مباشر</a></nav>
        </header>
        <main style="padding:10px;">
            <h2 style="color:#ccff00;">مباريات اليوم</h2>
            <div style="background:#1a1a1a; padding:20px; border-radius:15px; text-align:center; border:1px solid #333;">
                <div style="font-size:20px;">مصر VS جنوب أفريقيا</div>
                <div style="font-size:30px; color:#ccff00; font-weight:bold; margin:10px 0;">17:00</div>
                <div style="color:#888;">📍 استاد القاهرة | ⚖️ مصطفى غربال</div>
            </div>
            <h2 style="color:#ccff00;">أحدث الأخبار</h2>
            {news}
        </main>
    </body>
    </html>
    """
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)

if __name__ == "__main__":
    update()
