from PIL import Image
from pathlib import Path
import os


os.system('color')
reset = '\033[0m'
colors = [
'\033[91m',  # красный 0
'\033[93m',  # желтый 1
'\033[95m',  # пурпурный 2
'\033[96m',  # голубой 3
'\033[31m',  # темно-красный 4
'\033[32m',  # темно-зеленый 5
'\033[34m',  # темно-синий 6
]
print(f'{colors[6]}___________                  __     ________    .__                                       {reset}')
print(f'{colors[6]}\__    ___/  ___  ___  ___ _/  |_   \_____  \   |__|    _____   _____       ____    ____  {reset}')
print(f'{colors[6]}  |    |   / __ \ \  \/  / \   __\   /  ____/   |  |   /     \  \__  \     / ___\  / __ \ {reset}')
print(f'{colors[6]}  |    |  \  ___/  >    <   |  |    /       \   |  |  /  Y Y  \  / __ \   /_/    > | ___/ {reset}')
print(f'{colors[6]}  |____|   \___   >__/\_ \  |__|    \_______ \  |__| (  _|_|   ) (____ /  \___  /  \___   {reset}')
print(f'{colors[6]}                                                                          _____/          \n\n{reset}')
print(f'Write this command: "{colors[1]}[path to file] [name] [extencion] [color] [format]{reset}"\n{colors[1]}[path to file]{reset} - path to your text file\n{colors[1]}[name]{reset} - name of picture\n{colors[1]}[extencion]{reset} - extencion of picture {colors[3]}(png; jpg; ico; webp; bmp){reset}\n{colors[1]}[color]{reset} - type of color {colors[3]}(colored or gray){reset}\n{colors[1]}[format]{reset} - color format {colors[3]}(RGB or CMYK){reset}')
