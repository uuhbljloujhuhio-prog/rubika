import os
import requests

# ======= توکن ربات =======
BOT_TOKEN = "HAECC0BFUTKAJHIYHVMEFTSFLKWIQZZDVETWWHMLYGAGYFYNYBPFNRMAJSKQZNJV"
# =========================

# تابع دریافت پیام‌ها
def get_updates():
    url = f"https://api.rubika.ir/bot{BOT_TOKEN}/getUpdates"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

# تابع ارسال پیام
def send_message(chat_id, text):
    url = f"https://api.rubika.ir/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": chat_id, "text": text}
    requests.post(url, json=data)

# تابع جستجوی آهنگ (نسخه ساده - فقط لینک نمونه)
def search_song(song_name):
    # این فقط یک نمونه است؛ می‌توان بعداً API واقعی یا لینک رایگان اضافه کرد
    return f"https://example.com/search?q={song_name.replace(' ', '+')}"

# تابع اصلی ربات
def main():
    print("ربات آماده است!")
    updates = get_updates()
    if updates:
        for update in updates.get("result", []):
            message = update.get("message", {})
            chat_id = message.get("chat", {}).get("id")
            text = message.get("text")
            if chat_id and text:
                # اگر پیام حاوی دستور جستجوی آهنگ بود
                if text.startswith("/song "):
                    song_name = text.replace("/song ", "")
                    song_link = search_song(song_name)
                    send_message(chat_id, f"لینک آهنگ {song_name}: {song_link}")
                else:
                    send_message(chat_id, f"پیام شما دریافت شد: {text}")

if name == "__main__":
    main()
