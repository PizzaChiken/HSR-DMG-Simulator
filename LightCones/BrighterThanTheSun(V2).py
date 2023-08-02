class BrighterThanTheSun: 
    def __init__(self, Object, SuperImpose):
        print('\n\n주의 : 태양보다밝게빛나는것은 테섭 기준으로 작성되었음 (V2) \n\n')
        self.Object = Object
        self.SuperImpose = SuperImpose
        self.Object.BaseStat['기초HP'] += 1058
        self.Object.BaseStat['기초공격력'] += 635
        self.Object.BaseStat['기초방어력'] += 396
        self.Object.BaseStat['치명타확률'] += [0.18, 0.21, 0.24, 0.27, 0.3][self.SuperImpose-1]
        self.Value1 = [0.12, 0.14, 0.16, 0.18, 0.2][self.SuperImpose-1]
        self.Value2 = [0.07, 0.08, 0.09, 0.1, 0.11][self.SuperImpose-1]
        self.Stack = 0


    def Active(self, Trigger, Attacker, Target, Value):
        if Trigger == '캐릭터일반공격발동시작':
            if Attacker == self.Object:
                self.Stack = min(2, self.Stack + 1)
                self.Object.Game.ApplyBuff(Attacker = self.Object, Target = self.Object, Buff ={'버프형태' : '스탯', '설명' : '태양보다밝게빛나는것버프', '시간타입' : 'A', '체크' : False, '남은턴' : 2, '효과' : [('공격력%증가', self.Value1 * self.Stack), ('에너지회복효율', self.Value2 * self.Stack)]}, Except = self)

        if Trigger == '캐릭터턴종료':
            if Attacker == self.Object:
                if not any([buff['설명'] == '태양보다밝게빛나는것버프' for buff in self.Object.BuffList]):
                    self.Stack = 0
