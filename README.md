# <font color='BLUE'>What is purpose of this project</font>
----------
This project is for generating character to known pen and paper
tabletop RPG game Shadowrun 4th edition.
The project is as simple as possible in way to learn my friend something from Python.
He gives me some "what I want from this project",
but cause of complexity of whole Shadowrun system, looks little weird.
Done is generating by rand from list of "names, names of specific nationality etc in meaning of First Name, czech Nickname, Surname by Nationality, gods by tribe".

This project is written for my friend by hes level of python.
There's many things and comment to learn him something.
I hoped that together we grow, but he try programming and nowadays he don't want makes programmes.
So, I have project which is not done and I have no use for him, unlees I changed him
by innovation decision - see Down

### **<font color = 'CIAN'>I don't have done many things, like:</font>**
1. **<font color = 'GREEN'>Generate none-czech nicknames - I don't have data for it</font>**
2. **<font color = 'GREEN'>Generate skin/hair/eyes color</font>**
3. **<font color = 'GREEN'>Generate age of the character</font>**
4. **<font color = 'GREEN'>Generate background of the character</font>**

### **<font color = 'CIAN'>I have DONE:</font>**
1. **<font color = 'GREEN'>Generation of atributes by point system (see more on docstrings in generatorAtributu.py)</font>**
2. **<font color = 'GREEN'>Generation of race and updating the atributes by race statistics</font>**
3. **<font color = 'GREEN'>Generating of Name/Nickname/Surname by rand list</font>**
4. **<font color = 'GREEN'>Generating of God (greek, egypt, celtic, slovanic - nording in plan)</font>**
5. **<font color = 'GREEN'>Generating of Gender, character pros and cons</font>**
5. **<font color = 'GREEN'>Print all data of the character</font>**

There is no pip3 libraries, no special pipenv or .venv

### **<font color = 'CIAN'>Output is like this: </font>**
`Julie "Bobr" Hort
('Dispatera', 'Bůh, od něhož odvozovaly svůj původ všechny galské kmeny. Jedná se o velice významného keltského Boha.')
Počáteční body na rozdělení: 100
['Body 6', 'Logic 3', 'Willpower 2', 'Agility 1', 'Intuition 1', 'Strenght 1', 'Charisma 1', 'Reaction 1']
['Body 10 min 5 max 15', 'Agility 5 min 1 max 7', 'Agility 5 min 1 max 7', 'Reaction 6 min 1 max 9', 'Strenght 10 min 5 max 15', 'Charisma 4 min 1 max 6', 'Charisma 4 min 1 max 6', 'Intuition 5 min 1 max 7', 'Intuition 5 min 1 max 7', 'Logic 5 min 1 max 7', 'Willpower 6 min 1 max 9']
{'Metatype': 'Troll', 'Body': 10, 'Agility': 1, 'Reaction': 1, 'Strenght': 5, 'Charisma': 1, 'Intuition': 1, 'Logic': 2, 'Willpower': 2, 'Iniciative': 2, 'Edge': 2, 'Iniciative_Phases': 1, 'Metatype Ability': 'Thermographic Vision, +1 Reach, +1 natural armor (cumulative with worn armor)'}`

---
## **<font color='CIAN'>Innovation decision</font>**

1. refactor all
2. Use SQLLite database
3. Loading database by Pandas - see more in my learning project Decision table on my Github
4. SQLAlchemy need to thing if I will need it
5. If SQLAlchemy, then I need to learn more about, but maybe 
6. Security of DB - see Security Options
7. Think about PyInstaller and some better GUI than is pyQt

## next version:
  - more data to generate:
  - character defects
  - susceptibility to physical, mental or spiritual diseases
(and other baby steps gradually leading to the transition to the next version - the web version)
  - reading from csv or excel file using Pandas
  - generation of pdf, csv and txt using Pandas etc. 

## ??final?? versions:
  - Openapi/Fastapi/Flask - I will decide which will be more difficult and which will fit better into the context
  - database
  - AI text generator of the main events in the character's life
  - Connection to AI service that generates images based on text input to generate character images
  - Front-end (please dont coment it ;)

## futuristic versions:
  - AI/ML generators
  - load templates
  - more fiction worlds

## **<font color='CIAN'>Security options decision</font>**
**<font color='RED'>see more down on this link in section: Further reading</font>**
https://realpython.com/python-sqlite-sqlalchemy/

If your application will expose the database to users, then avoiding SQL injection attacks is an important skill. For more information, check out Preventing SQL Injection Attacks With Python.

Providing web access to a database is common in web-based single-page applications. To learn how, check out Python REST APIs With Flask, Connexion, and SQLAlchemy – Part 2.

Preparing for data engineering job interviews gives you a leg up in your career. To get started, check out Data Engineer Interview Questions With Python.

Migrating data and being able to roll back using Flask with Postgres and SQLAlchemy is an integral part of the Software Development Life Cycle (SDLC). You can learn more about it by checking out Flask by Example – Setting up Postgres, SQLAlchemy, and Alembic.
