import feedparser

# مصادر الأخبار (تقدر تضيف أكتر)
SOURCES = {
    'BBC Arabic': 'https://feeds.bbci.co.uk/arabic/rss.xml',
    'Goal.com': 'https://www.goal.com/feeds/ar/news'
}

def get_news():
    all_news = ""
    for source_name, url in SOURCES.items():
        feed = feedparser.parse(url)
        for entry in feed.entries[:5]: # بياخد آخر 5 أخبار من كل مصدر
            all_news += f"""
            <div class="card">
                <h3>{entry.title}</h3>
                <p>{entry.summary[:150]}...</p>
                <a href="{entry.link}" target="_blank">التفاصيل في {source_name}</a>
            </div>
            """
    return all_news

def update_site():
    news_content = get_news()
    
    # تصميم الموقع الأساسي
    html_template = f"""
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <title>صافرة | أخبار الكورة العالمية</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <header>
            <h1>صافرة - Safra</h1>
            <nav>
                <a href="index.html">الأخبار</a>
                <a href="live.html">بث مباشر</a>
            </nav>
        </header>
        
        <main id="news-container">
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
          
