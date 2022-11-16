
import replit
from getkey import getkey, keys

def FirstChoice():
 replit.clear()
 print("\nFörsta valet")
 input("Press Enter to continue...")

def SecondChoice():
  replit.clear()
  print("\nAndra valet")
  input("Press Enter to continue...")

def ThirdChoice():
  replit.clear()
  print("\nTredje valet")
  input("Press Enter to continue...")

def EndProgram():
  replit.clear()
  print("\nAvslutar programmet")
  input("Press Enter to continue...")
    
  
  
menuOptions = ["\nFörsta\t\t", "\nAndra\t\t" , "\nTredje\t\t",  "\nAvsluta\t\t"]
menuSelected = 0

while(True):
  replit.clear()
  print("\x1b[?25l")

  if menuSelected == 0:
    print(menuOptions[0] + "<--")
    print(menuOptions[1])
    print(menuOptions[2])
    print(menuOptions[3])
  elif menuSelected == 1:
    print(menuOptions[0])
    print(menuOptions[1] + "<--")
    print(menuOptions[2])
    print(menuOptions[3])
  elif menuSelected == 2:
    print(menuOptions[0])
    print(menuOptions[1])
    print(menuOptions[2] + "<--")
    print(menuOptions[3])
  elif menuSelected == 3:
    print(menuOptions[0])
    print(menuOptions[1])
    print(menuOptions[2])
    print(menuOptions[3] + "<--")  
     
  keyPressed = getkey()
  if keyPressed == keys.DOWN and menuSelected + 1 != len(menuOptions):
    menuSelected += 1
  elif keyPressed == keys.UP and not (menuSelected == 0):
    menuSelected -= 1
  elif keyPressed == keys.ENTER:
    if menuSelected == 0:
      FirstChoice()
    elif menuSelected == 1:
      SecondChoice()
    elif menuSelected == 2:
      ThirdChoice()
    elif menuSelected == 3:
      EndProgram()
      print("\x1b[?25h")
      break 
      
                                                           