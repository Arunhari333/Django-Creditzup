n = [0] * 90
for i in range(1, 3):
    n[10 * i + 8] = 60
    n[10 * i + 1] = 80
    for j in range(2, 5):
        n[10 * i + j] = 70
    for k in range(5, 8):
        n[10 * i + k] = 80

s = [0] * 30
for i in range(1, 3):
    s[10 * i + 1] = 8
    s[10 * i + 2] = 15
    s[10 * i + 3] = 25
    s[10 * i + 4] = 40
    s[10 * i + 5] = 60

c = [0] * 40
for i in range(1, 4):
    c[10 * i + 1] = 8
    c[10 * i + 2] = 12
    c[10 * i + 3] = 20
    c[10 * i + 4] = 40
    c[10 * i + 5] = 60

p = [0] * 100
p[20] = 50
p[40] = 20
p[50] = 30
p[60] = 20
p[70] = 20
p[80] = 5
p[90] = 60
for i in range(1, 4, 2):
    z = 10
    for j in range(1, 6):
        if i == 3 and j == 3:
            z -= 10
        p[i * 10 + j] += z
        z += 10
p[32] -= 5

e = [0] * 12
e[1] = 60
e[2] = 30
e[3] = 35
e[4] = 50
e[5] = 80
e[6] = 60
e[7] = 60
e[8] = 60
e[9] = 80
e[10] = 80
e[11] = 50

l = [0] * 65
for i in range(1, 6):
    l[10 * i + 1] = 15
    l[10 * i + 2] = 10
    l[10 * i + 3] = 5

l[61] = 30
l[62] = 25
l[63] = 15

class lead():
    CHOICE = {0: 'Select:',
              1: 'Student Professional Societies IEEE,IET, ASME, SAE,NASA etc.',
              2: 'College Association Chapters Mechanical, Civil,Electrical etc.',
              3: 'Festival & Technical EventsCollege approved',
              4: 'Hobby Clubs',
              5: 'Special InitiativesApproval from College and University is mandatory'}

    CHOICE1 = {0: 'Select:', 1: 'Core coordinator', 2: 'Sub coordinator', 3: 'Volunteer'}
    CHOICE2 = {0: 'Select:', 1: '(a) Certificate', 2: '(b) Letter from Authorities',
               3: '(c) Appreciation recognition letter', 4: '(d) Documentary evidence',
               5: '(e) Legal Proof', 6: 'Others'}
class nat():
    CHOICE = {1: 'Yes', 2: 'No'}
    CHOICE1 = {0: 'Select:', 1: 'NCC', 2: 'NSS'}
    CHOICE2 = {0: 'Select:',
               1: 'C certificateos performance',
               2: 'Best NSS Volunteer AwardeeUniversity Level',
               3: 'Participation in National Integration Camp',
               4: 'Participation in Pre-Republic Day Parade Camp',
               5: 'Best NSS AwardeeState Level/National Level',
               6: 'Participation in Republic Day Parade Camp',
               7: 'International Youth Exchange Programme',
               8: 'Others'}
    CHOICE3 = {0: 'Select:', 1: '(a) Certificate', 2: '(b) Letter from Authorities',
               3: '(c) Appreciation recognition letter', 4: '(d) Documentary evidence',
               5: '(e) Legal Proof', 6: 'Others'}

class cult():
    CHOICE = {1: 'Yes', 2: 'No'}
    CHOICE1 = {0: 'Select:', 1: 'Music', 2: 'Performing Arts', 3: 'Literary Arts'}
    CHOICE2 = {0: 'Select:', 1: 'College Events', 2: 'Zonal Events', 3: 'State/ University Events',
               4: 'National Events', 5: 'International Events'}
    CHOICE3 = {0: 'Select:', 1: 'First', 2: 'Second', 3: 'Third'}
    CHOICE4 = {0: 'Select:', 1: '(a) Certificate', 2: '(b) Letter from Authorities',
               3: '(c) Appreciation recognition letter', 4: '(d) Documentary evidence',
               5: '(e) Legal Proof', 6: 'Others'}

