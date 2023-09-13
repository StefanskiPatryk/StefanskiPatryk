import numpy as np
import cv2


class EdytorObrazkow:
    def __init__(self):
        self._image = None
        self._edited_image = None
        self._original_image = None

    def wczytaj_obrazek(self, nazwa_pliku):
        try:
            self._image = cv2.imread(nazwa_pliku)
            self._edited_image = np.copy(self._image)
            self._original_image = np.copy(self._image)
            print("Obrazek udało się wczytać.")
        except Exception as e:
            print("Napotkano błąd podczas wczytywania obrazka:", str(e))

    def zapisz_obrazek(self, nazwa_pliku):
        if self._edited_image is not None:
            try:
                cv2.imwrite(nazwa_pliku, self._edited_image)
                print("Obrazek został zapisany jako", nazwa_pliku)
            except Exception as e:
                print("Napotkano problem podczas zapisywania obrazka:", str(e))
        else:
            print("Problem z zapisaniem obrazka. Wczytaj obrazek, wykonaj edycję i spróbuj ponownie.")

    def wyswietl_obrazek(self):
        if self._image is not None:
            cv2.imshow("Edytor Obrazków", self._image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            print("Brak obrazka do wyświetlenia. Wczytaj obrazek, wykonaj edycję i spróbuj ponownie.")

    def przestrzen_barw(self):
        if self._original_image is not None:
            try:
                if len(self._original_image.shape) == 3:
                    self._edited_image = cv2.cvtColor(self._original_image, cv2.COLOR_BGR2RGB)
                    print("Obrazek został przekształcony do przestrzeni barw.")
                else:
                    print("Nieprawidłowa ilość kanałów obrazu. Spróbuj wczytać obraz kolorowy.")
            except Exception as e:
                print("Napotkano błąd podczas transformacji przestrzeni barw:", str(e))
        else:
            print("Brak obrazka do przekształcenia. Wczytaj obrazek i spróbuj ponownie.")

    def negatyw(self):
        if self._original_image is not None:
            try:
                self._edited_image = cv2.bitwise_not(self._original_image)
                print("Obrazek został zanegowany.")
            except Exception as e:
                print("Napotkano błąd podczas negatywu:", str(e))
        else:
            print("Brak obrazka do zanegowania. Wczytaj obrazek i spróbuj ponownie.")

    def binaryzacja(self, prog):
        if self._original_image is not None:
            try:
                _, self._edited_image = cv2.threshold(self._original_image, prog, 255, cv2.THRESH_BINARY)
                print("Obrazek został zbinaryzowany.")
            except Exception as e:
                print("Napotkano błąd podczas binaryzacji:", str(e))
        else:
            print("Brak obrazka do zbinaryzowania. Wczytaj obrazek i spróbuj ponownie.")

    def erozja(self, rozmiar, osmiospojna=True):
        if self._original_image is not None:
            try:
                kernel = cv2.getStructuringElement(cv2.MORPH_RECT if osmiospojna else cv2.MORPH_CROSS, (rozmiar, rozmiar))
                self._edited_image = cv2.erode(self._original_image, kernel)
                print("Zastosowano erozję.")
            except Exception as e:
                print("Napotkano błąd podczas erozji:", str(e))
        else:
            print("Brak obrazka do erozji. Wczytaj obrazek i spróbuj ponownie.")

    def otwarcie(self, rozmiar, osmiospojna=True):
        if self._original_image is not None:
            try:
                kernel = cv2.getStructuringElement(cv2.MORPH_RECT if osmiospojna else cv2.MORPH_CROSS, (rozmiar, rozmiar))
                self._edited_image = cv2.morphologyEx(self._original_image, cv2.MORPH_OPEN, kernel)
                print("Zastosowano otwarcie.")
            except Exception as e:
                print("Napotkano błąd podczas otwarcia:", str(e))
        else:
            print("Brak obrazka do otwarcia. Wczytaj obrazek i spróbuj ponownie.")

    def domkniecie(self, rozmiar, osmiospojna=True):
        if self._original_image is not None:
            try:
                kernel = cv2.getStructuringElement(cv2.MORPH_RECT if osmiospojna else cv2.MORPH_CROSS, (rozmiar, rozmiar))
                self._edited_image = cv2.morphologyEx(self._original_image, cv2.MORPH_CLOSE, kernel)
                print("Zastosowano domknięcie.")
            except Exception as e:
                print("Napotkano błąd podczas domknięcia:", str(e))
        else:
            print("Brak obrazka do domknięcia. Wczytaj obrazek i spróbuj ponownie.")

    def wyrownaj_histogram(self):
        if self._original_image is not None:
            try:
                self._edited_image = cv2.equalizeHist(self._original_image)
                print("Histogram został wyrównany.")
            except Exception as e:
                print("Napotkano błąd podczas wyrównywania histogramu:", str(e))
        else:
            print("Brak obrazka do wyrównania histogramu. Wczytaj obrazek i spróbuj ponownie.")

    def kompresja(self):
        if self._original_image is not None:
            try:
                _, self._edited_image = cv2.imencode(".jpg", self._original_image)
                print("Obrazek został skompresowany.")
            except Exception as e:
                print("Napotkano błąd podczas kompresji:", str(e))
        else:
            print("Brak obrazka do skompresowania. Wczytaj obrazek i spróbuj ponownie.")

    def wygladzanie(self, rozmiar):
        if self._original_image is not None:
            try:
                self._edited_image = cv2.blur(self._original_image, (rozmiar, rozmiar))
                print("Zastosowano wygładzanie przez uśrednianie.")
            except Exception as e:
                print("Napotkano błąd podczas wygładzania:", str(e))
        else:
            print("Brak obrazka do wygładzania. Wczytaj obrazek i spróbuj ponownie.")

    def zmien_filtr(self):
        if self._original_image is not None:
            try:
                print("\n--- DOSTĘPNE FILTRY ---")
                print("1. Filtr Gaussa")
                print("2. Filtr medianowy")
                wybor = input("Wybierz filtr: ")

                if wybor == "1":
                    rozmiar = int(input("Podaj rozmiar filtra Gaussa: "))
                    self._edited_image = cv2.GaussianBlur(self._original_image, (rozmiar, rozmiar), 0)
                    print("Zastosowano filtr Gaussa.")
                elif wybor == "2":
                    rozmiar = int(input("Podaj rozmiar filtra medianowego: "))
                    self._edited_image = cv2.medianBlur(self._original_image, rozmiar)
                    print("Zastosowano filtr medianowy.")
                else:
                    print("Nieprawidłowy wybór filtra.")

            except Exception as e:
                print("Napotkano błąd podczas zmiany filtru:", str(e))
        else:
            print("Brak obrazka. Wczytaj obrazek i spróbuj ponownie.")

def menu():
    edytor = EdytorObrazkow()
    while True:
        print("\nMENU EDYCJI: ")
        print("1. Wczytaj obrazek")
        print("2. Wyświetl obrazek")
        print("3. Zapisz obrazek")
        print("4. Przekształcenie do przestrzeni barw")
        print("5. Zbinaryzuj obrazek")
        print("6. Negatyw")
        print("7. Zastosuj erozję")
        print("8. Zastosuj otwarcie")
        print("9. Zastosuj domknięcie")
        print("10. Skompresuj obrazek")
        print("11. Wyrównaj histogram")
        print("12. Zmień filtr")
        print("13. Wygładź obrazek")
        print("0. Wyjście")

        opcja = input("Wybierz opcję: ")

        if opcja == "1":
            nazwa_pliku = input("Proszę podać nazwę pliku: ")
            edytor.wczytaj_obrazek(nazwa_pliku)
        elif opcja == "2":
            edytor.wyswietl_obrazek()
        elif opcja == "3":
            nazwa_pliku = input("Proszę podać nazwę pliku do zapisu: ")
            edytor.zapisz_obrazek(nazwa_pliku)
        elif opcja == "4":
            edytor.przestrzen_barw()
        elif opcja == "5":
            prog = int(input("Proszę podać próg binaryzacji: "))
            edytor.binaryzacja(prog)
        elif opcja == "6":
            edytor.negatyw()
        elif opcja == "7":
            rozmiar = int(input("Proszę podać rozmiar erozji: "))
            edytor.erozja(rozmiar)
        elif opcja == "8":
            rozmiar = int(input("Proszę podać rozmiar otwarcia: "))
            edytor.otwarcie(rozmiar)
        elif opcja == "9":
            rozmiar = int(input("Proszę podać rozmiar domknięcia: "))
            edytor.domkniecie(rozmiar)
        elif opcja == "10":
            edytor.kompresja()
        elif opcja == "11":
            edytor.wyrownaj_histogram()
        elif opcja == "12":
            edytor.zmien_filtr()
        elif opcja == "13":
            rozmiar = int(input("Proszę podać rozmiar wygładzania: "))
            edytor.wygladzanie(rozmiar)

        elif opcja == "0":
            break
        else:
            print("Nieprawidłowy wybór. Wybierz ponownie.")

menu()