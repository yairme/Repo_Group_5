import os, sys, time

#Verhalen in stukken zetten.
def verhaal01():
    print("Het is 7 uur s'ochtonds. Je staat op, douched. Poetst je tanden. eet je eten en gaat naar school.")
    time.sleep(5.0)
    print("Je geheime vriend komt je altijd tegemoet lopen. Jullie zijn stiekem bij elkaar omdat jullie ouders zwaar tegen Homosexualiteit zijn.")
    time.sleep(5.0)
    print("Op school krijg je een toets terug. Je hebt hem niet zo goed gemaakt")
    time.sleep(5.0)
    answer = input("Wat doe je met de toets? VERSTOPPEN/EERLIJK zijn?\n")
    if answer == "VERSTOPPEN":
        print("Je verstopt de toets diep in je tas en gaat verder met school")
        os.system("cls")
        verhaal02()
    if answer == "EERLIJK":
        print("Je bent eerlijk tegen je ouders en ze zijn niet blij. Ze zeggen dat je thuis wat te verwachten staat.")
        time.sleep(5.0)
        os.system("cls")
        verhaal03()

def verhaal02():
    print("Je komt thuis en je ouders vragen om de toets. Je liegt en zegt dat je hem niet hebt")
    time.sleep(5.0)
    print("Je gaat naar boven en laat je tas in je kamer. Je vader sluipt je kamer binnen en gaat je tas door.")
    time.sleep(5.0)
    print("Hij vindt je toets. En flipt. Je hebt amper de kans om te reageren of je vader stormt naar je toe.")
    time.sleep(5.0)
    answer = input("Je weet dat je vader je gaat slaan. Wat doe je? VERDEDIGEN/NIETS\n")
    if answer == "VERDEDIGEN":
        os.system("cls")
        verhaal04()
    if answer == "NIETS":
        os.system("cls")
        verhaal05()

def verhaal03():
    print("Je komt thuis nadat je je ouders hebt vertelt dat je een slecht cijfer had gehaald.")
    time.sleep(5.0)
    print("Je vader schreeuwt naar je en zegt dat je een slechte zoon bent.")
    time.sleep(5.0)
    print("Je eet die avond niet en gaat gelijk naar boven.")
    time.sleep(5.0)
    answer = input("Je voelt je zwaar depressief. Je vriend is iemand die je altijd opvrolijkt. Wat doe je? BERICHT/NIETS\n")
    if answer == "BERICHT":
        os.system("cls")
        verhaal06()
    if answer == "NIETS":
        os.system("cls")
        verhaal08()

def verhaal04():
    print("Je verdedigt jezelf tegen je vader. Maar het wordt al snel erger. Je vader wordt nog agressiever. Je wordt bewusteloos geslagen.")
    time.sleep(5.0)
    print("Je word die zelfde avond naar het ziekenhuis gebracht. Uiteindelijk overlijdt je in het ziekenhuis aan een hersenbloeding")
    time.sleep(5.0)
    os.system("cls")
    answer == input("Wil je opnieuw beginnen? Y/N\n")
    if answer == "Y":
        os.system("cls")
        verhaal01()
    if answer == "N":
        os.system('cls')

def verhaal05():
    print("Je doet niets en wordt geslagen door je vader. Hij stopt na een paar klappen en ja gaat naar boven")
    time.sleep(5.0)
    answer = input("Je gaat liggen op je bed. Je voelt je helemaal niet lekker. Je vriend vrolijkt je altijd op. wat doe je? BERICHT/NIETS\n")
    if answer == "BERICHT":
        os.system("cls")
        verhaal07()
    if answer == "NIETS":
        os.system("cls")
        verhaal08()

def verhaal06():
    print("Je kiest ervoor om je vriend een bericht te sturen.")
    time.sleep(5.0)
    print("Diezelfde avond sluip je het huis uit")
    time.sleep(5.0)
    print("Je komt aan bij je vriend zijn huis. Je ziet dat hij klaar staat met een tas en 2 tickets.")
    time.sleep(5.0)
    print("Je vriend vertelt je dat jullie samen gaan vluchten.")
    answer = input("Ga je akkoord Y/N\n")
    if answer == "Y":
        os.system("cls")
        verhaal09()
    if answer == "N":
        os.system("cls")
        verhaal10()

def verhaal07():
    print("Je kiest ervoor om je vriend een bericht te sturen.")
    time.sleep(5.0)
    print("Je sluipt het huis uit en komt bij je vriend. Het eerste wat hij doet is hij verzorgt je wonden")
    time.sleep(5.0)
    print("Daarna laat hij 2 tickets zien en een tas met kleding")
    time.sleep(5.0)
    input("Hij zegt dat jullie gaan vluchten naar een land waar je wel vrij mag zijn. Ga je akkoord Y/N\n")
    if answer == "Y":
        os.system("cls")
        verhaal09()
    if answer == "N":
        os.system("cls")
        verhaal10()

def verhaal08():
    print("Je kiest ervoor om op bed te blijfen liggen en niks te doen.")
    time.sleep(5.0)
    print("Je denkt een tijdje na en begint te huilen. Je doet je ogen dicht en overleeft de avond niet.")
    time.sleep(5.0)
    os.system("cls")
    answer = input("Wil je opnieuw beginnen? Y/N\n")
    if answer == "Y":
        os.system("cls")
        verhaal01()
    if answer == "N":
        os.system("cls")

