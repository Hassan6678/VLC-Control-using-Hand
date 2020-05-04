import pygetwindow as gw
import psutil
import keyboard
import pyautogui

# Iterate over all running process
title = ""
while True:
    if keyboard.is_pressed('A'):
        for proc in psutil.process_iter():
            try:
                if proc.name() == "vlc.exe":
                    title = gw.getActiveWindow().title
                    print(title)
                    if title.find("VLC media player") != -1:
                        print("True")
                        pyautogui.press('up')
                    else:
                        print(gw.getActiveWindow().title)
                        print("False")
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
    elif keyboard.is_pressed('B'):
        for proc in psutil.process_iter():
            try:
                if proc.name() == "vlc.exe":
                    title = gw.getActiveWindow().title
                    print(title)
                    if title.find("VLC media player") != -1:
                        print("True")
                        pyautogui.press('down')
                    else:
                        print(gw.getActiveWindow().title)
                        print("False")
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
    elif keyboard.is_pressed('6'):
        for proc in psutil.process_iter():
            try:
                if proc.name() == "vlc.exe":
                    title = gw.getActiveWindow().title
                    print(title)
                    if title.find("VLC media player") != -1:
                        print("True")
                        pyautogui.press('left')
                    else:
                        print(gw.getActiveWindow().title)
                        print("False")
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
    elif keyboard.is_pressed('7'):
        for proc in psutil.process_iter():
            try:
                if proc.name() == "vlc.exe":
                    title = gw.getActiveWindow().title
                    print(title)
                    if title.find("VLC media player") != -1:
                        print("True")
                        pyautogui.press('right')
                    else:
                        print(gw.getActiveWindow().title)
                        print("False")
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
    elif keyboard.is_pressed('8'):
        for proc in psutil.process_iter():
            try:
                if proc.name() == "vlc.exe":
                    title = gw.getActiveWindow().title
                    print(title)
                    if title.find("VLC media player") != -1:
                        print("True")
                        pyautogui.press('playpause')
                    else:
                        print(gw.getActiveWindow().title)
                        print("False")
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
