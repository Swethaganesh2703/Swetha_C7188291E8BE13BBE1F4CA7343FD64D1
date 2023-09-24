'''implement a class called player that represents a cricket player.
the play class should have a method called play()which prints"the player is playing cricket.
derive two classes,batsman and bowler,from the player class.
override the play ()method in each derived class to print"the batsman is batting"and"the bowler is bowling",
respectively.write a program to create objects of both the batsman and bowler classes and call the play ()method for each objects.'''


#define the base class player
class player:
  def play (self):
      print("The player is playing cricket.")

#define the derived class batsman
class Batsman(player):
  def play(self):
      print("The batsman is batting.")

#define the derived class bowler 
class Bowler(player):
  def play(self):
      print("The bowler is bowling")
    
#create objects of batsman and bowler classes 
batsman = Batsman()
bowler = Bowler()

#call the play()method to each object
batsman.play()
bowler.play()




    