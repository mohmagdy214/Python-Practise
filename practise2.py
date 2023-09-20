
class game:
    
        def __init__(self):
            while True:
                print('''
            welcome ... choose 1 of our games
                1: sentence_without_duplicate
                2: get_divided_numbers_by
                3: to Exit''')
                User_choise = int(input("Enter your choice :"))
                if User_choise == 1:
                    sentence = input("Enter your sentence :")
                    self.sentence_without_duplicate(sentence)
                    
                elif User_choise == 2:
                    x = int(input("Enter First Number :"))
                    y = int(input("Enter Second Number :"))
                    self.get_divided_numbers_by(x,y)
                    
                elif User_choise == 3:
                    print("Goodbye ...")
                    break
                else:
                    print ("Please Enter Numbers between 1:3")

                play_again = input("Press any key to play again , n to Exit")
                if play_again == "n":
                        print("Goodbye ...")
                        break

            
        def sentence_without_duplicate(self,sentence):
                words = sentence.split(" ")
                not_duplicated_words =[]
                for i in words:
                    if i not in not_duplicated_words:
                        not_duplicated_words.append(i)
                print(" ".join(not_duplicated_words))


        def get_divided_numbers_by(self,x,y):
                result = []
                for q in range(1,101):
                    if q%x == 0 and q%y == 0:
                        result.append(q)
                print(result)



g1 = game()







