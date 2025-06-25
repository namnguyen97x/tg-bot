# 📖 HƯỚNG DẪN CHI TIẾT PHÁT TRIỂN BOT TELEGRAM VỚI GEMINI AI

## 🎯 TỔNG QUAN

Hướng dẫn này sẽ giúp bạn tạo một bot Telegram hoàn chỉnh sử dụng Google Gemini AI, từ việc thiết lập môi trường phát triển đến deploy lên production và giám sát.

---

## 📚 BƯỚC 1: THIẾT LẬP MÔI TRƯỜNG PHÁT TRIỂN

### 1.1 Cài đặt Python

#### Windows:
1. Truy cập [python.org](https://www.python.org/downloads/)
2. Tải phiên bản Python 3.8+ (khuyến nghị 3.11)
3. Chạy installer, **nhớ tick "Add Python to PATH"**
4. Kiểm tra cài đặt:
```cmd
python --version
pip --version
```

#### macOS:
```bash
# Sử dụng Homebrew (khuyến nghị)
brew install python@3.11

# Hoặc tải từ python.org
```

#### Linux (Ubuntu/Debian):
```bash
sudo apt update
sudo apt install python3.11 python3.11-pip python3.11-venv
```

### 1.2 Cài đặt IDE (Tùy chọn)

**Visual Studio Code** (khuyến nghị):
1. Tải từ [code.visualstudio.com](https://code.visualstudio.com/)
2. Cài đặt extension Python
3. Cài đặt extension Python Debugger

**PyCharm Community** (miễn phí):
1. Tải từ [jetbrains.com](https://www.jetbrains.com/pycharm/)
2. Chọn phiên bản Community (miễn phí)

### 1.3 Tạo thư mục dự án

```bash
# Tạo thư mục
mkdir telegram-gemini-bot
cd telegram-gemini-bot

# Khởi tạo Git
git init
```

---

## 🤖 BƯỚC 2: TẠO BOT TELEGRAM

### 2.1 Tương tác với BotFather

1. **Mở Telegram** trên điện thoại hoặc web
2. **Tìm kiếm @BotFather** và bắt đầu chat
3. **Gửi lệnh `/newbot`**

### 2.2 Thiết lập thông tin bot

**Hội thoại mẫu:**
```
You: /newbot
BotFather: Alright, a new bot. How are we going to call it? Please choose a name for your bot.

You: My AI Assistant
BotFather: Good. Now let's choose a username for your bot. It must end in `bot`. Like this, for example: TetrisBot or tetris_bot.

You: myaiassistant_bot
BotFather: Done! Congratulations on your new bot. You will find it at t.me/myaiassistant_bot. You can now add a description, about section and profile picture for your bot, see /help for a list of commands. By the way, when you've finished creating your cool bot, ping our Bot Support if you want a better username.

Use this token to access the HTTP API: 1234567890:ABCdefGHIjklMNOpqrsTUVwxyz
Keep your token secure and store it safely, it can be used by anyone to control your bot.
```

### 2.3 Lưu trữ token an toàn

**⚠️ QUAN TRỌNG:** Token bot là thông tin nhạy cảm, không được share công khai!

```bash
# Tạo file .env (sẽ được gitignore)
echo "TELEGRAM_BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrsTUVwxyz" > .env
```

### 2.4 Tùy chỉnh bot (tùy chọn)

```
/setdescription - Đặt mô tả cho bot
/setabouttext - Đặt thông tin "About"
/setuserpic - Upload ảnh đại diện
/setcommands - Thiết lập menu commands
```

**Thiết lập commands:**
```
/setcommands
start - Khởi động bot
help - Hiển thị trợ giúp
clear - Xóa lịch sử hội thoại
```

---

## 🔑 BƯỚC 3: LẤY GEMINI API KEY

### 3.1 Truy cập Google AI Studio

1. Mở [makersuite.google.com](https://makersuite.google.com/app/apikey)
2. Đăng nhập với tài khoản Google
3. Chấp nhận điều khoản sử dụng

### 3.2 Tạo API Key

1. **Click "Create API Key"**
2. **Chọn project Google Cloud** (hoặc tạo mới)
3. **Copy API key** được sinh ra
4. **Lưu vào file .env:**

```bash
echo "GEMINI_API_KEY=your_gemini_api_key_here" >> .env
```

### 3.3 Kiểm tra quota

- **Free tier**: 60 requests/phút
- **Paid tier**: Cao hơn tùy theo plan
- **Monitor usage** tại [console.cloud.google.com](https://console.cloud.google.com)

---

## 💻 BƯỚC 4: VIẾT MÃ NGUỒN BOT

### 4.1 Tạo virtual environment

```bash
# Tạo virtual environment
python -m venv venv

# Kích hoạt
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 4.2 Cài đặt dependencies

```bash
# Tạo requirements.txt
cat > requirements.txt << EOF
python-telegram-bot==20.7
google-generativeai==0.3.2
python-dotenv==1.0.0
asyncio
EOF

# Cài đặt
pip install -r requirements.txt
```

### 4.3 Cấu trúc file main.py

**File đã được tạo sẵn** với cấu trúc:
- ✅ Import các thư viện cần thiết
- ✅ Cấu hình logging
- ✅ Load environment variables
- ✅ Khởi tạo Gemini model
- ✅ Class TelegramGeminiBot với các methods:
  - `start_command()` - Xử lý /start
  - `help_command()` - Xử lý /help  
  - `clear_command()` - Xử lý /clear
  - `handle_message()` - Xử lý tin nhắn
  - `error_handler()` - Xử lý lỗi

### 4.4 Test bot locally

```bash
# Chạy bot
python main.py
```

**Nếu thành công:**
```
INFO - Initializing Telegram Gemini Bot...
INFO - Starting Telegram Gemini Bot...
```

**Test trên Telegram:**
1. Tìm bot bằng username đã tạo
2. Gửi `/start`
3. Thử hỏi: "Xin chào, bạn là ai?"

---

## 🌐 BƯỚC 5: DEPLOY LÊN RENDER

### 5.1 Chuẩn bị files cho deployment

**Procfile** (đã tạo):
```
web: python main.py
```

**runtime.txt** (đã tạo):
```
python-3.11.0
```

### 5.2 Push code lên GitHub

```bash
# Thêm .gitignore
cat > .gitignore << EOF
.env
__pycache__/
*.pyc
venv/
.DS_Store
EOF

# Commit code
git add .
git commit -m "Initial bot implementation"

# Tạo repository trên GitHub và push
git remote add origin https://github.com/yourusername/telegram-gemini-bot.git
git branch -M main
git push -u origin main
```

### 5.3 Tạo tài khoản Render

1. Truy cập [render.com](https://render.com)
2. **Sign up** bằng GitHub account
3. **Authorize** Render truy cập GitHub
4. **Verify email**

### 5.4 Deploy Web Service

1. **Dashboard Render > "New +" > "Web Service"**
2. **Connect repository** từ GitHub
3. **Cấu hình:**
   - **Name**: `telegram-gemini-bot`
   - **Environment**: `Python 3`
   - **Region**: Singapore (gần Việt Nam nhất)
   - **Branch**: `main`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python main.py`

### 5.5 Cấu hình Environment Variables

**Trong tab "Environment":**
- **Key**: `TELEGRAM_BOT_TOKEN`, **Value**: `your_bot_token`
- **Key**: `GEMINI_API_KEY`, **Value**: `your_gemini_api_key`

### 5.6 Deploy và monitor

1. **Click "Create Web Service"**
2. **Theo dõi logs** trong tab "Logs"
3. **Đợi deploy hoàn tất** (3-5 phút)
4. **Test bot** trên Telegram

**Logs thành công:**
```
==> Building...
==> Deploying...
INFO - Starting Telegram Gemini Bot...
==> Your service is live 🎉
```

---

## 📊 BƯỚC 6: THIẾT LẬP UPTIME ROBOT

### 6.1 Tạo tài khoản

1. Truy cập [uptimerobot.com](https://uptimerobot.com)
2. **Sign up** với email
3. **Verify email**
4. **Complete profile**

### 6.2 Thêm monitor cho bot

1. **Dashboard > "Add New Monitor"**
2. **Monitor Type**: `HTTP(s)`
3. **Friendly Name**: `Telegram Gemini Bot`
4. **URL**: URL từ Render (ví dụ: `https://telegram-gemini-bot.onrender.com`)
5. **Monitoring Interval**: `5 minutes`
6. **Monitor Timeout**: `30 seconds`
7. **HTTP Method**: `GET`

### 6.3 Thiết lập cảnh báo

#### Email Alerts:
1. **"Alert Contacts" > "Add Alert Contact"**
2. **Type**: `E-mail`
3. **Email**: your-email@domain.com
4. **Friendly Name**: `Primary Email`

#### Webhook (Advanced):
```json
{
  "url": "https://hooks.slack.com/your-webhook",
  "method": "POST",
  "headers": {
    "Content-Type": "application/json"
  },
  "body": {
    "text": "🚨 Bot is DOWN: *monitorFriendlyName* - *alertDetails*"
  }
}
```

### 6.4 Cấu hình notifications

**Alert Settings:**
- ✅ **When DOWN**: Immediately
- ✅ **When UP**: Immediately  
- ✅ **Daily/Weekly Reports**: Weekly
- ✅ **Monthly Reports**: Yes

---

## 🔧 BƯỚC 7: TỐI ƯU VÀ BẢO TRÌ

### 7.1 Monitoring và Logging

#### Xem logs trên Render:
```bash
# Trong Render dashboard
Logs > Filter by "ERROR" hoặc "INFO"
```

#### Local debugging:
```python
# Thêm vào main.py để debug
import logging
logging.getLogger().setLevel(logging.DEBUG)
```

### 7.2 Performance optimization

#### Giảm memory usage:
```python
# Trong handle_message()
import gc
gc.collect()  # Thu gom rác
```

#### Rate limiting:
```python
from functools import wraps
import time

def rate_limit(max_calls=10, time_window=60):
    def decorator(func):
        calls = []
        @wraps(func)
        async def wrapper(*args, **kwargs):
            now = time.time()
            calls[:] = [call for call in calls if call > now - time_window]
            if len(calls) >= max_calls:
                return await args[0].message.reply_text("⏳ Quá nhiều requests, vui lòng chờ!")
            calls.append(now)
            return await func(*args, **kwargs)
        return wrapper
    return decorator

# Sử dụng
@rate_limit(max_calls=5, time_window=60)
async def handle_message(self, update, context):
    # ... existing code
```

### 7.3 Error handling nâng cao

```python
import traceback
from telegram.error import NetworkError, TelegramError

async def error_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Enhanced error handling"""
    logger.error(f"Exception while handling update {update}:")
    logger.error(traceback.format_exc())
    
    if isinstance(context.error, NetworkError):
        # Network issues - retry
        logger.warning("Network error, will retry...")
    elif isinstance(context.error, TelegramError):
        # Telegram API issues
        logger.error(f"Telegram error: {context.error}")
    else:
        # Other errors
        logger.error(f"Unexpected error: {context.error}")
    
    # Notify user if possible
    if update and update.effective_message:
        try:
            await update.effective_message.reply_text(
                "❌ Đã xảy ra lỗi kỹ thuật. Đội ngũ kỹ thuật đã được thông báo!"
            )
        except:
            pass
```

### 7.4 Health check endpoint

```python
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading

class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/health':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(b'{"status": "healthy", "bot": "running"}')
        else:
            self.send_response(404)
            self.end_headers()

def start_health_server():
    server = HTTPServer(('0.0.0.0', 8080), HealthHandler)
    server.serve_forever()

# Trong main()
health_thread = threading.Thread(target=start_health_server, daemon=True)
health_thread.start()
```

---

## 🚀 BƯỚC 8: TÍNH NĂNG NÂNG CAO (OPTIONAL)

### 8.1 Database integration

```python
import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('bot.db', check_same_thread=False)
        self.create_tables()
    
    def create_tables(self):
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                username TEXT,
                first_name TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.conn.commit()
    
    def add_user(self, user_id, username, first_name):
        self.conn.execute(
            'INSERT OR IGNORE INTO users (user_id, username, first_name) VALUES (?, ?, ?)',
            (user_id, username, first_name)
        )
        self.conn.commit()
```

### 8.2 Conversation memory

```python
class ConversationMemory:
    def __init__(self):
        self.conversations = {}
    
    def add_message(self, user_id, role, content):
        if user_id not in self.conversations:
            self.conversations[user_id] = []
        
        self.conversations[user_id].append({
            'role': role,
            'content': content,
            'timestamp': time.time()
        })
        
        # Giữ tối đa 10 tin nhắn
        if len(self.conversations[user_id]) > 10:
            self.conversations[user_id] = self.conversations[user_id][-10:]
    
    def get_context(self, user_id):
        if user_id not in self.conversations:
            return ""
        
        context = ""
        for msg in self.conversations[user_id][-5:]:  # 5 tin nhắn gần nhất
            context += f"{msg['role']}: {msg['content']}\n"
        
        return context
```

### 8.3 Admin commands

```python
ADMIN_IDS = [123456789]  # Thay bằng Telegram user ID của bạn

async def admin_stats(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Lệnh chỉ admin"""
    if update.effective_user.id not in ADMIN_IDS:
        await update.message.reply_text("❌ Không có quyền truy cập!")
        return
    
    # Thống kê
    total_users = len(self.conversations)
    stats_text = f"""
📊 **Thống kê Bot**
👥 Tổng users: {total_users}
💬 Tin nhắn hôm nay: {daily_messages}
⚡ Uptime: {uptime}
🧠 Memory usage: {memory_usage}MB
    """
    await update.message.reply_text(stats_text, parse_mode='Markdown')

# Thêm vào setup_handlers()
self.application.add_handler(CommandHandler("stats", self.admin_stats))
```

---

## 🛡️ BẢO MẬT VÀ BEST PRACTICES

### 9.1 Environment variables security

```bash
# Không commit .env
echo ".env" >> .gitignore

# Sử dụng .env.example
cp .env .env.example
# Xóa values trong .env.example, chỉ giữ keys
```

### 9.2 Input validation

```python
import re

def sanitize_input(text):
    """Làm sạch input từ user"""
    # Loại bỏ HTML tags
    text = re.sub('<[^<]+?>', '', text)
    # Giới hạn độ dài
    text = text[:1000]
    # Loại bỏ ký tự đặc biệt nguy hiểm
    text = re.sub(r'[<>"\']', '', text)
    return text.strip()

# Sử dụng trong handle_message
user_message = sanitize_input(update.message.text)
```

### 9.3 Rate limiting nâng cao

```python
from collections import defaultdict
import time

class RateLimiter:
    def __init__(self):
        self.calls = defaultdict(list)
    
    def is_allowed(self, user_id, max_calls=10, time_window=60):
        now = time.time()
        user_calls = self.calls[user_id]
        
        # Xóa calls cũ
        user_calls[:] = [call for call in user_calls if call > now - time_window]
        
        if len(user_calls) >= max_calls:
            return False
        
        user_calls.append(now)
        return True

# Sử dụng
rate_limiter = RateLimiter()

async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    
    if not rate_limiter.is_allowed(user_id):
        await update.message.reply_text("⏳ Bạn đang gửi tin nhắn quá nhanh!")
        return
    
    # ... xử lý tin nhắn
```

---

## 📈 SCALING VÀ PERFORMANCE

### 10.1 Webhook vs Polling

**Polling (hiện tại):** Bot chủ động check tin nhắn mới
**Webhook (production):** Telegram push tin nhắn đến bot

```python
# Để chuyển sang webhook, thêm vào main.py
def setup_webhook(self):
    """Setup webhook for production"""
    webhook_url = f"https://your-domain.com/webhook/{TELEGRAM_BOT_TOKEN}"
    self.application.run_webhook(
        listen="0.0.0.0",
        port=int(os.environ.get('PORT', 8080)),
        webhook_url=webhook_url,
        secret_token="your-secret-token"
    )
```

### 10.2 Caching responses

```python
from functools import lru_cache
import hashlib

@lru_cache(maxsize=100)
def get_cached_response(prompt_hash):
    """Cache Gemini responses"""
    # Implement caching logic
    pass

def get_prompt_hash(prompt):
    return hashlib.md5(prompt.encode()).hexdigest()

# Trong handle_message
prompt_hash = get_prompt_hash(prompt)
cached_response = get_cached_response(prompt_hash)

if cached_response:
    await update.message.reply_text(cached_response)
    return

# Gọi Gemini API và cache kết quả
```

### 10.3 Database scaling

```python
# Sử dụng PostgreSQL cho production
import psycopg2
from urllib.parse import urlparse

DATABASE_URL = os.environ.get('DATABASE_URL')

def get_db_connection():
    if DATABASE_URL:
        # Production - PostgreSQL
        url = urlparse(DATABASE_URL)
        conn = psycopg2.connect(
            database=url.path[1:],
            user=url.username,
            password=url.password,
            host=url.hostname,
            port=url.port
        )
    else:
        # Development - SQLite
        conn = sqlite3.connect('bot.db')
    
    return conn
```

---

## 🔍 TROUBLESHOOTING GUIDE

### Lỗi thường gặp:

#### 1. Bot không phản hồi
```bash
# Kiểm tra logs
# Render: Dashboard > Logs
# Local: Terminal output

# Các nguyên nhân phổ biến:
- Sai token
- Sai API key
- Network issues
- Rate limit exceeded
```

#### 2. Gemini API errors
```python
# Xử lý các lỗi Gemini
try:
    response = model.generate_content(prompt)
except Exception as e:
    if "quota exceeded" in str(e).lower():
        await update.message.reply_text("🚫 Đã hết quota API, vui lòng thử lại sau!")
    elif "safety" in str(e).lower():
        await update.message.reply_text("⚠️ Nội dung không phù hợp, vui lòng thử câu hỏi khác!")
    else:
        logger.error(f"Gemini error: {e}")
        await update.message.reply_text("❌ Lỗi AI, vui lòng thử lại!")
```

#### 3. Memory issues
```bash
# Render free tier: 512MB RAM
# Tối ưu:
- Giảm conversation history
- Clear cache định kỳ  
- Sử dụng generator thay vì list
```

#### 4. Deploy issues
```bash
# Build fails:
- Kiểm tra requirements.txt
- Kiểm tra Python version trong runtime.txt
- Xem build logs để debug

# Runtime fails:
- Kiểm tra environment variables
- Kiểm tra start command
- Xem application logs
```

---

## 📞 HỖ TRỢ VÀ CỘNG ĐỒNG

### Tài nguyên học tập:
- [Python Telegram Bot Documentation](https://docs.python-telegram-bot.org/)
- [Google Gemini API Docs](https://ai.google.dev/docs)
- [Render Documentation](https://render.com/docs)

### Cộng đồng:
- [Telegram Bot Developers](https://t.me/BotDevelopers)
- [Python Vietnam](https://www.facebook.com/groups/pythonvietnam/)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/python-telegram-bot)

---

**🎉 Chúc mừng! Bạn đã hoàn thành việc tạo một bot Telegram AI hoàn chỉnh!**

Nếu có thắc mắc, hãy tạo issue trên GitHub hoặc liên hệ qua email. 