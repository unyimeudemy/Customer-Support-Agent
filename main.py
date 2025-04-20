from commands.system_commands.general import Appearance, Networking, Audio
from utils.api import make_request
import re

command_str = make_request()

match = re.search(r'[`\'"](\w+)[`\'"]', command_str)
command_str = match.group(1) if match else None


appearance = Appearance()
command = getattr(appearance, command_str)
command()


# appearance.change_theme()
# appearance.increase_font_size()
# appearance.decrease_font_size()


networking = Networking()
# networking.connect_to_wifi("Galaxy AO3a187")
# networking.connect_to_wifi("IgbogboISS")
# networking.connect_to_wifi("IgbogboISS", "ABCDE2025")

audio = Audio()
# audio.increase_volume()
# audio.decrease_volume()
