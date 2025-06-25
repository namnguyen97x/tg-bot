# 📝 CHANGELOG

## [2024-01-17] - Cập nhật API Gemini mới nhất

### ✨ Cập nhật chính:
- **Cập nhật lên Gemini API v2.5**: Sử dụng `google-genai` package mới
- **Model mới**: Chuyển từ `gemini-pro` sang `gemini-2.5-flash`
- **Syntax mới**: Cập nhật cách gọi API theo [tài liệu chính thức](https://ai.google.dev/gemini-api/docs)

### 🔧 Thay đổi kỹ thuật:
- Thay đổi import: `from google import genai` thay vì `import google.generativeai as genai`
- Khởi tạo client mới: `genai.Client(api_key=GEMINI_API_KEY)`
- Gọi API mới: `client.models.generate_content(model="gemini-2.5-flash", contents=prompt)`

### 📊 Cải thiện hiệu suất:
- **Gemini 2.5 Flash**: Nhanh hơn và chính xác hơn so với phiên bản cũ
- **Tối ưu cost**: Model mới có chi phí thấp hơn
- **Multimodal**: Hỗ trợ tốt hơn cho text, image, video

### 📚 Cập nhật tài liệu:
- Cập nhật tất cả links đến tài liệu API mới
- Hướng dẫn lấy API key từ Google AI Studio mới
- Thêm ghi chú về rate limiting và quota

### ⚠️ Breaking Changes:
- **Requirements.txt**: Đổi từ `google-generativeai` sang `google-genai`
- **Code syntax**: Cần cập nhật cách gọi API
- **API endpoints**: Sử dụng endpoints mới của Gemini 2.5

### 🔄 Migration Guide:
1. Cập nhật `requirements.txt`
2. Thay đổi import statements
3. Cập nhật cách khởi tạo client
4. Kiểm tra và test lại bot

---

## [2024-01-17] - Release đầu tiên

### ✨ Tính năng:
- Bot Telegram cơ bản với Gemini AI
- Commands: /start, /help, /clear
- Xử lý tin nhắn và trả lời thông minh
- Deploy instructions cho Render
- Uptime monitoring với UptimeRobot

### 📚 Tài liệu:
- README.md chi tiết
- SETUP_GUIDE.md nhanh
- HUONG_DAN_CHI_TIET.md đầy đủ 