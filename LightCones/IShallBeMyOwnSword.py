import numpy as np
class IShallBeMyOwnSword: 
    def __init__(self, Object, SuperImpose):
        self.Object = Object
        self.SuperImpose = SuperImpose
        self.Object.BaseStat['기초HP'] += 1164
        self.Object.BaseStat['기초공격력'] += 635
        self.Object.BaseStat['기초방어력'] += 330
        self.Object.BaseStat['전투스킬피해증가'] += [0.3, 0.35, 0.4, 0.45, 0.5][self.SuperImpose-1]
        self.Value1 = [12, 14, 16, 18, 20][self.SuperImpose-1]
        self.Value2 = [0.36, 0.42, 0.48, 0.54, 0.6][self.SuperImpose-1]


    def Active(self, Trigger, Attacker, Target, Value):
        if Trigger == '캐릭터필살기발동시작':
            if Attacker == self.Object:
                self.Object.EnergyGenerate(self.Value1, False)
                self.Object.Game.ApplyBuff(Attacker = self.Object, Target = self.Object, Buff = {'버프형태' : '스탯', '설명': '이몸이검이니치피', '시간타입' : 'A', '체크' : False, '남은턴' : 2, '효과' : [('치명타피해', self.Value2)]}, Except = self)
