#This program is a starter chatbot program submitted by a fellow Elite 101 student.
# It's been modified to fit the purpose of the Elite 101 Pre-work Project.

import random
print("Hey, My name is Millah. What is your name ?")
name = input("(Enter your name)")
print("Hey, " + name  + ".  I am glad to meet you")


#------------------------Feeling/Emotion Questions ----------------------

def myFeeling(feeling):
  randresp1 = random.randint(1,2)
  randresp2 = random.randint(1,2)
  goodFeelings = ["happy","amazing" , "great" , "okay" ,"good" , "fabulous" , "nice"]
  badFeelings = ["sad","down","depressed", "unwell","unhappy" ,"bad"]
  
  if feeling in goodFeelings:
      if randresp1 == 1:
          print("Good to hear!")
      elif randresp1 == 2:
          print("Great!")
  elif  feeling in badFeelings:
      if randresp2 == 1:
          print("I'm sorry to hear that!")
          print("I hope you will get better with your issue.")
          print("let's talk about something else")
      elif randresp2 == 2:
          print("I'm sorry for you!")
          wrong = input("What's wrong? ")
          if wrong == "nothing" or wrong == "don't want to share." or wrong == "It's okay":
              print("Alright, no worries.")
          else:
              print("We don't have to talk about it if you don't want to. \n Let's move on.")
  else:
      print("Alright. Let's continue.")

  
feeling = input("\nHow are you feeling? ").lower()
myFeeling(feeling)

#------------------------Age Questions ----------------------  

def myAge(age):
  response3 = random.randint(1, 2)
  
  if age <15:
      if response3 == 1:
          print("You are so young! What interest you ?")
      elif response3 == 2:
          print("That's great that you are still young!")        
  elif age >= 15 and age < 18:
      print("Yeah! You are a teenager! That's crazy!")
  elif age >= 18 and age < 55:
      print("Oh, cool!")
  elif age >= 55 and age<120:
      print("So glad to see you here today!")
  else:
      print("You can't be that old. Try again.")
      age2 = int(input("What is your age?"))
      if age2<120:
        print("Okay! This more like an age number.")

try:
  age = int(input("\nWhat is your age? "))
except:
  age =5

myAge(age)
 
#------------------------Sports Questions ----------------------  

def mySports(sports):
  sports1 =["track" ,"cross country" , "tennis","hockey" , "swimming"]
  goat =['Ronaldo','Messi','','Bird','Lebron','Curry'] 
  if sports == "yes":
      favorite_sport = input("Which sport is your favorite? ").lower()
      if favorite_sport== "basketball":
        print("Cool! I heard that Lebron is a nice player.")
      elif favorite_sport== "Soccer":     
          favorite_bball_player = input("Nice! Which player is your favorite? ").capitalize()
          if favorite_bball_player in goat: 
              print("I heard he's the GOAT of Basketball, that's pretty cool.")
          else:
            print(f"I agree!{favorite_bball_player} is a great basketball player")          
      elif favorite_sport == "la crosse":
          print("Cool! I heard that Paul Rabil is a nice player.")
      elif favorite_sport == "e-sport":
          print("Cool! I heard that Faker is a nice player.")
      elif favorite_sport in sports1:
          print("Really? That must take a lot of endurance!")
      elif favorite_sport == "gaming":
          print("Whoah! That's so cool that we have something in common!")
      else:
        notListed = input(" Humm! Tell me about this sports: ")
        print(f"{notListed} sounds very intersting,{name}!")
  elif sports == "no" or sports == "none":
      print("That's okay. We all have our own interests and waste of time.")
  
  else:
      print("Not to worry. This is not a required section. Let's move on.")


sports = input("\nDo you like sports?(yes/no) ").lower()  
mySports(sports)


#------------------------Weekday Activities ----------------------

def daysOfWeek(day):
  weekdays =["Monday", "Tuesday", "Wednesday" ,"Thursday" ,"Friday"]
  weekend = ["Saturday", "Sunday"]
  if userDay in weekdays: 
      print("Weekday, huh. You must be busy.\n We can talk another time, have a good day!")
  elif userDay in weekend.capitalize(): 
      print("Great! You should go and enjoy your day.")


userDay = input("\nWhat day of the week is it today? ").capitalize()
daysOfWeek(userDay)
#
