from enum import Enum
import random
class Gods_slovan (Enum):
	Bělboh=(
		"Bělboh",
		"god of good and light"),
	Cica=(
		"Cica",
		"goddess mentioned in the 17th century"),
	Černoboh=(
		"Černoboh",
		"god of evil and darkness"),
	Dažbog=(
		"Dažbog",
		"the sun god, according to some sources the god of the east, justice and power"),
	Dzidzileyla=(
		"Dzidzileyla",
		"Venera, goddess of marriage, according to Matthew Stryjkowski, of fertility and pleasure."),
	Dziewanna=(
		"Dziewanna",
		"Diana, bride and maiden at the same time ruling the forests"),
	Flins=(
		"Flins",
		"a god mentioned by the Saxon chronicle of Konrad Botha in 1492, his idol was to be destroyed by Duke Lothar"),
	Goderac=(
		"Goderac",
		"a local name, considered a deity by Arnold of Lübeck in the early 13th century"),
	Hammon=(
		"Hammon",
		"deity from the second Ebsdorf legend, probably Amon, the Slavic name has the meaning \"holy bull\""),
	Chliba=(
		"Chliba",
		"Unknown"),
	Chors=(
		"Chors",
		"associated with fairies and considered the goddess of the moon and the night sky"),
	Jarobud=(
		"Jarobud",
		"Unknown"),
	Jarovít=(
		"Jarovít",
		"god of fertility or spring, depicted as a youth"),
	Jasni=(
		"Jasni",
		"Unknown"),
	Jesza=(
		"Jesza",
		"Jupiter, the supreme god from whom all good and bad things come."),
	Julius=(
		"Julius",
		"the god whose name the chronicler Ebbo derived from the name of the city of Wolin"),
	Jutrobog=(
		"Jutrobog",
		"the god mentioned in the 1519 chronicle of Albinus"),
	Krodo=(
		"Krodo",
		"a god of obscure meaning, supposedly worshipped by the pagan Saxons"),
	Krt=(
		"Krt",
		"Mars, the god of war, to whom was prayed for victory and courage, and worshipped in fierce ceremonies. \
Matthias of Miechov regards her as the goddess who is the mother of Lel a Polel, and compares her to Léthé."),
	Lada=(
		"Lada",
		"Lada is generally understood as the goddess of love, spring, marriage, sowing and ploughing. \
The name Lady can be derived from the word lad, harmony. \
In the forged glosses in the Old Czech dictionary Mater verborum, Lada is compared to Venus. \
Matthias of Miechov in the early 16th century compares Lada to the Greek Leda, mother of the twins Kastor and Polydeuces."),
	Lel=(
		"Lel",
		"the twins Kastor and Pollux"),
	Letnicě=(
		"Letnicě",
		"Ceres, goddess of harvest and motherhood, according to Matthew Stryjkowski, had a large temple in Hnězdno"),
	Marzanna=(
		"Marzanna",
		"goddess of earth and water, Slavic form of the Great Mother"),
	Mokoš=(
		"Mokoš",
		"supreme deity, possibly the Polabian equivalent of Svarog"),
	nebeský=(
		"nebeský",
		"Pluto, god of the underworld and protector of souls leaving the body. \
According to Matthew Stryjkowski, he was asked for rain and to ward off bad weather. \
According to some theories, the goddess of death and extinction analogous to the Greek Enyó, \
the name may then be related to the Old Czech nav \"consecrate\"."),
	Nyja=(
		"Nyja",
		"goddess of drinks and changing fortunes"),
	Pereplut=(
		"Pereplut",
		"the god of thunder at the head of the pantheon, sometimes also called the god of war, storms and lightning"),
	Perun=(
		"Perun",
		"a god mentioned in the Knytlingasaga, whose idol in Jasmund was destroyed in 1168, perhaps Běsomar or Bezmiar."),
	Pizamar=(
		"Pizamar",
		"a god worshipped in Plun, perhaps a weather god"),
	Podaga=(
		"Podaga",
		"\"weather\", the giver of suitable weather, according to Matej Miechowski also revered as Pochwist or Pogwizd \
- the god of wind, according to Stryjkowski the god of bright and cheerful days"),
	Pogoda=(
		"Pogoda",
		"Pochvist - also Pogvizd, Pohvizd, a god mentioned in the Life of St. Vladimir, perhaps the god of wind"),
	Pochvist=(
		"Pochvist",
		"son of Perun, he had four heads and a fifth on his breast"),
	Porenut=(
		"Porenut",
		"a god worshipped at Corenice in Rüjana, he had five heads."),
	Porevít=(
		"Porevít",
		"Unknown"),
	Porvata=(
		"Porvata",
		"a fertility-related god worshipped by the Lutic tribe"),
	Pripegala=(
		"Pripegala",
		"Unknown"),
	Příje=(
		"Příje (Venus)",
		"Unknown"),
	Radegast=(
		"Radegast",
		"god of the Ratara tribe, god of the sun, war and abundance"),
	Rod=(
		"Rod",
		"god of birth, perhaps a lesser being"),		
	Rožanice=(
		"Rožanice",
		"a trio of goddesses of fate analogous to the Czech Weird Sister"),
	Rujevít=(
		"Rujevít",
		"God is worshipped in Korenica on Ruyana"),
	Simargl=(
		"Simargl",
		"one of the most mysterious gods, according to one interpretation a winged dog with two claws, protecting vegetation and livestock"),
	Stribog=(
		"Stribog",
		"god of wind and air"),
	Svantovít=(
		"Svantovít",
		"the god of the tribe of the Ranas inhabiting Ruyana"),
	Svarog=(
		"Svarog",
		"heavenly father of creation and celestial light, father of Dažboga and Svarožice"),
	Svarožic=(
		"Svarožic",
		"god of sacred fire associated with the harvest, son of Svarog"),
	Svoba=(
		"Svoba",
		"god of the Ratars, the sacred fire associated with the harvest, son of Svarog"),
	Svor=(
		"Svor",
		"Unknown"),
	Svračec=(
		"Svračec",
		"Unknown"),
	Sytivrat=(
		"Sytivrat",
		"Unknown"),
	Tjarnaglof=(
		"Tjarnaglof",
		"an idol mentioned in the Knytlingasaza, revered in the Jasmund, possibly Trihlav, Chernobog or the separate god Chernohlav. \
His idol was supposed to have a silvered beard and was destroyed 1171. Since he accompanied the army into battle \
one might consider his warlike function."),
	Trihlav=(
		"Trihlav",
		"a god worshipped mainly in Szczecin, he has a war and economic function"),
	Trojan=(
		"Trojan",
		"god of unclear meaning, appears as a wealthy tsar."),
	Turupid=(
		"Turupid",
		"also Turupit, a god worshipped at Garsu in Ruyana. Mentioned in the Knytlingasazi, may be related to the Estonian Tarapit or Toropec"),
	Veles=(
		"Veles",
		"god of water, wealth and the underworld, together with Perun the chief deity"),
	Vitelubbe=(
		"Vitelubbe",
		"deity of the second Ebsdorf legend, probably personal name Itoljub or Vitold"),
	Volos=(
		"Volos",
		"cattle god, almost certainly identical with Veles"),
	Zcuor=(
		"Zcuor",
		"Unknown"),
	Zela=(
		"Zela",
		"goddess mentioned in the 14th century Neplach Chronicle, according to Ivanov and Toporov, perhaps a goddess of vegetation"),
	Živa=(
		"Živa",
		"goddess associated with fertility, perhaps a form of Mokoš"),
	Žywy=(
		"Žywye",
		"god of life, according to Stryjkowski, the rustling wind")

make_list = list(Gods_slovan)
GODS_SLOVAN = random.choice(make_list)
GODS_SLOVAN = (GODS_SLOVAN.value)
