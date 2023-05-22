import random
from enum import Enum

class Family_street_selling(Enum):
    DRUGS = "ilegal drugs"
    STOLEN = "stolen things"
    BODY = "own body"


class Family_Tragedy(Enum):
    lost_all_betrayed = "Your family lost everything and was betrayed."
    lost_all_investment = "Your family lost everything through bad investment."
    captured = "Your family was captured by organleggers. So sad."
    experimented = "Your family was experimented on. You escaped."
    murdered = "Your family was murdered in front of you."
    imprisoned = "family was imprisoned, but you escaped."
    killed_by_violent = "family was killed by violent organization, such as a human policlub."
    street_work = f"work on street in not too gentle and safe way to get by. \
Especially if you're selling {random.choice(list(Family_street_selling)).value}."
    suicide = "lost everything, Committed Suicide."
    money_freak = "gave up on the money"
    crossfire = "gang crossfire."
    accident = "accident."

make_list = list(Family_Tragedy)
FAMILY_TRAGEDY = random.choice(make_list)
FAMILY_TRAGEDY = (FAMILY_TRAGEDY.value)


class Childhood_Environment(Enum):
    street_child = "Grew up on the tough streets alone."
    btl = "Grew up jacked into BTL’s because life sucked so bad."
    megaplex = "Grew up in a safe megaplex under heavy guard."
    squatter = "Grew up in a derelict squatter house in the Boarderlands."
    skyscraper = "Grew up in Corporate territory in posh skyscraper."
    ganger = "Grew up in a gang war zone."
    slave = "Grew up in a slave shop."
    farmed = "Grew up in human organ farm and escaped."
    vandal = "Grew up in a boring area and sought vandalism as form of excitement."
    mafioso = "Grew up in crime family house. Safe and secure."
    organizationed = "Grew up in a " + random.choice((
            "cadet school.",
            "noviciat at the priest.",
            "n orphanage."))

make_list = list(Childhood_Environment)
childhood_environment = random.choice(make_list)
childhood_environment = (childhood_environment.value)

class Family_Parents(Enum):
    living = "Both of parents are alive."
    mother_died = f"Mother died afther {FAMILY_TRAGEDY}"
    father_died = f"Father died afther {FAMILY_TRAGEDY}"
    orphaned_died = f"Parents died afther {FAMILY_TRAGEDY}"
    accident_all = "Parents are on life support in hospital. After an serious accident."
    accident_mother = "Mother is on life support in hospital. After an serious accident."
    accident_father = "Father is on life support in hospital. After an serious accident."
    adopted_parents_unknown = "Never knew real parents, is adopted."
    father_unknown = "Mother not talking about your father."
    mother_unknown = "Grow up with relatives and never listen about your mom."
    cloned = "You were cloned for organs, but you escaped during the police raid at age of 16 years."
    street_child = "You grew up on the street and never knew your parents."
    mother_life_support = "Mother is on life support in hospital. Afther " + random.choice(list(Family_Tragedy)).value
    father_life_support = "Father is on life support in hospital. Afther " + random.choice(list(Family_Tragedy)).value
    both_life_support = "Parents are on life support in hospital. Afther " + random.choice(list(Family_Tragedy)).value
    solded = "Parents sold you for money " +random.choice((
        "to the infertile rich parents.",
        "to serve as slave and sexual toy.",
        "to work at factory."
    ))
    parents_illegal_emigrants = random.choice((
        "Parents are lost emigrants. " + random.choice(list(Childhood_Environment)).value + random.choice((
        " In the country of Your parent origin.",
        " In the country of emigration.")),
        "Your parents are arrested emigrants in country of their origin. Meanwhile he " + random.choice((
            "raised hidden in the country of origin of the parent",
            "raised in the country of emigration")) + " on the " + random.choice((
            "cadet school.",
            "noviciat at the priest.",
            "orphanage."        
            )),
        "Your parents are emigrants living in the country of their origin, but trying to find you \
Meanwhile you " + random.choice((
            "raised hidden in the country of origin of the parent",
            "raised in the country of emigration")) + " on the " + random.choice((
            "cadet school.",
            "noviciat at the priest.",
            "orphanage."        
            )),
        "Parents are emigrants living in new country, \
but trying to find you. Meanwhile you " + random.choice((
            "left hidden in the country of origin of the parent",
            "left in the country of emigration",
            )) + " and " + random.choice(list(Childhood_Environment)).value,
    ))
