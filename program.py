import time
import pyautogui
import pyperclip
import platform
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

time.sleep(3)  # Delay before starting (so you can switch windows)

print("Starting automation...")

# Step 1: Click icon at (1356, 1050)
pyautogui.moveTo(1245,1052, duration=0.7)
pyautogui.click()
print("Clicked icon.")

time.sleep(1)

# Step 2: Click + drag from (547,141) to (1888,945)
pyautogui.moveTo(667,202, duration=0.7)
pyautogui.dragTo(1789, 945, duration=1.5, button='left')
print("Drag selection completed.")

time.sleep(1.0)

# Step 3: Copy to clipboard (OS auto-detect)
os_type = platform.system()

if os_type == "Darwin":  # macOS
    pyautogui.hotkey("command", "c")
else:  # Windows + Linux
    pyautogui.hotkey("ctrl", "c")

print("Copied to clipboard.")

time.sleep(2.0)
pyautogui.click(1514, 953)

# Step 4: Read clipboard content
chat_history = pyperclip.paste()
print("\n===== COPIED TEXT =====")
print(chat_history)
print("=======================")
command ='''
copied
'''
completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a person named Hrishikesh who speaks hindi aw well as english.you are from India. Analyse chat history and respond like Hrishikesh"},
        {"role": "user", "content": command}
    ]
)
response= completion.choices[0].message.content
pyperclip.copy(response)
pyautogui.click(918,969)
time.sleep(1)

# Step 2: Paste text
if platform.system() == "Darwin":  # macOS
    pyautogui.hotkey("command", "v")
else:  # Windows / Linux
    pyautogui.hotkey("ctrl", "v")

time.sleep(0.2)

# Step 3: Press Enter to send
pyautogui.press("enter")
