class BandOfSizzlingThunder:
    def __init__(self, Object, SetCount):
        self.Object = Object
        self.SetCount = SetCount
        if self.SetCount >= 2:
            self.Object.BaseStat['번개속성피해증가'] += 0.1
        
    def Active(self, Trigger, Attacker, Target, Value):
        if self.SetCount >= 4:
            if Trigger == '캐릭터전투스킬발동시작':
                if Attacker == self.Object:
                    self.Object.Game.ApplyBuff(Attacker = self.Object, Target = self.Object, Buff ={'버프형태' : '스탯', '설명' : '뇌전을울리는밴드공증', '시간타입' : 'A', '체크' : False, '남은턴' : 1, '효과' : [('공격력%증가', 0.2)]}, Except = self)