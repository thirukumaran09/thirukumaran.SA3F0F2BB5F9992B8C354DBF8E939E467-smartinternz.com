# Define the base class palyer
class player:
    def play(self):
      print("The player is playing cricket.")
      
# Define the derived class Batsman
class Batsman(player):
  def play(self):
    print("The batsman is batting.")
    
# Define the derived class Bowler
class Bowler(player):
  def play(self):
    print("The bowler is bowling.")

# create objects of Batsmen and Bowler classes
batsman = Batsman()
bowler = Bowler()

  # call the paly() method for each object
batsman.play()
bowler.play()