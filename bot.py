import feedparser

def get_news():
    # سحب أخبار رياضية حقيقية
    sources = {
        'يلا كورة': 'https://www.yallakora.com/News/rss',
        'في الجول': 'https://www.filgoal.com/section/rss?sectionid=1'
    }
    html = ""
    for name, url in sources.items():
        feed = feedparser.parse(url)
        for entry in feed.entries[:4]:
            html += f'''
            <div class="news-card">
                <h3>{entry.title}</h3>
                <a href="{entry.link}" target="_blank" class="read-more">إقرأ في {name}</a>
            </div>
            '''
    return html

def update_site():
    news = get_news()
    # كود الصفحة الرئيسي بتصميم الموبايل
    html_template = f'''
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
        <title>صافرة - SAFRA</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <header>
            <div class="logo">صافرة - SAFRA</div>
            <nav>
                <a href="index.html" class="nav-item active">المباريات</a>
                <a href="live.html" class="nav-item">بث مباشر</a>
            </nav>
        </header>
        <main>
            <div class="match-center">
                <div class="match-card">
                    <div class="team">مصر</div>
                    <div class="score">VS</div>
                    <div class="team">جنوب أفريقيا</div>
                    <div class="time">17:00</div>
                    <div class="info">📍 استاد القاهرة | ⚖️ مصطفى غربال</div>
                </div>
            </div>
            <h2 class="title">أحدث الأخبار الرياضية</h2>
            {news}
        </main>
    </body>
    </html>
    '''
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_template)

if __name__ == "__main__":
    update_site()
    
