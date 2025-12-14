from colorama import Fore, Style

animal = input("Sisesta oma lemmikloom: ").lower()

match animal:
    case "koer":
        print(Fore.YELLOW + "Sa oled ustav!" + Style.RESET_ALL)
    case "kass":
        print(Fore.MAGENTA + "Sa oled iseseisev!" + Style.RESET_ALL)
    case "hobune":
        print(Fore.GREEN + "Sa oled tugev!" + Style.RESET_ALL)
    case "delfiin":
        print(Fore.CYAN + "Sa oled tark!" + Style.RESET_ALL)
    case _:
        print(Fore.RED + "Sa oled haruldane!" + Style.RESET_ALL)
