class MessengerTraversingHackerSpace:
    def __init__(self, Object, SetCount):
        self.Object = Object
        self.SetCount = SetCount
        if self.SetCount >= 2:
            self.Object.BaseStat['속도%증가'] += 0.06
    
    def Active(self, Trigger, Attacker, Target, Value):
        if self.SetCount >= 4:
            if Trigger == '캐릭터필살기발동종료':
                if Attacker == self.Object:
                    if self.Object.SkillRange['필살기'] in ('아군지정', '아군전체', '자신지정'):
                        for Character in self.Object.Game.Characters.copy():
                            self.Object.Game.ApplyBuff(Attacker = self.Object, Target = Character, Buff ={'버프형태' : '스탯', '설명' : '가상공간을누비는메신저가속', '시간타입' : 'A', '체크' : False, '남은턴' : 1, '효과' : [('속도%증가', 0.12)]}, Except = self)

 