def verhaal09():
    print("Je gaat ermee akkoord en jullie vluchten snel nog naar je huis.")
    time.sleep(5.0)
    print("Je pakt heel snel en stil je spullen.")
    time.sleep(5.0)
    print("Je laat perongeluk iets vallen en je vader schrikt wakker")
    time.sleep(5.0)
    answer = input("Wat doe je? REN/VERSTOP\n")
    if answer == "REN":
        os.system("cls")
        verhaal11()
    if answer == "VERSTOP":
        os.system("cls")
        verhaal12()

def verhaal10():
    print("Je kan er niet mee akkoord.")
    time.sleep(5.0)
    print("Je vriend ziet er teleurgesteld uit en vlucht in zijn eentje")
    time.sleep(5.0)
    print("Je komt die avond thuis en wordt uitgescholden door je ouders.")
    time.sleep(5.0)
    print("Je sluit jezelf op in je kamer")
    time.sleep(5.0)
    print("Je blijft stil en verliest je enige kans om weg te komen")
    os.system('cls')
    answer = input("Wil je opnieuw beginnen? Y/N\n")
    if answer == "Y":
        os.system("cls")
        verhaal01()
    if answer == "N":
        os.system('cls')

def verhaal11():
    print("Je kiest ervoor om weg te rennen.")
    time.sleep(5.0)
    print("Je rent naar buiten en je vrient rent alvast weg")
    time.sleep(5.0)
    answer = input("Je vader tackled je. Wat doe je. ELLEBOOG/KNIE\n")
    if answer == "ELLEBOOG":
        os.system("cls")
        verhaal13()
    if answer == "KNIE":
        os.system('cls')
        verhaal14()

def verhaal12():
    print("Je verstopt je in de kamer.")
    time.sleep(5.0)
    print("Na 15 minuten is het weer stil")
    time.sleep(5.0)
    print("Je gaat stiekem naar buiten")
    time.sleep(5.0)
    os.system("cls")
    verhaal15()

def verhaal13():
    print("Je geeft je vader een ellenboog op ze kaak.")
    time.sleep(5.0)
    print("Je vader laat je los en je rent zo snel mogelijk weg")
    time.sleep(5.0)
    print("Je vriend rent met je mee")
    time.sleep(1.0)
    os.system('cls')
    verhaal16()

def verhaal14():
    print("Je probeert je vader een knie in zijn buik te geven")
    time.sleep(5.0)
    print("Je vader verdedigt zichzelf")
    time.sleep(5.0)
    print("Je wordt mee terug naar binnen gesleept. Je ziet je enige kans om weg te vluchten voor je ogen verdwijnen")
    time.sleep(5.0)
    os.system('cls')
    answer = input("Wil je opnieuw beginnen? Y/N\n")
    if answer == "Y":
        os.system("cls")
        verhaal01()
    if answer == "N":
        os.system('cls')

def verhaal15():
    print("Je loopt naar buiten")
    time.sleep(5.0)
    print("Je vriend staat je op te wachten en geeft je een knuffel")
    time.sleep(5.0)
    print("Jullie gaan samen naar het vliegveld")
    time.sleep(5.0)
    os.system('cls')
    verhaal17()

def verhaal16():
    print("Je rent samen met je vriend naar het vliegveld")
    time.sleep(5.0)
    print("Je stopt onderweg voor een kleine pauze")
    time.sleep(5.0)
    print("Je gaat erna weer door.")
    time.sleep(5.0)
    os.system("cls")
    verhaal17()

def verhaal17():
    print("Jullie komen aan op het vliegveld")
    time.sleep(5.0)
    print("Jullie wachten een uurtje ofzo en stappen het vliegtuig in")
    time.sleep(5.0)
    print("Je bent zo moe na wat er vandaag is gebeurt dat je tegen je vriend aan in slaap valt")
    time.sleep(5.0)
    os.system("cls")
    verhaal18()

def verhaal18():
    print("Je komt aan op schipol airport.")
    time.sleep(5.0)
    print("Je loopt naar een beveiliger en legt je hele verhaal uit")
    time.sleep(5.0)
    print("Je moet wachten in een kamer samen met je vriend")
    time.sleep(5.0)
    os.system("cls")
    verhaal19()

def verhaal19():
    print("Je wordt door het hele process geholpen")
    time.sleep(5.0)
    print("Na lang wachten mag je uiteindelijk in het land blijfen")
    time.sleep(5.0)
    print("Nu staat er nog een keuzen te wachten")
    time.sleep(5.0)
    answer = input("ZAANDAM/AMSTERDAM\n")
    if answer == 'ZAANDAM':
        os.system("cls")
        verhaal20()
    if answer == "AMSTERDAM":
        os.system('cls')
        verhaal21()

def verhaal20():
    print("Jullie hebben gekozen om in Zaandam te wonen")
    time.sleep(5.0)
    print("5 jaar later en jullie nederlands is best goed")
    time.sleep(5.0)
    print("Jullie weten nu ook meer van de cultuur")
    time.sleep(5.0)
    print("Jullie zijn extreem gelukkig met elkaar")
    time.sleep(5.0)
    print("Het einde.")
    time.sleep(2.0)
    os.system('cls')

def verhaal21():
    print("Jullie hebben gekozen om in Amsterdam te wonen")
    time.sleep(5.0)
    print("5 jaar later en jullie nederlands is best goed")
    time.sleep(5.0)
    print("Jullie weten nu ook meer van de cultuur")
    time.sleep(5.0)
    print("Jullie zijn extreem gelukkig met elkaar")
    time.sleep(5.0)
    print("Het einde.")
    time.sleep(2.0)
    os.system('cls')

print("Korea is een streng land als het gaat om je sexualiteit. ")
print("Wat zou jij doen in welke situatie. We gaan het uitvinden.")
answer = input("Beginnen Y/N\n")

if answer == 'Y':
    verhaal01()
if answer == "N":
    os.system("cls")
