import feedparser

# مصادر كورة احترافية فقط
SOURCES = {
    'يلا كورة': 'https://www.yallakora.com/News/rss',
    'في الجول': 'https://www.filgoal.com/section/rss?sectionid=1'
}

def get_news():
    all_news = ""
    for source_name, url in SOURCES.items():
        feed = feedparser.parse(url)
        # سحب أول 6 أخبار من كل مصدر
        for entry in feed.entries[:6]:
            all_news += f"""
            <div class="card">
                <h3>{entry.title}</h3>
                <p>{entry.summary[:140]}...</p>
                <a class="btn" href="{entry.link}" target="_blank">فتح الخبر في {source_name}</a>
            </div>
            """
    return all_news

def update_site():
    news_content = get_news()
    html_template = f"""
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
        <title>صافرة | أخبار الكورة</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <header>
            <div class="logo">صافرة - SAFRA</div>
            <nav>
                <a href="index.html" class="nav-btn active">الأخبار</a>
                <a href="live.html" class="nav-btn">بث مباشر</a>
            </nav>
        </header>
        <main>
            {news_content}
        </main>
        <footer>
            موقع صافرة - تحديث آلي كل ساعة
        </footer>
    </body>
    </html>
    """
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_template)

if __name__ == "__main__":
    update_site()
    
