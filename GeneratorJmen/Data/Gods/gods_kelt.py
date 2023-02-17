from enum import Enum
import random
class Gods_kelt(Enum):
	ANDRASTE=(
        "Andraste",
        "Celtic goddess of victory, worshipped in the British Isles."),
	ARAWN=(
        "Arawn",
        "God worshipped in the British Isles, including Ireland. As king, he rules the underworld. \
He can sometimes appear in our world with a pack of white dogs. He's the one to whom travellers turn in times of need."),
	ARDUINNA=(
        "Arduinna",
        "A goddess riding on a wild boar, who watched over the forest massif of the Ardennes (Belgium)."),
	ARIANRHOD=(
        "Arianrhod",
        "The island goddess of the oracles and is also often considered the Goddess of Fate."),
	BELINUS=(
        "Belinus",
        "She is also known by the names Bel or Belenus. It is a deity symbolizing spring, new life, \
and a very important Celtic festival Beltine (Beltaine) is associated with his name. He protects artists."),
	BRAHN=(
        "Brahn",
        "He is a British God of giant stature, whose head is said to be buried beneath White Hill. \
He was originally a hero who became a god after death. He protects the tribal borders."),
	BRIGHID=(
        "Brighid",
        "Originally named Brigancia, she was famous as a Goddess protecting people who are in distress. \
With the advent of Christianity, this originally Celtic Goddess turned into a saint. \
This occurred in Ireland, where St. Patrick found her in the form of a sleeping child under an oak tree. \
She is said to have founded the first female monastery in a town called Kildare. \
The feast of Imbolc (today's Groundhog Day) is dedicated to her."),
	CERIDWEN=(
        "Ceridwen",
        "A goddess worshipped in the British Isles by a tribe of Britons, she may appear in the forms of an old or young woman. \
She is associated with wisdom."),
	CERNUNN=(
        "Cernunn",
        "A deer god. He is called the lord of the forest. He wears rich antlers adorned with shining rings. \
In addition to the title of lord of the forest, he is also the god of abundance and fertility. \
Today he is appropriated by environmentalists and nature lovers, among others."),
	CAILLEACH=(
        "Cailleach",
        "In Irish, this word means old woman. She is also known by the names Blue Witch or Black Annis."),
	DAGDA=(
        "Dagda",
        "A tribal god in Ireland. His function was to protect the tribe. \
He is credited with the ability to control the weather and create miracles. \
Translated, it means: 'Good God. He is also often represented as a typical Druid God \
and his attribute is a huge iron staff with which he can kill, but also raise the dead. Dagda of Gundestrup"),
	DEIOTAROS=(
        "Deiotaros",
        "Literally translated, it means divine bull. Perhaps it was the mythical animal Tarvos trigarnos. \
Tarvos trigarnos is a sculpture of a bull with three horns from Gaul. \
Deiotaros is an animal worshipped mainly by the Galatians in Asia Minor."),
	DISPATERA=(
        "Dispatera",
        "The god from whom all the Gallic tribes derived their origin. It is a very important Celtic god."),
	EPONA=(
        "Epona - Kotyz",
        "This is a Goddess who was worshipped throughout the Celtic world. \
She is depicted as riding a horse and her horse is therefore a sacred animal. \
She is known as Epona in the western countries, but in Boiohaem and not only there, she is known as Kotyz. \
If you know a little bit about the Czech Karst, you will have already come across the term Kotýz, \
it is a national nature reserve, where in addition to the paleontologically and geologically significant \
rock outcrops (Kotýz\'s limestones, PRAG trace, Lower Devonian), the double ramparts of the Hallstatt hillfort are visible. \
There is also the ever-important so-called Leaky Cave, where finds of slate tablets with engraved symbols (non-Celtic) have been made, \
and it is the oldest manifestation of art in Bohemia, and many flint stones have been found here. \
On a nearby rock promontory is the site of the Golden Horse with the Koněprus's Caves, \
even this name evokes that this place is an important site. \
Rituals were probably held in the cave Above the Grove during the Hallstatt period."),
	ESUS=(
        "Esus",
        "It has many adjectives, e.g. cruel Esus, divine woodcutter, heavenly ploughman, etc. \
The Gauls feared him, and the Druids left food for him on trees. He is depicted as a muscular man with an axe."),
	GRANNUS=(
        "Grannus",
        "A god who is considered to be the Celtic equivalent of the Roman god Apollo and was worshipped in Roman-controlled \
territory from the second half of the 1st century BC."),
	LUG=(
        "Lug",
        "This word denotes both a raven and a god to whom the Gauls dedicated the middle day of summer, \
the first of August. He is the god of light, and for this reason it would seem strange that the Celts should thus designate \
a raven with black feathers. It is because ravens flew away every night to accompany the sun on his nocturnal journey \
that this is not an illogical deduction."),
	MACHA=(
        "Macha",
        "Celtic Goddess worshipped in Ireland. She appears in the form of a tall red-haired woman \
who in some cases holds a mirror as a symbol of her power over the souls of men. She is terrifying, but in some cases she helps those in need."),
	OGMIOS=(
        "Ogmios",
        "This god was depicted as an old man with a bent back, with sparse tufts of hair falling on his shoulders. \
He is dressed in lion's skin, with a quiver hanging from his shoulder, and holds a club in his right hand and a bow in his left. \
According to legend, a group of people walked behind him. \
Their ears were attached to a thin gold chain that connected them to Ogmio's pierced tongue. \
Ogmios is also the god of eloquence and the ruler of words. He drew people to him by the piercing power of his voice. \
The arrows in his quiver symbolize his quickness of thought, sharp wit, quick responses, and wit."),
	RIGANTONA=(
        "Rigantona - Rhiannon",
        "Celtic Goddess of the Irish and Britons. She is very often seen with a horse's head instead of a human's and a foal at her side. \
She helped women and wrongly accused people."),
	SIRONA=(
        "Sirona - Serena",
        "A goddess occurring in a pair with the god Grannus. \
She is worshipped as the patroness of healers and is attested mainly from Pannonia and Noricum."),
	SUCELL=(
        "Sucell",
        "He is armed with a long staff, and every Gaul shall meet him in the land of the dead. \
A blow with one side of the staff brings death, but a blow with the other side can revive. \
Sucell was therefore the god of death and resurrection."),
	TIGERNONOS=(
        "Tigernonos - Teeger-nonos",
        "Husband of the goddess Rhiannon, and in the British Isles and Ireland he was recognized as the supreme Celtic God. \
He acts as a shepherd in our world, is very wise and protects the wayfarers."),
	TARANIS=(
        "Taranis",
        "Lord of Heaven. He is able to send lightning bolts by means of the spirals that adorn his shoulders. \
He is the lord of the fire of heaven, and his wrath was appeased by the priests by sacrifices being burnt alive. \
He protects mountains and high places, for these are sacred areas. The Romans compared him to their supreme god, Jupiter. \
In our country, the so-called Taranis wheels - perhaps a symbol of the sun - are quite abundant in various locations. \
Later on, this symbol evolved into the well-known Celtic cross, but it is a \"mutant\" between the Taranis symbol \
and the classical Christian cross. Many people wear it around their necks thinking it is a purely Celtic thing, \
the opposite is true, so watch out!"),
	VOSEGUS=(
        "Vosegus",
        "Like Arduinna protects the Vosges"),

make_list = list(Gods_kelt)
GODS_KELT = random.choice(make_list)
GODS_KELT = (GODS_KELT.value)
