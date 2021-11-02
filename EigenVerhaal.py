import time
import datetime







def vraag1():
    print("Mijn verhaal: In 2012 brak er een burgeroorlog uit in Syrië. Door de dictator die de hoofd was van de staat ging hij de Rejim (Syrische leger) op de burgers afsturen.  Er vallen veel doden door de soldaten en de bommen. Er zijn veel protesten waar ik en je familie ook mee aan doet. Helaas heb ik al mijn vrienden en familie verloren alleen niet mijn     beste vriend en oom. Ahmad (mijn vriend) en ik maken een plan en willen naar een andere stad toe genaamd Homs. Voor het vertrek vraag ik aan mijn oom of hij meewilt.. mijn oom heeft nog hoop en wilt blijven in Syrië. Wanneer hij hoort dat Ahmad en ik naar Homs gaan zegt hij dat het een heel slecht idee is.. omdat, hij heeft gehoord dat daar ook burger-oorlog is uitgebroken. Hij geeft Ahmad en mij het advies om naar Afrin te vluchten en vandaar naar Turkije te gaan. ")
    time.sleep(1)
    print(" \nAhmad en ik hebben lang nagedacht over het advies van mijn oom. Wij hebben samen wat geld verzameld voor onze reis en hebben een tent, 2 grote tassen, voedsel en andere benodigdheden gekochten voor de lange reis naar ...")
    time.sleep(1)
    print("a: Ik ga naar Turkije!")
    time.sleep(1)
    print("b: Ik ga naar Homs!")
    antwoord = input()
    if antwoord.lower() == "a": 
        print("Op weg naar Turkije...")
        vraag2()
    elif antwoord.lower() =="b": 
        print("Op weg naar Homs")
        vraag3()
    else:
        print("Kies alleen a of b >>>")
        vraag1()
    
def vraag2():
    time.sleep(1)
    print("Ahmad en ik pakken 2 grote rugtassen en stoppen wij daar onze pasporten, wat eten en drinken en kleding in en wat hulp middelen zoals een snijmes en aansteker… Het duurt 6 uur op te voet om naar Afrin te gaan.")
    time.sleep(1)
    print("Na 4 uur lopen zijn Ahmad en ik heel moe dus willen wij even een pauze gaan nemen en een dutje te doen. \n \nUren later…\n \nWij worden wakker en kijken na de tijd.. wij zijn 6 uur veder. Ahmad en ik schrikken.. hoe hebben wij ons zolang verslapen vragen wij tegen onszelf. Het is nu nacht en donker, wij zijn heel bang omdat, wij allemaal wolven geluiden horen en we hebben niks bij ons om ons zelf te verdedigen… alleen een snijmes en een aansteker die weinig tot geen invloed gaat hebben op een grote groep wolven.\n \n2 uur later…\n \nNa vele angst van opgegeten te worden door een wolf zijn wij eindelijk bij Afrin. Wij horen van andere dat van Afrin naar de Turkse grens 435,3km is. Ahmad en ik verliezen geen tijd en gaan snel weer reizen…\n \nWeek later…\n \nAhmad en ik gaan naar de grens en de Turkse soldaten controleren onze pasporten.. we mogen over de grens en Ahmad & ik voelen ons meteen stuk veiliger, het is alsof een zwaar stuk steen van ons rug is gegleden. Wij kopen 1 grote tent want die van ons is verslepen en wat eten om de nacht te overleven. Ze proberen en goed plek uit te zoeken in de bos van Turkije om te overnachten met onze tent… Ahmad en ik hebben de dag overleeft ondanks de kou. We zoeken dagen lang naar een organisatie die een toekomst te bieden heeft voor vluchtelingen.\n \nDagen later…\n \nNa dagen lang zoeken hebben wij een Turks organisatie gevonden die vluchtelingen met een paspoort een reis aanbiedt naar Nederland. Ahmad en ik hebben ons meteen aangemeld naar de organisatie en we zijn goedgekeurd.. dat betekent dat wij naar Nederland mogen gaan over paar dagen.. ")
    time.sleep(1)
    print("Dagen later..\n \nDe organistatie regelt vervoer voor ons en Ahmad en ik gaan naar Turkije! Wij zijn erg blij dat de organisatie ons heeft goedgekeurd en naar Turkije mogen.")
    time.sleep(1)
    print("a: in Turkije blijven.")
    time.sleep(1)
    print("b: Naar Nederland gaan.")
    antwoord = input()
    if antwoord.lower() == "a":
        vraag6()
    elif antwoord.lower() == "b":
        vraag7()
    else:
        print("Kies alleen a of b >>>")
        vraag1()

