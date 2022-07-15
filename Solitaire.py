import random
### Id: 825337929, Janhav Khanna, Solitaire Game

class Deque:
    def __init__(self):
        self.items = []
    def return_data(self): #I added this to return a string
        str1 = ""
        for i in self.items:
            str1 += str(i) + " "
        return str1
    def total(self): #This returns the total number of items in the list
        list1 = []
        for i in self.items:
            list1.append(i)
        return len(list1)
    def isdesc(self): #I added this to evaluate if the order is descending
        list1 = []
        if len(self.items) <= 1:
            return True
        slist1 = sorted(self.items)
        for nums in range(len(slist1) -1, -1, -1):
            list1.append(slist1[nums])
        print (self.items)
        print(list1)
        if self.items == list1:
            return True
        else:
            return False
    def return_list(self): #I added this to return a list instead of string
        list1 = []
        for i in self.items:
            list1.append(i)
        return list1
    def add_front(self, item):
        self.items.append(item)
    def add_rear(self, item):
        self.items.insert(0,item)
    def remove_front(self):
        return self.items.pop(-1)
    def remove_rear(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)
    def peek(self):
        return self.items[-1]
    def peeklast(self):
        return self.items[0]
    def printall(self, index): #This gets called to print the initial row 0
        str1 = ""
        count = 0
        for nums in range(0, len(self.items)):
            if index == 0:
                if nums == 0:
                    first = str(self.items[nums])
                    number = self.items[nums]
                else:
                    count += 1
            else:
                count += 1
        try:
            if number < 10:
                str1 += (""".------.""" + """.------.""" * count + "\n")
                str1 += ("       " + """|""" + first + """     |""" + """|░░░░░░|""" * count + "\n")
                str1 += ("       " + """|      |""" + """|░░░░░░|""" * count + "\n")
                str1 += ("       " + """|      |""" + """|░░░░░░|""" * count + "\n")
                str1 += ("       " + """|     """ + first + """|""" + """|░░░░░░|""" * count + "\n")
                str1 += ("       " + """`------'""" + """`------'""" * count + "\n")
            else:
                str1 += (""".------.""" + """.------.""" * count + "\n")
                str1 += ("       " + """|""" + first + """    |""" + """|░░░░░░|""" * count + "\n")
                str1 += ("       " + """|      |""" + """|░░░░░░|""" * count + "\n")
                str1 += ("       " + """|      |""" + """|░░░░░░|""" * count + "\n")
                str1 += ("       " + """|    """ + first + """|""" + """|░░░░░░|""" * count + "\n")
                str1 += ("       " + """`------'""" + """`------'""" * count)
        except:
            random = 1
        return str1


