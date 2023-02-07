
import random
cage = []

class Monster:

    def __init__(self, temp = []):
        self.dna = []
        if len(temp) == 0:
            for i in range(5):
                self.dna.append(random.randrange(0,10))
        else:
            self.dna = temp

    def displayer(self):
        print(* self.dna)

    def cute(self):    #vráti stupeň krásnosti príšerky
        return self.dna.count(1)

    def __add__(self, other):  #other je druhy
        temp = []
        for i in range(5):
            mut = random.randrange(0,101)    #mutants
            if mut <13:
                temp.append(random.randrange(0,10))
            else:
                par = random.randrange(0,2)    # parents
                if par == 0:
                    temp.append(self.dna[i])
                else:
                    temp.append(other.dna[i])
        return Monster(temp)

for i in range(10):
    temp = Monster()
    cage.append(temp)

for mnozenie in range(100):
    cage.sort(key = lambda x: x.cute(), reverse = True)
    for prišera in cage[0:5]:
        for i in range(5):
            čísla = [0,1,2,3,4]
            muta = []
            otec = random.choice(čísla)
            mama = random.choice(čísla)
            if mama == otec:
                mama = random.choice(čísla)
            mutan = random.randrange(0,101)
            if mutan <13:
                muta.append(random.randrange(0,10))
            dna = [mama, otec, muta]
            dieta = []
            dieta.append(random.choice(dna))
            cage.append(dieta)
    for monster in cage:
        monster.displayer()
