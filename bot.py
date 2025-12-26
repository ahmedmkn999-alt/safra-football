import feedparser

# مصادر كورة متخصصة فقط
SOURCES = {
    'في الجول': 'https://www.filgoal.com/section/rss?sectionid=1',
    'يلا كورة': 'https://www.yallakora.com/News/rss'
}

def get_news():
    all_news = ""
    for source_name, url in SOURCES.items():
        feed = feedparser.parse(url)
        for entry in feed.entries[:6]:
            all_news += f"""
            <div class="card">
                <h3>{entry.title}</h3>
                <p>{entry.summary[:120]}...</p>
                <a class="btn" href="{entry.link}" target="_blank">إقرأ الخبر كاملاً في {source_name}</a>
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
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>صافرة | أخبار الكورة العالمية</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <header>
            <div class="logo">صافرة - Safra</div>
            <nav>
                <a href="index.html" class="nav-btn active">الأخبار</a>
                <a href="live.html" class="nav-btn">بث مباشر</a>
            </nav>
        </header>
        <main>
            {news_content}
        </main>
        <footer>
            <p>موقع صافرة - تحديث تلقائي كل ساعة</p>
        </footer>
    </body>
    </html>
    """
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_template)

if __name__ == "__main__":
    update_site()
