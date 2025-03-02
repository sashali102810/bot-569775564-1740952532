Для создания Telegram-бота с использованием библиотеки `python-telegram-bot` версии 20.x и `requests`, а также с учетом всех указанных требований, можно использовать следующий код:

### Установка необходимых библиотек

Сначала установите необходимые библиотеки:

```bash
pip install python-telegram-bot requests
```

### Код бота

```python
import logging
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Настройка логирования
logging.basicConfig(
    filename='bot_errors.log',
    level=logging.ERROR,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Привет! Я ваш телеграм бот. Используйте /help для получения списка команд.')

# Обработчик команды /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Доступные команды:\n/start - Начать работу с ботом\n/help - Получить справку')

# Функция для автоматического перезапуска при сбоях
async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    logging.error(f"Update {update} caused error {context.error}")
    # Здесь можно добавить логику для перезапуска бота
    # Например, отправка сообщения администратору или перезапуск бота

# Основная функция для запуска бота
def main():
    # Создаем приложение бота с токеном
    application = ApplicationBuilder().token("YOUR_BOT_TOKEN").build()

    # Регистрируем обработчики команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # Регистрируем обработчик ошибок
    application.add_error_handler(error_handler)

    # Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    main()
```

### Описание кода

1. **Логирование ошибок**: Ошибки логируются в файл `bot_errors.log`. Это позволяет отслеживать проблемы, возникающие в работе бота.

2. **Обработчики команд**:
   - `/start`: Отправляет приветственное сообщение.
   - `/help`: Отправляет список доступных команд.

3. **Обработчик ошибок**: Логирует ошибки и может быть расширен для автоматического перезапуска бота в случае сбоев.

4. **Автоматический перезапуск**: В текущей реализации ошибки логируются, но для автоматического перезапуска бота потребуется дополнительная логика, например, использование системного демона или скрипта для мониторинга состояния бота и его перезапуска.

### Запуск бота

1. Замените `"YOUR_BOT_TOKEN"` на токен вашего бота, полученный от BotFather.
2. Запустите скрипт:

```bash
python your_bot_script.py
```

Теперь ваш бот будет работать, обрабатывать команды `/start` и `/help`, логировать ошибки и может быть расширен для автоматического перезапуска в случае сбоев.