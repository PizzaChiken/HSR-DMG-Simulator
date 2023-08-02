class BrokenKeel:
    def __init__(self, Object, SetCount):
        self.Object = Object
        self.SetCount = SetCount
        if self.SetCount == 2:
            self.Object.BaseStat['효과저항'] += 0.1
        else:
            raise ValueError
    
    def Active(self, Trigger, Attacker, Target, Value):
        if self.SetCount == 2:
            if Trigger in ('데미지발동시작', '도트데미지발동시작', '격파데미지발동시작', '힐발동시작' , '버프발동시작', '디버프발동시작'):
                if self.Object.CurrentStat['효과저항'] >= 0.3:
                    if Attacker in self.Object.Game.Characters:
                        Attacker.TempBuffList.append(('치명타피해', 0.1))
