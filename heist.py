from models import Bank, Hacker, Muscle, Locker_Picker

if __name__ == "__main__":
  print('Python Heist')
  rolodex = []


  garrett = Muscle("garrett", 75, 10)
  william = Hacker("william", 75, 10)
  asia = Locker_Picker("asia", 100, 25)

  rolodex.append(garrett)
  rolodex.append(william)
  rolodex.append(asia)

  print(f'The rolodex currently has {len(rolodex)} heisters to select!')

  while True:
    user_Input_Name = input('Please add a new crew member. Or press enter to choose your team    ')
    if user_Input_Name == "":
      break
    while True:
      user_Input_Specialty = input(f'What is {user_Input_Name}\'s specialty: hacker, muscle or lock picker??    ')
      if user_Input_Specialty.lower() == 'muscle':
        user_Input_skill = input('What is their skill level?   ')
        user_Input_Cut = input('What is their take on this score   ')
        new_Muscle = Muscle(user_Input_Name, int(user_Input_skill), int(user_Input_Cut))
        rolodex.append(new_Muscle)
        break

      elif user_Input_Specialty.lower() == 'lock picker':
        user_Input_skill = input('What is their skill level?   ')
        user_Input_Cut = input('What is their take on this score  ')
        new_Lock_Picker = Locker_Picker(user_Input_Name, int(user_Input_skill), int(user_Input_Cut))
        rolodex.append(new_Lock_Picker)
        break

      elif user_Input_Specialty.lower() == 'hacker':
        user_Input_skill = input('What is their skill level?   ')
        user_Input_Cut = input('What is their take on this score   ')
        new_Hacker = Hacker(user_Input_Name, int(user_Input_skill), int(user_Input_Cut))
        rolodex.append(new_Hacker)
        break
      else:
        print(f'{user_Input_Specialty} is not a speciality. Please enter a valid speciality.')
  # End of team builder
    