# Co od toho chci:

## otazky: 
<pre><code>
#### jaky system:
</code></pre>
<pre><code>
shadowrun 4th edice ktery s kamarady hrajeme a mohu si vysledky ozkouset
??? mozna i VOID d6, ktery vypada ze ma jen vicero skillu
</code></pre>
### jake svety a atypicky background: 
<pre><code>
kvuli zdrojum dat uvazuji o fantasy, sci-fi jako shadorun a pod., post apo, mozna dark (to by byl chalenge)
    - moznost zvolit si rasy ktere tam nejsou
    - moznost zvolit si Slovany, Germany, Nordicy, Galy, Skoty, Iry, Americke indiany, Eskymaky, Aborigince, Krovaky
</code></pre>
### nove rasy a pod.
<pre><code>
ne ted mozna az to budu mit v DB
</code></pre>
### Koncept:
<pre><code>
- NPC generator backgoundu - zivotni udalosti od 6teho roku zivota
- po te co refaktoruji rasy, prejdu na novou verzi kdy vsechny vstupni staticke data si budu ukladat do souboru abych je pak pouzil 
- napriklad ve verzi 3 kdy by uz mela byt databaze a zaklad webu
- generator by mel vyplivnout postavu s dobrym backgroundem a popisem vzhledu
- komunikace s lidmi a prace s lidmi muze mit stejnou stupnici
</code></pre>
### Jak na to:
<pre><code>- typ sveta
    scifi
    post apo scifi
    post apo fantasy
    post apo normal (natural disaster)
    fantasy no magic
    fantasy
</code></pre>
<pre><code>- pohlavi
    muz
    zena
</code></pre>
<pre><code> - volba za kolik bodu (asi pridam vybery slovni plus v zavorce pocet bodu)
</code></pre>
<pre><code>- generator jmen
    - dle kmenu
        - slovan
        - kelt
        - ancient egyptian
        - ancient greek
        - aboriginal
    - dle zemi (dvou mistne zkratky statu)
        - gk
        - fi
        - pl
        - it
        - no
        - nl
        - se
        - hu
        - us
        - sk
        - fr
        - es
        - vn
        - au_aboriginal
        - au
        - eg_ancient
</code></pre>
<pre><code>- atributy
    - dle magie (adept, shaman, thaumaturgist, priest)
        - ano
        - ne
    - dle technologie (Technomancer)
        - ano
        - ne
</code></pre>
<pre><code>- merits and flows (max 2+ a 2- (???s okecem ci bez??? - asi na volbe uzivatele))
</code></pre>
<pre><code>- skilly vzdy s pouzitym atributem (- to bude orisek a obavam se ze bez nacitani dat z txt ci db to nepujde)
</code></pre>
<pre><code>- vzhled
    - head
        vlasy
        oci
        celo
        brada
        nadocnice
        nos
        usi
    - Body
        vyska
        vaha
        maskularita
        hrudnik
        delka koncetin
    - pozdeji i zapojim AI na generovani obrazku postavy, mozna i toho co vlastni a mozna i pribehu
    - co ma na sobe a pod. - bude ovlivneno ostatnimi - napriklad ze je bezdak, nebo pokud nemel behem detstvi prisun potravy ci generace hladoveli a nemeli maso
</code></pre>
<pre><code>
########################################################
zkouska
########################################################
- Zavislosti rodice
    na adrenalinu
    na praci
    na zabave
    na hazardu
    na drogach
    na alkoholu
    na BTL
    na milenci
    na sexu

- Ostatni pribuzni
    mrtvi
    daleko
    nechteji komunikovat
    maji sve starosti ale vidate se
    pomahaji s vychovou
    nevedi o nem

- Rodice sirotka
    nevedi ze zije
    nezajimaji se
    po smrti jednoho z rodicu jej cela rozvetvena rodina hleda
#################################################################    
    # TODO toto cele zakomponovat do jednoho smysluplneho stringu
#################################################################
    ztraceni emigranti
        vychovavan v zemi puvodu rodicu
        vychovavan v zemi emigrace
    emigranti zijici v zemi puvodu ve vezeni
    emigranti zijici v zemi puvodu - hledaji ho
        vychovavan v zemi puvodu rodicu
        vychovavan v zemi emigrace
    emigranti zijici v nove zemi - hledaji ho
    emigranti zijici v nove zemi - zapomeli na nej
        vychovavan v zemi puvodu rodicu
        vychovavan v zemi emigrace
    oba na vojenske misi - only if kadetka

