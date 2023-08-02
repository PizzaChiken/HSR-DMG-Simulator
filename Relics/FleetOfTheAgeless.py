class FleetOfTheAgeless:
    def __init__(self, Object, SetCount):
        self.Object = Object
        self.SetCount = SetCount
        if self.SetCount == 2:
            self.Object.BaseStat['HP%증가'] += 0.12
        else:
            raise ValueError
    
    def Active(self, Trigger, Attacker, Target, Value):
        if self.SetCount == 2:
            if Trigger in ('데미지발동시작', '도트데미지발동시작', '격파데미지발동시작', '힐발동시작' , '버프발동시작', '디버프발동시작'):
                if self.Object.CalcSpeed() >= 120:
                    if Attacker in self.Object.Game.Characters:
                        Attacker.TempBuffList.append(('공격력%증가', 0.08))
