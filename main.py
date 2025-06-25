import os
import logging
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import google.generativeai as genai
from dotenv import load_dotenv
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading
import json

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Configure Gemini API
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

if not GEMINI_API_KEY or not TELEGRAM_BOT_TOKEN:
    logger.error("Missing required environment variables")
    exit(1)

# Initialize Gemini with stable API (Python 3.8 compatible)
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-pro')

class TelegramGeminiBot:
    def __init__(self):
        self.application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
        self.setup_handlers()
    
    def setup_handlers(self):
        """Thiết lập các handler cho bot"""
        # Command handlers
        self.application.add_handler(CommandHandler("start", self.start_command))
        self.application.add_handler(CommandHandler("help", self.help_command))
        self.application.add_handler(CommandHandler("clear", self.clear_command))
        
        # Message handler
        self.application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_message))
    
    async def start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Xử lý lệnh /start"""
        welcome_message = """
🤖 Chào mừng bạn đến với Bot AI powered by Gemini!

Tôi có thể giúp bạn:
✅ Trả lời câu hỏi
✅ Giải thích khái niệm
✅ Hỗ trợ học tập
✅ Sáng tạo nội dung
✅ Và nhiều việc khác!

Gửi tin nhắn bất kỳ để bắt đầu trò chuyện!

Các lệnh có sẵn:
/help - Hiển thị trợ giúp
/clear - Xóa lịch sử hội thoại
        """
        await update.message.reply_text(welcome_message)
    
    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Xử lý lệnh /help"""
        help_message = """
📖 **Hướng dẫn sử dụng Bot AI**

**Các lệnh:**
/start - Khởi động bot
/help - Hiển thị hướng dẫn này
/clear - Xóa lịch sử hội thoại

**Cách sử dụng:**
- Gửi bất kỳ tin nhắn nào để hỏi AI
- Bot sẽ trả lời dựa trên công nghệ Gemini AI
- Bạn có thể hỏi về mọi chủ đề

**Ví dụ:**
"Giải thích về trí tuệ nhân tạo"
"Viết một bài thơ về mùa thu"
"Hướng dẫn nấu phở"

🔥 **Tip:** Bot có thể nhớ ngữ cảnh cuộc hội thoại!
        """
        await update.message.reply_text(help_message, parse_mode='Markdown')
    
    async def clear_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Xử lý lệnh /clear"""
        # Clear conversation context if needed
        context.user_data.clear()
        await update.message.reply_text("✅ Đã xóa lịch sử hội thoại. Bắt đầu cuộc trò chuyện mới!")
    
    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Xử lý tin nhắn từ user"""
        user_message = update.message.text
        user_name = update.message.from_user.first_name
        
        logger.info(f"Message from {user_name}: {user_message}")
        
        try:
            # Hiển thị typing indicator
            await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="typing")
            
            # Tạo prompt với context
            prompt = f"""
            Bạn là một AI assistant thông minh và hữu ích. Hãy trả lời câu hỏi của người dùng một cách chi tiết, 
            chính xác và dễ hiểu. Sử dụng tiếng Việt để trả lời.
            
            Câu hỏi của {user_name}: {user_message}
            """
            
            # Gọi Gemini API với syntax ổn định Python 3.8
            response = model.generate_content(prompt)
            
            if response.text:
                # Chia nhỏ tin nhắn nếu quá dài (Telegram limit: 4096 chars)
                if len(response.text) > 4000:
                    chunks = [response.text[i:i+4000] for i in range(0, len(response.text), 4000)]
                    for chunk in chunks:
                        await update.message.reply_text(chunk)
                else:
                    await update.message.reply_text(response.text)
            else:
                await update.message.reply_text("Xin lỗi, tôi không thể xử lý yêu cầu này. Vui lòng thử lại!")
                
        except Exception as e:
            logger.error(f"Error processing message: {e}")
            await update.message.reply_text(
                "❌ Đã xảy ra lỗi khi xử lý tin nhắn. Vui lòng thử lại sau!"
            )
    
    async def error_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Xử lý lỗi toàn cục"""
        logger.error(f"Update {update} caused error {context.error}")
    
    def run(self):
        """Chạy bot"""
        # Add error handler
        self.application.add_error_handler(self.error_handler)
        
        # Start the bot
        logger.info("Starting Telegram Gemini Bot...")
        self.application.run_polling(allowed_updates=Update.ALL_TYPES)

class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/health' or self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            health_data = {
                "status": "healthy",
                "service": "telegram-gemini-bot",
                "version": "1.0.0"
            }
            self.wfile.write(json.dumps(health_data).encode())
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        # Suppress HTTP server logs
        pass

def start_health_server():
    """Start health check server"""
    port = int(os.environ.get('PORT', 8080))
    server = HTTPServer(('0.0.0.0', port), HealthHandler)
    logger.info(f"Health server starting on port {port}")
    server.serve_forever()

def main():
    """Main function"""
    logger.info("Initializing Telegram Gemini Bot...")
    
    # Start health check server in background
    health_thread = threading.Thread(target=start_health_server, daemon=True)
    health_thread.start()
    
    # Start bot
    bot = TelegramGeminiBot()
    bot.run()

if __name__ == '__main__':
    main() 