class Solitaire: #this is the main solitaire class
    def __init__(self, ncards):
        self.total = 0
        self.t = []
        self.__CardNo = len(ncards)
        self.__ColNo = (self.__CardNo // 8) + 3
        self.__ChanceNo = self.__CardNo * 2
        for i in range(self.__ColNo):
            self.t.append(Deque())
        for i in range(self.__CardNo):
            self.t[0].add_front(ncards[i])

    def display(self): #this gets called to print all rows in the game
        count = 0
        num = 0
        while count != self.__ColNo:
            if count == 0: #this prints row 0
                print("Row 0" + ":", self.t[count].printall(count))
                num += 1
            if count != 0: #this prints all rows that are not 0
                if self.total >= 1:
                    popped = self.popper(count)
                    str1 = ""
                    str1 += (""".------.""" * len(popped) + "\n")
                    if len(popped) == 1:
                        if popped[0] < 10:
                            str1 += ("       " + """|""" + str(popped[0]) + """     |""" + "\n")
                            str1 += ("       " + """|      |""" + "\n")
                            str1 += ("       " + """|      |""" +"\n")
                            str1 += ("       " + """|     """ + str(popped[0]) + """|""" + "\n")

                    if len(popped) == 2:
                        if popped[0] < 10:
                            str1 += ("       " + """|""" + str(popped[0]) + """     |""" + """|""" + str(popped[1]) + """     |""" + "\n")
                            str1 += ("       " + """|      |""" * len(popped) + "\n")
                            str1 += ("       " + """|      |""" * len(popped) + "\n")
                            str1 += ("       " + """|""" + str(popped[0]) + """     |""" + """|""" + str(popped[1]) + """     |""" + "\n")

                    if len(popped) == 3:
                        if popped[0] < 10:
                            str1 += ("       " + """|""" + str(popped[0]) + """     |""" + """|""" + str(popped[1]) + """     |""" + """|""" + str(popped[2]) + """     |""" + "\n")
                            str1 += ("       " + """|      |""" * len(popped) + "\n")
                            str1 += ("       " + """|      |""" * len(popped) + "\n")
                            str1 += ("       " + """|""" + str(popped[0]) + """     |""" + """|""" + str(popped[1]) + """     |""" + """|""" + str(popped[2]) + """     |""" + "\n")

                    if len(popped) == 4:
                        if popped[0] < 10:
                            str1 += ("       " + """|""" + str(popped[0]) + """     |""" + """|""" + str(popped[1]) + """     |""" + """|""" + str(popped[2]) + """     |""" + """|""" + str(popped[3]) + """     |""" + "\n")
                            str1 += ("       " + """|      |""" * len(popped) + "\n")
                            str1 += ("       " + """|      |""" * len(popped) + "\n")
                            str1 += ("       " + """|""" + str(popped[0]) + """     |""" + """|""" + str(popped[1]) + """     |""" + """|""" + str(popped[2]) + """     |""" + """|""" + str(popped[3]) + """     |""" + "\n")

                    if len(popped) == 5:
                        if popped[0] < 10:
                            str1 += ("       " + """|""" + str(popped[0]) + """     |""" + """|""" + str(popped[1]) + """     |""" + """|""" + str(popped[2]) + """     |""" + """|""" + str(popped[3]) + """     |""" + """|""" + str(popped[4]) + """     |""" + "\n")
                            str1 += ("       " + """|      |""" * len(popped) + "\n")
                            str1 += ("       " + """|      |""" * len(popped) + "\n")
                            str1 += ("       " + """|""" + str(popped[0]) + """     |""" + """|""" + str(popped[1]) + """     |""" + """|""" + str(popped[2]) + """     |""" + """|""" + str(popped[3]) + """     |""" + """|""" + str(popped[4]) + """     |""" + "\n")

                    if len(popped) == 6:
                        if popped[0] < 10:
                            str1 += ("       " + """|""" + str(popped[0]) + """     |""" + """|""" + str(popped[1]) + """     |""" + """|""" + str(popped[2]) + """     |""" + """|""" + str(popped[3]) + """     |""" + """|""" + str(popped[4]) + """     |""" + """|""" + str(popped[5]) + """     |""" + "\n")
                            str1 += ("       " + """|      |""" * len(popped) + "\n")
                            str1 += ("       " + """|      |""" * len(popped) + "\n")
                            str1 += ("       " + """|""" + str(popped[0]) + """     |""" + """|""" + str(popped[1]) + """     |""" + """|""" + str(popped[2]) + """     |""" + """|""" + str(popped[3]) + """     |""" + """|""" + str(popped[4]) + """     |""" + """|""" + str(popped[5]) + """     |""" + "\n")

                    if len(popped) == 7:
                        if popped[0] < 10:
                            str1 += ("       " + """|""" + str(popped[0]) + """     |""" + """|""" + str(popped[1]) + """     |""" + """|""" + str(popped[2]) + """     |""" + """|""" + str(popped[3]) + """     |""" + """|""" + str(popped[4]) + """     |""" + """|""" + str(popped[5]) + """     |""" + """|""" + str(popped[6]) + """     |""" + "\n")
                            str1 += ("       " + """|      |""" * len(popped) + "\n")
                            str1 += ("       " + """|      |""" * len(popped) + "\n")
                            str1 += ("       " + """|""" + str(popped[0]) + """     |""" + """|""" + str(popped[1]) + """     |""" + """|""" + str(popped[2]) + """     |""" + """|""" + str(popped[3]) + """     |""" + """|""" + str(popped[4]) + """     |""" + """|""" + str(popped[5]) + """     |""" + """|""" + str(popped[6]) + """     |""" + "\n")

                    if len(popped) == 8:
                        if popped[0] < 10:
                            str1 += ("       " + """|""" + str(popped[0]) + """     |""" + """|""" + str(popped[1]) + """     |""" + """|""" + str(popped[2]) + """     |""" + """|""" + str(popped[3]) + """     |""" + """|""" + str(popped[4]) + """     |""" + """|""" + str(popped[5]) + """     |""" + """|""" + str(popped[6]) + """     |""" + """|""" + str(popped[7]) + """     |""" + "\n")
                            str1 += ("       " + """|      |""" * len(popped) + "\n")
                            str1 += ("       " + """|      |""" * len(popped) + "\n")
                            str1 += ("       " + """|""" + str(popped[0]) + """     |""" + """|""" + str(popped[1]) + """     |""" + """|""" + str(popped[2]) + """     |""" + """|""" + str(popped[3]) + """     |""" + """|""" + str(popped[4]) + """     |""" + """|""" + str(popped[5]) + """     |""" + """|""" + str(popped[6]) + """     |""" + """|""" + str(popped[7]) + """     |""" + "\n")

                    if len(popped) == 9:
                        if popped[0] < 10:
                            str1 += ("       " + """|""" + str(popped[0]) + """     |""" + """|""" + str(popped[1]) + """     |""" + """|""" + str(popped[2]) + """     |""" + """|""" + str(popped[3]) + """     |""" + """|""" + str(popped[4]) + """     |""" + """|""" + str(popped[5]) + """     |""" + """|""" + str(popped[6]) + """     |""" + """|""" + str(popped[7]) + """     |""" + """|""" + str(popped[8]) + """     |""" + "\n")
                            str1 += ("       " + """|      |""" * len(popped) + "\n")
                            str1 += ("       " + """|      |""" * len(popped) + "\n")
                            str1 += ("       " + """|""" + str(popped[0]) + """     |""" + """|""" + str(popped[1]) + """     |""" + """|""" + str(popped[2]) + """     |""" + """|""" + str(popped[3]) + """     |""" + """|""" + str(popped[4]) + """     |""" + """|""" + str(popped[5]) + """     |""" + """|""" + str(popped[6]) + """     |""" + """|""" + str(popped[7]) + """     |""" + """|""" + str(popped[8]) + """     |""" + "\n")

                    if len(popped) == 10:
                        if popped[0] < 10:
                            str1 += ("       " + """|""" + str(popped[0]) + """     |""" + """|""" + str(popped[1]) + """     |""" + """|""" + str(popped[2]) + """     |""" + """|""" + str(popped[3]) + """     |""" + """|""" + str(popped[4]) + """     |""" + """|""" + str(popped[5]) + """     |""" + """|""" + str(popped[6]) + """     |""" + """|""" + str(popped[7]) + """     |""" + """|""" + str(popped[8]) + """     |""" + """|""" + str(popped[9]) + """     |""" + "\n")
                            str1 += ("       " + """|      |""" * len(popped) + "\n")
                            str1 += ("       " + """|      |""" * len(popped) + "\n")
                            str1 += ("       " + """|""" + str(popped[0]) + """     |""" + """|""" + str(popped[1]) + """     |""" + """|""" + str(popped[2]) + """     |""" + """|""" + str(popped[3]) + """     |""" + """|""" + str(popped[4]) + """     |""" + """|""" + str(popped[5]) + """     |""" + """|""" + str(popped[6]) + """     |""" + """|""" + str(popped[7]) + """     |""" + """|""" + str(popped[8]) + """     |""" + """|""" + str(popped[9]) + """     |""" + "\n")
                        
                    str1 += ("       " + """`------'""" * len(popped) + "\n")
                    print("Row " + str(num) + ":", str1)
                        
                else:
                    popped = ""
                    print("Row " + str(num) + ":", popped)
                num += 1
            count += 1
        self.total += 1

    def popper(self, count): #I use this as a gateway to return list into the stacks printer
        return self.t[count].return_list()
        
    def move(self, c1, c2): #This moves cards
        if c1 == c2 and c1 == 0:
            temp = self.t[c1].remove_rear()
            self.t[c1].add_front(temp)
            
        if c1 == 0 and c2 > 0:
            temp = self.t[c1].remove_rear()
            self.t[c2].add_front(temp)
            
        if c1 > 0 and c2 > 0:
            list1 = self.t[c1].return_list()
            for nums in range(len(list1)):
                temp = self.t[c1].remove_rear()
                self.t[c2].add_front(temp)
            
        return self.t
        
    def iscomplete(self): #This checks if the conditions for win are met
        count = 0
        for nums in self.t:
            if len(nums.return_list()) != 0:
                count += 1
        if len(self.t[0].return_list()) == 0 and count == 1:
            return True
        for nums in self.t:
            if nums.isdesc == True:
                random = 1
            else:
                break
        return False

    
    def play(self): #This where my first ascii art is introduced, kind of like an intro for the game
        print("""         Welcome to Solitaire - By Janhav Khanna ID: 825337929
.------..------..------..------..------..------..------..------..------.
|S.--. ||O.--. ||L.--. ||I.--. ||T.--. ||A.--. ||I.--. ||R.--. ||E.--. |
| :/\: || :/\: || :/\: || (\/) || :/\: || (\/) || (\/) || :(): || (\/) |
| :\/: || :\/: || (__) || :\/: || (__) || :\/: || :\/: || ()() || :\/: |
| '--'S|| '--'O|| '--'L|| '--'I|| '--'T|| '--'A|| '--'I|| '--'R|| '--'E|
`------'`------'`------'`------'`------'`------'`------'`------'`------'

Game has started!
Your cards are below:""")
        for game_iter in range(self.__ChanceNo):
            self.display()
            print()
            print("Round ", game_iter+1, " of ", self.__ChanceNo, ":", sep="")
            col1 = int(input("Move cards from row number:"),10)
            col2 = int(input("Moving cards to row number:"),10)
            if col1 >= 0 and col2 >= 0 and col1 < self.__ColNo and col2 < self.__ColNo:
                self.move(col1, col2)
            clear()
            if (self.iscomplete() == True): #This where the win screen and loss screen are put for printing
                print("""
.------..------..------.     .------..------..------..------.
|Y.--. ||O.--. ||U.--. |.-.  |W.--. ||I.--. ||N.--. ||!.--. |
| (\/) || :/\: || (\/) ((5)) | :/\: || (\/) || :(): || (\/) |
| :\/: || :\/: || :\/: |'-.-.| :\/: || :\/: || ()() || :\/: |
| '--'Y|| '--'O|| '--'U| ((1)) '--'W|| '--'I|| '--'N|| '--'!|
`------'`------'`------'  '-'`------'`------'`------'`------'
In only""", game_iter+1, "steps!")
                break;
            else:
                if game_iter+1 == self.__ChanceNo:
                   print("""
.------..------..------.     .------..------..------..------..------.
|Y.--. ||O.--. ||U.--. |.-.  |L.--. ||O.--. ||S.--. ||E.--. ||!.--. |
| (\/) || :/\: || (\/) ((5)) | :/\: || :/\: || :/\: || (\/) || (\/) |
| :\/: || :\/: || :\/: |'-.-.| (__) || :\/: || :\/: || :\/: || :\/: |
| '--'Y|| '--'O|| '--'U| ((1)) '--'L|| '--'O|| '--'S|| '--'E|| '--'!|
`------'`------'`------'  '-'`------'`------'`------'`------'`------'
Game over!""")
        print()

                
def clear(): #I made this to clear the game and allow for the seperation of the previous round from the next making it look cleaner
    print()
    print ("-" * 30, "Next Round", "-" * 30)
    print()
    print ("Your cards are below:")


def main(): #This where I made the randomisation and creating of cards numbers for the game to run
    cards = []
    count = 0
    length = random.randrange(3, 10)
    while count != length:
        cards.append(random.randrange(0, 9))
        count +=1
    game = Solitaire(cards)
    game.play()
    return

main()
