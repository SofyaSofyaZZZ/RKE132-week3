from colorama import Fore, Style

animal = input("Sisesta oma lemmikloom: ").lower()

match animal:
    case "koer":
        print(Fore.YELLOW + "Sa oled ustav ja alati valmis tegutsema!" + Style.RESET_ALL)
    case "kass":
        print(Fore.MAGENTA + "Sa oled iseseisev ja salapärane!" + Style.RESET_ALL)
    case "hobune":
        print(Fore.GREEN + "Sa oled tugev ja vabadust armastav!" + Style.RESET_ALL)
    case "delfiin":
        print(Fore.CYAN + "Sa oled tark ja sõbralik!" + Style.RESET_ALL)
    case _:
        print(Fore.RED + "Sa oled haruldane müütiline olend!" + Style.RESET_ALL)
