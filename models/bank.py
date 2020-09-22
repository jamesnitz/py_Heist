class Bank:
  def __init__(self, cash_On_Hand, alarm_Score, vault_Score, security_Score):
    self.cash_On_Hand = cash_On_Hand
    self.alarm_Score = alarm_Score
    self.vault_Score = vault_Score
    self.security_Score = security_Score

  @property
  def is_Secure(self):
    if self.alarm_Score <= 0 and self.vault_Score <= 0 and self.security_Score <= 0:
      return False
    else:
      return True