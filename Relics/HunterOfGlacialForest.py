class HunterOfGlacialForest:
    def __init__(self, Object, SetCount):
        self.Object = Object
        self.SetCount = SetCount
        if self.SetCount >= 2:
            self.Object.BaseStat['얼음속성피해증가'] += 0.1
        self.Start = False
        
    def Active(self, Trigger, Attacker, Target, Value):
        if self.SetCount >= 4:
            if Trigger == '캐릭터필살기발동시작':
                if Attacker == self.Object:
                    self.Object.Game.ApplyBuff(Attacker = self.Object, Target = self.Object, Buff ={'버프형태' : '스탯', '설명' : '혹한밀림의사냥꾼치피', '시간타입' : 'A', '체크' : False, '남은턴' : 2, '효과' : [('치명타피해', 0.25)]}, Except = self)