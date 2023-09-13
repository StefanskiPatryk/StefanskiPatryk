import random


class Character:
    def __init__(self, imie, rasa, klasa, hp, obrazenia, wzrost, pieniadze):
        self.imie = imie
        self.rasa = rasa
        self.klasa = klasa
        self.hp = hp
        self.obrazenia = obrazenia
        self.wzrost = wzrost
        self.pieniadze = pieniadze


class Przeciwnik:
    def __init__(self, rasa, hp, obrazenia):
        self.rasa = rasa
        self.hp = hp
        self.obrazenia = obrazenia


class Straznik:
    def __init__(self, hp, obrazenia):
        self.obrazenia = obrazenia
        self.hp = hp


class ZakazaneImiona:
    def __init__(self):
        self.zakazane_Imiona = set()

    def dodaj_imie(self, imie):
        self.zakazane_Imiona.add(imie)

    def czy_imie_zakazane(self, imie):
        return imie in self.zakazane_Imiona


def create_character():
    zakazane = ZakazaneImiona()
    zakazane.dodaj_imie("Janusz")
    zakazane.dodaj_imie("Grażyna")
    zakazane.dodaj_imie("Bagno")
    zakazane.dodaj_imie("Rafał")
    zakazane.dodaj_imie("Czopek")
    zakazane.dodaj_imie("Majonez")
    zakazane.dodaj_imie("Grzegorz")
    zakazane.dodaj_imie("Helikopter")
    zakazane.dodaj_imie("Jola")
    zakazane.dodaj_imie("Mariusz")

    # Usuwanie polskich znaków
    imie = input("Podaj imię postaci: ").replace("ł", "l").replace("ń", "n").replace("ś", "s").replace("ż",
                                                                                                       "z").replace(
        "ó", "o").replace("ź", "z").replace("ą", "a").replace("ę", "e").replace("ć", "c")
    if zakazane.czy_imie_zakazane(imie):
        print("Nie możesz użyć tego imienia!")
        return None
    else:
        print("Poprawne imię!")

    klasa = input("Wybierz klasę postaci (wojownik/paladyn/zabojca/strzelec): ").replace("ł", "l").replace("ń",
                                                                                                           "n").replace(
        "ś", "s").replace("ż", "z").replace("ó", "o").replace("ź", "z").replace("ą", "a").replace("ę", "e").replace("ć",
                                                                                                                    "c")
    if "wojownik" in klasa:
        print("Wybrałeś klasę: Wojownik")
    elif "paladyn" in klasa:
        print("Wybrałeś klasę: Paladyn")
    elif "zabojca" in klasa:
        print("Wybrałeś klasę: Zabójca")
    elif "strzelec" in klasa:
        print("Wybrałeś klasę: Strzelec")
    else:
        print("Wybrałeś nieistniejącą klasę")
        return None

    if klasa == "wojownik":
        hp = random.randint(113, 149)
        obrazenia = random.randint(18, 22)
    elif klasa == "paladyn":
        hp = random.randint(150, 170)
        obrazenia = random.randint(11, 27)
    elif klasa == "zabojca":
        hp = random.randint(96, 112)
        obrazenia = random.randint(23, 31)
    elif klasa == "strzelec":
        hp = random.randint(75, 95)
        obrazenia = random.randint(30, 34)

    rasa = input("Wybierz rasę postaci (elf/krasnolud/czlowiek/gigant): ").replace("ł", "l").replace("ń", "n").replace(
        "ś", "s").replace("ż", "z").replace("ó", "o").replace("ź", "z").replace("ą", "a").replace("ę", "e").replace("ć",
                                                                                                                    "c")
    if "elf" in rasa:
        print("Wybrałeś rasę: Elf")
    elif "krasnolud" in rasa:
        print("Wybrałeś rasę: Krasnolud")
    elif "czlowiek" in rasa:
        print("Wybrałeś rasę: Człowiek")
    elif "gigant" in rasa:
        print("Wybrałeś rasę: Gigant")
    else:
        print("Wybrałeś nieistniejącą rasę")
        return None
    wzrost = 0
    pieniadze = 0
    if rasa == "Elf":
        wzrost = random.randint(190, 210)
        pieniadze = random.randint(200, 300)
    elif rasa == "krasnolud":
        wzrost = random.randint(100, 140)
        pieniadze = random.randint(300, 350)
    elif rasa == "czlowiek":
        wzrost = random.randint(160, 190)
        pieniadze = random.randint(220, 300)
    elif rasa == "gigant":
        wzrost = random.randint(240, 320)
        pieniadze = random.randint(200, 240)

    return Character(imie, rasa, klasa, hp, obrazenia, wzrost, pieniadze)


