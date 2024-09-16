ourNumber=7
chance=1
while chance<=5:
  number=int(input("Enter a number between 0 and 9"))
  if number==ourNumber:
      print("You Won")
      break
  chance+=1
else :
    print("Loss the game")