- Family parents (zkouska)
    kompletni rodina, + ostatni pribuzni
    velka a rozvetvena rodina zijici pohromade
    jen s otcem + ostatni pribuzni
        matka nejevi zajem
            ma jinou rodinu
            je zavisla
                zavislosti rodice
            je na ulici
                zavislosti rodice
        matka zemrela
            pri porodu
            pri nestesti
            na nasledky upracovani
            na psychicke nesnaze
                na nasledky upracovani
                na nasledky toxicity zamestnani
                na predavkovani (BTL, drogy, prasky)
                na nasledky trestneho cinu (
                    zpackany unos 
                    nedobrovolny darce organu
                    pri pokusu se osvobodit
                        z otrocke prace
                        z bordelu
                        z vezeni
                        z mafie
                        z nesvobodne zeme
                )
                skokem z budovy ci mostu
            na nasledky zavislosti
                zavislosti rodice
            sebevrazdou kvuli dluhum
            sebevrazdou kvuli znesveceni cti rodiny
            zabita behem 
                poulicnich boju
                teroristickych boju
                armadnich boju
                policejni akce

    jen s matkou + ostatni pribuzni
        otec nejevi zajem
            otec nevi ze ma potomka
            ma jinou rodinu
            je zavisly
                zavislosti rodice
            je na ulici
                zavislosti rodice            
        otec zemrel
            pri porodu
            pri nestesti
            na nasledky upracovani
            na psychicke nesnaze
                na nasledky upracovani
                na nasledky toxicity zamestnani
                na predavkovani (BTL, drogy, prasky)
                na nasledky trestneho cinu (
                    zpackany unos 
                    nedobrovolny darce organu
                    pri pokusu se osvobodit
                        z otrocke prace
                        z bordelu
                        z vezeni
                        z mafie
                        z nesvobodne zeme
                )
                skokem z budovy ci mostu
            na nasledky zavislosti
                zavislosti rodice
            sebevrazdou kvuli dluhum
            sebevrazdou kvuli znesveceni cti rodiny
            zabit behem 
                poulicnich boju
                teroristickych boju
                armadnich boju
                policejni akce
    komunita - spolecne deti (hare kirshna, indiani, aboriginci, krovaci...),
    dve matky + ostatni pribuzni
        homosexualni par
        dve svobodne matky pomajici si s vychovou
    dva tatove + ostatni pribuzni
        homosexualni par
        dve svobodne matky pomajici si s vychovou
    matka s otcimem  + ostatni pribuzni
        otcim te bral
        otcim se te chtel zbavit
    macecha s tatou
        macecha te brala
        macecha se te chtel zbavit
    ustav
        kadetka + Rodice sirotka
        noviciat na kneze + Rodice sirotka
        sirotcinec + Rodice sirotka
    kocovne 
        cirkus
        divadlo
        pastevci
        sberaci
        lovci
        lovci a sberaci z ruky do huby
        strihaci vlny
        honaci
    otrok bez rodicu
        sexualni
        tezkou praci
        domaci prace
        hlidani deti
        schovanek
    naklonovany
        nezna svuj original
        zna svuj original
    sirotek na ulici + Rodice sirotka
        zebrani
        kradeze
        organizovana banda
            vypalne
            hazard
            kradeze
            zebrani
            informace
    na statku 
        dite nevolnika
        dite klona
        dite sluzebne
        dite sluhy
        dite vychovatelky
        dite majitele statku
    ve meste
        rodice
            remeslnici
                drahe veci
                levna bezna spotreba
                    pekar
                    cukrar
                    stanek fastfood
        obchodnici
        delnici
        slouzici
            armada
            policejni slozky
            celnici
            v dome
        urednici
        architekti
        stavebni firma
        politici
        starostove
        analytici ruznych organizaci
        

if aboriginal:
    spolecenstvi - spolecne deti,
    kocovne (lovci a sberaci z ruky do huby)
########################################################
zkouska
########################################################

