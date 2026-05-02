# add levels, creatures and form randomly the level threat, 
# so the level or the creatures in the level could kill, 
# add fighting till the end and human_migration, also add the love code

import random

# class of Backroom's objects

class Human:
    def __init__(self, name, age, sex):
        self.h_name = name
        self.h_age = age
        self.h_sex = sex
        self.h_faction = "Human"
        self.h_strength = random.randint(5, 20)
        self.h_HP = 100
        self.love_code = random.randint(1, 20)
    
    def grow_function(self):
        self.h_age += 1
        return self.h_age

class Creature:
    def __init__(self, name):
        self.c_name = name
        self.c_strength = random.randint(10, 30)
        self.c_HP = 100
        self.c_faction = "Creature"

# level features

class Levels:
    def __init__(self, name_level):
        self.level_name = name_level
        self.level_threat = random.randint(0, 5)
        self.h_population = []
        self.c_population = []

    def human_reproduction(self, human_1, human_2):
        kid = Human(
            random.choice([
                "Kaelion","Mireva","Zayden","Althira","Roneth",
                "Lioraen","Tavrik","Selmira","Nyvor","Elvara",
                "Corvian","Ismara","Vaelor","Thalise"
            ]),
            random.randint(0, 0),  # age 0
            random.choice(["M", "F"])
        )
        print(f"Baby born from {human_1.h_name} and {human_2.h_name}. Name: {kid.h_name}, Sex: {kid.h_sex}")
        self.h_population.append(kid)

    def add_human(self, human: Human):
        self.h_population.append(human)
    
    def remove_human(self, human: Human):
        if human in self.h_population:
            self.h_population.remove(human)
    
    def show_population(self):
        if not self.h_population:
            print("No humans are here")
        for k in self.h_population:
            print(f"{k.h_name}, Age: {k.h_age}, HP: {k.h_HP}, Sex: {k.h_sex}")
    
    def add_creature(self, creature: Creature):
        self.c_population.append(creature)
    
    def remove_creature(self, creature: Creature):
        if creature in self.c_population:
            self.c_population.remove(creature)
    
    def show_creatures(self):
        if not self.c_population:
            print("No creatures are here")
        for creature in self.c_population:
            print(f"{creature.c_name}, HP: {creature.c_HP}")

    def love_code_interest(self):
        for i in range(len(self.h_population)):
            for j in range(i + 1, len(self.h_population)):
                human_M = self.h_population[i]
                human_F = self.h_population[j]

                if human_M.h_sex == human_F.h_sex:
                    continue  # skip same-sex pairs

                if not (16 <= human_M.h_age <= 41) or not (16 <= human_F.h_age <= 41):
                    continue

                love_difference = abs(human_M.love_code - human_F.love_code)
                attraction = max(0, 1 - love_difference / 20)

                if random.random() < attraction:
                    male = human_M if human_M.h_sex == "M" else human_F
                    female = human_F if human_F.h_sex == "F" else human_M
                    self.human_reproduction(male, female)
                else:
                    human_M.love_code += 0.4
                    human_F.love_code += 0.4

    def level_dangerous_measure(self):
        if self.level_threat == 0:
            print(f"{self.level_name}: Safe level, no threats detected")
        elif 1 <= self.level_threat <= 3:
            print(f"{self.level_name}: Minor creatures, still survivable")
            if random.random() < 0.1 and self.h_population:
                dead_human = random.choice(self.h_population)
                self.remove_human(dead_human)
                print(f"{dead_human.h_name} died due to level danger")
                self.fight()
        elif self.level_threat == 4:
            print(f"{self.level_name}: Dangerous, average creatures")
            if random.random() < 0.5 and self.h_population:
                dead_human = random.choice(self.h_population)
                self.remove_human(dead_human)
                print(f"{dead_human.h_name} died due to level danger")
                self.fight()
        elif self.level_threat == 5:
            print(f"{self.level_name}: Very dangerous, low chance to survive")
            if random.random() < 0.85 and self.h_population:
                dead_human = random.choice(self.h_population)
                self.remove_human(dead_human)
                print(f"{dead_human.h_name} died due to level danger")
                self.fight()

    def fight(self):
        if not self.c_population or not self.h_population:
            print(f"{self.level_name}: No humans or creatures to fight")
            return

        human_fighter = random.choice(self.h_population)
        creature_fighter = random.choice(self.c_population)

        while human_fighter.h_HP > 0 and creature_fighter.c_HP > 0:
            human_fighter.h_HP -= creature_fighter.c_strength
            creature_fighter.c_HP -= human_fighter.h_strength

        if human_fighter.h_HP > 0 and creature_fighter.c_HP <= 0:
            print(f"{human_fighter.h_name} defeated {creature_fighter.c_name}")
            self.remove_creature(creature_fighter)
        elif human_fighter.h_HP <= 0 and creature_fighter.c_HP <= 0:
            print(f"Both {human_fighter.h_name} and {creature_fighter.c_name} died in the fight")
            self.remove_human(human_fighter)
            self.remove_creature(creature_fighter)
        elif human_fighter.h_HP <= 0 and creature_fighter.c_HP > 0:
            print(f"{creature_fighter.c_name} defeated {human_fighter.h_name}")
            self.remove_human(human_fighter)

