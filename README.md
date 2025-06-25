# 🤖 Telegram Bot với Gemini AI

Một bot Telegram thông minh sử dụng Google Gemini AI để trả lời câu hỏi và hỗ trợ người dùng.

## 🎯 Mục đích dự án

Bot này được phát triển để:
- Tạo ra một trợ lý AI thông minh trên Telegram
- Tích hợp công nghệ Gemini AI của Google
- Cung cấp trải nghiệm tương tác tự nhiên và hữu ích
- Học cách deploy ứng dụng lên cloud và giám sát uptime

## ✨ Tính năng chính

- ✅ **Trả lời câu hỏi thông minh**: Sử dụng Gemini AI để trả lời mọi câu hỏi
- ✅ **Hỗ trợ tiếng Việt**: Bot được tối ưu để trả lời bằng tiếng Việt
- ✅ **Xử lý tin nhắn dài**: Tự động chia nhỏ tin nhắn quá dài
- ✅ **Logging chi tiết**: Theo dõi hoạt động bot
- ✅ **Error handling**: Xử lý lỗi graceful
- ✅ **Commands hữu ích**: /start, /help, /clear

## 📋 Yêu cầu hệ thống

- **Python**: 3.8 hoặc cao hơn
- **Thư viện cần thiết**:
  - `python-telegram-bot==20.7`
  - `google-genai` (API mới nhất của Google)
  - `python-dotenv==1.0.0`
- **API Keys**:
  - Telegram Bot Token (từ BotFather)
  - Gemini API Key (từ Google AI Studio)

## 🚀 Hướng dẫn cài đặt

### Bước 1: Cài đặt môi trường phát triển

