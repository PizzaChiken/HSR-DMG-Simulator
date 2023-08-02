class ButTheBattleIsntOver:
    def __init__(self, Object, SuperImpose):
        self.Object = Object
        self.SuperImpose = SuperImpose
        self.Object.BaseStat['기초HP'] += 1164
        self.Object.BaseStat['기초공격력'] += 529
        self.Object.BaseStat['기초방어력'] += 463
        self.Object.BaseStat['에너지회복효율'] += [0.1, 0.12, 0.14, 0.16, 0.18][self.SuperImpose-1]
        self.Value1 = [0.3, 0.35, 0.4, 0.45, 0.5][self.SuperImpose-1]
        self.Possible = True
        self.Start = False

    def Active(self, Trigger, Attacker, Target, Value):
        if Trigger == '캐릭터필살기발동시작':
            if Attacker == self.Object:
                if Target[0] in self.Object.Game.Characters:
                    if self.Possible == True:
                        self.Object.Game.ChangeSkillPoint(1)
                        self.Possible = False
                    elif self.Possible == False:
                        self.Possible = True
        
        if Trigger == '캐릭터전투스킬발동시작':
            if Attacker == self.Object:
                self.Start = True
        
        if Trigger == '캐릭터턴시작':
            if Attacker in self.Object.Game.Characters:
                if self.Start == True:
                    self.Object.Game.ApplyBuff(Attacker = self.Object, Target = Attacker, Buff = {'버프형태' : '스탯', '설명' : '아직전투는끝나지않았다피증', '시간타입' : 'B', '체크' : False, '남은턴' : 1, '효과' : [(f'모든피해증가', self.Value1)]}, Except = self)
                    self.Start = False


                