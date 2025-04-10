# BetterKiwi

# Step 1 Environment & User Interface Setup
# 🛠️ Open WebUI Local Setup Guide

This guide will walk you through setting up a local environment using Anaconda and running Open WebUI on your machine.

## ✅ Prerequisites

Make sure you have the following installed:
- [Anaconda](https://www.anaconda.com/products/distribution)
- Python 3.11 or higher (Anaconda will help manage this)

## 📦 Step 1.1 : Create and Activate a New Environment

1. Open Anaconda Prompt (Windows) or Terminal (macOS/Linux)  
2. Create a new virtual environment:

```bash
conda create -n open-webui-env python=3.11
```

3.Activate the environment

```bash
conda activate open-webui-env
```

## 📥 Step 1.2 : Install Open WebUI

Once the environment is activated, run:
```bash
pip install open-webui
```

## 🚀 Step 1.3 : Start the Server and Access the UI

Start the server:
```bash
open-webui serve
```
Then open your browser and go to:
```bash
http://localhost:8080
```
You’re now ready to use Open WebUI locally!



# Step 2 Creating Models by Importing Your API and Using Prompt Designed by Ours

## 💡 Step 2.1 Create an Account

Create an account using email and log in

## 🤖 Step 2.2 Importing API

After logging in, click the account icon in the bottom-left corner.
Then navigate to Admin Panel > Settings > Connection.
Enter your OpenAI API key in the appropriate field.

## ✨ Step 2.3 Choosing Models

Next, return to the home screen and start a new conversation.
In the Model dropdown, select 4o-mini.
Then, click the Control option in the top-right corner of the screen.
Paste the contents of the prompt file into the System Prompt field.


# 🎉 Step 3 Start your Conversation

After finishing above instructions, you successfully got a perfect test problem giver!






