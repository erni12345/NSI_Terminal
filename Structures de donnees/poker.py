from typing import Collection
import random

class Card:

    def __init__(self, chiffre, type):
        self.chiffre = chiffre
        self.type = type

    def __repr__(self):
        return f"{self.chiffre} of {self.type}"



chiffre = [x for x in range(1, 13)]
CHECKSTUFF = {11:"J", 12:"Q", 13: "K", 1:"A"}
couleur = ["hearts", "spades", "clubs", "diamonds"]

class Jeu:
    

    def __init__(self):
        deck = [Card(y, x) for y in chiffre for x in couleur]

        self.deck = deck
    
    def creer_main(self):

        self.cards_5 = random.sample(self.deck, 5)
    

    def royal_flush(self):
        
        type_check = self.cards_5[0].type
        for x in self.cards_5:
            if x.type != type_check:
                return False

        for x in self.cards_5:
            if x.chiffre not in [10, "Valet", "Damme", "Roi", "Ace"]:
                return False
        return True

    def straight_flush(self):
        type_check = self.cards_5[0].type
        for x in self.cards_5:
            if x.type != type_check:
                return False
        nums = []
        for x in self.cards_5:
            nums.append(x.chiffre)

        nums.sort()
        
        if nums[0] != nums[4]-4:
            return False

        return True

    def four_kind(self):

        check_dic = {}
        for x in self.cards_5:
            num = x.chiffre
            if num in check_dic:
                check_dic[num] += 1
            else:
                check_dic[num] = 1
        
        for x in check_dic:
            if check_dic[x] == 4:
                return True
        return False

    def full_house(self):

        double = False
        triple = False
        check_dic = {}
        for x in self.cards_5:
            num = x.chiffre
            if num in check_dic:
                check_dic[num] += 1
            else:
                check_dic[num] = 1
        
        for x in check_dic:
            if check_dic[x] == 3:
                triple = True
            elif check_dic[x] == 2:
                double = True
        return double and triple


    def flush(self):
    
        type_check = self.cards_5[0].type
        for x in self.cards_5:
            if x.type != type_check:
                return False
        return True


    def quinte(self):
        nums = []
        for x in self.cards_5:
            nums.append(x.chiffre)
        nums.sort()
        if nums[0] != nums[4]-4:
            return False
        return True

    def three_of_a_kind(self):
        check_dic = {}
        for x in self.cards_5:
            num = x.chiffre
            if num in check_dic:
                check_dic[num] += 1
            else:
                check_dic[num] = 1
        
        for x in check_dic:
            if check_dic[x] == 3:
                return True
        return False

    
    def two_pair(self):

        pair1 = False
        pair2 = False

        check_dic = {}
        for x in self.cards_5:
            num = x.chiffre
            if num in check_dic:
                check_dic[num] += 1
            else:
                check_dic[num] = 1
        
        for x in check_dic:
            if check_dic[x] == 2 and not pair1:
                pair1 = True
            elif check_dic[x] == 2 and not pair2:
                pair2 = True
        return pair1 and pair2


    def one_pair(self):
        check_dic = {}
        for x in self.cards_5:
            num = x.chiffre
            if num in check_dic:
                check_dic[num] += 1
            else:
                check_dic[num] = 1
        
        for x in check_dic:
            if check_dic[x] == 2:
                return True
        return False

    



    def combinaison_main(self):

        what_was_done = ["royal_flush", "straight_flush", "four of a kind", "full_house", "flush", "quinte", "three of a kind", "two pair", "one pair"]
        checks = [self.royal_flush(), self.straight_flush(), self.four_kind(), self.full_house(), self.flush(), \
                    self.quinte(), self.three_of_a_kind(), self.two_pair(), self.one_pair()]

        for x in range(len(checks)):
            if checks[x]:
                return what_was_done[x], self.cards_5

        return "high card", self.cards_5

    

        


def faire_stats(n):
    jeu = Jeu()
    stats = {"royal_flush":0, "straight_flush":0, "four of a kind":0, "full_house":0, "flush":0, "quinte":0, "three of a kind":0, "two pair":0, "one pair":0, "high card":0}
    x = 0
    while x < n:
        x+=1
        jeu.creer_main()
        stats[jeu.combinaison_main()[0]]

    return stats



print(faire_stats(100))


