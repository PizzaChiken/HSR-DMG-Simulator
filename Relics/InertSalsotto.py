class InertSalsotto:
    def __init__(self, Object, SetCount):
        self.Object = Object
        self.SetCount = SetCount
        if self.SetCount == 2:
            self.Object.BaseStat['치명타확률'] += 0.08
        else:
            raise ValueError
    
    def Active(self, Trigger, Attacker, Target, Value):
        if self.SetCount == 2:
            if Trigger == '데미지발동시작':
                if Attacker.Type == '캐릭터' and Target[0].Type == '적':
                    if Attacker == self.Object and Value[0] in ('필살기', '추가공격'):
                        if self.Object.CurrentStat['치명타확률'] >= 0.5:
                            self.Object.TempBuffList.append(('필살기피해증가', 0.15))
                            self.Object.TempBuffList.append(('추가공격피해증가', 0.15))