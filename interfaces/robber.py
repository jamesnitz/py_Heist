class IRobber:
  def __init__(self, name, skill_level, percentage_cut):
    self.name = name
    self.skill_level = skill_level
    self.percentage_cut = percentage_cut
    
  def Perform_Skill(self):
    print("skill performed")