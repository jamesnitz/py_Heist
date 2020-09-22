import random
import operator
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
  # build crew
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
  # create bank
  cash = random.randint(50000, 1000000)
  alarm_Score = random.randint(0, 100)
  vault_Score = random.randint(0, 100)
  sec_Score = random.randint(0, 100)
  national_Bank = Bank(cash, alarm_Score, vault_Score, sec_Score)
  # create dictionary for report
  bank_scores = {
    "alarm": alarm_Score,
    "vault": vault_Score,
    "security": sec_Score
  }  
  most_Secure = max(bank_scores.items(), key=operator.itemgetter(1))[0]
  least_Secure = min(bank_scores.items(), key=operator.itemgetter(1))[0]
  print('-------RECON REPORT-------')
  print(f'The most secure part of the job is the {most_Secure}. Least Secure is {least_Secure}.')
  print('--------------------------')

  # choose crew
  for mem in rolodex:
    print(f'{rolodex.index(mem)} {mem}')
  chosen_Crew = []
  total_Take = 100
  while True:
    selected_Crew_member = input('Assemble your crew! Enter in the member\'s number ')
    if selected_Crew_member == '':
      break
    for mem in rolodex:
      if int(selected_Crew_member) == rolodex.index(mem):
        chosen_Crew.append(mem)
        total_Take -= mem.percentage_Cut
        print(f'{total_Take} is left')
        rolodex.remove(mem)
        break
    for mem in rolodex:
      if mem.percentage_Cut < total_Take:
        print(f'{rolodex.index(mem)} {mem}')
  print('Your assembled crew is:')
  for mem in chosen_Crew:
    print(mem)
    mem.Perform_Skill(national_Bank)
  if national_Bank.is_Secure:
    print('The heist has failed everyone is going to jail.')
  else:
    print('HEIST WAS SUCCESSFUL')
    total_Member_Earnings = 0
    for mem in chosen_Crew:
      earnings = (mem.percentage_Cut / 100) * national_Bank.cash_On_Hand
      total_Member_Earnings += earnings
      print(f'{mem.name} earned ${earnings}')
    mastermind_Money = national_Bank.cash_On_Hand - total_Member_Earnings
    print(f'The mastermind earned ${mastermind_Money}')




