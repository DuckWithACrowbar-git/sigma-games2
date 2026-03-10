import pyautogui
import time

# Path to your text file
file_path = "games.txt"

# Delay before typing starts (so you can click into the target window)
print("You have 10 seconds to click into the window where the names should be typed...")
time.sleep(10)

with open(file_path, "r", encoding="utf-8") as f:
    for line in f:
        name = line.strip()
        if name:  # skip empty lines
            pyautogui.write("<a ")
            pyautogui.write("href=")
            pyautogui.write("assets/games")
            pyautogui.write("/")
            pyautogui.write(name)
            pyautogui.write("/index.html>")
            pyautogui.write(name)
            pyautogui.write("</a>")
            pyautogui.press("enter")  # optional: presses Enter after each name
            time.sleep(0.5)  # small delay between names
