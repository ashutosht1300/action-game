"""type command like:
     
     say hello , say bye , say apple
     let's go , let's drive , let's walk
     go there , go left , go right
     
thanks 
by @Ashutosh Tamrakar"""

def getinput():
 command = input().split()
 verb_word = command[0]
 if verb_word in verb_dict:
  verb = verb_dict[verb_word ]
 else:
  print("verb not found")
  return
 
 if len(command) >= 2:
  noun = command[1]
 else :
  noun = "nothing"
 verb(noun)

def say(noun):
 print("you said {}".format(noun))
 
def let(verb):
 print("you want to {}".format(verb))
 
def go(dir):
 print("you have to go for {}".format(dir))

verb_dict = {
    "say": say,
    "let's":let,
    "go": go,
}

While True:
 getinput()