def create_przeciwnik():
    enemies = [
        Przeciwnik("Goblin", 60, 12),
        Przeciwnik("Ork", 85, 18),
        Przeciwnik("Troll", 120, 16)
    ]
    enemy = random.choice(enemies)
    return enemy


def walka_z_potworami(character, przeciwnik):
    print(f"Walczysz z {przeciwnik.rasa}em!")

    while character.hp > 0 and przeciwnik.hp > 0:
        character.hp -= przeciwnik.obrazenia
        przeciwnik.hp -= character.obrazenia

    if character.hp <= 0:
        print("Przegrałeś walkę. Koniec gry.")
        return False
    else:
        print("Wygrałeś walkę!")
        return True


def walka_z_straznikiem(character, przeciwnik):
    przeciwnik.hp = 100
    przeciwnik.obrazenia = 5

    print("Walczysz z strażnikiem!")

    while character.hp > 0 and przeciwnik.hp > 0:
        character.hp -= przeciwnik.obrazenia
        przeciwnik.hp -= character.obrazenia

    if character.hp <= 0:
        print("Przegrałeś walkę. Koniec gry.")
        return False
    else:
        print("Wygrałeś walkę!")
        return True


def main():
    print(
        "Witaj w Bagnie! \n Jest to kraina przepełniona różnymi stworami, której władcą jest król Majonez drugi Kielecki. \n\n\n Wszystko co wpisujesz nie może posiadać polskich znaków takich jak: Ż , Ź , Ń, Ó, Ł, Ć, Ą, Ę !!!")
    print(
        "Oto lista imion zakazanych w królestwie: Janusz, Grażyna, Bagno, Rafał, Czopek, Majonez, Grzegorz, Grzegorz, Helikopter, Jola, Mariusz")
    character = create_character()

    if character is None:
        return

    print(f"Witaj, {character.imie}!")
    print(f"Rasa: {character.rasa}")
    print(f"Klasa: {character.klasa}")
    print(f"HP: {character.hp}")
    print(f"Obrażenia: {character.obrazenia}")
    print(f"Wzrost: {character.wzrost}")
    print(f"Pieniądze: {character.pieniadze}")

    choice = input("Czy chcesz przyjąć zadanie od Króla Bagien? (1 - tak, 2 - nie): ")

    if choice == "1":
        print("Przyjąłeś zadanie, wyruszasz w niebezpieczną podróż, na której może stanąć wielu wrogów.")
        print("Eksplorujesz okolice w poszukiwaniu jaskini, słyszysz dziwny szelest w krzakach.")

        choice = input("1 - Podchodzisz do krzaków i sprawdzasz, co się w nich czai\n2 - Ignorujesz i dalej poszukujesz zaginionej jaskini: ")

        if choice == "1":
            if random.random() < 1.0:  # 100% szansa na spotkanie wroga
                enemy = create_przeciwnik()
                if walka_z_potworami(character, enemy):
                    print("Gratulacje, pokonałeś wroga!")
                    print("Podróżujesz dalej aż w końcu natknąłęś się na jaskinie. Przed nią czeka strażnik, który oferuje ci wejście za 200 złotych monet")
                    choice = input("1 - Płacisz strażnikowi za przejscie\n 2 - Ignorujesz prośbę strażnika")
                    if choice == "1":
                        kasa = random.randint(200, 500)
                        print("stan konta: ", kasa - 200)
                        print("Udało ci się przejść dalej. \n Eksplorujesz jaskinie w poszukiwaniu skarbu i nagle natrafiasz na błyszczącą szkatułke, której pilnuje potęrzny trol")
                        choice = input("1- Walczysz o skarb \n 2- Uciekasz w popłochu")
                        if choice == "1":
                            straznik = create_przeciwnik()
                            if walka_z_straznikiem(character, straznik):
                                print("Udało ci się wygrać długą walke, podchodzisz do złotej skrzyni, otwierasz ją i znajdujesz 1000 złotych monet")
                                choice = input("1 - Zabierasz skarb ze sobą i ruszasz w drogę, aby oddać go królowi \n 2. Twierdzisz, że jeśli to ty pokonałeś strażnika to tobie należy się skarb")
                                if choice == "1":
                                    print("Wróciłeś bezpiecznie do zamku w którym czekał na ciebie Król Majonez drugi Kielecki")
                                    print("Oddałeś skarb królowi, a on za twą męskość postanowił mianować cię na swoją prawą rękę.")
                                    print("Gratulacje!!! Wygrałeś grę")
                            elif choice == "2":
                                    print("Król wystawił za twoją głowę list gończy, starasz się uciec z bagnolandu, lecz jest wysoka szansa, że królewska gwardia znajdzie cię i zabije")
                                    if random.random() < 0.5:  # 50% na ucieczkę
                                        straznik = create_przeciwnik()
                                        if walka_z_straznikiem(character, straznik):
                                            print(
                                                "Znaleziono cię ale jesteś na tyle potężnym wojownikiem, że udało ci się wygrać kolejną walkę. Uciekasz ze skarbem do odległej krainy.")
                                            print("Gratulacje!!! Wygrałeś grę")
                                        else:
                                            print("Niestety strażnik cie pokonał. Zginąłeś za swoją zachłanność.")
                                            print("Koniec gry. Przegrałeś")
                                    else:
                                        print("Nie udało ci się pokonać wroga. Koniec gry. Przegrałeś")

                        elif choice == "2":
                            if random.random() < 0.5:  # 50% na ucieczkę
                                straznik = create_przeciwnik()
                                if walka_z_straznikiem(character, straznik):
                                    print(
                                        "Strażnik cię dogonił ale udało ci się z nim wygrać i zdobyłeś skarb w postaci 1000 złotych monet")
                                else:
                                    print("Nie udało ci się pokonać wroga. Koniec gry")
                            else:
                                print(
                                    "Udało ci się uciec, niestety zawiodłeś króla ponieważ wróciłeś bez skarbu. \n Koniec gry.")

                    elif choice == "2":
                        print("Strażnik się na ciebie zdenerwował, albo odejdziesz albo cie zabije")
                        choice = input("1 - Uciekasz \n 2 - I tak próbojesz wejść do jaskini")
                        if choice == "1":
                            print("Odchodzisz w spokoju jako przegrany")
                            print("Przegrałeś grę król jest zawiedziony")
                        elif choice == "2":
                            straznik = create_przeciwnik()
                            if walka_z_straznikiem(character, straznik):
                                print("Pokonałeś wroga, wchodzisz do jaskini w poszukiwaniu skarbu")
                                print(
                                    "Udało ci się przejść dalej. \n Eksplorujesz jaskinie w poszukiwaniu skarbu i nagle natrafiasz na błyszczącą szkatułke, której pilnuje potęrzny trol")
                                choice = input("1- Walczysz o skarb \n 2- Uciekasz w popłochu")
                                if choice == "1":
                                    straznik = create_przeciwnik()
                                    if walka_z_straznikiem(character, straznik):
                                        print(
                                            "Udało ci się wygrać długą walke, podchodzisz do złotej skrzyni, otwierasz ją i znajdujesz 1000 złotych monet")
                                        choice = input(
                                            "1 - Zabierasz skarb ze sobą i ruszasz w drogę, aby oddać go królowi \n 2. Twierdzisz, że jeśli to ty pokonałeś strażnika to tobie należy się skarb")
                                        if choice == "1":
                                            print(
                                                "Wróciłeś bezpiecznie do zamku w którym czekał na ciebie Król Majonez drugi Kielecki")
                                            print(
                                                "Oddałeś skarb królowi, a on za twą męskość postanowił mianować cię na swoją prawą rękę.")
                                            print("Gratulacje!!! Wygrałeś grę")
                                        elif choice == "2":
                                            print(
                                                "Król wystawił za twoją głowę list gończy, starasz się uciec z bagnolandu, lecz jest wysoka szansa, że królewska gwardia znajdzie cię i zabije")
                                            if random.random() < 0.5:  # 50% na ucieczkę
                                                straznik = create_przeciwnik()
                                                if walka_z_straznikiem(character, straznik):
                                                    print(
                                                        "Znaleziono cię ale jesteś na tyle potężnym wojownikiem, że udało ci się wygrać kolejną walkę. Uciekasz ze skarbem do odległej krainy.")
                                                    print("Gratulacje!!! Wygrałeś grę")
                                                else:
                                                    print(
                                                        "Niestety strażnik cie pokonał. Zginąłeś za swoją zachłanność.")
                                                    print("Koniec gry. Przegrałeś")
                                    else:
                                        print("Nie udało ci się pokonać wroga. Koniec gry. Przegrałeś")
                            else:
                                print("Niestety strażnik cie pokonał. Zginąłeś za swoją zachłanność.")
                                print("Koniec gry. Przegrałeś")
            else:
                print("Nie udało Ci się pokonać wroga. Koniec gry.")
            return

        elif choice=="2":
            print(
                "Podróżujesz dalej aż w końcu natknąłęś się na jaskinie. Przed nią czeka strażnik, który oferuje ci wejście za 200 złotych monet")
            choice = input("1 - Płacisz strażnikowi za przejscie\n 2 - Ignorujesz prośbę strażnika")
            if choice == "1":
                # pieniadze=pieniadze-200
                print(
                    "Udało ci się przejść dalej. \n Eksplorujesz jaskinie w poszukiwaniu skarbu i nagle natrafiasz na błyszczącą szkatułke, której pilnuje potęrzny trol")
                choice = input("1- Walczysz o skarb \n 2- Uciekasz w popłochu")
                if choice == "1":
                    straznik = create_przeciwnik()
                    if walka_z_straznikiem(character, straznik):
                        print(
                            "Udało ci się wygrać długą walke, podchodzisz do złotej skrzyni, otwierasz ją i znajdujesz 1000 złotych monet")
                        choice = input(
                            "1 - Zabierasz skarb ze sobą i ruszasz w drogę, aby oddać go królowi \n 2. Twierdzisz, że jeśli to ty pokonałeś strażnika to tobie należy się skarb")
                        if choice == "1":
                            print(
                                "Wróciłeś bezpiecznie do zamku w którym czekał na ciebie Król Majonez drugi Kielecki")
                            print(
                                "Oddałeś skarb królowi, a on za twą męskość postanowił mianować cię na swoją prawą rękę.")
                            print("Gratulacje!!! Wygrałeś grę")
                        elif choice == "2":
                            print(
                                "Król wystawił za twoją głowę list gończy, starasz się uciec z bagnolandu, lecz jest wysoka szansa, że królewska gwardia znajdzie cię i zabije")
                            if random.random() < 0.5:  # 50% na ucieczkę
                                straznik = create_przeciwnik()
                                if walka_z_straznikiem(character, straznik):
                                    print(
                                        "Znaleziono cię ale jesteś na tyle potężnym wojownikiem, że udało ci się wygrać kolejną walkę. Uciekasz ze skarbem do odległej krainy.")
                                    print("Gratulacje!!! Wygrałeś grę")
                                else:
                                    print("Niestety strażnik cie pokonał. Zginąłeś za swoją zachłanność.")
                                    print("Koniec gry. Przegrałeś")
                    else:
                        print("Nie udało ci się pokonać wroga. Koniec gry. Przegrałeś")

                elif choice == "2":
                    if random.random() < 0.5:  # 50% na ucieczkę
                        straznik = create_przeciwnik()
                        if walka_z_straznikiem(character, straznik):
                            print(
                                "Strażnik cię dogonił ale udało ci się z nim wygrać i zdobyłeś skarb w postaci 1000 złotych monet")
                        else:
                            print("Nie udało ci się pokonać wroga. Koniec gry")
                    else:
                        print(
                            "Udało ci się uciec, niestety zawiodłeś króla ponieważ wróciłeś bez skarbu. \n Koniec gry.")

    elif choice == "2":
        print("Król jest na ciebie zły, ponieważ jesteś jego najbardziej zaufanym rycerzem")
        choice = input(
            "1 - Mówisz królowi, że nie czujesz się na siałach na taką wyprawę \n 2 - Mówisz królowi, że i tak nie miał byś z tego pewnie żadnej nagrody")
        if choice == "1":
            print("Król jest wyrozumiały i mówi ci, żebyś odpoczął")
            choice = input(
                "1 - Ignorujesz jego polecenia, i wyruszasz w samotną podróż aby zdobyć pieniądze na lepsze życie \n"
                "2- Idziesz odpocząć aby móc walczyć dla swojego króla.")
            if choice == "1":
                print("Przechodząc przez las zauwazasz nie dogaszone ognisko")
                choice - input(
                    "1 - Sprawdzasz czy ktoś tam czegoś nie zostawił \n 2- Idziesz dalej i ignorujesz wszystko")
                if choice == "1":
                    print("Była to zasadzka miejscowych rabusiów. Zostajesz ogłuszony i okradziony")
                    print("Koniec gry straciłeś wszystko. Przegrałeś ale żyjesz :)")
                elif choice == "2":
                    print("Idąc dalej natrafiłeś na porzucony wóz")
                    print(
                        "Przeszukujesz go i natrafiasz na różne kosztowności takie jak złote sygnety, broń oraz pieniądze")
                    print("Zabierasz je wszystkie ze sobą i szcześliwy jak nigy udajesz się do odległej krainy")
                    print("Wygrałeś grę, ułożyłeś sobie życie na nowo za znalezione przemdioty")
            elif choice == "2":
                print("Odpoczywasz w swoim pokoju, nagle natchneła cię myśl aby jednak wykonać królewskie zadanie")

        elif choice == "2":
            print(
                "Król teraz jest już na ciebie wściekły za znieważenie jego majestatu i nakazuje strażnikom ciebie zabić")
            choice = input("1 - Próbujesz uciec 2 - Nie poddajesz się i walczysz o swój honor")
        if choice == "1":
            print("")
        if random.random() < 0.5:  # 50% na ucieczkę
            straznik = create_przeciwnik()
        if walka_z_straznikiem(character, straznik):
            print(
                "Znaleziono cię ale jesteś na tyle potężnym wojownikiem, że udało ci się wygrać kolejną walkę. Uciekasz do odległej krainy.")
            print("Gratulacje!!! Wygrałeś grę")
        else:
            print("Niestety strażnik cie pokonał. Zginąłeś za swoją zachłanność.")
            print("Koniec gry. Przegrałeś")
    elif choice == "2":
        print("Giniesz w walce o honor 7 strażników rzuciło się na ciebie nie zostawiając żadnych szans")
        print("Niestety przegrałeś grę al przynajmniej z honorem")


print("Koniec gry.")

if __name__ == "__main__":
    main()