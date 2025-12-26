import feedparser
import os

def get_data():
    # سحب أخبار رياضية من "يلا كورة" و "في الجول"
    sources = {
        'يلا كورة': 'https://www.yallakora.com/News/rss',
        'في الجول': 'https://www.filgoal.com/section/rss?sectionid=1'
    }
    news_html = ""
    for name, url in sources.items():
        feed = feedparser.parse(url)
        for entry in feed.entries[:4]:
            news_html += f'''
            <div class="news-card">
                <h3>{entry.title}</h3>
                <a href="{entry.link}" target="_blank" class="news-btn">إقرأ الخبر في {name}</a>
            </div>'''
    return news_html

def update_site():
    news = get_data()
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
                <a href="index.html" class="nav-btn active">المباريات</a>
                <a href="live.html" class="nav-btn">البث المباشر</a>
            </nav>
        </header>
        <main>
            <h2 class="section-title">مباريات اليوم</h2>
            <div class="match-card">
                <div class="team">مصر</div>
                <div class="score">VS</div>
                <div class="team">جنوب أفريقيا</div>
                <div class="match-time">17:00</div>
                <div class="match-info">📍 استاد القاهرة الدولي | ⚖️ الحكم: مصطفى غربال</div>
            </div>
            <h2 class="section-title">أحدث الأخبار الرياضية</h2>
            {news}
        </main>
    </body>
    </html>'''
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_template)

if __name__ == "__main__":
    update_site()
