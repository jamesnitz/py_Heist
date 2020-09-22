from interfaces.robber import IRobber
class Muscle(IRobber):
  def __init__(self, name, skill, cut):
    super().__init__(name, skill, cut)

  def Perform_Skill(self, bank):
    bank.security_Score -= self.skill_level
    print(f'The muscle: {self.name} is buff. Security score decreased by: {self.skill_level}')
    if bank.alarm_Score <= 0:
      print(f'{self.name} has restrained the guards')
  
  def __str__(self):
    return f'{self.name} is buff with {self.skill_level} skills and wants a {self.percentage_cut}% cut'