Family_Parents
Both of your parents are alive.
go to Family Status.
Something has happened to your parent random.choice(("s", "")).
    if 's'
    # TODO kdo vychovaval
    - ulice

Go to Something Happened to your Parents.

Family Status
    - in danger
        you may lose it all (if they haven’t
        drekked everything up already).
        choose from Family Tragedy

    - secure
        even if you’re parents are maimed, dead, or missing. 
        Go to Childhood Environment.

Family Tragedy
    You’re family was forced to leave everything and emigrate 
    You’re family lost everything and was betrayed.
    You’re family lost everything through bad investment.
    Family captured by organleggers. So sad.
    Your family was experimented on. You escaped.
    Your family was murdered in front of you.
    Family imprisoned, you escaped.
    Family was killed by violent organization, such as a human policlub.
    Parent random.choice(("s", "")) work on street in not too gentle and safe way to get by. Mainly when You selling 
        prodej drog
        prodej kradenych veci
        prodej vlastniho tela
    Parent random.choice(("s", "")) committed suicide after losing it all.
    Parent random.choice(("s", "")) pissed money


Childhood Environment
Grew up on the tough streets alone.
Grew up jacked into BTL’s because life sucked so bad.
if something weird with parents and pribuzni:
    Grew up in random.choice((
        cadet school + Rodice sirotka
        novitiate for priest + Rodice sirotka
        orphanage + Rodice sirotka))
Grew up in a safe megaplex under heavy guard.
Grew up in a derelict squatter house in the Boarderlands.
Grew up in Corporate territory in posh skyscraper.
Grew up in a gang war zone. 
Grew up in a slave shop. 
Grew up in human organ farm and escaped.
Grew up in a boring area and sought vandalism as form of excitement.
Grew up in crime family house. Safe and secure.
Go to Siblings.






- Family Character
    - je rodina vlivna
        - vliv
            - vliv na uzemi kde ziji - znama rodina
            - vliv ve state - politicky aktivni rodina
            - vliv na korporaci/Guildu/Mesto
            - velky vliv ve specializaci odvetvi v kterem delaji
        - bez vlivu
            - rodina nema konexe a neni znama
    - je rodina tradicni
        - prisne zachovava tradice jako japonci
        - zachovava kulturni zvyky jako jsou vanoce a pod.
        - zachovava nabozenske zvyky
        - zachovava tradici krevni msty
        - nezachovava tradice ani krevni msty
    - je rodina spokojena se svym statusem
        - ne
            - zvysovat svuj majetkovy vliv
            - zvysovat svuj mocensky vliv
            - zvysovat svuj mocensky i majetkovy vliv
        - ano
            - zit v klidu v ustrani politiky bez nepratel
            - byt na vysluni ale nedelat si nepratele
            - jen zit byt spokojen a uzivat si zivota

- Family work domain (plati na Corporate/Guild/City a Megaplex krome Corp Wage Slaves)
        IT Development, 
        firmy (pouze u high class), 
        technicke podpory,
        bezpecnosti,
        vyzkumu,
        logistiky,
        tajnych operaci,
        Human resources,
        Public Relations,
        pravni oddeleni,
        supportniho oddeleni,
        cizi zdroju,
        statisticke a ucetni
        vyroby,

- Family ranking
    High Corporate/Guild/City Profile
    Mid Corporate/Guild/City Profile
    Corp Wage Slaves 
        (delnici, uklizeci, hlidaci, recepcni, hornici)
    Average Income
        dedictvi
        rodinne investice
        freelancing (v ramci zakonu - ICAR)
        firma
        znami umelci
    Poor Income
        (namezdni delnici, pristavni delnici, prilozitostne male kontrakty, malinka firma/kramek/dilna)
    Shadowrunner(s)
    Street Urchins
        na ulici (zebrani, kradeze, podpora dobrocinne organizace, organizovana banda(vypalne, hazard, kradeze, zebrani, informace, prostituce, drogy))
    Boardlanders
        proti imigracni straz
        celnici
        ochranci chraneneho uzemi
        hotelieri a pohostinsti
        policiste
        prislusnici ozbrojenych slozek
        lesnici
        tezari (drevo, pisek, kamen, nerosty)
        rekultivatori   
    Megaplex/Main City Dwellers