# Rules of the world 

class Backrooms_World:
    def __init__(self):
        self.level_list = []
        self.time = 0
    
    def add_level(self, level: Levels):
        self.level_list.append(level)
        print(f"{level.level_name} has been added")
    
    def show_levels(self):
        for i in self.level_list:
            print(f"- {i.level_name}")
    
    def human_migration(self):
        if random.random() > 0.5:
            from_level, to_level = random.sample(self.level_list, 2)
            if not from_level.h_population:
                return
            number_of_migrants = random.randint(1, len(from_level.h_population))
            migrants = random.sample(from_level.h_population, number_of_migrants)
            for human in migrants:
                from_level.remove_human(human)
                to_level.add_human(human)
            names = ', '.join([h.h_name for h in migrants])
            print(f"{number_of_migrants} humans migrated from {from_level.level_name} to {to_level.level_name}: {names}")
    
    def Time(self):
        self.time += 1
        print(f"\nWorld Time: {self.time}")

        for level in self.level_list:
            for human in level.h_population:
                human.grow_function()
            level.love_code_interest()
            level.level_dangerous_measure()
            level.fight()

        self.human_migration()

# ------------------ MAIN ------------------

world = Backrooms_World()

def human_creator():
    return Human(
        random.choice([
            "Kaelion","Mireva","Zayden","Althira","Roneth",
            "Lioraen","Tavrik","Selmira","Nyvor","Elvara",
            "Corvian","Ismara","Vaelor","Thalise"
        ]),
        random.randint(16,41),
        random.choice(["M","F"])
    )

# Create levels and populate them
for i in range(3):
    level = Levels(f"Level-{i+1}")
    world.add_level(level)
    print(f"locates at {level.level_name}")
    for _ in range(3):
        level.add_human(human_creator())
        print(f"- added in the level: {level.level_name}")
    creature_name = input(f"Enter the name of a creature for {level.level_name}: ")
    level.add_creature(Creature(creature_name))

# THe engine

while True:
    command = input("Enter command: 1 - next tick | 2 - show humans | 3 - show creatures | 4 - show levels | 5 - add level | 6 - add creature|0 - exit: ")
    if command == "1":
        world.Time()
    elif command == "2":
        for level in world.level_list:
            level.show_population()
    elif command == "3":
        for level in world.level_list:
            level.show_creatures()
    elif command == "4":
        world.show_levels()
    elif command == "5":
        level_name = input("Enter new level name: ")
        new_level = Levels(level_name)
        world.add_level(new_level)
    elif command=="6":
        creature_name = input(f"Enter the name of a creature for {level.level_name}: ")
        level.add_creature(Creature(creature_name))
        print(f"The creature has appeared")

    elif command == "0":
        print("Ending simulation...")
        break
    else:
        print("Invalid command.")