import subprocess
import objc
import pyautogui
import time
import objc






class Appearance:

    def __init__(self):
        pass

    def change_theme(self):

        subprocess.run(["osascript", "-e", '''
        tell application "System Events"
            tell appearance preferences
                set dark mode to not dark mode
            end tell
        end tell
        '''])

    def increase_font_size(self):
        time.sleep(1)
        pyautogui.keyDown('command')
        pyautogui.press('=') 
    
    def decrease_font_size(self):
        time.sleep(1)
        pyautogui.keyDown('command')
        pyautogui.press('-')
    

    def open_settings(self):
        subprocess.run([
            "open", "x-apple.systempreferences:com.apple.Accessibility-Settings.extension?Keyboard"
        ])      


class Audio:

    def __init__(self):
        pass

    def get_volume(self):
        """Get the current system volume."""
        script = """
        output volume of (get volume settings)
        """
        result = subprocess.run(['osascript', '-e', script], capture_output=True, text=True)
        return int(result.stdout.strip())

    def set_volume(self, volume):
        """Set the system volume to the specified level (0 to 100)."""
        volume = max(0, min(volume, 100))  # Clamps the volume between 0 and 100
        script = f"""
        set volume output volume {volume}
        """
        subprocess.run(['osascript', '-e', script])
        print(f"Volume set to: {volume}%")

    def increase_volume(self):
        """Increase the system volume by 10%."""
        current_volume = self.get_volume()
        new_volume = min(current_volume + 10, 100)  # Increase volume by 10%
        self.set_volume(new_volume)

    def decrease_volume(self):
        """Decrease the system volume by 10%."""
        current_volume = self.get_volume()
        new_volume = max(current_volume - 10, 0)  # Decrease volume by 10%
        self.set_volume(new_volume)



class Networking:

    def __init__(self):
        pass

    def connect_to_wifi(self, ssid, password=None):
        from CoreWLAN import CWInterface
        import time

        interface = CWInterface.interfaceWithName_("en0")

        if interface.ssid() == ssid:
            print(f"Already connected to '{ssid}'")
            return

        print(f"Connecting to '{ssid}'...")

        time.sleep(2)  # avoid "Resource busy" error
        networks, error = interface.scanForNetworksWithName_error_(ssid, None)
        if error:
            print("Error scanning:", error)
            return

        if not networks:
            print(f"No network found with SSID '{ssid}'")
            return

        network = list(networks)[0]

        # Try with saved credentials
        print("Trying saved credentials (if any)...")
        success, error = interface.associateToNetwork_password_error_(network, None, None)

        if success:
            print(f"Successfully connected to '{ssid}' using saved credentials.")
            return

        print("Saved credentials failed or not found.")

        if not password:
            print("Password is required but not provided.")
            return

        # Retry with provided password
        print("Retrying with provided password...")
        success, error = interface.associateToNetwork_password_error_(network, password, None)

        if success:
            print(f"Successfully connected to '{ssid}' using password.")
        else:
            print("Failed to connect:", error)


     