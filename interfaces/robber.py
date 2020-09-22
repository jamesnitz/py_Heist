class IRobber:
  def __init__(self, name, skill_level, percentage_cut):
    self.name = name
    self.skill_Level = skill_level
    self.percentage_Cut = percentage_cut
    
  def Perform_Skill(self):
    print("skill performed")