def vraag3():
    print("Het duurt 2.5 uur om naar Homs te gaan... Ahmad en ik kopen wat benodigenheden zoals een tent, voedsel, aansteker, snijmes ect.. Het is een best gevaarlijke reis want wij moeten door veel bossen lopen om Homs te bereiken. Er vliegt van alles in ons hoofd.. we kunnen door wolven of beren gegeten worden! er kan val alles gebeuren denken wij. Over een half uur gaan wij vertrekken.. we gaan nog snel langs mijn oom om afscheid te nemen. Wanneer mijn oom hoort dat wij toch naar Homs gaan ondanks zijn advies is hij een beetje teleurgesteld.\n \n 3 uur later...\n \nEenmaal aangekomen in Homs zijn Ahmad en ik erg blij. Ons reis was verschikkelijk erg, wij hoorden allerei wolf geluiden en hadden het erg moe en koud. Eenmaal in Homs maken wij wat eten klaar omdat, wij verschikkelijke honger hebben. We maken ook ons tent klaar om een dutje te doen.")
    time.sleep(1)
    print("Na ons dutje gingen Ahmad en ik dit doen:")
    time.sleep(1)
    print("a: Ahmad en ik gingen meteen werk zoeken")
    time.sleep(1)
    print("b: Ahmad en ik gingen bedelen voor wat geld omdat, wij nog heel weinig geld over hadden.")
    antwoord = input()
    if antwoord.lower() == "a":
        vraag4()
    elif antwoord.lower() == "b":
        vraag5()
    else:
        print("Kies alleen a of b >>>")
        vraag1()


def vraag4():
    time.sleep(1)
    print("Na lang zoeken hebben wij werk gevonden bij een restaurant van een Hotel. Het betaalt niet al te best maar we kunnen er veder mee... Ahmad en ik werken lang bij de restaurant en sparen aardig wat geld bij elkaar.")
    print("Ahmad en ik gingen: \n \na: Doorwerken \nb: Een ander werk zoeken")
    antwoord = input()
    if antwoord.lower() == "a":
        vraag14()
    elif antwoord.lower() == "b":
        vraag15()
    else:
        print("Kies alleen a of b >>>")
        vraag1()





def vraag5():
    time.sleep(1)
    print("Met het bedelen gingen wij niet vooruit. We bedelde per dag ongeveer 5 tot 6 uur en maakte er heel weinig geld mee dus besloten wij toch te gaan werken.")
    print("Ahmad en ik hadden door dat wij tijdens het bedelen in de gaten werden gehouden door een man. Tijdens wij gingen zoeken naar werk ging de man ons achtervolgen... \n \nna een tijdje kwam hij naar ons toen, hij zei: zoeken jullie werk? Ahmad & ik: ja, wij bedelde eerst maar, zoeken nu naar werk. Man: als je voor mij bedeld krijg je %20 van het geld en ik geef je locatie's door waar je veel geld kan bedelen. \n \nAhmad en ik hadden het verzoek geaccepteerd van de man en begonnen met bedelen.")
    print("Na een tijdje merkte Ahmad en ik dat wij heel slecht werden betaalt door de bedelaar-baas. We gingen \n \na: Door met bedelen \nb: Stoppen met bedelen.")
    antwoord = input()
    if antwoord.lower() == "a":
        vraag10()
    elif antwoord.lower() == "b":
        vraag11()
    else:
        print("Kies alleen a of b >>>")
        vraag1()

def vraag6():
    time.sleep(0.5)
    print("Ahmad en ik blijven nog even in Turkije door onze baan hier. We wennen aan de levenswijze hier in Turkije en verzamelen aardig wat geld.")
    time.sleep(1)
    print("a: Ahmad en ik gingen door met verzamelen van geld in Turkije")
    time.sleep(1)
    print("b: Ahmad en ik hadden best wat Lira (Turkse geld) verzamelt en bedachten ons het geld om te wisselen bij een geldwisselkantoor")
    antwoord = input()
    if antwoord.lower() == "a":
        vraag16()
    elif antwoord.lower() == "b":
        vraag8()
    else:
        print("Kies alleen a of b >>>")
        vraag1()



