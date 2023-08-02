class WastelanderOfBanditryDesert:
    def __init__(self, Object, SetCount):
        self.Object = Object
        self.SetCount = SetCount
        if self.SetCount >= 2:
            self.Object.BaseStat['허수속성피해증가'] += 0.1
    
    def Active(self, Trigger, Attacker, Target, Value):
        if self.SetCount >= 4:
            if Trigger == '데미지발동시작':
                if Attacker.Type == '캐릭터' and Target[0].Type == '적':
                    if Attacker == self.Object:
                        if len(Target[0].DebuffList) > 0 :
                            self.Object.TempBuffList.append(('치명타확률', 0.1))
                        if any([debuff['디버프형태'] == '속박' for debuff in Target[0].DebuffList]):
                            self.Object.TempBuffList.append(('치명타피해', 0.2))