</code></pre>
<pre><code>- charakter
    - vira - viz bohove OK
    - sexualni preference uchylky/orientace OK
    - 2 positivni vlastnosti (pilny, mily ...) OK
    - 2 negaticni vlastnosti (liny, puntickar ...) OK
    - ??? mozna budu davat dalsi dle toho co vyjde jinde ???
    - toto bude ovlivneno svetem
        - je si jisty pri delani:
            - hlavou
            - rukama
            - ve meste
            - v prirode
            - na venkove
            - se zakazniky
            - obchodovani
            - rodici ci temi co jej vychovali
            - s velmi starymi lidmi
            - se stejne starymi lidmi
            - opacnym pohlavim
            - promlouvani k vicero lidem
            - prateli
            - znamymi
            - sousedy
            - uplne cizimi lidmi
            - s autoritami
            - s samany/knezimi... lidmi co maji co delat s bohy
            - se spodinou
            - s opacnym pohlavim
            - se sexualnimi pracovniky
            - hazardu
            - lehkem fetu (trava, cigara)
            - v hospode a na oslavach
            - ve vyssi spolecnosti
            - s vladci velkych uzemi
            - vysokymi predstaviteli cirkvi/samany...
            - magicky praktikujicimi
            - magicky prirozenymi tvory
            - dusemi zemrelych a ozivlymi mrtvolami - asi jen pokud bude nekde ze je uchyl ci nekdo kdo je studuje ci zabiji
        -  jednani s lidmi a tvory a interakce - dela to rad ci je nerudny, je mily ci politicky pri jednani s:
            - lidmi co delaji hlavou
            - lidmi co delaji rukama
            - ve meste
            - v prirode
            - na venkove
            - rodici ci temi co jej vychovali
            - s velmi starymi lidmi
            - se stejne starymi lidmi
            - opacnym pohlavim
            - promlouvani k vicero lidem
            - prateli
            - znamymi
            - sousedy
            - uplne cizimi lidmi
            - se zakazniky
            - pri obchodovani
            - s autoritami
            - s samany/knezimi... lidmi co maji co delat s bohy
            - se spodinou
            - s opacnym pohlavim
            - se sexualnimi pracovniky
            - pri hazardu - vcetne zda je zavisly ci ma rad
            - lehkem fetu (trava, cigara) - vcetne zda je zavisly ci ma rad
            - v hospode a na oslavach
            - ve vyssi spolecnosti
            - s vladci velkych uzemi
            - vysokymi predstaviteli cirkvi/samany...
            - magicky praktikujicimi
            - magicky prirozenymi tvory
            - dusemi zemrelych a ozivlymi mrtvolami - asi jen pokud bude nekde ze je uchyl ci nekdo kdo je studuje ci zabiji
        - background
        - jak vyrustal (kompletni rodina, ustav, kocovne, cirkus, sexualni otrok jako v princi prudasovi ;) )
            - jak se dokazal bavit a jake mel vztahy s:
                - mladsimi
                - vrstevniky
                - starsimi
                - velmi starymi
                - temi kdo jej vychovavali
                - promlouvani k vicero lidem
                - prateli
                - znamymi
                - sousedy
                - uplne cizimi lidmi
        - jakou meli zivotni uroven rodice (vcetne obzivy - i mafian, zoldak, cirkusak a pod.)
        - udrzuje kontakty s rodici/pribuznymi/instituci
        - je soucasti organizace/spolku/etnika se zpusobem zivota ze ktereho nejde odejit snadno (Aboriginec, krovak, cigan, eskymak, zabijak mafie, starosta s neprateli, klanova/rodinna cest)
        - pratele/nepratele
            - je na nej vystavena odmena
            - dluzi mu nekdo neco
            - je na nem vykonavana vendeta ci on je k ni zavazan
        - jaka je jeho zivotni uroven
            - kde, jak a v cem zije
                - vlastni hospodarske zvirata
                - vlastni mazlicka
        - je soucasti komunity/organizace
        - vybaveni: 
            - zbrane
            - zbroje
            - udelatka
            - dopravni prostredky
            - zvirata - viz vyse zivotni uroven
            - nemovitosti
            - informace na mediich
            - dluzni upisy a jine prisliby
            - otroci, vojaci, remeslnici ci nevolnici
</code></pre>

<pre><code>This is a code block.
</code></pre>





