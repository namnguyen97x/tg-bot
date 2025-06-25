# 🚀 HƯỚNG DẪN SETUP NHANH

## 📋 CHECKLIST SETUP

### ✅ Bước 1: Môi trường phát triển
- [ ] Cài Python 3.8+
- [ ] Cài Git
- [ ] Tạo virtual environment
- [ ] Clone/tạo project

### ✅ Bước 2: Tạo Bot Telegram  
- [ ] Chat với @BotFather
- [ ] Tạo bot mới với `/newbot`
- [ ] Lưu token bot

### ✅ Bước 3: Lấy Gemini API Key
- [ ] Truy cập [Google AI Studio](https://ai.google.dev/gemini-api/docs)
- [ ] Click "Get a Gemini API Key"
- [ ] Tạo API key mới trong Google AI Studio
- [ ] Lưu API key

### ✅ Bước 4: Cấu hình môi trường
- [ ] Copy `env.example` thành `.env`
- [ ] Điền token bot và API key
- [ ] Cài đặt dependencies: `pip install -r requirements.txt`

### ✅ Bước 5: Test local
- [ ] Chạy `python main.py`
- [ ] Test bot trên Telegram

### ✅ Bước 6: Deploy Render
- [ ] Push code lên GitHub
- [ ] Tạo Web Service trên Render
- [ ] Cấu hình environment variables
- [ ] Deploy thành công

### ✅ Bước 7: Setup Uptime Robot
- [ ] Tạo tài khoản UptimeRobot
- [ ] Thêm monitor HTTP(s)
- [ ] Cấu hình alerts

---

## 🔗 Links quan trọng

- **BotFather**: https://t.me/BotFather
- **Google AI Studio**: https://ai.google.dev/gemini-api/docs
- **Render**: https://render.com
- **Uptime Robot**: https://uptimerobot.com

---

## 💡 Tips

1. **Lưu tokens an toàn** - Không commit file `.env`
2. **Test thoroughly** - Luôn test local trước khi deploy
3. **Monitor logs** - Theo dõi logs trên Render
4. **Model mới** - Bot sử dụng `gemini-2.5-flash` mới nhất với hiệu suất tốt hơn
5. **Rate limiting** - Gemini free tier có giới hạn requests, check quota trong console

---

## 🆘 Cần trợ giúp?

Xem file `README.md` để có hướng dẫn chi tiết hơn! 