import requests
from datetime import datetime, timedelta

def get_matches():
    # هنا نستخدم API لجلب المباريات (يمكنك استبدال الرابط بـ API مفضل)
    # هذا مثال لهيكل البيانات الذي سيتم عرضه
    today = datetime.now().strftime('%Y-%m-%d')
    past_days = (datetime.now() - timedelta(days=3)).strftime('%Y-%m-%d')
    
    # محاكاة لجلب البيانات (في الواقع ستحتاج API Key)
    matches_html = ""
    
    # مثال لكارت مباراة
    matches_html += f"""
    <div class="match-card" onclick="showDetails('stadium-1', 'referee-1')">
        <div class="team">الأهلي</div>
        <div class="score">VS</div>
        <div class="team">الزمالك</div>
        <div class="time">الساعة 9:00 م</div>
        <div class="details" id="details-1">
            الملعب: استاد القاهرة | الحكم: إبراهيم نور الدين
        </div>
    </div>
    """
    return matches_html

def update_site():
    content = get_matches()
    html_template = f"""
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>صافرة | جدول المباريات</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <header>
            <div class="logo">صافرة - Safra</div>
            <nav>
                <a href="index.html" class="nav-btn active">المباريات</a>
                <a href="live.html" class="nav-btn">البث المباشر</a>
            </nav>
        </header>
        <main>
            <h2 class="section-title">مباريات اليوم</h2>
            {content}
            <h2 class="section-title">نتائج الـ 3 أيام الماضية</h2>
            <div class="past-matches">
                <div class="match-card finished">
                    <div class="team">ريال مدريد</div>
                    <div class="score">3 - 1</div>
                    <div class="team">برشلونة</div>
                    <div class="status">منتهية (إحصائيات)</div>
                </div>
            </div>
        </main>
        <script>
            function showDetails(stadium, referee) {{
                alert("الملعب: " + stadium + "\\nالحكم: " + referee);
            }}
        </script>
    </body>
    </html>
    """
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_template)

if __name__ == "__main__":
    update_site()
    
