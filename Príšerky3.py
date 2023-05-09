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


for mnozenie in range(100):
    if mnozenie == 0:
        for i in range(10):
            temp = Monster()
            cage.append(temp)
    else:
        cage.sort(key = lambda x: x.cute(), reverse = True)
        for i in range(5):
            cage.pop(5)
        for i in range(len(cage)):
            mutant_1 = []
            otec = random.randrange(0,len(cage))
            mama = random.randrange(0,len(cage))
            if mama == otec:
                mama = random.randrange(0,len(cage))
            pravdep_mutant = random.randrange(0,101)
            if pravdep_mutant <13:
                mutant_1.append(random.randrange(0,10))
            dieta = cage[mama]+cage[otec]
            cage.append(dieta)
        print("Generation", mnozenie+1)
        for monster in cage:
            monster.displayer()