def vraag8():
    time.sleep(0.5)
    print("Eenmaal aangekomen kwam een man naar ons toe toen hij zag dat wij naar geldwisselkantoor zochten. Hij was een oplichter en wij vertrouwde het meteen niet en gingen naar een officiële geldwisselkantoor.")
    time.sleep(0.5)
    print("We wisselde ons geld en kochten met een deel wat eten, kleding. We huurden een klein hotel kamertje, dat noemen ze ótel in Turkije. Na een tijdje besloten wij:")
    time.sleep(0.5)
    print("a: Proberen een huis te huren \n \nb: Geld proberen te lenen bij de bank om een huis te kopen.")
    antwoord = input()
    if antwoord.lower() == "a":
        vraag21()
    elif antwoord.lower() == "b":
        vraag22()
    else:
        print("Kies alleen a of b >>>")
        vraag1()

def vraag7():
    time.sleep(0.5)
    print("Met het zelfde organisatie hebben Ahmad en ik geprobeerd te regelen dat wij naar Nederland mogen gaan. De Turkse organisatie heeft contact gemaakt met een Nederlandse organisatie voor ons om naar Nederland te gaan. Ahmad en ik zijn erg blij met die mooi nieuws!")
    print("Ahmad en ik gaan naar de stad om wat nieuwe kleding te halen voor Nederland... de organisatie betaalt de helft van onze ticket, de ander helft moeten wij betalen.")
    print("2 dagen later...")
    print("Ahmad en ik hebben weer goed nieuws, ons vlucht is gehaald voor over 2 dagen. Wij moeten in totaal 125 euro betalen de andere helft betaalt de organisatie.   ")
    
    time.sleep(0.5)
    print("2 dagen later...")
    time.sleep(0.5)
    print("Onze reis is gekomen, we gaan vandaag vluchten naar Nederland. Over 5 uur moeten wij op de vliegveld zijn.")
    time.sleep(0.5)
    print("5 uur later...")
    time.sleep(0.5)

    print("We zijn aangekomen in Nederland.. HOERA! Na een tijdje wennen we met Ahmad aan een heel schoon begin. Wij werken bij een hotel en groeien snel uit van medewerkers tot asssistent manager en daarna tot manager.")
    print("Later gingen Ahmad en ik trouwen en kregen we kinderen... EINDE! ")
    print("\n")
    vraag1()
    antwoord = input()
    
    


def vraag16():
    time.sleep(0.5)
    print("Op een gegeven moment hadden wij zo veel geld verzameld bij elkaar dat wij naar een ander land wouden gaan. Wij wouden naar Nederland gaan omdat, in Nederland de economie beter was, je verdient gemiddeld meer en krijg je beter hulp hoorde wij. Ahmad en ik gingen opzoek naar tickets voor naar Nederland te gaan. We hadden de tickets gevonden en gingen met:")
    print("a: KLM")
    print("b: Turkisch airlines")
    antwoord = input()
    if antwoord.lower() == "a":
        vraag9()
    elif antwoord.lower() == "b":
        vraag9()
    else:
        print("Kies alleen a of b >>>")
        vraag1()


