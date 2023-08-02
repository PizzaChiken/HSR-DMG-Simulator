class SolitaryHealing: 
    def __init__(self, Object, SuperImpose):
        print('\n\n주의 : 고독의치유는 테섭 기준으로 작성되었음\n\n')
        self.Object = Object
        self.SuperImpose = SuperImpose
        self.Object.BaseStat['기초HP'] += 1058
        self.Object.BaseStat['기초공격력'] += 529
        self.Object.BaseStat['기초방어력'] += 396
        self.Object.BaseStat['격파특수효과'] += [0.2, 0.25, 0.3, 0.35, 0.4][self.SuperImpose-1]
        self.Value1 = [0.24, 0.3, 0.36, 0.42, 0.48][self.SuperImpose-1]
        self.Value2 = [4, 5, 6, 7, 8][self.SuperImpose-1]


    def Active(self, Trigger, Attacker, Target, Value):
        if  Trigger == '캐릭터필살기발동시작':
            if Attacker == self.Object:
                 self.Object.Game.ApplyBuff(Attacker = self.Object, Target = self.Object, Buff ={'버프형태' : '스탯', '설명' : '고독의치유지피증', '시간타입' : 'A', '체크' : False, '남은턴' : 2, '효과' : [('지속피해피해증가', self.Value1)]}, Except = self)
        
        if Trigger == '적사망' or Trigger == '적전원사망':
            check = False
            for debuff in Target[0].DebuffList:
                if debuff['디버프형태'] in ('풍화', '감전', '연소', '열상') :
                    if debuff['공격자']==self.Object:
                        check = True
            if check == True:
                self.Object.EnergyGenerate(self.Value2, False)