make_list = list(Family_Parents)
family_parents = random.choice(make_list)
family_parents = (family_parents.value)
print(family_parents)


class Family_ranking(Enum):
    high = "Your parents ranking was High " + random.choice(("Corporate", "Guild", "City")) + " Profile."
    mid = "Your parents ranking was Mid " + random.choice(("Corporate", "Guild", "City")) + " Profile."
    wage = "Your parents ranking was " + random.choice(("wage earners", "wage laborers")) + "."
    average = "Your parents has Average Income from " + random.choice((
        "the production of expensive things on the custom",
        "the business activities",
        "the service" + random.choice((
            "in the army",
            "at the police of the flesh",
            "at the customs")),
        "care of the rich man's house",
        "rents",
        "the architectural designs",
        "their construction company",
        "their politic activities",
        "the bribery",
        "the the mayor adversely",
        "the analytical capabilities for various organisations",
        "their artistic activities",
        "the heritage",
        "family investments"
    )) + "."
    poor = "Your parents has Poor Income."
    nomadic = "Your parents lived nomadic life as " + random.choice((
        "the circus artist", 
        "the actors of the nomadic Theater", 
        "the shepherds",
        "the fishers",
        "hunters",
        "war correspondenters",
        "highest bussinessmans",
        "the IT developers",
        "the tourist reporter"
        )) + "."
    shadowrunners="Your parents was Shadowrunners"
    urchins = "Your parents was Street Urchins and earning money by " + random.choice((
        "beggary",
        "small stealing",
        "cooperation with organized gang with speciality on " + random.choice((
        "burning",
        "gambling", 
        "stealing",
        "collecting",
        "information"))
    ))+ "."
    boarderlanders = "Your parents was Boardlanders and worked as " + random.choice((
        "an immigration guards",
        "a customs officers",
        "a Protectors of Protected Areas",
        "the hotel and hospitality operators",
        "police officers",
        "members of the armed forces",
        "foresters",
        "tessars"
        "the miners in " + random.choice(("sand", "stone", "minerals")) + " mine.",
        "reclaimers",
    )) + "."

make_list = list(Family_ranking)
family_ranking = random.choice(make_list)
family_ranking = (family_ranking.value)


# TODO find best way
siblings_count = random.int(1,10)
if siblings_count < 8:
    print(f"You have {siblings_count} of siblings.")
    # Loop here ?
else:
    print("You are only child.")

class Siblings(Enum):
    siblings_count = random.randint(0, 5)
    if siblings_count > 0:
        sibl_count=siblings_count
        if siblings_count >= 3:
            siblings_mother = sibl_count - 2
        

class Siblings(Enum):
    older = " has " + random.randint(0, 10) + "years older " + random.choice(("brother.", "sister.",))
    younger = random.randint(0, 10) + "years younger " + random.choice(("brother", "sister",))
    twin = random.choice(("identic", "not identic",)) + " twin " + random.choice(("brother", "sister",))

siblings_count = random.randint(0, 5)
make_list = list(Siblings)
SIBLINGS = random.sample(make_list, siblings_count)
# SIBLINGS = SIBLINGS[0].value, SIBLINGS[1].value

# 8-10 you are an only child.
# 1 Roll d10: Even sibling is female. Odd
# sibling is male.
# 2 Roll age, relative to you:
# 1-5 Older
# 6-9 Younger
# 10 Twin

# How each sibling feels about you:
# 1-2 Sibling dislikes you.
# 3-4 Sibling likes you.
# 5-6 Sibling is neutral to you.
# 7-8 You are Jesus to them.
# 9-10 They hate you.
# Go to Motivations.



