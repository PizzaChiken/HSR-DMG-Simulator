 
class PanGalacticCommercialEnterpriseclass:
    def __init__(self, Object, SetCount):
        self.Object = Object
        self.SetCount = SetCount
        if self.SetCount == 2:
            self.Object.BaseStat['효과명중'] += 0.1
        else:
            raise ValueError
    
    def Active(self, Trigger, Attacker, Target, Value):
        if self.SetCount == 2:
            if Trigger in ('데미지발동시작', '도트데미지발동시작', '격파데미지발동시작', '힐발동시작' , '버프발동시작', '디버프발동시작'):
                if Attacker == self.Object:
                    self.Object.TempBuffList.append(('공격력%증가', min(0.25, self.Object.CurrentStat['효과명중'] * 0.25)))
