import numpy as np
class PatienceIsAllYouNeed: 
    def __init__(self, Object, SuperImpose):
        self.Object = Object
        self.SuperImpose = SuperImpose
        self.Object.BaseStat['기초HP'] += 1058
        self.Object.BaseStat['기초공격력'] += 582
        self.Object.BaseStat['기초방어력'] += 463
        self.Object.BaseStat[f'{self.Object.Element}속성피해증가'] += [0.24, 0.28, 0.32, 0.36, 0.4][self.SuperImpose-1]
        self.Value1 = np.array([[0, 0.6, 0], 
                                [0, 0.7, 0], 
                                [0, 0.8, 0], 
                                [0, 0.9, 0], 
                                [0, 1.0, 0]])[self.SuperImpose-1]
        self.Value2 = [0.047, 0.055, 0.063, 0.071, 0.08][self.SuperImpose-1]
        self.Stack = 0
        self.Start = False
        self.Attack = False

    def Active(self, Trigger, Attacker, Target, Value):
        if Trigger in ('캐릭터일반공격발동시작', '캐릭터전투스킬발동시작', '캐릭터필살기발동시작', '캐릭터추가공격발동시작'):
            if Attacker == self.Object:
                self.Start = True

        if Trigger == '데미지발동종료':
            if Attacker.Type == '캐릭터' and Target[0].Type == '적':
                if self.Start == True:
                    if Attacker == self.Object:
                        self.Attack = True
                        if all([Debuff['설명'] != '기다림만필요해흐름' for Debuff in Target[0].DebuffList]):
                            self.Object.Game.ApplyDebuff(Attacker = self.Object, Target = Target[0], BaseProbability = 1.0, Debuff = {'디버프형태' : '감전', '설명' :  f'기다림만필요해흐름', '공격자' : self.Object, '발동타입' : '스킬', '남은턴' : 1, '계수' : self.Value1}, Except = self)
        
        if Trigger in ('캐릭터일반공격발동종료', '캐릭터전투스킬발동종료', '캐릭터필살기발동종료', '캐릭터추가공격발동종료'):
            if self.Start == True:
                if self.Attack == True:
                    self.Stack = min(3, self.Stack + 1)
                    self.Object.Game.ApplyBuff(Attacker = self.Object, Target = self.Object, Buff = {'버프형태' : '스탯', '설명': '기다림만필요해가속', '시간타입' : 'A', '체크' : False, '남은턴' : 1000, '효과' : [('속도%증가', self.Value2 * self.Stack)]}, Except = self)

            self.Start = False
            self.Attack = False