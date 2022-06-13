print('loading..')


from colorama import Fore,Style,init
from os import system
from time import sleep
from random import randint


init()
clear = lambda: system('cls')



yellow = Fore.YELLOW
green = Fore.GREEN
reset = Fore.RESET
cyan = Fore.CYAN
red = Fore.RED
dark_yellow = Fore.YELLOW+Style.DIM
dark_cyan = Fore.CYAN+Style.DIM
bright = Style.BRIGHT

PLAYER_name = ""
code = [randint(1,9) for i in range(4)]
codeVariable = ""
for i in range(len(code)):
    codeVariable += str(code[i])

codeVariable = int(codeVariable)

items = []
rooms = ["Nincs információ","Nincs információ","Nincs információ","Nincs információ","Nincs információ"]



def title():
    
    print("")
    print(f"""{cyan}
                ███████╗░██████╗░█████╗░░█████╗░██████╗░███████╗  ██████╗░░█████╗░░█████╗░███╗░░░███╗
                ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝  ██╔══██╗██╔══██╗██╔══██╗████╗░████║
                █████╗░░╚█████╗░██║░░╚═╝███████║██████╔╝█████╗░░  ██████╔╝██║░░██║██║░░██║██╔████╔██║
                ██╔══╝░░░╚═══██╗██║░░██╗██╔══██║██╔═══╝░██╔══╝░░  ██╔══██╗██║░░██║██║░░██║██║╚██╔╝██║
                ███████╗██████╔╝╚█████╔╝██║░░██║██║░░░░░███████╗  ██║░░██║╚█████╔╝╚█████╔╝██║░╚═╝░██║
                ╚══════╝╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░░░░╚══════╝  ╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝{reset}""")
    print("\n")


def SCREEN_room(room):
    clear()
    title()
    if room == 1:
        if "poster" in items:
            print(f"{red} Nincs itt már semmi sem!{reset}\n")
            sleep(1.2)
            SCREEN_MENU_ROOM()
        else:
            KEY_lightswitch = input(f"{dark_cyan} Fel szeretnéd kapcsolni a lámpát? (igen/nem){reset} ")
            if KEY_lightswitch == "igen":
                clear()
                title()
                KEY_take = input(f"{yellow} A sötétben a falon látsz egy plakátot. Szeretnéd magaddal vinni? (igen/nem){reset} ")
                if KEY_take == "igen":
                    items.append("poster")
                    rooms[0] = f"Világos szoba, plakát, {str(code[0])}"
                    clear()
                    title()
                    print(f"{green} Sikeresen eltetted a plakátot a táskádba!{reset}\n")
                    sleep(1)
                    print(f"{red} Álljunk csak meg egy pillanatra!!!!!!!!{reset}")
                    sleep(2)
                    print(f"{green} Erre a plakátra az van írva: A KÓD ELSŐ SZÁMA: {str(code[0])}")
                    print(f"{red} Ezt jól vésd az eszedbe!{reset}\n")
                    input(f"{yellow} Nyomj entert a továbblépéshez!{reset} ")
                    SCREEN_MENU_ROOM()
                else:
                    clear()
                    title()
                    print(f"{cyan} Látom inkább a biztonságra utazol :D{reset}")
                    sleep(1.3)
                    SCREEN_MENU_ROOM()
            else:
                print(f"{red} Nem látsz így semmit sem a szobában, ezért inkább kimész a szobából.{reset}\n")
                input(f"{yellow} Nyomj entert a továbblépéshez{reset} ")
                SCREEN_MENU_ROOM()
    elif room == 2:
        if "Szörny" not in rooms:
            KEY_escape = input(f"{red} Jaj, NE!!!! A szobában egy nagy szörny van! El akarsz menekülni? (igen/nem){reset} ")
            if KEY_escape == "igen":
                rooms[1] = "Szörny"
                print(f"{dark_cyan} Meghallott téged a szörny, de szerencsédre még gyorsan ki tudtál menekülni a szobából!{reset}\n")
                input(f"{yellow} Nyomj entert a továbblépéshez{reset} ")
                SCREEN_MENU_ROOM()
            else:
                print(f"{red} Beszakadt alattad a padló és lehuzantál egy hosszú járaton. A végén újból az ajtók előtt lyukadtál ki szerencsére. {reset}\n")
                rooms[1] = "Szörny"
                input(f"{yellow} Nyomj entert a továbblépéshez{reset} ")
                SCREEN_MENU_ROOM()
        else:
            print(f"{red} Mostmár ide többet nem tudsz bejönni, mert az ajtót elállja a nagy szörny!{reset}\n")
            input(f"{yellow} Nyomj entert a továbblépéshez{reset} ")
            SCREEN_MENU_ROOM()
    elif room == 3:
        if "Bomba" not in rooms:
            print(f"{red} Jaj, NE!!!! A szobában van egy bomba. De szerencsédre hatástalanítani tudod! Csak egy számot kell megadnod.{reset}")
            KEY_defuse = int(input(f"{dark_yellow} Add meg a KÓD ELSŐ SZÁMÁT{reset} "))
            if KEY_defuse == code[0]:
                print(f"{green} Bomba sikeresen hatástalanítva!{reset}")
                rooms[2] = f"Bomba, {code[1]}"
                print(f"{yellow} Észreveszed, hogy a bomba mellett van egy kis cetlike. A cetlire van valami írva: A KÓD MÁSODIK SZÁMA {str(code[1])}{reset}")
                print(f"{red} Ezt jól vésd az eszedbe!{reset}\n")
                input(f"{yellow} Nyomj entert a továbblépéshez!{reset} ")
                SCREEN_MENU_ROOM()
            else:
                clear()
                title()
                print(f"{red} GAME OVER!{reset}")
                input()
                system('exit')
        else:
            print(f"{red} Itt már nincs semmi sem! {reset}\n")
            input(f"{yellow} Nyomj entert a továbblépéshez{reset} ")
            SCREEN_MENU_ROOM()
    elif room == 4:
        print(f"{dark_yellow} Itt tudod megadni a titkos számkódot, hogy kijuthassál a szabadulószobából!")
        KEY_codetip = int(input(f"{cyan} KÓD:{reset} "))
        if KEY_codetip == codeVariable:
            clear()
            title()
            print(f"{green} Gratulálok, nyertél! {reset}")
            input()
            system('exit')
        else:
            rooms[3] = "Titkos kód megadási lehetőség"
            print(f"{red} Helytelen!{reset}\n")
            input(f"{yellow} Nyomj entert a továbblépéshez!{reset} ")
            SCREEN_MENU_ROOM()
            
        
    elif room == 5:
        print(f"{red} A 3. és 4. számjegyet egy picike játékkal tudhatod meg! Először a harmadikkal kezdem és utána fog jönni a negyedik\n")
        input(f"{yellow} Nyomj entert a továbblépéshez!{reset} ")
        clear()
        title()
        print(f"{cyan} Gondoltam egy számra (a 3. számjegyre). Ha hozzáadok kettőt, akkor {code[2]+2}-t kapok.{reset}\n")
        print(f"{red} Gondoltam egy számra (a 4. számjegyre). Ha megszorzom eggyel, akkor {code[3]}-t kapok.{reset}\n")
        rooms[4] = f"Játék, x+2={code[2]+2}, y*1={code[3]}"
        input(f"{yellow} Nyomj entert a továbblépéshez!{reset} ")
        SCREEN_MENU_ROOM()
        