def vraag9():
    time.sleep(1)
    print("Ahmad en ik hebben een vliegtuig gekocht... helaas hebben wij veel geld gegeven aan de 2 tickets maar we gaan naar Nederland! Ahmad en ik zijn heel blij en we gaan na 2 dagen vliegen! \n \n2 dagen later... \n \nhet is zo ver.. vandaag is onze vlucht. Ahmad en ik moet over precies 6 uur op de vliegveld zijn. We roepen een Taksi (Taxi) en gaan naar de vliegveld. Eenmaal aangekomen op de vliegveld betalen wij de Taksi, het heeft ons aardig wat gekost om naar hier te komen. We checken snel in bij de vliegveld en gaan de rij in om onze koffers in te leveren. Na dat wij onze koffers hebben ingeleverd wachten tot dat wij de vliegtuig in mogen gaan.\n \n45 minuten later... \n \nAhmad en ik zijn in de vliegtuig na 10 minuten gaat de vliegtuig stijgen en zijn wij na ongeveer 3.5 uur in Nederland. 2 dagen van te voren hebben wij met behulp van een geldbedrag via via een orginisatie geregeld in Nederland waar Ahmad en ik mogen verblijven.")
    print("3.5 uur later...")
    print("Ahmad en ik zijn aangekomen in Nederland wij pakken onze koffers en worden opgehaald door 1 man en 1 vrouw van de organisatie. Ze brengen ons naar ons verblijfplaats... \n \nEenmaal aangekomen bij ons nieuw verblijfplaats in Nederland proberen we aan deze nieuwe levensomgeving te wennen. Het is hier allemaal anders, je betaalt hier met Euro en alles is hier duurder. Ahmad en ik vinden meteen werk en vragen de organisatie om hulp of zei weten waar wij mogen werken. De organisatie zegt dat wij de komende 2 dagen niet naar buiten mogen gaan omdat, er wat testje van ons moet worden afgenomen.\n \n2 dagen later... Ahmad en ik hebben meteen werk gevonden bij een snackbar... we houden de snackbar schoon en verdienen aardig wat centjes vergeleken met Turkije omdat, je hier in Euro's word uitbetaald.")
    print("Maanden later...")
    print("Ahmad en ik wennen aan Nederland wij zijn ook overgestapt van werk na een tijdje en hebben zo veel geld verdiend dat wij besloten in Nederland te wonen en een verblijfsvergunning proberen te krijgen.")
    print("Dagen later...\n \nhet is Ahmad en mij gelukt om een verblijfsvegunning te krijgen. Ons aanvraag bij de Gemeente is goedgekeurd... Ahmad en ik zijn heel blij en huren samen een huis.")
    print("De zaken gaan zo goed dat wij zelfs een 2e snackbar openen. In de tussentijd hebben Ahmad en ik 2 vriendinnen. Na een lange periode besluiten wij te trouwen en gaan Ahmad en ik apart wonen.")
    print("1 jaar later... \n \n Ahmad en ik zijn al bijna 1 jaar getrouwd met 2 andere vrouwen en Ahmad zijn vrouw is al zwanger. Ze denken dat het een kind wordt. Ik en mijn vrouw zijn heel blij voor Ahmad en zijn vrouw. Ons leven gaat goed door in Nederland! EINDE...")
    print("\n")
    vraag1()
    antwoord = input()



def vraag10():
    time.sleep(1)
    print("Ondanks wij worden genaaid verdienen wij toch aardig wat met dit bedelen... na een tijdje stoppen wij toch en gaan wij werken bij een restaurant...")
    print("Bij het restaurant verdienen wij ongeveer 2x zo veel dan met het bedelen. Wij (Ahmad & ik) merken wel dat het lastiger werk is dan het bedelen.")

    time.sleep(1)
    print("11 maanden later...")

    time.sleep(1)
    print("Wij hebben zo veel geld verdiend bij elkaar omdat, wij zijn opgegroeid tot manager want, Ahmad en ik werkte zo hard, snel en prof. dat wij promotie kregen naar manager.")
    
    print("5 maanden later... \n \nAhmad en ik bedenken ons om een eigen restaurant te beginnen")
    print("We beginnen de restaurant we voor: \n \na: 1 verdieping \nb: 2 verdiepingen")
    antwoord = input()
    if antwoord.lower() == "a":
        vraag12()
    elif antwoord.lower() == "b":
        vraag12()
    else:
        print("Kies alleen a of b >>>")
        vraag1()
        

    


def vraag11():
    time.sleep(1)
    print("Ahmad en ik zoeken naar normaal werk. Wij werken bij een supermarket. We doen van alles, denk maar aan vakkenvullen, kassa, schoonmaken ect. Ahmad en ik merken dat de economie in Homs steeds slechter worden.")
    print("Wij bedenken ons om naar Nederland te gaan of door te gaan met werken maar dan in Turkije. \n \na: Turkije \nb: Nederland")
    antwoord = input()
    if antwoord.lower() == "a":
        vraag13()
    elif antwoord.lower() == "b":
        vraag9()
    else:
        print("Kies alleen a of b >>>")
        vraag1()
    

def vraag12():
    time.sleep(1)
    print("Ons restraunt gaat open. Ahmad en ik delen flyers uit. Bij onze opening komen er veel mensen wat eten... \n \n4 maanden later...\n \nAhmad en ik wennen aan Turkije, wij verbeteren ook onze Turks en blijven leven in Turkije. Ik trouw met een Turks vrouw waardoor ik ook een Turks pasport krijg. Ahmad en ik wonen na mijn trouwfeest apart maar, spreken elkaar wel elke dag door onze band. En door de restaurant die van ons 2 is.... EINDE!")
    print("\n")
    vraag1()
    antwoord = input()


