from interfaces.robber import IRobber
class Locker_Picker(IRobber):
  def __init__(self, name, skill, cut):
    super().__init__(name, skill, cut)

  def Perform_Skill(self, bank):
    bank.vault_Score -= self.skill_Level
    print(f'The lock picker: {self.name} is cracking the safe. Vault score decreased by: {self.skill_Level}')
    if bank.alarm_Score <= 0:
      print(f'{self.name} has opened the lock')
  
  def __str__(self):
    return f'{self.name} is a lock picker with {self.skill_Level} skills and wants a {self.percentage_Cut}% cut'