"""
MOTIVATIONS:
Personality Traits
Mam uz v SocialInteractions

Person You Value
Most
Choose or Roll One:
1 A parent
2 A Sibling
3 Yourself
4 Lover
5 Fictional Character
6 Friend
7 Mentor
8 Politician
9 Entertainment/Sport
Hero
10 Priest/Shaman...
11 Your senapai, master teacher
12 Can’t count on anyone

What Do You Value
Most
Choose or Roll One:
1 My family
2 It’s all about the credits
3 Love and romance
4 It’s all about fucking, baby!
5 I just want to have fun!
6 Education
7 My word is my bond
8 Getting even
9 Being number one
10 Pets
11 Animals
12 Flora (flowers, trees, muchrooms, all(Flora))
13 My life
14 Richness
15 Poorichness (chudoba)
16 Samota

How Do You Feel About Most People
Choose or Roll One:
1 Neutral
2 I like most people
3 I hate most people
4 We’re in need of another plague!
5 Persons are cool, people suck
6 Everyone has something to offer
7 Use them like tools
8 Don’t trust anyone
9 Don’t let them stand in my way
10 I love people!

Most Valued Possession
Choose or Roll One:
1 A pet
2 A collector’s item
3 A trusty weapon
4 Family heirloom
5 Piece of technology
6 Entertainment program
7 A book
8 Family album or recording
9 Bullet removed from your body
10 Weapon from a dead enemy

Life Events
4) Life Events
You now are getting an idea of who your Shadowrunner is, chummer. Now let’s get their age
and what’s happened in their life. Roll 2d6 +16 or choose your age. For each year past 16 roll
a 1d10 and consult the chart below.

# TODO: nutno rozvinout
1-3 Shadowrunning Highs and Lows
4-6 Making Friends and Enemies
7-8 Romantic Involvement
9-10 You Had a Boring Year

My Life Sucks Right Now
Roll 1d10:
1 Debt- You start with 1d10 x 50 subtracted from
you starting Nuyen. It is possible to start the
game completely bankrupt.
2 Jail Time– You were in jail for 1d10 months.
3 Accident– You were in a horrible accident.
Choose Ugly or Phobia (Minor) Hindrance.
4 Betrayal– You were betrayed by a Johnson, a
friend, fellow runner, or lover (your choice). Gain
the Vow (Minor) Hindrance
5 Illness or Addiction– Choose either Habit
(Major) or Anemic Hindrance.
6 Death– Someone you loved died by your hand
accidentally, gain the Back Luck Hindrance or
they were murdered by another, gain the Vow
(Major) Hindrance.
7 False Accusation– You’ve been accused of
something you didn’t do. Gain the Outsider
Hindrance or Lower Reputation by –2.
8 Wanted- A bounty hunter, police, or Lone Star
are after your ass. Gain the Wanted (Minor)
Hindrance.
9 Corporate Enemy– You’ve managed to piss of
a corporation. Good job. Gain the Wanted
(Major) Hindrance.
10 Mental Breakdown– You’ve had a nervous
breakdown and can’t sleep and feel fragile.
Choose either Nightmares, Secret (Minor), Phobia
(Major), or Yellow (Major) Hindrance.
Go to Whatchu Gonna Do About it, Punk?

Whatchu Gonna Do About it, Punk?
Roll 1d10:
1-2 Make all those motherfuckers pay!
3-4 Piss my pants and live in shame.
5-6 Attempt to restore my reputation.
7-8 Go after what’s mine.
9-10 Save everyone that I care about, if I can.
Roll Next Life Event

Damn it’s Good to be a Runner
Roll 1d10:
1 Damned Fine Run– Up your Reputation by 1.
2 It’s All About the Creds– You gain an additional
1d10 x 50 credits at game start (after character
creation).
3 Jackpot!– You gain an additional 1d10 x 100
credits at game start (after character creation).
4 Somebody Likes Me– Create a Level 1 Contact.
5 You REALLY Like Me– Create a Level 2 Contact.
6 Oh You REALLY Like Me- Create a Level 3
Contact.
7 Get Out of Jail Free– You’ve done a favor to a cop
or a Lone Star op and can get out of jail one time.
8 Trainer– Someone teaches you one new skill at d4.
9 Favor– A Cop, Lone Star Op, or Corporate Man
owes you one favor.
10 You Got Skillz– Someone teaches you some
tricks. Choose one skill and up die level by one.
Roll Next Life Event

Lifepath
4b) Making Friends and Enemies

You’ve Pissed
Someone Off
Gain the Enemy
(Minor) Hindrance.
Choose sex or roll
1d10:
Even– Male; Odd
Female
Choose or Roll One:
1 Fixer
2 Corporate Exec
3 Police Officer
4 Hooker
5 Fellow Runner
6 Lone Star Op.
7 Government Official
8 Sibling
9 Contact
10 Childhood Enemy
Go to The Cause

The Cause
Choose or Roll One:
1 You betrayed them.
2 You caused the
death of their loved
one.
3 Spurned their
advances.
4 Never liked each
other.
5 You left them behind
during a run.
6 You wrongfully
accused them.
7 You rightly accused
them and they lost
face.
8 Stopped their plans
to sell you out.
9 Kicked their ass.
10 You/they stole
romantic
interest.
Go to Who’s Pissed
Off

Who’s Pissed Off?
Choose or Roll One:
1-4 They hate you.
5-7 You hate them.
8-10 You hate each
other.
Go to Whatchu Gonna
Do About it, Punk?

Whatchu Gonna Do
About it, Punk?
If you ever run into one
another, the pissed off
person will:
Choose or Roll One:
1-2 Attempt to kill their
ass right then and there.
3-4 Attempt to get back
at them through skullduggery and backstabbing.
5-6 Just avoid them.
7-8 Ignore them but not
leave.
9-10 Chew them the fuck
out.
Go to Their Resources

Their Resources
What will they bring to the
table to fuck up your day?
Roll 1d10:
1-3 Only himself
4-5 A good friend
6-7 A small gang
8 A large gang
9 Considerable funding
10 Corporate backing
Roll Next Life Event

What Makes Them Tick
Flush out the character by
rolling up description info from
Origins and Personal Style
and Motivations. This info
can be used to really bring
the character to life and create some good role-playing
moments.

You’ve Made a Friend
You’ve somehow done something right and made
a friend in the Sprawl (treat this as a Level 3 Contact). Roll 1d10– Even– Male; Odd– Female.
Choose or Roll One (or make something up):
1 Corporate middle man
2 Fixer
3 Whore
4 Decker/Rigger
5 Street Samurai
6 Shaman/Magician
7 Street Meat
8 Ganger
9 Drug
10 Weapons Specialist
Roll Next Life Event


4c) Romantic Involvement

How Did it Pan Out For Ya?
Sometimes it’s good… And sometimes it ends up covered in drek.
Roll One and go to corresponding
section.
1-4 Happily Ever After. Roll Next
Life Event.
5 Romeo and Juliet
6-7 Trouble in the Nest
8-10 Good Fucking. Roll Next Life
Event.

Romeo and Juliet
Sometimes relationships end badly…
In this case, very badly.
Choose or Roll One:
1 Lover was killed by Organleggers.gender
2 Lover was killed in auto accident.
3 Lover went insane.
4 Lover committed suicide.
5 Lover lost in VR.
6 Lover murdered.gender
7 Lover imprisoned.
8 Bullet meant for you killed lover.
9 Stolen by rival.
10 Tried to kill you.
Roll Next Life Event.

Trouble in the Nest
Paradise may seem lost here Chummer, but with a box
of chocolates, some good strong liquor, and a nice
steamy porn BTL you can surely make this relationship
work!
Choose or Roll One:
1 Family doesn’t approve of lover/you. Nasty looks and
phone calls.
2 Lover is a drug addict.
3 Family is attempting to get dirt to get rid of lover/you.
4 Constant fighting.
5 Too many secrets.
6 “Work” has followed you home more than once.
7 One of you is fucking on the side.
8 Lover/you have been hired to kill the other.
9 Politics and religion baby!
10 Fatal Attraction, need any more be said?
Go to Current Feelings

Current Feelings
Oh no! Your relationship is in trouble! What’s
some of the emotions that are bubbling under the
surface?
Choose or Roll One:
1 They really love you.
2 You really love them.
3 You both love one another.
4 You/they can’t stand to look at the other.
5 Sometimes shit just falls apart.
6 They are plotting your downfall.
7 Smothering you with a pillow looks better each
day.
8 You love them, they hate you.
9 They love you, you hate them.
10 You’re both neutral.
Roll Next Life Event.

What Makes Them Tick
Flush out the character by rolling up description
info from Origins and Personal Style and Motivations. This info can be used to really bring
the character to life and create some good roleplaying moments.

"""