from pyfiglet import figlet_format
from termcolor import colored

print("\n[+] T-HEADER TOOL | Public Custom Banner Generator\n")

name = input("[?] Enter your name for banner: ")

banner = figlet_format(name)
colored_banner = colored(banner, color="red")

print(colored_banner)
