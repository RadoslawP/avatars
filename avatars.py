def cecha(zapytanie, domyslna):
	pytanie = zapytanie + '[' + domyslna + ']? '
	odpowiedz = input(pytanie)
	if (odpowiedz == ''):
		odpowiedz = domyslna
	print ('Wybrales: ', odpowiedz)
	return odpowiedz

wlosy = cecha('Jaki kolor wlosow', 'brazowy')
wlosy_dlugosc = cecha('Jaka dlugosc wlosow', 'krotkie')
oczy = cecha('Jakie kolor oczu', 'niebieskie')
plec = cecha('Jaka plec', 'kobieta')
okulary = cecha('Okulary', 'nie')
broda = cecha('Broda', 'nie')
