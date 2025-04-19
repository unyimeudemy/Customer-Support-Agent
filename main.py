# import subprocess
# import pyautogui
# import time

# subprocess.Popen(["open", "/System/Applications/System Settings.app"])
# time.sleep(5)

# settings_general_icon_location = pyautogui.locateOnScreen("assets/chrome.png", confidence=0.8)
# print(settings_general_icon_location)
# if settings_general_icon_location:
#     print("Icon found")
#     icon_center = pyautogui.center(settings_general_icon_location)
#     print(icon_center)
#     time.sleep(0.5)
#     pyautogui.moveTo(icon_center, duration=0.5)
#     pyautogui.click()

# else:
#     print("Icon not found")


# print(pyautogui.size)

############################################################


# import subprocess

# def get_current_mode():
#     """Check if current mode is Dark or Light."""
#     result = subprocess.run(
#         ["defaults", "read", "-g", "AppleInterfaceStyle"],
#         capture_output=True, text=True
#     )
#     return "Dark" if result.returncode == 0 and "Dark" in result.stdout else "Light"

# def toggle_theme():
#     current = get_current_mode()
#     print(f"Current mode: {current}")
#     new_mode = "Light" if current == "Dark" else "Dark"

#     subprocess.run(["osascript", "-e", f'''
#         tell application "System Events"
#             tell appearance preferences
#                 set dark mode to {"false" if new_mode == "Light" else "true"}
#             end tell
#         end tell
#     '''])

#     print(f"Switched to {new_mode} mode.")

# if __name__ == "__main__":
#     toggle_theme()

############################################################

import subprocess

subprocess.run(["osascript", "-e", '''
tell application "System Events"
    tell appearance preferences
        set dark mode to not dark mode
    end tell
end tell
'''])