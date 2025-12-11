# personal-expense-tracker
A group of freshmen's first programming project at AUPP for an introductory course to python. 

# Personal Expense Tracker (Telegram + Google Sheets)

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python) ![Telegram](https://img.shields.io/badge/Telegram-Bot-blue?logo=telegram) ![Google Sheets](https://img.shields.io/badge/Google%20Sheets-API-green?logo=google-sheets)

A group project by freshmen at AUPP for our introductory Python course.  
This bot helps users **track personal expenses directly through Telegram**, storing all data securely in **Google Sheets**.

---

## 📌 Overview

This project is a **Telegram expense tracker bot** that allows users to:

- Add and log expenses directly through Telegram  
- View previously logged expenses  
- Store all data in **Google Sheets**  
- Use simple Telegram commands for quick interaction  

> ⚠️ **Important:** The bot **will not run** unless all dependencies are installed and API credentials are properly configured.

---

## 🛠 Features

- Telegram bot interface for ease of use  
- Google Sheets backend for persistent storage  
- Environment variable configuration for secure API keys  
- Easy installation and setup  

---

## 💻 Technology Stack

- Python 3.13.x  
- [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI)  
- Google Sheets API  
- python-dotenv for environment variables  

---

## 🚀 Installation Guide

Follow these steps carefully:

### **1. Create a virtual environment**

```bash
py -3.13 -m venv .venv
venv\Scripts\activate     # Windows
source venv/bin/activate  # macOS/Linux

```

### **2. Install dependencies**

```bash
pip install -r requirements.txt


```

### 3. Request a Telegram Bot API Token

- Open Telegram → Search for **BotFather**  
- Create a new bot using `/newbot`  
- Copy the generated token  

💡 Video guide: [Create Telegram Bot & Get Token](https://youtu.be/vZtm1wuA2yc?si=wcb3zfxManxYn7qc&t=32)

---

### 4. Create Google Sheets API credentials

- Go to Google Cloud Console  
- Enable **Google Sheets API** and **Google Drive API**  
- Create **Service Account Credentials**  
- Download the JSON credential file and save it inside your project  

💡 Video guide: [Google Sheets API Setup for Python](https://youtu.be/zCEJurLGFRk?si=nnxnWlhtuI1xfTa7&t=116)

---

### 5. Get your Google Sheet ID

- Open your Google Sheet  
- Copy the ID from the URL:

```
https://docs.google.com/spreadsheets/d/THIS_IS_THE_SHEET_ID/edit
```

---

### 6. Configure environment variables

Create a `.env` file in the project root and add:

```env
BOT_TOKEN=your_telegram_bot_token_here
SHEET_ID=your_google_sheet_id_here
```

---

### 7. Run the bot

```bash
python main.py
```
