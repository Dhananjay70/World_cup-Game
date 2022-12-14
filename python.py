from playsound import playsound
playsound('/home/dhananja/Downloads/Vida - Ricky Martin (2014 FIFA World Cup Song) - 320Kbps.mp3')
from PIL import Image
im = Image.open('/home/dhananja/Downloads/image0.jpeg')
im.show()
football = ['Ronaldo', 'Messi', 'Neymar Jr', 'Ozil']
print("The gratest footbaler of all time is ", football[0:2])
Fifa = input("The gragest Footbaler of all Time is :")
Worldcup_Team = ['France', 'Purgtal', 'Argentina', 'Brazil']
print(Worldcup_Team)
Semi_Final_1= input("Team 1: ")
Semi_Final_2= input("Team 2: ")
print("The SemiFinalist of the world Cup 2022 is",Semi_Final_1,Semi_Final_2)
print("And, The Winner of the semi_final of 2022 is", Worldcup_Team[1])
print(Semi_Final_1)
Semi_Final_3= input("Team 3: ")
Semi_Final_4= input("Team 4: ")
print("The SemiFinalist of the world Cup 2022 is",Semi_Final_3,Semi_Final_4)
print("And, The Winner of the semi_final of 2022 is", Worldcup_Team[2])
Worldcup_Final = ('Purgtal','Argentina')
print("The finalist of World cup 2022 is", Worldcup_Final)
Portugal_scores = 3
print("Purtugal Score in 90 mins is:", Portugal_scores)
Argentina_scores = 3
print("Argentina Score in 90 mins is:",Argentina_scores)
if Portugal_scores > Argentina_scores:
 print("Argentina Wins")
else:
    print("Match Goes to Penalty:")
Argentina_Pen = 4
print("Argentina_Penalty score is", Argentina_Pen)
Portugal_Pen = 5
print("Portugal_Penalty score is", Portugal_Pen)
if Portugal_scores > Argentina_scores:
    print("The winner of World_Cup 2022 is Argentina")
else:
    print("AND,The winner of World_Cup 2022 is Purgtal")