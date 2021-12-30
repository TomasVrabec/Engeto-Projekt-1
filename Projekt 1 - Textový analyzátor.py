TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

oddelovac = "-"*35

registrovani = {
	"bob": "123",
	"ann": "pass123",
	"mike": "password123",
	"liz": "pass123",
			}

# PRIHLASOVANI:
username = input("username: ")
password = input("password: ")
print(oddelovac)

if registrovani.get(username) == password:
	print(f"""Welcome to the app, {username}
We have 3 texts to be analyzed.
{oddelovac}""")

else:
	print("Unregistered user, terminating the program...")
	quit()

# VYBER TEXTU
vyber = input("Enter a number btw. 1 and 3 to select: ")
print(oddelovac)

if vyber.isnumeric() and 0 < int(vyber) < 4:
	text = TEXTS[int(vyber) - 1]
	vycistena_slova = list()
	pocet_slov = 0
	zacinajici_velkym = 0
	velkymi_pismeny = 0
	malymi_pismeny = 0
	pocet_cisel = 0
	soucet_cisel = 0
	vyskyt_delky = dict()

	for slovo in text.split():
		vycistena_slova.append(
			slovo.strip(",.:;")
		)
		pocet_slov += 1

		if slovo.isalpha() and slovo.isupper():
			velkymi_pismeny += 1

		if slovo[0].isupper():
			zacinajici_velkym += 1

		elif slovo.islower():
			malymi_pismeny += 1

		elif slovo.isnumeric():
			pocet_cisel += 1
			soucet_cisel += int(slovo)

else:
	print("Incorrect input, terminating the program...")
	quit()

# POCET PISMEN
for i in vycistena_slova:
	for pocet_pismen in i:
		delka = len(i)
		if delka not in vyskyt_delky:
			vyskyt_delky[delka] = 1
			break
		else:
			vyskyt_delky[delka] += 1
			break

print(f"""There are {pocet_slov} words in the selected text.
There are {zacinajici_velkym} titlecase words.
There are {velkymi_pismeny} uppercase words.
There are {malymi_pismeny} lowercase words.
There are {pocet_cisel} numeric strings."
The sum of all the numbers is {soucet_cisel}.
{oddelovac}
LEN|   OCCURENCES    |NR.
{oddelovac}""")

vysledky = list()
for vyskyt in vyskyt_delky:
	vysledky.append((vyskyt_delky[vyskyt], vyskyt))

setridene_vysledky = sorted(vysledky, key=lambda x: x[1])

for tupl in setridene_vysledky:
	graf = tupl[0]*"*"
	print(f"{tupl[1]:>3}|{graf:<17}|{tupl[0]}")