@echo off
echo Starting AnshiChatRobot...
python -m venv venv
call venv\Scripts\activate
pip install -r requirements.txt
python main.py
