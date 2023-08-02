class ClassList:
    def __init__(self):
        pass

    def GetCharacter(self, Character):
        if Character == '웰트':
            from Characters.Welt import Welt
            return Welt
    
        elif Character == '제레':
            from Characters.Seele import Seele
            return Seele
        
        elif Character == '경원':
            from Characters.JingYuan import JingYuan
            return JingYuan

        elif Character == '백로':
            from Characters.Bailu import Bailu
            return Bailu
        
        elif Character == '브로냐':
            from Characters.Bronya import Bronya
            return Bronya
        
        elif Character == '정운':
            from Characters.Tingyun import Tingyun
            return Tingyun
        
        elif Character == '카프카':
            from Characters.Kafka import Kafka
            return Kafka
        
        elif Character == '은랑':
            from Characters.SilverWolf import SilverWolf
            return SilverWolf
        
        elif Character == '삼포':
            from Characters.Sampo import Sampo
            return Sampo
        
        elif Character == '서벌':
            from Characters.Serval import Serval
            return Serval
        
        elif Character == '루카':
            from Characters.Luka import Luka
            return Luka        
        
        elif Character == '블레이드':
            from Characters.Blade import Blade
            return Blade
        
        elif Character == '나찰':
            from Characters.Luocha import Luocha
            return Luocha
        
        elif Character == '클라라':
            from Characters.Clara import Clara
            return Clara

        elif Character == '단항음월':
            from Characters.DanHengImbibitorLunae import DanHengImbibitorLunae
            return DanHengImbibitorLunae
        
        elif Character == '어공':
            from Characters.Yukong import Yukong
            return Yukong
        
        elif Character == '페라':
            from Characters.Pela import Pela
            return Pela
        
        else:
            raise ValueError
        
    def GetEnemy(self, Enemy):
        if Enemy == '허수아비일반':
            from Enemys.TestEnemyNormal import TestEnemyNormal
            return TestEnemyNormal
        
        elif Enemy == '허수아비정예':
            from Enemys.TestEnemyElite import TestEnemyElite
            return TestEnemyElite
        
        elif Enemy == '허수아비보스':
            from Enemys.TestEnemyBoss import TestEnemyBoss
            return TestEnemyBoss

        else:
            raise ValueError
        
    def GetLightCone(self, LightCone):
        if LightCone == '세계의이름으로':
            from LightCones.InTheNameOfTheWorld import InTheNameOfTheWorld
            return InTheNameOfTheWorld

        elif LightCone == '야경속에서':
            from LightCones.InTheNight import InTheNight
            return InTheNight
        
        elif LightCone == '동트기전':
            from LightCones.BeforeDawn import BeforeDawn
            return BeforeDawn
        
        elif LightCone == '세월은흐를뿐':
            from LightCones.TimeWaitsForNoOne import TimeWaitsForNoOne
            return TimeWaitsForNoOne
        
        elif LightCone == '아직전투는끝나지않았다':
            from LightCones.ButTheBattleIsntOver import ButTheBattleIsntOver
            return ButTheBattleIsntOver
        
        elif LightCone == '기다림만필요해':
            from LightCones.PatienceIsAllYouNeed import PatienceIsAllYouNeed
            return PatienceIsAllYouNeed
        
        elif LightCone == '초보자임무시작전':
            from LightCones.BeforetheTutorialMissionStarts import BeforeTheTutorialMissionStarts
            return BeforeTheTutorialMissionStarts
        
        elif LightCone == '계속내리는비':
            from LightCones.IncessantRain import IncessantRain
            return IncessantRain
        
        elif LightCone == '밤인사와잠든얼굴':
            from LightCones.GoodNightAndSleepWell import GoodNightAndSleepWell
            return GoodNightAndSleepWell

        elif LightCone == '행성과의만남':
            from LightCones.PlanetaryRendezvou import PlanetaryRendezvou
            return PlanetaryRendezvou
        
        elif LightCone == '기억속모습':
            from LightCones.MemoriesOfThePast import MemoriesOfThePast
            return MemoriesOfThePast
        
        elif LightCone == '사냥감의시선':
            from LightCones.EyesOfThePrey import EyesOfThePrey
            return EyesOfThePrey
        
        elif LightCone == '오늘도평화로운하루':
            from LightCones.TodayIsAnotherPeacefulDay import TodayIsAnotherPeacefulDay
            return TodayIsAnotherPeacefulDay
        
        elif LightCone == '연장기호':
            from LightCones.Fermata import Fermata
            return Fermata
        
        elif LightCone == '고독의치유':
            from LightCones.SolitaryHealing import SolitaryHealing
            return SolitaryHealing
        
        elif LightCone == '닿을수없는저편':
            from LightCones.TheUnreachableSide import TheUnreachableSide
            return TheUnreachableSide

        elif LightCone == '어떤에이언즈의몰락':
            from LightCones.OnTheFallOfAnAeon import OnTheFallOfAnAeon
            return OnTheFallOfAnAeon
        
        elif LightCone == '비밀맹세':
            from LightCones.ASecretVow import ASecretVow
            return ASecretVow

        elif LightCone == '대체할수없는것':
            from LightCones.SomethingIrreplaceable import SomethingIrreplaceable
            return SomethingIrreplaceable
        
        elif LightCone == '두더지파가환영해':
            from LightCones.TheMolesWelcomeYou import TheMolesWelcomeYou
            return TheMolesWelcomeYou
        
        elif LightCone == '관의울림':
            from LightCones.EchoesOfTheCoffin import EchoesOfTheCoffin
            return EchoesOfTheCoffin
        
        elif LightCone == '태양보다밝게빛나는것':
            from LightCones.BrighterThanTheSun import BrighterThanTheSun
            return BrighterThanTheSun
        
        elif LightCone == '땀방울처럼빛나는결심':
            from LightCones.ResolutionShinesAsPearlsOfSweat import ResolutionShinesAsPearlsOfSweat
            return ResolutionShinesAsPearlsOfSweat
        else:
            raise ValueError
    
    def GetRelic(self, Relic):
        # 일반 유물
        if Relic == '황무지의도적,황야인':
            from Relics.WastelanderOfBanditryDesert import WastelanderOfBanditryDesert
            return WastelanderOfBanditryDesert
    
        elif Relic == '별처럼빛나는천재':
            from Relics.GeniusOfBrilliantStars import GeniusOfBrilliantStars
            return GeniusOfBrilliantStars
        
        elif Relic == '뇌전을울리는밴드':
            from Relics.BandOfSizzlingThunder import BandOfSizzlingThunder
            return BandOfSizzlingThunder

        elif Relic == '흔적없는손님':
            from Relics.PasserByOfWanderingCloud import PasserByOfWnderingCloud
            return PasserByOfWnderingCloud
        
        elif Relic == '혹한밀림의사냥꾼':
            from Relics.HunterOfGlacialForest import HunterOfGlacialForest
            return HunterOfGlacialForest
        
        elif Relic == '밤낮의경계를나는매':
            from Relics.EagleOfTwilightLine import EagleOfTwilightLine
            return EagleOfTwilightLine
        
        elif Relic == '들이삭과동행하는거너':
            from Relics.MusketeerOfWildWheat import MusketeerOfWildWheat
            return MusketeerOfWildWheat
        
        elif Relic == '스트리트격투왕':
            from Relics.ChampionOfStreetWiseBoxing import ChampionOfStreetWiseBoxing
            return ChampionOfStreetWiseBoxing
        
        elif Relic == '장수를원하는제자':
            from Relics.LongevousDisciple import LongevousDisciple
            return LongevousDisciple
        
        elif Relic == '가상공간을누비는메신저':
            from Relics.MessengerTraversingHackerSpace import MessengerTraversingHackerSpace
            return MessengerTraversingHackerSpace
        
        # 시뮬 유물
        elif Relic == '우주봉인정거장':
            from Relics.SpaceSealingStation import SpaceSealingStation
            return SpaceSealingStation

        elif Relic == '회전을멈춘살소토':
            from Relics.InertSalsotto import InertSalsotto
            return InertSalsotto

        elif Relic == '불로인의선주':
            from Relics.FleetOfTheAgeless import FleetOfTheAgeless
            return FleetOfTheAgeless
        
        elif Relic == '뭇별경기장':
            from Relics.RutilantArena import RutilantArena
            return RutilantArena

        elif Relic == '부러진용골':
            from Relics.BrokenKeel import BrokenKeel
            return BrokenKeel
        
        elif Relic == '범은하상사':
            from Relics.PanGalacticCommercialEnterprise import PanGalacticCommercialEnterpriseclass
            return PanGalacticCommercialEnterpriseclass
        
        elif Relic == '생명의바커공':
            from Relics.SprightlyVonwacq import SprightlyVonwacq
            return SprightlyVonwacq
        
        else:
            raise ValueError
        
class ManageRelic:
    def __init__(self, Character, RelicList):
        # 세트 효과 체크
        SetList = {} 
        for Relic in RelicList:
            if Relic[0] in SetList:
                SetList[Relic[0]] += 1
            else:
                SetList[Relic[0]] = 1
        
        classlist = ClassList()
        # 유물 옵션 추가
        for Relic in RelicList:
            for Option in Relic[1]:
                Character.BaseStat[Option[0]] += Option[1]
        for Set in SetList:
            if SetList[Set] >= 2:
                Character.TriggerList.append(classlist.GetRelic(Set)(Character, SetList[Set]))