#### Cài đặt Python
1. Tải và cài đặt Python từ [python.org](https://www.python.org/downloads/)
2. Kiểm tra cài đặt:
```bash
python --version
pip --version
```

#### Cài đặt Git (nếu chưa có)
```bash
# Windows
# Tải từ https://git-scm.com/downloads

# macOS
brew install git

# Ubuntu/Debian
sudo apt update
sudo apt install git
```

### Bước 2: Clone repository

```bash
git clone <repository-url>
cd tg-bot
```

### Bước 3: Tạo virtual environment

```bash
# Tạo virtual environment
python -m venv venv

# Kích hoạt virtual environment
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### Bước 4: Cài đặt dependencies

```bash
pip install -r requirements.txt
```

### Bước 5: Tạo bot Telegram

1. **Mở Telegram và tìm @BotFather**
2. **Gửi lệnh `/newbot`**
3. **Đặt tên cho bot** (ví dụ: "My AI Assistant")
4. **Đặt username** (phải kết thúc bằng "bot", ví dụ: "myaiassistant_bot")
5. **Lưu lại token** mà BotFather cung cấp

### Bước 6: Lấy Gemini API Key

1. **Truy cập [Google AI Studio](https://ai.google.dev/gemini-api/docs)**
2. **Đăng nhập** với tài khoản Google
3. **Click "Get a Gemini API Key"**
4. **Tạo API Key mới** trong Google AI Studio
5. **Copy và lưu lại API Key**

> **Lưu ý**: API đã được cập nhật và sử dụng model `gemini-2.5-flash` mới nhất với hiệu suất tốt hơn.

### Bước 7: Cấu hình environment variables

1. **Copy file mẫu**:
```bash
cp env.example .env
```

2. **Chỉnh sửa file `.env`**:
```env
TELEGRAM_BOT_TOKEN=your_actual_telegram_bot_token
GEMINI_API_KEY=your_actual_gemini_api_key
LOG_LEVEL=INFO
```

## 🏃‍♂️ Chạy bot cục bộ

```bash
# Đảm bảo virtual environment đã được kích hoạt
python main.py
```

Nếu thành công, bạn sẽ thấy:
```
INFO - Initializing Telegram Gemini Bot...
INFO - Starting Telegram Gemini Bot...
```

## 🌐 Deploy lên Render

### Bước 1: Tạo tài khoản Render

1. Truy cập [render.com](https://render.com)
2. Đăng ký tài khoản (có thể dùng GitHub)
3. Verify email

### Bước 2: Chuẩn bị code

1. **Push code lên GitHub**:
```bash
git add .
git commit -m "Initial commit"
git push origin main
```

### Bước 3: Tạo Web Service trên Render

1. **Trong dashboard Render, click "New +"**
2. **Chọn "Web Service"**
3. **Connect GitHub repository**
4. **Cấu hình service**:
   - **Name**: `telegram-gemini-bot`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python main.py`

### Bước 4: Cấu hình Environment Variables

Trong tab "Environment", thêm:
- `TELEGRAM_BOT_TOKEN`: Token từ BotFather
- `GEMINI_API_KEY`: API key từ Google AI Studio

### Bước 5: Deploy

1. Click "Create Web Service"
2. Chờ quá trình build và deploy hoàn tất
3. Bot sẽ tự động chạy khi deploy thành công

## 📊 Thiết lập Uptime Robot

### Bước 1: Tạo tài khoản

1. Truy cập [uptimerobot.com](https://uptimerobot.com)
2. Đăng ký tài khoản miễn phí
3. Verify email

### Bước 2: Thêm monitor

1. **Click "Add New Monitor"**
2. **Cấu hình monitor**:
   - **Monitor Type**: HTTP(s)
   - **Friendly Name**: Telegram Gemini Bot
   - **URL**: URL của ứng dụng trên Render
   - **Monitoring Interval**: 5 minutes

### Bước 3: Thiết lập cảnh báo

1. **Trong "Alert Contacts"**, thêm:
   - Email notifications
   - SMS (nếu cần)
   - Webhook (advanced)

2. **Cấu hình thông báo**:
   - Khi service down
   - Khi service up trở lại

## 📝 Ví dụ sử dụng

### Commands cơ bản

```
/start - Khởi động bot và xem hướng dẫn
/help - Hiển thị trợ giúp chi tiết  
/clear - Xóa lịch sử hội thoại
```

### Ví dụ hội thoại

**User**: "Giải thích về machine learning"

**Bot**: "Machine Learning (Học máy) là một nhánh của trí tuệ nhân tạo (AI) cho phép máy tính học hỏi và cải thiện hiệu suất từ dữ liệu mà không cần được lập trình cụ thể cho từng tác vụ..."

## 🔧 Cấu trúc dự án

```
tg-bot/
├── main.py              # Code chính của bot
├── requirements.txt     # Dependencies
├── env.example         # Mẫu file environment
├── Procfile            # Cấu hình cho Render
├── runtime.txt         # Phiên bản Python
└── README.md           # Tài liệu này
```

## 🛠️ Customization

### Thêm tính năng mới

1. **Chỉnh sửa class `TelegramGeminiBot`** trong `main.py`
2. **Thêm handler mới** trong method `setup_handlers()`
3. **Implement logic** cho tính năng

### Thay đổi prompt Gemini

Chỉnh sửa biến `prompt` trong method `handle_message()`:

```python
prompt = f"""
Bạn là một chuyên gia về {domain}. 
Hãy trả lời câu hỏi một cách chuyên sâu và chi tiết.

Câu hỏi: {user_message}
"""
```

## 🐛 Troubleshooting

### Bot không phản hồi

1. **Kiểm tra logs** trên Render
2. **Verify API keys** trong environment variables
3. **Kiểm tra network connectivity**

### Lỗi Gemini API

```python
# Thêm error handling chi tiết
try:
    response = model.generate_content(prompt)
except Exception as e:
    logger.error(f"Gemini API error: {e}")
```

### Memory issues trên Render

- Render free tier có giới hạn 512MB RAM
- Tối ưu code để sử dụng ít memory hơn
- Consider upgrade plan nếu cần

## 📈 Monitoring và Maintenance

### Logs

- **Render**: Xem logs trong dashboard
- **Local**: Logs hiển thị trong terminal

### Health checks

```python
# Thêm endpoint health check
async def health_check(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot is healthy! 🟢")
```

### Cập nhật dependencies

```bash
pip list --outdated
pip install --upgrade package_name
pip freeze > requirements.txt
```

## 🤝 Đóng góp

1. Fork repository
2. Tạo branch mới: `git checkout -b feature/amazing-feature`
3. Commit changes: `git commit -m 'Add amazing feature'`
4. Push to branch: `git push origin feature/amazing-feature`
5. Tạo Pull Request

## 📄 License

Dự án này sử dụng MIT License. Xem file `LICENSE` để biết thêm chi tiết.

## 📞 Liên hệ và hỗ trợ

- **Email**: your-email@example.com
- **GitHub Issues**: [Tạo issue mới](https://github.com/your-username/tg-bot/issues)
- **Telegram**: @your_telegram_username

## 🙏 Lời cảm ơn

- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) - Thư viện Telegram Bot
- [Google Gemini](https://ai.google.dev/) - AI API
- [Render](https://render.com) - Hosting platform
- [Uptime Robot](https://uptimerobot.com) - Monitoring service

---

⭐ **Nếu project này hữu ích, hãy cho một star nhé!** ⭐ 