def vraag13():
    time.sleep(1)
    print("Onderweg naar Turkije... je gaat terug naar je oom omdat, hij je naar Afrin gaat brengen met zijn auto. Het is gevaarlijk maar, het is jou en Ahmad gelukt om Turkije te bereiken. \n \n \n je komt aan in Turkije. Het is in Turkije makkelijk om werk te vinden. Je verdient meer in Turkije dan in Homs.   ")
    print("Uiteindelijk werken wij lang bij een bakkal (Turks market) en openen zelf een klein bakkal. Ahmad en ik verdienen goed genoeg met ons winkel en leven lang en gelukkig EINDE! ")
    print("\n")
    vraag1()
    antwoord = input()


def vraag14():
    time.sleep(1)
    print("We gingen doorwerken bij de Hotel en verdiende daarom heel veel geld. We bedachten ons om te verhuizen naar een ander land.")
    time.sleep(1)
    print("a: Nederland \nb: Blijven in Homs")
    antwoord = input()
    if antwoord.lower() == "a":
        vraag17()
    elif antwoord.lower() == "b":
        vraag18()
    else: 
        print("Kies alleen a of b >>>")
        vraag1()



def vraag15():
    time.sleep(1)
    print("Wij zochten naar een ander werk. ik was nu bezorger met Ahmad, eigenlijk was het illegaal wat jullie deden want, jullie hadden geen rijbewijs.")
    time.sleep(1)
    print("a: Stoppen met dit werk \nb: Doorgan met dit werk")
    antwoord = input()
    if antwoord.lower() == "a":
        vraag19()
    elif antwoord.lower() == "b":
        vraag20()
    else:
        print("Kies alleen a of b >>>")
        vraag1()




def vraag17():
    time.sleep(1)
    vraag9()
    antwoord = input()



def vraag18():
    time.sleep(1)
    print("Ahmad en ik begonnen na een tijdje werklooz te zijn en begonnen uit te hongeren. Omdat, wij in Homs bleven kwam de oorlog ook in Homs. Door de slechte leefomgeving en hongerarmoede gingen Ahmad en ik helaas overlijden.... EINDE!")
    print("\n")
    vraag1()
    antwoord = input()


def vraag19():
    time.sleep(1)
    print("Door het bedelen moesten Ahmad en ik de gevangenis is. Doordat ze zagen dat wij vluchtelingen waren hadden wij een nog erger straf... wij moesten levenlangs de gevangenis in EINDE...")
    print("\n")
    vraag1()
    antwoord = input()




def vraag20():
    time.sleep(1)
    print("Je verdient heel veel geld en gaat naar Nederland verhuizen samen met Ahmad.")
    vraag9()
    antwoord = input


def vraag21():
    time.sleep(1)
    print("We huurden een klein kamer in een apartement. Ookal was de kamer niet groot de verhuurder vroeg er aardig wat voor.")
    vraag23()
    antwoord = input()



def vraag22():
    time.sleep(1)
    print("Doordat wij vluchtenlingen zijn heeft de bank helaas geen geld aan ons geleend. Daardoor moesten wij toch met ons budget een kamer blijven huren.")
    vraag23()
    antwoord = input()

def vraag23():
    time.sleep(1)
    print("Na het huren zoeken Ahmad en ik naar werk... wij hebben werk gevonden bij een aquapark. Wij beginnen bij schoonmakers en in korte tijd krijgen wij promotie tot aquapark manager.")
    time.sleep(1)
    print("\n 2 jaar  later...")
    time.sleep(1)
    print("Ahmad en ik hebben in de tussentijd een groot vermogen opgeboud en lekker wat geld bij elkaar verzameld. Wij openen zelfs onze aqua park en noemen het naar onze buurt van Syrië.")
    time.sleep(1)
    print("Helaas heeft mijn oom de oorlog niet overleeft... toen ik het slecht nieuws hoorde barste ik uit tranen... gelukkig stond Ahmad altijd naast mij en hielp mij met deze zware tijd.")
    time.sleep(1)
    print("We leefden lang en gelukkig in Turkije en gingen later trouwen met 2 Turkse vrouwen en bouwden een gezin op. EINDE!")
    print("\n")
    vraag1()
    antwoord = input()




vraag1()
vraag2()
vraag3()
vraag4()
vraag5()
vraag6()
vraag7()
vraag8()
vraag9()
vraag10()
vraag11()
vraag12()
vraag13()
vraag14()
vraag15()
vraag16()
vraag17()
vraag18()
vraag19()
vraag20()
vraag21()
vraag22()
vraag23()




