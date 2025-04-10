# BetterKiwi

# 🛠️ Open WebUI Local Setup Guide

This guide will walk you through setting up a local environment using Anaconda and running Open WebUI on your machine.

## ✅ Prerequisites

Make sure you have the following installed:
- [Anaconda](https://www.anaconda.com/products/distribution)
- Python 3.11 or higher (Anaconda will help manage this)

## 📦 Step 1: Create and Activate a New Environment

1. Open Anaconda Prompt (Windows) or Terminal (macOS/Linux)  
2. Create a new virtual environment:

```bash
conda create -n open-webui-env python=3.11
```

3.Activate the environment

```bash
conda activate open-webui-env
```

## 📥 Step 2: Install Open WebUI

Once the environment is activated, run:
```bash
pip install open-webui
```

## 🚀 Step 3: Start the Server and Access the UI

Start the server:
```bash
open-webui serve
```
Then open your browser and go to:
```bash
http://localhost:8080
```
You’re now ready to use Open WebUI locally!