def SCREEN_MENU_ROOM():
    clear()
    title()
    print(f" [{cyan}1{reset}] {rooms[0]}")
    print(f" [{cyan}2{reset}] {rooms[1]}")
    print(f" [{cyan}3{reset}] {rooms[2]}")
    print(f" [{cyan}4{reset}] {rooms[3]}")
    print(f" [{cyan}5{reset}] {rooms[4]}\n")
    KEY_room = int(input(f"{yellow} >> Melyik szobát választod?{reset} "))
    SCREEN_room(KEY_room)
    

def CREATE_player():
    clear()
    title()
    PLAYER_name = input(f"{yellow} Szia! Hogy hívnak téged? {reset}")
    clear()
    title()
    print(f"{bright} Szia {PLAYER_name}!")
    sleep(1)
    print(f" Itt van pár instrukció, ami majd jól fog jönni neked utad során!{reset}")
    sleep(3)
    clear()
    title()
    print(f"{yellow} - Minden szobában majd eldönheted, hogy magaddal szeretnél-e vinni valamit\n{cyan} - Legyél óvatos, mert az ismeretlen helyről származó tárgyak veszélyesek is lehetnek\n{red} - A szobákban alaposan nézzél körbe{reset}\n{bright} - Nem kötelező, de ajánlatos a szobákon sorrendben átmenni{reset}\n\n{green} Sok szerencsét! :)\n")
    input(f"{yellow} Nyomj entert a továbblépéshez!{reset}")
    SCREEN_MENU_ROOM()


def SCREEN_welcome():
    clear()
    title()
    print(f"{bright} Üdvözöllek a szabadulószobában! Remélem jól fogod magadat érezni :){reset}\n")
    sleep(2)
    input(f"{yellow} Nyomj entert a továbblépéshez!{reset} ")
    CREATE_player()


SCREEN_welcome()