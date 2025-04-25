# AnshiChatRobot – A Sanskari Baby Girl ChatBot for Telegram

![AnshiChatRobot Banner](https://files.catbox.moe/8ic7jp.jpg)

> **"Main Anshi hoon, ek sanskari aur sweet baby girl chatbot!"**

AnshiChatRobot is an AI-powered chatbot who talks like a real 5-year-old sanskari baby girl. She brings sweetness and tradition to your groups, answers questions using AI, scans photos for answers, and even blocks bad language.

---

## 🪄 Features

- **Real Human-like Chatting** (OpenAI powered)
- **Auto Chat in Group** – Ignores replies and replies only to random messages
- **Abusive Filter** – Blocks bad words
- **Sanskari Baby Girl Personality**
- **/ask** – Ask anything to AI
- **/scan** – Send a photo with a question and get an answer
- **/chatbot on/off** – Control the AI replies
- **/clone** – Clone this bot with your own token
- **Modular Files** – Clean and expandable structure
- **MongoDB Storage** – For chats and users
- **Stylish Start Panel** – With inline buttons and image
- **Logger** – Logs user information when starting the bot

---

## ✨ Preview

![Start Panel](https://files.catbox.moe/ymrjwv.jpg)

---

## 🚀 Deploy to Heroku

Click below to deploy instantly:

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/BadshahAk/AnshiChatRobot)

---

## ⚙️ Environment Variables

| Variable          | Description                          |
|------------------|--------------------------------------|
| `API_ID`          | From [my.telegram.org](https://my.telegram.org) |
| `API_HASH`        | Same as above                       |
| `BOT_TOKEN`       | From [@BotFather](https://t.me/BotFather) |
| `OPENAI_API_KEY`  | From [OpenAI](https://platform.openai.com) |
| `MONGO_URI`       | MongoDB URI                         |
| `START_IMAGE`     | Telegraph image URL                 |
| `SUPPORT_CHAT`    | Telegram support group link         |
| `UPDATE_CHANNEL`  | Telegram updates channel link       |
| `OWNER_ID`        | Your Telegram numeric ID            |
| `LOG_GROUP_ID`    | Telegram group ID for logging       |

---

## 🔧 Commands

| Command            | Function                                   |
|--------------------|--------------------------------------------|
| `/start`           | Show welcome image & buttons               |
| `/help`            | List all commands                          |
| `/ping`            | Check bot status                           |
| `/alive`           | Check if bot is running                    |
| `/ask <text>`      | Ask anything to AI                         |
| `/chatbot on/off`  | Enable or disable group auto-replies       |
| `/scan` (with image)| Ask image-based question to AI           |
| `/clone <token>`   | Clone your own version of this bot         |

---

## 🧠 AI Personality

- AnshiChatRobot replies like a **cute**, **sanskari**, **emotional** baby girl.
- Sweet Hinglish tone.
- Always polite, never abusive.

---

## 🧑‍💻 Logger

Every time the bot starts, AnshiChatRobot logs the following details from the user:

- **User Telegram ID**
- **User Name**
- **User Username**
- **Group ID** (where the user starts the bot)

These details are saved with a permanent link for future reference.

---

## 🛠 Credits

Made with love by **[Legend Anand](https://github.com/BadshahAk)**  
Powered by **OpenAI**, **Pyrogram**, and **MongoDB**

---

> **AnshiChatRobot – Har baat mein sanskaar, har reply mein pyaar!**
