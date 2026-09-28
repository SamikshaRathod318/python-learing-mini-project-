#1 import random module
import random

#2 create subjects
subjects = ["Sharukh khan", "Amitabh Bachchan", "Salman Khan", "Deepika Padukone", "Priyanka Chopra", "Ranveer Singh", 
            "Alia Bhatt", "Katrina  Kaif", "Hrithik Roshan", "Kareena Kapoor"]
actions = ["launches","cancels","reveals","criticizes","supports","denies","confirms","attacks","defends","celebrates"]
places_or_things = [
    "at Red Fort",
    "in Mumbai Local Train",
    "a plate of samosa",
    "inside parliament",
    "at Ganga Ghat",
    "spring IPL Match"
]

#3 start the headline generation loop
while True:
   subject = random.choice(subjects)
   action = random.choice(actions)
   place_or_thing = random.choice(places_or_things)

   headline = f" BREAKING NEWS: {subject} {action} {place_or_thing}"
   print ("\n" + headline ) 

   user_input = input("\nDo you want to generate another headline? (yes/no): ").strip().lower()
   if user_input != "yes":
       
       break
   
   #goodbye message
   print("Thank you for using the Fake Headline Generator! Have a Fun day!")