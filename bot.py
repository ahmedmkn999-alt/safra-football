import requests
from datetime import datetime, timedelta

def get_matches_data():
    # في المواقع الاحترافية نستخدم Football API، وهذا كود يحاكي جلب البيانات بدقة
    today = datetime.now().strftime('%d-%m-%Y')
    
    # هيكل بيانات المباراة (يمكنك لاحقاً ربطها بـ API للحصول على بيانات حقيقية لحظية)
    matches = [
        {
            "home": "مصر", "away": "جنوب أفريقيا", "time": "17:00", 
            "status": "لم تبدأ", "stadium": "استاد القاهرة الدولي", "referee": "مصطفى غربال"
        }
    ]
    
    html = ""
    for m in matches:
        html += f"""
        <div class="match-card" onclick="toggleDetails('detail-{m['home']}')">
            <div class="team-box">
                <span class="team-name">{m['home']}</span>
            </div>
            <div class="score-box">
                <span class="status-tag">{m['status']}</span>
                <span class="match-time">{m['time']}</span>
            </div>
            <div class="team-box">
                <span class="team-name">{m['away']}</span>
            </div>
            <div class="match-info" id="detail-{m['home']}">
                <p>📍 الملعب: {m['stadium']}</p>
                <p>⚖️ الحكم: {m['referee']}</p>
                <a href="live.html" class="live-btn-small">انتقل للبث المباشر</a>
            </div>
        </div>
        """
    return html

def update_site():
    matches_html = get_matches_data()
    html_template = f"""
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
        <title>صافرة | Safra Football</title>
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
            <div class="date-bar">مباريات اليوم - {datetime.now().strftime('%Y-%m-%d')}</div>
            {matches_html}
        </main>
        <script>
            function toggleDetails(id) {{
                var el = document.getElementById(id);
                el.style.display = (el.style.display === 'block') ? 'none' : 'block';
            }}
        </script>
    </body>
    </html>
    """
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_template)

if __name__ == "__main__":
    update_site()
    
