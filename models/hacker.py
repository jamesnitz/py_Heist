from interfaces.robber import IRobber
class Hacker(IRobber):
  def __init__(self, name, skill, cut):
    super().__init__(name, skill, cut)

  def Perform_Skill(self, bank):
    bank.alarm_Score -= self.skill_Level
    print(f'The hacker: {self.name} is hacking. Alarm score decreased by: {self.skill_Level}')
    if bank.alarm_Score <= 0:
      print(f'{self.name} has disabled the alarm')
  
  def __str__(self):
    return f'{self.name} is a hacker with {self.skill_Level} skills and wants a {self.percentage_Cut}% cut'