class prof():
    CHOICE = {0: 'Select:',
              1: 'Tech Fest, Tech Quiz',
              2: 'MOOC with final assessment certificate',
              3: 'Competitions conducted by Professional Societies - IEEE, IET, ASME, SAE, NASA etc.',
              4: 'Attending Full time Conference/Seminars /Exhibitions/Workshop/STTP conducted at IITs/NITs',
              5: 'Paper presentation/publication at IITs/NITs',
              6: 'Poster Presentation at IITs /NITs',
              7: 'Industrial Training/Internship at least for 5 full days',
              8: 'Industrial/Exhibition visits',
              9: 'Foreign Language Skill TOFEL/IELTS/BEC exams etc.'}
    CHOICE1 = {0: 'Select', 1: 'College Events', 2: 'Zonal Events', 3: 'State/ University Events',
               4: 'National Events', 5: 'International Events'}
    CHOICE2 = {0: 'Select:', 1: '(a) Certificate', 2: '(b) Letter from Authorities',
               3: '(c) Appreciation recognition letter', 4: '(d) Documentary evidence',
               5: '(e) Legal Proof', 6: 'Others'}
               

class entr():
    CHOICE = {0: 'Select:',
              1: 'Start-up Company –Registered legally',
              2: 'Patent-Filed',
              3: 'Patent-Published',
              4: 'Patent-Approved',
              5: 'Patent-Licensed',
              6: 'Prototype developed and tested',
              7: 'Awards for Products developed',
              8: 'Innovative technologies developed and used by industries/users',
              9: 'Got venture capital funding for innovative ideas/products',
              10: 'Startup Employment Offering jobs to two persons less than Rs. 15000/- per month',
              11: 'Societal innovations'}
    CHOICE1 = {0: 'Select:', 1: '(a) Certificate', 2: '(b) Letter from Authorities',
               3: '(c) Appreciation recognition letter', 4: '(d) Documentary evidence',
               5: '(e) Legal Proof', 6: 'Others'}
               

class game():
    CHOICE = {1: 'Yes', 2: 'No'}
    CHOICE1 = {0: 'Select:', 1: 'Sports', 2: 'Games'}
    CHOICE2 = {0: 'Select:', 1: 'College Events', 2: 'Zonal Events', 3: 'State/ University Events',
               4: 'National Events', 5: 'International Events'}
    CHOICE3 = {0: 'Select:', 1: 'First', 2: 'Second', 3: 'Third'}
    CHOICE4 = {0: 'Select:', 1: '(a) Certificate', 2: '(b) Letter from Authorities',
               3: '(c) Appreciation recognition letter', 4: '(d) Documentary evidence',
               5: '(e) Legal Proof', 6: 'Others'}

l2 = lead()
n2 = nat()
c2 = cult()
p2 = prof()
e2 = entr()
g2 = game()

def nat_point_calc(Category, SubCategory):
    x = 10 * int(Category) + int(SubCategory)
    return n[x]

def game_point_calc(Category, Level, Position):
    h = 0
    if int(Position) == 1:
        if int(Level) in [1, 2, 3]:
            h += 10
        elif int(Level) in [4, 5]:
            h += 20
    elif int(Position) == 2:
        if int(Level) in [1, 2, 3]:
            h += 8
        elif int(Level) in [4, 5]:
            h += 16
    elif int(Position) == 3:
        if int(Level) in [1, 2, 3]:
            h += 5
        elif int(Level) in [4, 5]:
            h += 12
    x = 10 * int(Category) + int(Level)
    return s[x]+h

def cult_point_calc(Category, Level, Position):
    h = 0
    if int(Position) == 1:
        if int(Level) in [1, 2, 3]:
            h += 10
        elif int(Level) in [4, 5]:
            h += 20
    elif int(Position) == 2:
        if int(Level) in [1, 2, 3]:
            h += 8
        elif int(Level) in [4, 5]:
            h += 16
    elif int(Position) == 3:
        if int(Level) in [1, 2, 3]:
            h += 5
        elif int(Level) in [4, 5]:
            h += 12
    x = 10 * int(Category) + int(Level)
    return c[x]+h

def prof_point_calc(Category, Level):
    x = 0
    if int(Category) == 1 or int(Category) == 3:
        x = 10 * int(Category) + int(Level)
    elif Category != 0:
        x = 10 * int(Category)
    return p[x]

def entre_point_calc(Category):
    x = int(Category)
    return e[x]

def lead_point_calc(Category, SubCategory):
    x = 10 * int(Category) + int(SubCategory)
    return l[x]
