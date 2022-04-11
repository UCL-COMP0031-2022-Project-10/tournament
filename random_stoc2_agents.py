from tournament.action import Action
from tournament.agents.random import ProbabilisticLB2

class Stoc0(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.24555198035154002, (Action.COOPERATE, Action.DEFECT): 0.6689138330233754, (Action.DEFECT, Action.COOPERATE): 0.9094055193691336, (Action.DEFECT, Action.DEFECT): 0.26130955248599574 }


class Stoc1(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.6434809118932705, (Action.COOPERATE, Action.DEFECT): 0.9527022385704482, (Action.DEFECT, Action.COOPERATE): 0.4594417812850451, (Action.DEFECT, Action.DEFECT): 0.004331505318258211 }


class Stoc2(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.03406234655659324, (Action.COOPERATE, Action.DEFECT): 0.40364092588576295, (Action.DEFECT, Action.COOPERATE): 0.03864841874161229, (Action.DEFECT, Action.DEFECT): 0.5635169885547961 }


class Stoc3(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.05797725066432835, (Action.COOPERATE, Action.DEFECT): 0.5307121577458125, (Action.DEFECT, Action.COOPERATE): 0.7134569862560709, (Action.DEFECT, Action.DEFECT): 0.9252681396944807 }


class Stoc4(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.578361877262347, (Action.COOPERATE, Action.DEFECT): 0.2707399172747419, (Action.DEFECT, Action.COOPERATE): 0.21018411337230425, (Action.DEFECT, Action.DEFECT): 0.32773055158260145 }


class Stoc5(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.355583073160022, (Action.COOPERATE, Action.DEFECT): 0.03464048089584881, (Action.DEFECT, Action.COOPERATE): 0.13294725132277496, (Action.DEFECT, Action.DEFECT): 0.38686517934879205 }


class Stoc6(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.29402799576762395, (Action.COOPERATE, Action.DEFECT): 0.003994859666313966, (Action.DEFECT, Action.COOPERATE): 0.7301750343209867, (Action.DEFECT, Action.DEFECT): 0.415405565937195 }


class Stoc7(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.9540068344357912, (Action.COOPERATE, Action.DEFECT): 0.7306629776087092, (Action.DEFECT, Action.COOPERATE): 0.2377325920387554, (Action.DEFECT, Action.DEFECT): 0.9624160929519162 }


class Stoc8(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.21997562090745038, (Action.COOPERATE, Action.DEFECT): 0.6255389579965568, (Action.DEFECT, Action.COOPERATE): 0.42137057855740634, (Action.DEFECT, Action.DEFECT): 0.12533079720298923 }


class Stoc9(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.903611483606926, (Action.COOPERATE, Action.DEFECT): 0.033189560653139716, (Action.DEFECT, Action.COOPERATE): 0.0060233543179002424, (Action.DEFECT, Action.DEFECT): 0.310862203708019 }


class Stoc10(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.13946570835704009, (Action.COOPERATE, Action.DEFECT): 0.1003919881646822, (Action.DEFECT, Action.COOPERATE): 0.564091687922157, (Action.DEFECT, Action.DEFECT): 0.2532799253068492 }


class Stoc11(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.46012691814910367, (Action.COOPERATE, Action.DEFECT): 0.1093300250990209, (Action.DEFECT, Action.COOPERATE): 0.92591398315716, (Action.DEFECT, Action.DEFECT): 0.02200221654825163 }


class Stoc12(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.7210984036536764, (Action.COOPERATE, Action.DEFECT): 0.04159367129228875, (Action.DEFECT, Action.COOPERATE): 0.48738141714211114, (Action.DEFECT, Action.DEFECT): 0.21732437233698443 }


class Stoc13(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.24431746948820543, (Action.COOPERATE, Action.DEFECT): 0.7753693144337314, (Action.DEFECT, Action.COOPERATE): 0.5996557759291836, (Action.DEFECT, Action.DEFECT): 0.45523512711674174 }


class Stoc14(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.9119542583670177, (Action.COOPERATE, Action.DEFECT): 0.6197116293034924, (Action.DEFECT, Action.COOPERATE): 0.29428007778197474, (Action.DEFECT, Action.DEFECT): 0.9802404369373245 }


class Stoc15(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.7482550796979737, (Action.COOPERATE, Action.DEFECT): 0.6822703719120007, (Action.DEFECT, Action.COOPERATE): 0.3131164676286381, (Action.DEFECT, Action.DEFECT): 0.3770904870628461 }


class Stoc16(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.9045280532988547, (Action.COOPERATE, Action.DEFECT): 0.8096633200881911, (Action.DEFECT, Action.COOPERATE): 0.0329491735247468, (Action.DEFECT, Action.DEFECT): 0.21514082033903226 }


class Stoc17(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.22973350689937877, (Action.COOPERATE, Action.DEFECT): 0.5323738423256549, (Action.DEFECT, Action.COOPERATE): 0.5342008277943291, (Action.DEFECT, Action.DEFECT): 0.3351262690918504 }


class Stoc18(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.29813063482557967, (Action.COOPERATE, Action.DEFECT): 0.3550600527976512, (Action.DEFECT, Action.COOPERATE): 0.6467637770765942, (Action.DEFECT, Action.DEFECT): 0.4720672526217117 }


class Stoc19(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.2787675885661589, (Action.COOPERATE, Action.DEFECT): 0.5668150353632064, (Action.DEFECT, Action.COOPERATE): 0.6574833922443439, (Action.DEFECT, Action.DEFECT): 0.0005273566626349258 }


class Stoc20(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.9679316532422065, (Action.COOPERATE, Action.DEFECT): 0.9930375636577186, (Action.DEFECT, Action.COOPERATE): 0.508908544595752, (Action.DEFECT, Action.DEFECT): 0.18337707610547804 }


class Stoc21(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.9146778714341666, (Action.COOPERATE, Action.DEFECT): 0.5257068926711905, (Action.DEFECT, Action.COOPERATE): 0.25068730477553114, (Action.DEFECT, Action.DEFECT): 0.26720943365278893 }


class Stoc22(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.10563578834193421, (Action.COOPERATE, Action.DEFECT): 0.6552914430171511, (Action.DEFECT, Action.COOPERATE): 0.5405886829639728, (Action.DEFECT, Action.DEFECT): 0.6994235056704322 }


class Stoc23(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.6266350618090202, (Action.COOPERATE, Action.DEFECT): 0.5667493019611046, (Action.DEFECT, Action.COOPERATE): 0.2235584188304428, (Action.DEFECT, Action.DEFECT): 0.04302550020449436 }


class Stoc24(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.8854261680432118, (Action.COOPERATE, Action.DEFECT): 0.03276925187105484, (Action.DEFECT, Action.COOPERATE): 0.7424817802270463, (Action.DEFECT, Action.DEFECT): 0.6432927700742592 }


class Stoc25(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.7033976953544395, (Action.COOPERATE, Action.DEFECT): 0.41219111130440644, (Action.DEFECT, Action.COOPERATE): 0.3246590337540034, (Action.DEFECT, Action.DEFECT): 0.6793043983318916 }


class Stoc26(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.9350139026527069, (Action.COOPERATE, Action.DEFECT): 0.0622941374882644, (Action.DEFECT, Action.COOPERATE): 0.4032650647948375, (Action.DEFECT, Action.DEFECT): 0.6528574613331762 }


class Stoc27(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.9457382844992196, (Action.COOPERATE, Action.DEFECT): 0.040690510403396996, (Action.DEFECT, Action.COOPERATE): 0.8381773133724917, (Action.DEFECT, Action.DEFECT): 0.25373931111705894 }


class Stoc28(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.8603215859547623, (Action.COOPERATE, Action.DEFECT): 0.8706839095352594, (Action.DEFECT, Action.COOPERATE): 0.9358367770107265, (Action.DEFECT, Action.DEFECT): 0.6230039665217292 }


class Stoc29(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.8257129349535292, (Action.COOPERATE, Action.DEFECT): 0.8338080477154006, (Action.DEFECT, Action.COOPERATE): 0.2222822430104101, (Action.DEFECT, Action.DEFECT): 0.6256851051822283 }


class Stoc30(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.4705018311846747, (Action.COOPERATE, Action.DEFECT): 0.2042185075676568, (Action.DEFECT, Action.COOPERATE): 0.5333814648418512, (Action.DEFECT, Action.DEFECT): 0.4230164751406347 }


class Stoc31(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.3524969099296412, (Action.COOPERATE, Action.DEFECT): 0.3283173237972332, (Action.DEFECT, Action.COOPERATE): 0.21880109250886182, (Action.DEFECT, Action.DEFECT): 0.09525980439984238 }


class Stoc32(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5204467471797322, (Action.COOPERATE, Action.DEFECT): 0.15814559115536242, (Action.DEFECT, Action.COOPERATE): 0.2465953301742202, (Action.DEFECT, Action.DEFECT): 0.12354871444121518 }


class Stoc33(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.9569120568827945, (Action.COOPERATE, Action.DEFECT): 0.755386614118337, (Action.DEFECT, Action.COOPERATE): 0.09030046109880807, (Action.DEFECT, Action.DEFECT): 0.5049902359937181 }


class Stoc34(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.7725885995200135, (Action.COOPERATE, Action.DEFECT): 0.2942030179660712, (Action.DEFECT, Action.COOPERATE): 0.6464225645710301, (Action.DEFECT, Action.DEFECT): 0.589104306261808 }


class Stoc35(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.998421517890145, (Action.COOPERATE, Action.DEFECT): 0.33589949241113803, (Action.DEFECT, Action.COOPERATE): 0.7705577792876779, (Action.DEFECT, Action.DEFECT): 0.32455641466431595 }


class Stoc36(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.3930464700799473, (Action.COOPERATE, Action.DEFECT): 0.9624769353904528, (Action.DEFECT, Action.COOPERATE): 0.5009682830230255, (Action.DEFECT, Action.DEFECT): 0.009012082955532796 }


class Stoc37(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.08332593384227427, (Action.COOPERATE, Action.DEFECT): 0.047817006187663824, (Action.DEFECT, Action.COOPERATE): 0.9083031264915898, (Action.DEFECT, Action.DEFECT): 0.48506213964817924 }


class Stoc38(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.32858566204396966, (Action.COOPERATE, Action.DEFECT): 0.30640947740278335, (Action.DEFECT, Action.COOPERATE): 0.3680213322513205, (Action.DEFECT, Action.DEFECT): 0.2679709667289121 }


class Stoc39(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.455282791595386, (Action.COOPERATE, Action.DEFECT): 0.2879060335889292, (Action.DEFECT, Action.COOPERATE): 0.5100577228660369, (Action.DEFECT, Action.DEFECT): 0.7893714246141885 }


class Stoc40(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.4666177727031854, (Action.COOPERATE, Action.DEFECT): 0.668142804673361, (Action.DEFECT, Action.COOPERATE): 0.14503415612031167, (Action.DEFECT, Action.DEFECT): 0.06677940338412736 }


class Stoc41(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.28270098570757196, (Action.COOPERATE, Action.DEFECT): 0.21692450137764585, (Action.DEFECT, Action.COOPERATE): 0.10984081322712258, (Action.DEFECT, Action.DEFECT): 0.09868381179576224 }


class Stoc42(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.2831276262801, (Action.COOPERATE, Action.DEFECT): 0.15197776342005542, (Action.DEFECT, Action.COOPERATE): 0.9714354707077721, (Action.DEFECT, Action.DEFECT): 0.1271990348346702 }


class Stoc43(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.6101396970883693, (Action.COOPERATE, Action.DEFECT): 0.47015455624417735, (Action.DEFECT, Action.COOPERATE): 0.12183085209582922, (Action.DEFECT, Action.DEFECT): 0.2429038354223253 }


class Stoc44(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.52700294410562, (Action.COOPERATE, Action.DEFECT): 0.9458075820588094, (Action.DEFECT, Action.COOPERATE): 0.5363985311380839, (Action.DEFECT, Action.DEFECT): 0.21841106219891304 }


class Stoc45(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.6985148610825832, (Action.COOPERATE, Action.DEFECT): 0.7349827916584952, (Action.DEFECT, Action.COOPERATE): 0.24558833102197208, (Action.DEFECT, Action.DEFECT): 0.691311294448296 }


class Stoc46(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.888296962984728, (Action.COOPERATE, Action.DEFECT): 0.620161513939621, (Action.DEFECT, Action.COOPERATE): 0.71623030181864, (Action.DEFECT, Action.DEFECT): 0.37645868570494667 }


class Stoc47(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.761611703269811, (Action.COOPERATE, Action.DEFECT): 0.6684942114208136, (Action.DEFECT, Action.COOPERATE): 0.5208796156769303, (Action.DEFECT, Action.DEFECT): 0.4072758202080774 }


class Stoc48(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.46204325743075614, (Action.COOPERATE, Action.DEFECT): 0.5233700221577949, (Action.DEFECT, Action.COOPERATE): 0.6042599402233563, (Action.DEFECT, Action.DEFECT): 0.8552189650770854 }


class Stoc49(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.8485980677378232, (Action.COOPERATE, Action.DEFECT): 0.5610300245915624, (Action.DEFECT, Action.COOPERATE): 0.3218067961275354, (Action.DEFECT, Action.DEFECT): 0.877755304696451 }


class Stoc50(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.45032481511449596, (Action.COOPERATE, Action.DEFECT): 0.35438052626254046, (Action.DEFECT, Action.COOPERATE): 0.8752428696632496, (Action.DEFECT, Action.DEFECT): 0.021734179509899754 }


class Stoc51(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5742697310681144, (Action.COOPERATE, Action.DEFECT): 0.1758458728708655, (Action.DEFECT, Action.COOPERATE): 0.08338419690705712, (Action.DEFECT, Action.DEFECT): 0.08595017427565033 }


class Stoc52(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.22544259762043906, (Action.COOPERATE, Action.DEFECT): 0.9470792416398783, (Action.DEFECT, Action.COOPERATE): 0.7417116707975098, (Action.DEFECT, Action.DEFECT): 0.5512967447548568 }


class Stoc53(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.9290565256945246, (Action.COOPERATE, Action.DEFECT): 0.6080203515801893, (Action.DEFECT, Action.COOPERATE): 0.48917885696282026, (Action.DEFECT, Action.DEFECT): 0.9230389474482616 }


class Stoc54(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.7616095868245583, (Action.COOPERATE, Action.DEFECT): 0.7518457463334428, (Action.DEFECT, Action.COOPERATE): 0.26136501962562264, (Action.DEFECT, Action.DEFECT): 0.4590547213448767 }


class Stoc55(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.8480192443027368, (Action.COOPERATE, Action.DEFECT): 0.5964688637229312, (Action.DEFECT, Action.COOPERATE): 0.4053258091924601, (Action.DEFECT, Action.DEFECT): 0.30808567680480015 }


class Stoc56(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.6574685801392158, (Action.COOPERATE, Action.DEFECT): 0.3887776067219135, (Action.DEFECT, Action.COOPERATE): 0.474348640384304, (Action.DEFECT, Action.DEFECT): 0.0963810597348187 }


class Stoc57(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.39790764330759754, (Action.COOPERATE, Action.DEFECT): 0.9707582923072421, (Action.DEFECT, Action.COOPERATE): 0.8150401649943101, (Action.DEFECT, Action.DEFECT): 0.9690663943897644 }


class Stoc58(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.8606451136990755, (Action.COOPERATE, Action.DEFECT): 0.4065841471838426, (Action.DEFECT, Action.COOPERATE): 0.7660951546614193, (Action.DEFECT, Action.DEFECT): 0.08027858227601925 }


class Stoc59(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.08849179743877933, (Action.COOPERATE, Action.DEFECT): 0.18799045681181425, (Action.DEFECT, Action.COOPERATE): 0.6716235343100901, (Action.DEFECT, Action.DEFECT): 0.7761108229345605 }


class Stoc60(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.1652267437825442, (Action.COOPERATE, Action.DEFECT): 0.02199318055373678, (Action.DEFECT, Action.COOPERATE): 0.5431307338682256, (Action.DEFECT, Action.DEFECT): 0.526288589836196 }


class Stoc61(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.8603920197575516, (Action.COOPERATE, Action.DEFECT): 0.49744627715146605, (Action.DEFECT, Action.COOPERATE): 0.8620255101454486, (Action.DEFECT, Action.DEFECT): 0.879992838545905 }


class Stoc62(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.4202546255697366, (Action.COOPERATE, Action.DEFECT): 0.2552400973430141, (Action.DEFECT, Action.COOPERATE): 0.6368888228242873, (Action.DEFECT, Action.DEFECT): 0.7247690332568114 }


class Stoc63(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5539963451834998, (Action.COOPERATE, Action.DEFECT): 0.31147507733657276, (Action.DEFECT, Action.COOPERATE): 0.45136662205912903, (Action.DEFECT, Action.DEFECT): 0.5470007493085689 }


class Stoc64(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.8210496084223728, (Action.COOPERATE, Action.DEFECT): 0.0007243756413928271, (Action.DEFECT, Action.COOPERATE): 0.48732422002585474, (Action.DEFECT, Action.DEFECT): 0.8381320457223569 }


class Stoc65(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.7412765739435052, (Action.COOPERATE, Action.DEFECT): 0.31820285002725934, (Action.DEFECT, Action.COOPERATE): 0.7893451466533873, (Action.DEFECT, Action.DEFECT): 0.43747457425706415 }


class Stoc66(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.8982638637506498, (Action.COOPERATE, Action.DEFECT): 0.826342935318325, (Action.DEFECT, Action.COOPERATE): 0.36129268813842197, (Action.DEFECT, Action.DEFECT): 0.7811082049686151 }


class Stoc67(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.9793152085314719, (Action.COOPERATE, Action.DEFECT): 0.9982479167661823, (Action.DEFECT, Action.COOPERATE): 0.23868511139713966, (Action.DEFECT, Action.DEFECT): 0.7876874885387257 }


class Stoc68(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.20956368164674588, (Action.COOPERATE, Action.DEFECT): 0.8932628242857878, (Action.DEFECT, Action.COOPERATE): 0.9791768495917936, (Action.DEFECT, Action.DEFECT): 0.4642159819293644 }


class Stoc69(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.13119050769633034, (Action.COOPERATE, Action.DEFECT): 0.46330350743150783, (Action.DEFECT, Action.COOPERATE): 0.6874467778511003, (Action.DEFECT, Action.DEFECT): 0.9781088264663822 }


class Stoc70(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.4850994150342869, (Action.COOPERATE, Action.DEFECT): 0.014022033113094912, (Action.DEFECT, Action.COOPERATE): 0.40797306115276655, (Action.DEFECT, Action.DEFECT): 0.4479338750062186 }


class Stoc71(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.2613690538526825, (Action.COOPERATE, Action.DEFECT): 0.44371536982328275, (Action.DEFECT, Action.COOPERATE): 0.9342334643642877, (Action.DEFECT, Action.DEFECT): 0.6310258899146641 }


class Stoc72(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.06138986700229099, (Action.COOPERATE, Action.DEFECT): 0.4547348577840884, (Action.DEFECT, Action.COOPERATE): 0.033194304208610914, (Action.DEFECT, Action.DEFECT): 0.3728878938586636 }


class Stoc73(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.08965954269461607, (Action.COOPERATE, Action.DEFECT): 0.6020345904184227, (Action.DEFECT, Action.COOPERATE): 0.010021742583354087, (Action.DEFECT, Action.DEFECT): 0.15346998283316104 }


class Stoc74(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5404863517193383, (Action.COOPERATE, Action.DEFECT): 0.6507302859086906, (Action.DEFECT, Action.COOPERATE): 0.9195997782822396, (Action.DEFECT, Action.DEFECT): 0.9186678080805907 }


class Stoc75(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.17700235488750016, (Action.COOPERATE, Action.DEFECT): 0.941150134051194, (Action.DEFECT, Action.COOPERATE): 0.32151063854825346, (Action.DEFECT, Action.DEFECT): 0.8229106174156999 }


class Stoc76(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.9724340883834263, (Action.COOPERATE, Action.DEFECT): 0.10641730761256396, (Action.DEFECT, Action.COOPERATE): 0.4025965854270537, (Action.DEFECT, Action.DEFECT): 0.5835175588024558 }


class Stoc77(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.48101050395335454, (Action.COOPERATE, Action.DEFECT): 0.6275258919947833, (Action.DEFECT, Action.COOPERATE): 0.5335027400326287, (Action.DEFECT, Action.DEFECT): 0.007416238260647412 }


class Stoc78(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.6941799391087348, (Action.COOPERATE, Action.DEFECT): 0.8329487710050248, (Action.DEFECT, Action.COOPERATE): 0.867052997209027, (Action.DEFECT, Action.DEFECT): 0.9599833553606051 }


class Stoc79(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.6667026283983063, (Action.COOPERATE, Action.DEFECT): 0.8950050891063462, (Action.DEFECT, Action.COOPERATE): 0.6848441407360306, (Action.DEFECT, Action.DEFECT): 0.6934232643844787 }


class Stoc80(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5625024220216499, (Action.COOPERATE, Action.DEFECT): 0.44566089406985676, (Action.DEFECT, Action.COOPERATE): 0.8617108533403153, (Action.DEFECT, Action.DEFECT): 0.9245515668862584 }


class Stoc81(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.8377607199272427, (Action.COOPERATE, Action.DEFECT): 0.906335596345318, (Action.DEFECT, Action.COOPERATE): 0.7578220268847189, (Action.DEFECT, Action.DEFECT): 0.26128322928238257 }


class Stoc82(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.044250223871733274, (Action.COOPERATE, Action.DEFECT): 0.23032458047848747, (Action.DEFECT, Action.COOPERATE): 0.8026008150554612, (Action.DEFECT, Action.DEFECT): 0.3253588813038871 }


class Stoc83(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.6216074287837501, (Action.COOPERATE, Action.DEFECT): 0.6232057506849089, (Action.DEFECT, Action.COOPERATE): 0.930173517142538, (Action.DEFECT, Action.DEFECT): 0.11821267225882826 }


class Stoc84(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.1429556943569792, (Action.COOPERATE, Action.DEFECT): 0.5236731069862467, (Action.DEFECT, Action.COOPERATE): 0.692594365840037, (Action.DEFECT, Action.DEFECT): 0.2664474646632745 }


class Stoc85(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.36727564379553534, (Action.COOPERATE, Action.DEFECT): 0.380976441008509, (Action.DEFECT, Action.COOPERATE): 0.022151761769413802, (Action.DEFECT, Action.DEFECT): 0.7946840386196782 }


class Stoc86(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.8206420190406282, (Action.COOPERATE, Action.DEFECT): 0.29263438196095226, (Action.DEFECT, Action.COOPERATE): 0.32744789844056366, (Action.DEFECT, Action.DEFECT): 0.7407314735557265 }


class Stoc87(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.9213636968475741, (Action.COOPERATE, Action.DEFECT): 0.8487602207415373, (Action.DEFECT, Action.COOPERATE): 0.011744437236327121, (Action.DEFECT, Action.DEFECT): 0.3420233714797697 }


class Stoc88(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.12438712773272032, (Action.COOPERATE, Action.DEFECT): 0.13872288045133863, (Action.DEFECT, Action.COOPERATE): 0.3657736454669219, (Action.DEFECT, Action.DEFECT): 0.4166744164238593 }


class Stoc89(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.9412655490280184, (Action.COOPERATE, Action.DEFECT): 0.1859541749966459, (Action.DEFECT, Action.COOPERATE): 0.2249207331697861, (Action.DEFECT, Action.DEFECT): 0.8056605302166695 }


class Stoc90(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.18007313892418852, (Action.COOPERATE, Action.DEFECT): 0.20078654985131716, (Action.DEFECT, Action.COOPERATE): 0.01737491515027423, (Action.DEFECT, Action.DEFECT): 0.1958751188998772 }


class Stoc91(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.6611545067564258, (Action.COOPERATE, Action.DEFECT): 0.2636807453387776, (Action.DEFECT, Action.COOPERATE): 0.6314694453733073, (Action.DEFECT, Action.DEFECT): 0.34553892202934056 }


class Stoc92(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.19868222705844396, (Action.COOPERATE, Action.DEFECT): 0.06966477198406429, (Action.DEFECT, Action.COOPERATE): 0.5217293408075796, (Action.DEFECT, Action.DEFECT): 0.21117929346947018 }


class Stoc93(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.7277110254361271, (Action.COOPERATE, Action.DEFECT): 0.8212514027659039, (Action.DEFECT, Action.COOPERATE): 0.9245124817112804, (Action.DEFECT, Action.DEFECT): 0.7933399782270586 }


class Stoc94(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.8083994527542947, (Action.COOPERATE, Action.DEFECT): 0.2190750858386843, (Action.DEFECT, Action.COOPERATE): 0.9614236608903135, (Action.DEFECT, Action.DEFECT): 0.8932276386239763 }


class Stoc95(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.6287030125974655, (Action.COOPERATE, Action.DEFECT): 0.7358220902603789, (Action.DEFECT, Action.COOPERATE): 0.04888373978368499, (Action.DEFECT, Action.DEFECT): 0.3753361982930794 }


class Stoc96(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.3275827035947557, (Action.COOPERATE, Action.DEFECT): 0.03326648571474489, (Action.DEFECT, Action.COOPERATE): 0.6231457451756053, (Action.DEFECT, Action.DEFECT): 0.011586689481839496 }


class Stoc97(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.8338694002144922, (Action.COOPERATE, Action.DEFECT): 0.873776986457856, (Action.DEFECT, Action.COOPERATE): 0.9860323852584378, (Action.DEFECT, Action.DEFECT): 0.08101035719960814 }


class Stoc98(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.4585822967349379, (Action.COOPERATE, Action.DEFECT): 0.2069885131459751, (Action.DEFECT, Action.COOPERATE): 0.4355432038729018, (Action.DEFECT, Action.DEFECT): 0.7488323313518882 }


class Stoc99(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.9206100218211557, (Action.COOPERATE, Action.DEFECT): 0.5808919405725447, (Action.DEFECT, Action.COOPERATE): 0.32376037518564826, (Action.DEFECT, Action.DEFECT): 0.6307184167814762 }


class Stoc100(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.857417003298197, (Action.COOPERATE, Action.DEFECT): 0.9169736644826626, (Action.DEFECT, Action.COOPERATE): 0.5433534160801399, (Action.DEFECT, Action.DEFECT): 0.8316353443638754 }


class Stoc101(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.39568817154131997, (Action.COOPERATE, Action.DEFECT): 0.6299365254457299, (Action.DEFECT, Action.COOPERATE): 0.9811784628550668, (Action.DEFECT, Action.DEFECT): 0.9778870007791512 }


class Stoc102(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.3170815290337856, (Action.COOPERATE, Action.DEFECT): 0.6542937168890385, (Action.DEFECT, Action.COOPERATE): 0.08108127446919333, (Action.DEFECT, Action.DEFECT): 0.8880561820076129 }


class Stoc103(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.8453601028078177, (Action.COOPERATE, Action.DEFECT): 0.8747665651166718, (Action.DEFECT, Action.COOPERATE): 0.9149641554119852, (Action.DEFECT, Action.DEFECT): 0.41543662537248693 }


class Stoc104(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.3999591732296698, (Action.COOPERATE, Action.DEFECT): 0.44881999648393167, (Action.DEFECT, Action.COOPERATE): 0.11721966146508467, (Action.DEFECT, Action.DEFECT): 0.040151965202402495 }


class Stoc105(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.710084567117013, (Action.COOPERATE, Action.DEFECT): 0.22816310460768718, (Action.DEFECT, Action.COOPERATE): 0.009726591679690921, (Action.DEFECT, Action.DEFECT): 0.7495575776144153 }


class Stoc106(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5865543424564661, (Action.COOPERATE, Action.DEFECT): 0.5623967658105353, (Action.DEFECT, Action.COOPERATE): 0.29747318060162364, (Action.DEFECT, Action.DEFECT): 0.6449246302534148 }


class Stoc107(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.4831442234736374, (Action.COOPERATE, Action.DEFECT): 0.6677024300024682, (Action.DEFECT, Action.COOPERATE): 0.06102521993825527, (Action.DEFECT, Action.DEFECT): 0.944240095404506 }


class Stoc108(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.4502156817126769, (Action.COOPERATE, Action.DEFECT): 0.8918708977836246, (Action.DEFECT, Action.COOPERATE): 0.06683948076441149, (Action.DEFECT, Action.DEFECT): 0.9009348640704858 }


class Stoc109(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.7544402625638046, (Action.COOPERATE, Action.DEFECT): 0.15078175813339056, (Action.DEFECT, Action.COOPERATE): 0.7614331758178212, (Action.DEFECT, Action.DEFECT): 0.5121379173349055 }


class Stoc110(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.568253607501865, (Action.COOPERATE, Action.DEFECT): 0.46618846353117394, (Action.DEFECT, Action.COOPERATE): 0.22345804617271847, (Action.DEFECT, Action.DEFECT): 0.6041274700478134 }


class Stoc111(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.18949091301702214, (Action.COOPERATE, Action.DEFECT): 0.3304747586785187, (Action.DEFECT, Action.COOPERATE): 0.6147737370744301, (Action.DEFECT, Action.DEFECT): 0.5960215204542911 }


class Stoc112(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.3819695216600637, (Action.COOPERATE, Action.DEFECT): 0.3670837376546403, (Action.DEFECT, Action.COOPERATE): 0.8418837219258939, (Action.DEFECT, Action.DEFECT): 0.15507098777180395 }


class Stoc113(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.18058557889871074, (Action.COOPERATE, Action.DEFECT): 0.018925345077290268, (Action.DEFECT, Action.COOPERATE): 0.8399197401856718, (Action.DEFECT, Action.DEFECT): 0.0757137549003124 }


class Stoc114(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5823611797274225, (Action.COOPERATE, Action.DEFECT): 0.6684420510600094, (Action.DEFECT, Action.COOPERATE): 0.6714515315148842, (Action.DEFECT, Action.DEFECT): 0.19818035261517863 }


class Stoc115(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.255684949996981, (Action.COOPERATE, Action.DEFECT): 0.30779247631649087, (Action.DEFECT, Action.COOPERATE): 0.8747931250788279, (Action.DEFECT, Action.DEFECT): 0.028300569841126832 }


class Stoc116(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.7713410796947855, (Action.COOPERATE, Action.DEFECT): 0.2480438790523375, (Action.DEFECT, Action.COOPERATE): 0.21555589917466345, (Action.DEFECT, Action.DEFECT): 0.38960130566170625 }


class Stoc117(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.7699172848758024, (Action.COOPERATE, Action.DEFECT): 0.7883022542146874, (Action.DEFECT, Action.COOPERATE): 0.08046702834705632, (Action.DEFECT, Action.DEFECT): 0.12156842951193503 }


class Stoc118(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.8562782096067278, (Action.COOPERATE, Action.DEFECT): 0.20133181948518053, (Action.DEFECT, Action.COOPERATE): 0.1856740721992125, (Action.DEFECT, Action.DEFECT): 0.07113972289227022 }


class Stoc119(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.8917572989987822, (Action.COOPERATE, Action.DEFECT): 0.7037151520314388, (Action.DEFECT, Action.COOPERATE): 0.026362169207947983, (Action.DEFECT, Action.DEFECT): 0.4717798848468999 }


class Stoc120(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.7246807510034585, (Action.COOPERATE, Action.DEFECT): 0.8695417757875359, (Action.DEFECT, Action.COOPERATE): 0.886076235850941, (Action.DEFECT, Action.DEFECT): 0.09129232006287602 }


class Stoc121(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.16562185096164206, (Action.COOPERATE, Action.DEFECT): 0.06241388285890426, (Action.DEFECT, Action.COOPERATE): 0.5503116520678242, (Action.DEFECT, Action.DEFECT): 0.48955540513459306 }


class Stoc122(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.34805163884259505, (Action.COOPERATE, Action.DEFECT): 0.03636154522417101, (Action.DEFECT, Action.COOPERATE): 0.017524183409411753, (Action.DEFECT, Action.DEFECT): 0.7948846024112134 }


class Stoc123(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.6004205152088871, (Action.COOPERATE, Action.DEFECT): 0.1357097063898095, (Action.DEFECT, Action.COOPERATE): 0.333941249575998, (Action.DEFECT, Action.DEFECT): 0.9366937011819967 }


class Stoc124(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.07735025370694637, (Action.COOPERATE, Action.DEFECT): 0.08835684289764989, (Action.DEFECT, Action.COOPERATE): 0.9872878977895552, (Action.DEFECT, Action.DEFECT): 0.1612923971310667 }


class Stoc125(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.813595754050417, (Action.COOPERATE, Action.DEFECT): 0.162837137945831, (Action.DEFECT, Action.COOPERATE): 0.5622397512730358, (Action.DEFECT, Action.DEFECT): 0.1554522119942342 }


class Stoc126(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.7299030822648505, (Action.COOPERATE, Action.DEFECT): 0.2162177006036512, (Action.DEFECT, Action.COOPERATE): 0.6752197932387793, (Action.DEFECT, Action.DEFECT): 0.029597965318688302 }


class Stoc127(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.6814276352817246, (Action.COOPERATE, Action.DEFECT): 0.5813269663863203, (Action.DEFECT, Action.COOPERATE): 0.20112351407066353, (Action.DEFECT, Action.DEFECT): 0.8119993233278858 }


class Stoc128(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.1975957545171726, (Action.COOPERATE, Action.DEFECT): 0.9767304907184792, (Action.DEFECT, Action.COOPERATE): 0.09734123802572114, (Action.DEFECT, Action.DEFECT): 0.06721022978025049 }


class Stoc129(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.8047060844235847, (Action.COOPERATE, Action.DEFECT): 0.9224275075508597, (Action.DEFECT, Action.COOPERATE): 0.447027724949144, (Action.DEFECT, Action.DEFECT): 0.004114235063378158 }


class Stoc130(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.4620231893541895, (Action.COOPERATE, Action.DEFECT): 0.37931195120490335, (Action.DEFECT, Action.COOPERATE): 0.6095141841915002, (Action.DEFECT, Action.DEFECT): 0.9924938949420099 }


class Stoc131(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5587843700143265, (Action.COOPERATE, Action.DEFECT): 0.40346964967771626, (Action.DEFECT, Action.COOPERATE): 0.952421642990698, (Action.DEFECT, Action.DEFECT): 0.7479571830106763 }


class Stoc132(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.12870960133470433, (Action.COOPERATE, Action.DEFECT): 0.002725358852181281, (Action.DEFECT, Action.COOPERATE): 0.9985492501090197, (Action.DEFECT, Action.DEFECT): 0.4836731638988423 }


class Stoc133(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.3408839393487577, (Action.COOPERATE, Action.DEFECT): 0.9258924822901351, (Action.DEFECT, Action.COOPERATE): 0.2576199133033472, (Action.DEFECT, Action.DEFECT): 0.5866478127995369 }


class Stoc134(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.20539881315504538, (Action.COOPERATE, Action.DEFECT): 0.7457360320137859, (Action.DEFECT, Action.COOPERATE): 0.9922457588562231, (Action.DEFECT, Action.DEFECT): 0.6883327430219893 }


class Stoc135(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.14656433761597665, (Action.COOPERATE, Action.DEFECT): 0.1453280999804406, (Action.DEFECT, Action.COOPERATE): 0.41766901989628147, (Action.DEFECT, Action.DEFECT): 0.31563274772924665 }


class Stoc136(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.419990086202647, (Action.COOPERATE, Action.DEFECT): 0.9347940659517722, (Action.DEFECT, Action.COOPERATE): 0.2571536872517497, (Action.DEFECT, Action.DEFECT): 0.9060609883403954 }


class Stoc137(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.9303511121296902, (Action.COOPERATE, Action.DEFECT): 0.25654793008625776, (Action.DEFECT, Action.COOPERATE): 0.9959304618461974, (Action.DEFECT, Action.DEFECT): 0.14328013835048703 }


class Stoc138(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.1550929736480735, (Action.COOPERATE, Action.DEFECT): 0.5191358491140482, (Action.DEFECT, Action.COOPERATE): 0.9672262541727852, (Action.DEFECT, Action.DEFECT): 0.42286488220333585 }


class Stoc139(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.1891113877842061, (Action.COOPERATE, Action.DEFECT): 0.34780644827675156, (Action.DEFECT, Action.COOPERATE): 0.24402046589477855, (Action.DEFECT, Action.DEFECT): 0.08506496102539074 }


class Stoc140(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.632138682525744, (Action.COOPERATE, Action.DEFECT): 0.2901040819982701, (Action.DEFECT, Action.COOPERATE): 0.7773287442197415, (Action.DEFECT, Action.DEFECT): 0.5043744284592299 }


class Stoc141(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.2091471831760925, (Action.COOPERATE, Action.DEFECT): 0.5399307176624998, (Action.DEFECT, Action.COOPERATE): 0.7802845493476444, (Action.DEFECT, Action.DEFECT): 0.23467945579798455 }


class Stoc142(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5577926325857906, (Action.COOPERATE, Action.DEFECT): 0.13852233984689943, (Action.DEFECT, Action.COOPERATE): 0.4308243683351204, (Action.DEFECT, Action.DEFECT): 0.5425169688039843 }


class Stoc143(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.6737567480602543, (Action.COOPERATE, Action.DEFECT): 0.001691391792417729, (Action.DEFECT, Action.COOPERATE): 0.5505359754980116, (Action.DEFECT, Action.DEFECT): 0.18361320336677123 }


class Stoc144(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.4048662226844434, (Action.COOPERATE, Action.DEFECT): 0.5123675001278434, (Action.DEFECT, Action.COOPERATE): 0.29447917507292765, (Action.DEFECT, Action.DEFECT): 0.3747892218660275 }


class Stoc145(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.652676896925552, (Action.COOPERATE, Action.DEFECT): 0.12772895508357074, (Action.DEFECT, Action.COOPERATE): 0.6989377936959599, (Action.DEFECT, Action.DEFECT): 0.04488724384719667 }


class Stoc146(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5955303311632774, (Action.COOPERATE, Action.DEFECT): 0.4307827437264542, (Action.DEFECT, Action.COOPERATE): 0.7280652334601175, (Action.DEFECT, Action.DEFECT): 0.8265231710604557 }


class Stoc147(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.2961389479269707, (Action.COOPERATE, Action.DEFECT): 0.6404712011279073, (Action.DEFECT, Action.COOPERATE): 0.3154691070050947, (Action.DEFECT, Action.DEFECT): 0.38984467120723176 }


class Stoc148(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.9589549086366645, (Action.COOPERATE, Action.DEFECT): 0.7251329140670102, (Action.DEFECT, Action.COOPERATE): 0.6988127489127165, (Action.DEFECT, Action.DEFECT): 0.4458125409545153 }


class Stoc149(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.44828252959833215, (Action.COOPERATE, Action.DEFECT): 0.4062362284245584, (Action.DEFECT, Action.COOPERATE): 0.8735511194724644, (Action.DEFECT, Action.DEFECT): 0.795692536224389 }


class Stoc150(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.9488583239481262, (Action.COOPERATE, Action.DEFECT): 0.40799361164652326, (Action.DEFECT, Action.COOPERATE): 0.7569963327058027, (Action.DEFECT, Action.DEFECT): 0.6077968199965219 }


class Stoc151(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.43970523241100856, (Action.COOPERATE, Action.DEFECT): 0.228054804832304, (Action.DEFECT, Action.COOPERATE): 0.14813419367695213, (Action.DEFECT, Action.DEFECT): 0.6229534709477285 }


class Stoc152(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.772620033510795, (Action.COOPERATE, Action.DEFECT): 0.051025513520853494, (Action.DEFECT, Action.COOPERATE): 0.3327099560137122, (Action.DEFECT, Action.DEFECT): 0.19720110468034469 }


class Stoc153(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.7698943717976668, (Action.COOPERATE, Action.DEFECT): 0.4258876263321477, (Action.DEFECT, Action.COOPERATE): 0.9986378333565193, (Action.DEFECT, Action.DEFECT): 0.15231752136393917 }


class Stoc154(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.4981735032032186, (Action.COOPERATE, Action.DEFECT): 0.5736865247794659, (Action.DEFECT, Action.COOPERATE): 0.8046769474820145, (Action.DEFECT, Action.DEFECT): 0.4677582005917432 }


class Stoc155(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5904518947685312, (Action.COOPERATE, Action.DEFECT): 0.7348036376202056, (Action.DEFECT, Action.COOPERATE): 0.16072036175550208, (Action.DEFECT, Action.DEFECT): 0.9399694681028578 }


class Stoc156(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.279831371452954, (Action.COOPERATE, Action.DEFECT): 0.07348706172067576, (Action.DEFECT, Action.COOPERATE): 0.7861870726827401, (Action.DEFECT, Action.DEFECT): 0.18067977155454307 }


class Stoc157(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.8260436470978768, (Action.COOPERATE, Action.DEFECT): 0.022276687464868883, (Action.DEFECT, Action.COOPERATE): 0.3093265500445451, (Action.DEFECT, Action.DEFECT): 0.7526465201242889 }


class Stoc158(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.24919508486444208, (Action.COOPERATE, Action.DEFECT): 0.11442262187571273, (Action.DEFECT, Action.COOPERATE): 0.6358944713527717, (Action.DEFECT, Action.DEFECT): 0.42954560861540025 }


class Stoc159(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.8619221168032739, (Action.COOPERATE, Action.DEFECT): 0.46761550346736735, (Action.DEFECT, Action.COOPERATE): 0.11414853116944224, (Action.DEFECT, Action.DEFECT): 0.6537856820148448 }


class Stoc160(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.34297583443776813, (Action.COOPERATE, Action.DEFECT): 0.9966388539123341, (Action.DEFECT, Action.COOPERATE): 0.6949940887315059, (Action.DEFECT, Action.DEFECT): 0.9050147908605366 }


class Stoc161(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.11613121398763582, (Action.COOPERATE, Action.DEFECT): 0.7392355746296284, (Action.DEFECT, Action.COOPERATE): 0.48659646871760476, (Action.DEFECT, Action.DEFECT): 0.17770670416173184 }


class Stoc162(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.9026929891391141, (Action.COOPERATE, Action.DEFECT): 0.8428026177669727, (Action.DEFECT, Action.COOPERATE): 0.921280570623468, (Action.DEFECT, Action.DEFECT): 0.4953483114145918 }


class Stoc163(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.8107226842802944, (Action.COOPERATE, Action.DEFECT): 0.22046972512994933, (Action.DEFECT, Action.COOPERATE): 0.18995025103814855, (Action.DEFECT, Action.DEFECT): 0.5723591106782636 }


class Stoc164(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.4853008051369889, (Action.COOPERATE, Action.DEFECT): 0.11006408555095182, (Action.DEFECT, Action.COOPERATE): 0.961113599471648, (Action.DEFECT, Action.DEFECT): 0.09169488703450768 }


class Stoc165(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.9501945207999739, (Action.COOPERATE, Action.DEFECT): 0.7700156320240217, (Action.DEFECT, Action.COOPERATE): 0.8180750070420781, (Action.DEFECT, Action.DEFECT): 0.589705627570822 }


class Stoc166(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.3211548920716162, (Action.COOPERATE, Action.DEFECT): 0.6869366996975843, (Action.DEFECT, Action.COOPERATE): 0.26064910909913686, (Action.DEFECT, Action.DEFECT): 0.8616507886719359 }


class Stoc167(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.4480000223656727, (Action.COOPERATE, Action.DEFECT): 0.5683143154900756, (Action.DEFECT, Action.COOPERATE): 0.7861744632222557, (Action.DEFECT, Action.DEFECT): 0.35215404222875313 }


class Stoc168(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.8983137989891793, (Action.COOPERATE, Action.DEFECT): 0.3543163032717409, (Action.DEFECT, Action.COOPERATE): 0.3067437375867317, (Action.DEFECT, Action.DEFECT): 0.27271084949293034 }


class Stoc169(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.8115029119213887, (Action.COOPERATE, Action.DEFECT): 0.4768298871026704, (Action.DEFECT, Action.COOPERATE): 0.8533525942921136, (Action.DEFECT, Action.DEFECT): 0.17779057926483766 }


class Stoc170(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5507840847129875, (Action.COOPERATE, Action.DEFECT): 0.7145056848447372, (Action.DEFECT, Action.COOPERATE): 0.8476991799038115, (Action.DEFECT, Action.DEFECT): 0.8039778232287456 }


class Stoc171(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.7262954935837634, (Action.COOPERATE, Action.DEFECT): 0.09017682512662162, (Action.DEFECT, Action.COOPERATE): 0.8273024100727986, (Action.DEFECT, Action.DEFECT): 0.278924545926559 }


class Stoc172(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.21327058129374676, (Action.COOPERATE, Action.DEFECT): 0.9794383308170588, (Action.DEFECT, Action.COOPERATE): 0.668847434208247, (Action.DEFECT, Action.DEFECT): 0.8451446130037231 }


class Stoc173(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.9634828835239486, (Action.COOPERATE, Action.DEFECT): 0.39615150039023306, (Action.DEFECT, Action.COOPERATE): 0.5494222127736949, (Action.DEFECT, Action.DEFECT): 0.6730743220992982 }


class Stoc174(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.25527637914469703, (Action.COOPERATE, Action.DEFECT): 0.6141406344165836, (Action.DEFECT, Action.COOPERATE): 0.37078568007583623, (Action.DEFECT, Action.DEFECT): 0.02692789698241249 }


class Stoc175(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.4812945387619636, (Action.COOPERATE, Action.DEFECT): 0.4629400838905302, (Action.DEFECT, Action.COOPERATE): 0.01747688845911699, (Action.DEFECT, Action.DEFECT): 0.2231638271499835 }


class Stoc176(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.8846066380892764, (Action.COOPERATE, Action.DEFECT): 0.356601925940642, (Action.DEFECT, Action.COOPERATE): 0.8232577428402712, (Action.DEFECT, Action.DEFECT): 0.18253385058354143 }


class Stoc177(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.9963522537952577, (Action.COOPERATE, Action.DEFECT): 0.7596541926355868, (Action.DEFECT, Action.COOPERATE): 0.938773305431125, (Action.DEFECT, Action.DEFECT): 0.43029074598951755 }


class Stoc178(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.9878412788453445, (Action.COOPERATE, Action.DEFECT): 0.24619474921681306, (Action.DEFECT, Action.COOPERATE): 0.41027194814904766, (Action.DEFECT, Action.DEFECT): 0.22973096275275073 }


class Stoc179(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.003845199901548413, (Action.COOPERATE, Action.DEFECT): 0.3113970159194597, (Action.DEFECT, Action.COOPERATE): 0.9339177799194052, (Action.DEFECT, Action.DEFECT): 0.8669226279643458 }


class Stoc180(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.9355982961288708, (Action.COOPERATE, Action.DEFECT): 0.7938554823865337, (Action.DEFECT, Action.COOPERATE): 0.08553692523025913, (Action.DEFECT, Action.DEFECT): 0.6758527828987002 }


class Stoc181(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.8399145304124972, (Action.COOPERATE, Action.DEFECT): 0.6078657450628834, (Action.DEFECT, Action.COOPERATE): 0.07283119033669183, (Action.DEFECT, Action.DEFECT): 0.40326146071338576 }


class Stoc182(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.8477395937674712, (Action.COOPERATE, Action.DEFECT): 0.5118772588643101, (Action.DEFECT, Action.COOPERATE): 0.7911480575603006, (Action.DEFECT, Action.DEFECT): 0.21657131152586062 }


class Stoc183(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.8314555211763852, (Action.COOPERATE, Action.DEFECT): 0.3680528276813443, (Action.DEFECT, Action.COOPERATE): 0.4707637268443725, (Action.DEFECT, Action.DEFECT): 0.24944267506994888 }


class Stoc184(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.26018450510864033, (Action.COOPERATE, Action.DEFECT): 0.4199090857106923, (Action.DEFECT, Action.COOPERATE): 0.6300997805246977, (Action.DEFECT, Action.DEFECT): 0.03334943669653234 }


class Stoc185(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.44998911541938014, (Action.COOPERATE, Action.DEFECT): 0.7545394269502652, (Action.DEFECT, Action.COOPERATE): 0.3380944929680394, (Action.DEFECT, Action.DEFECT): 0.639840814133092 }


class Stoc186(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5870521919283843, (Action.COOPERATE, Action.DEFECT): 0.5601027713306701, (Action.DEFECT, Action.COOPERATE): 0.24960473939329042, (Action.DEFECT, Action.DEFECT): 0.7385912034798336 }


class Stoc187(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.02516132200661869, (Action.COOPERATE, Action.DEFECT): 0.8641637003900535, (Action.DEFECT, Action.COOPERATE): 0.8819225824282586, (Action.DEFECT, Action.DEFECT): 0.09586647363901712 }


class Stoc188(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.7107771275906398, (Action.COOPERATE, Action.DEFECT): 0.12479628251703023, (Action.DEFECT, Action.COOPERATE): 0.3190349510988312, (Action.DEFECT, Action.DEFECT): 0.28652247372855955 }


class Stoc189(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.8847257478341185, (Action.COOPERATE, Action.DEFECT): 0.8116962981175663, (Action.DEFECT, Action.COOPERATE): 0.08700239906462515, (Action.DEFECT, Action.DEFECT): 0.6726662505971562 }


class Stoc190(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.6921482304783564, (Action.COOPERATE, Action.DEFECT): 0.6804378528716903, (Action.DEFECT, Action.COOPERATE): 0.7201839713697389, (Action.DEFECT, Action.DEFECT): 0.39268338829711524 }


class Stoc191(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.31569397861590687, (Action.COOPERATE, Action.DEFECT): 0.7824301296330597, (Action.DEFECT, Action.COOPERATE): 0.7688459894520092, (Action.DEFECT, Action.DEFECT): 0.6608373972588414 }


class Stoc192(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.3276408037304155, (Action.COOPERATE, Action.DEFECT): 0.11496454133111833, (Action.DEFECT, Action.COOPERATE): 0.3838143729835767, (Action.DEFECT, Action.DEFECT): 0.8299136385300817 }


class Stoc193(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.2082580818540264, (Action.COOPERATE, Action.DEFECT): 0.8483975828038258, (Action.DEFECT, Action.COOPERATE): 0.19534115734614288, (Action.DEFECT, Action.DEFECT): 0.8767192698824358 }


class Stoc194(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.9257159752719133, (Action.COOPERATE, Action.DEFECT): 0.6620884725135002, (Action.DEFECT, Action.COOPERATE): 0.9178697153641663, (Action.DEFECT, Action.DEFECT): 0.09703368495159836 }


class Stoc195(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.36598848195631284, (Action.COOPERATE, Action.DEFECT): 0.36771435608762193, (Action.DEFECT, Action.COOPERATE): 0.6493779580308109, (Action.DEFECT, Action.DEFECT): 0.420127999028199 }


class Stoc196(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.9930180137266137, (Action.COOPERATE, Action.DEFECT): 0.3493205744923358, (Action.DEFECT, Action.COOPERATE): 0.17274939082680674, (Action.DEFECT, Action.DEFECT): 0.3726714546367368 }


class Stoc197(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.6309643825995851, (Action.COOPERATE, Action.DEFECT): 0.6769401042360292, (Action.DEFECT, Action.COOPERATE): 0.214318523563913, (Action.DEFECT, Action.DEFECT): 0.3853067729750487 }


class Stoc198(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.7270957262191917, (Action.COOPERATE, Action.DEFECT): 0.935754071025023, (Action.DEFECT, Action.COOPERATE): 0.6066149144013395, (Action.DEFECT, Action.DEFECT): 0.813838076209029 }


class Stoc199(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.0064150362107198156, (Action.COOPERATE, Action.DEFECT): 0.37277783548293275, (Action.DEFECT, Action.COOPERATE): 0.4679861754035114, (Action.DEFECT, Action.DEFECT): 0.976505042280034 }


class Stoc200(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.4597981001339084, (Action.COOPERATE, Action.DEFECT): 0.522352659985699, (Action.DEFECT, Action.COOPERATE): 0.4353407469732574, (Action.DEFECT, Action.DEFECT): 0.002383209971864364 }


class Stoc201(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.9716971747000137, (Action.COOPERATE, Action.DEFECT): 0.9241125015640982, (Action.DEFECT, Action.COOPERATE): 0.06381774186924494, (Action.DEFECT, Action.DEFECT): 0.6479542273754187 }


class Stoc202(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.33203100738988145, (Action.COOPERATE, Action.DEFECT): 0.40085273778573527, (Action.DEFECT, Action.COOPERATE): 0.7468105767263488, (Action.DEFECT, Action.DEFECT): 0.6824499632441884 }


class Stoc203(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.44047594321897565, (Action.COOPERATE, Action.DEFECT): 0.7218169456215668, (Action.DEFECT, Action.COOPERATE): 0.12444230420613589, (Action.DEFECT, Action.DEFECT): 0.2662787383145224 }


class Stoc204(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.981083300516125, (Action.COOPERATE, Action.DEFECT): 0.1436415384547105, (Action.DEFECT, Action.COOPERATE): 0.47686673908375765, (Action.DEFECT, Action.DEFECT): 0.38160839504127475 }


class Stoc205(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.7806050874607025, (Action.COOPERATE, Action.DEFECT): 0.3229061445852389, (Action.DEFECT, Action.COOPERATE): 0.17349443812900356, (Action.DEFECT, Action.DEFECT): 0.9918185277827707 }


class Stoc206(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.6991782991567564, (Action.COOPERATE, Action.DEFECT): 0.9842977231213981, (Action.DEFECT, Action.COOPERATE): 0.36617138908524116, (Action.DEFECT, Action.DEFECT): 0.5608744806825099 }


class Stoc207(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5770635055063946, (Action.COOPERATE, Action.DEFECT): 0.01139985799239962, (Action.DEFECT, Action.COOPERATE): 0.7730354080660173, (Action.DEFECT, Action.DEFECT): 0.6964724705378669 }


class Stoc208(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.772546168124448, (Action.COOPERATE, Action.DEFECT): 0.23355083856834935, (Action.DEFECT, Action.COOPERATE): 0.5645371227148583, (Action.DEFECT, Action.DEFECT): 0.6041956041170807 }


class Stoc209(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.26724013643019895, (Action.COOPERATE, Action.DEFECT): 0.7251731063104168, (Action.DEFECT, Action.COOPERATE): 0.45033689406729316, (Action.DEFECT, Action.DEFECT): 0.1066795255803189 }


class Stoc210(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.11432655806711434, (Action.COOPERATE, Action.DEFECT): 0.12268751495233765, (Action.DEFECT, Action.COOPERATE): 0.5836848089396469, (Action.DEFECT, Action.DEFECT): 0.25284450251054424 }


class Stoc211(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.9361344450122981, (Action.COOPERATE, Action.DEFECT): 0.9003804004113111, (Action.DEFECT, Action.COOPERATE): 0.19121105636269686, (Action.DEFECT, Action.DEFECT): 0.5042211335695399 }


class Stoc212(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.43839655824448753, (Action.COOPERATE, Action.DEFECT): 0.5517521723623503, (Action.DEFECT, Action.COOPERATE): 0.8684711054910582, (Action.DEFECT, Action.DEFECT): 0.6933054914963676 }


class Stoc213(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.31304485648386904, (Action.COOPERATE, Action.DEFECT): 0.01601350134694579, (Action.DEFECT, Action.COOPERATE): 0.8630651910191379, (Action.DEFECT, Action.DEFECT): 0.03865406240929414 }


class Stoc214(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.6609630657495824, (Action.COOPERATE, Action.DEFECT): 0.8750350410967231, (Action.DEFECT, Action.COOPERATE): 0.5467299353965991, (Action.DEFECT, Action.DEFECT): 0.19168390254770584 }


class Stoc215(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.2066435561435881, (Action.COOPERATE, Action.DEFECT): 0.13415506887054918, (Action.DEFECT, Action.COOPERATE): 0.40583036149801655, (Action.DEFECT, Action.DEFECT): 0.871458478001958 }


class Stoc216(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.032888608632130056, (Action.COOPERATE, Action.DEFECT): 0.7444011889788705, (Action.DEFECT, Action.COOPERATE): 0.9121633627938821, (Action.DEFECT, Action.DEFECT): 0.0026847128030715872 }


class Stoc217(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.8937090148983616, (Action.COOPERATE, Action.DEFECT): 0.05069946743402809, (Action.DEFECT, Action.COOPERATE): 0.9333352889024078, (Action.DEFECT, Action.DEFECT): 0.3526790804561808 }


class Stoc218(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.0950648432224156, (Action.COOPERATE, Action.DEFECT): 0.5902515558246588, (Action.DEFECT, Action.COOPERATE): 0.019412820792732544, (Action.DEFECT, Action.DEFECT): 0.14149069465137531 }


class Stoc219(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.8232932152765559, (Action.COOPERATE, Action.DEFECT): 0.18985923258827175, (Action.DEFECT, Action.COOPERATE): 0.08485229196305555, (Action.DEFECT, Action.DEFECT): 0.5085797209693795 }


class Stoc220(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.03352729335099347, (Action.COOPERATE, Action.DEFECT): 0.9771873851793977, (Action.DEFECT, Action.COOPERATE): 0.49500093806163514, (Action.DEFECT, Action.DEFECT): 0.1689739848347095 }


class Stoc221(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5456030577426262, (Action.COOPERATE, Action.DEFECT): 0.23036656383157295, (Action.DEFECT, Action.COOPERATE): 0.005463151904294472, (Action.DEFECT, Action.DEFECT): 0.7405253736274338 }


class Stoc222(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.9433090000218403, (Action.COOPERATE, Action.DEFECT): 0.23631388349870042, (Action.DEFECT, Action.COOPERATE): 0.372126919502917, (Action.DEFECT, Action.DEFECT): 0.00013560461089845433 }


class Stoc223(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.8144349059426327, (Action.COOPERATE, Action.DEFECT): 0.09605224996784467, (Action.DEFECT, Action.COOPERATE): 0.5031249317541696, (Action.DEFECT, Action.DEFECT): 0.1020145053237741 }


class Stoc224(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.6958952418496467, (Action.COOPERATE, Action.DEFECT): 0.0526125675104373, (Action.DEFECT, Action.COOPERATE): 0.6591731748386679, (Action.DEFECT, Action.DEFECT): 0.14505714150071936 }


class Stoc225(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.9903457546807807, (Action.COOPERATE, Action.DEFECT): 0.2401754469206252, (Action.DEFECT, Action.COOPERATE): 0.9381766546258152, (Action.DEFECT, Action.DEFECT): 0.029213107715732933 }


class Stoc226(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.23660582207301195, (Action.COOPERATE, Action.DEFECT): 0.4953058102880431, (Action.DEFECT, Action.COOPERATE): 0.4521865920493451, (Action.DEFECT, Action.DEFECT): 0.2747356130861065 }


class Stoc227(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.44275481559311125, (Action.COOPERATE, Action.DEFECT): 0.7798839538921534, (Action.DEFECT, Action.COOPERATE): 0.8884321980685065, (Action.DEFECT, Action.DEFECT): 0.5014358144115507 }


class Stoc228(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.9213456804197897, (Action.COOPERATE, Action.DEFECT): 0.005488232718083186, (Action.DEFECT, Action.COOPERATE): 0.8770464532823995, (Action.DEFECT, Action.DEFECT): 0.3998393408079969 }


class Stoc229(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.7652359409119001, (Action.COOPERATE, Action.DEFECT): 0.6751463430458896, (Action.DEFECT, Action.COOPERATE): 0.3962513358282047, (Action.DEFECT, Action.DEFECT): 0.445372462168548 }


class Stoc230(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.1686995741151851, (Action.COOPERATE, Action.DEFECT): 0.15208358640078834, (Action.DEFECT, Action.COOPERATE): 0.9431097478187482, (Action.DEFECT, Action.DEFECT): 0.7637848588131307 }


class Stoc231(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.42590598926858647, (Action.COOPERATE, Action.DEFECT): 0.5647514953878758, (Action.DEFECT, Action.COOPERATE): 0.39460301697294875, (Action.DEFECT, Action.DEFECT): 0.21679490081102115 }


class Stoc232(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5156458647913603, (Action.COOPERATE, Action.DEFECT): 0.04421834194142993, (Action.DEFECT, Action.COOPERATE): 0.8566384291021267, (Action.DEFECT, Action.DEFECT): 0.5630482935121838 }


class Stoc233(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.7618954199903304, (Action.COOPERATE, Action.DEFECT): 0.6479753645758224, (Action.DEFECT, Action.COOPERATE): 0.5664201578094931, (Action.DEFECT, Action.DEFECT): 0.015031826728484243 }


class Stoc234(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.2088514939940762, (Action.COOPERATE, Action.DEFECT): 0.9908475414543557, (Action.DEFECT, Action.COOPERATE): 0.9945410861937951, (Action.DEFECT, Action.DEFECT): 0.20824982305649364 }


class Stoc235(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.3041203684637105, (Action.COOPERATE, Action.DEFECT): 0.8568892793416555, (Action.DEFECT, Action.COOPERATE): 0.8538034695053285, (Action.DEFECT, Action.DEFECT): 0.5543650295102207 }


class Stoc236(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.4016548111202758, (Action.COOPERATE, Action.DEFECT): 0.8108253470939767, (Action.DEFECT, Action.COOPERATE): 0.198449292630283, (Action.DEFECT, Action.DEFECT): 0.3982689753936556 }


class Stoc237(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.004690061523766942, (Action.COOPERATE, Action.DEFECT): 0.12192700351191965, (Action.DEFECT, Action.COOPERATE): 0.6557449281540202, (Action.DEFECT, Action.DEFECT): 0.8676202563413972 }


class Stoc238(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.6115398719943622, (Action.COOPERATE, Action.DEFECT): 0.5654891308679053, (Action.DEFECT, Action.COOPERATE): 0.8870386143308155, (Action.DEFECT, Action.DEFECT): 0.6719225147257644 }


class Stoc239(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.09848913285171645, (Action.COOPERATE, Action.DEFECT): 0.8547412513906728, (Action.DEFECT, Action.COOPERATE): 0.14984016098564967, (Action.DEFECT, Action.DEFECT): 0.8661865496671531 }


class Stoc240(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.17025597307818985, (Action.COOPERATE, Action.DEFECT): 0.638895288900332, (Action.DEFECT, Action.COOPERATE): 0.7324206730870877, (Action.DEFECT, Action.DEFECT): 0.20654066816381145 }


class Stoc241(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.7162882465906917, (Action.COOPERATE, Action.DEFECT): 0.8505255171040726, (Action.DEFECT, Action.COOPERATE): 0.2566691177114919, (Action.DEFECT, Action.DEFECT): 0.7350386810084978 }


class Stoc242(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.8867525045212468, (Action.COOPERATE, Action.DEFECT): 0.8708934775186705, (Action.DEFECT, Action.COOPERATE): 0.8551902010211182, (Action.DEFECT, Action.DEFECT): 0.026311959446002176 }


class Stoc243(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.341302671769373, (Action.COOPERATE, Action.DEFECT): 0.8284587693280796, (Action.DEFECT, Action.COOPERATE): 0.6614417679595489, (Action.DEFECT, Action.DEFECT): 0.5578187483033529 }


class Stoc244(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.684170898117988, (Action.COOPERATE, Action.DEFECT): 0.4866837666826973, (Action.DEFECT, Action.COOPERATE): 0.03642148617886343, (Action.DEFECT, Action.DEFECT): 0.03214237780434437 }


class Stoc245(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.6203065988474232, (Action.COOPERATE, Action.DEFECT): 0.41512848615589315, (Action.DEFECT, Action.COOPERATE): 0.866528722725183, (Action.DEFECT, Action.DEFECT): 0.42133064304683276 }


class Stoc246(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.11324092664229335, (Action.COOPERATE, Action.DEFECT): 0.667285944383968, (Action.DEFECT, Action.COOPERATE): 0.5749997743068721, (Action.DEFECT, Action.DEFECT): 0.8080094480843075 }


class Stoc247(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.3932105858300148, (Action.COOPERATE, Action.DEFECT): 0.12974038918742326, (Action.DEFECT, Action.COOPERATE): 0.9508290115078207, (Action.DEFECT, Action.DEFECT): 0.5478367784171563 }


class Stoc248(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.06686146643335678, (Action.COOPERATE, Action.DEFECT): 0.5033608994020475, (Action.DEFECT, Action.COOPERATE): 0.22795097537737619, (Action.DEFECT, Action.DEFECT): 0.947202706866822 }


class Stoc249(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.0376963314512998, (Action.COOPERATE, Action.DEFECT): 0.8358457571723689, (Action.DEFECT, Action.COOPERATE): 0.15729940226520067, (Action.DEFECT, Action.DEFECT): 0.5058148606705173 }


class Stoc250(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5857590664218187, (Action.COOPERATE, Action.DEFECT): 0.12012898337227229, (Action.DEFECT, Action.COOPERATE): 0.2744937773595466, (Action.DEFECT, Action.DEFECT): 0.9366090091458971 }


class Stoc251(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5493973879544941, (Action.COOPERATE, Action.DEFECT): 0.7023534885447973, (Action.DEFECT, Action.COOPERATE): 0.5968095874867753, (Action.DEFECT, Action.DEFECT): 0.6340040866559741 }


class Stoc252(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.15266607249497144, (Action.COOPERATE, Action.DEFECT): 0.9992589242263014, (Action.DEFECT, Action.COOPERATE): 0.760653547943587, (Action.DEFECT, Action.DEFECT): 0.8945409117382617 }


class Stoc253(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.86681166189041, (Action.COOPERATE, Action.DEFECT): 0.9806261336649358, (Action.DEFECT, Action.COOPERATE): 0.5248985330621088, (Action.DEFECT, Action.DEFECT): 0.9398514713597336 }


class Stoc254(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.7229570765738096, (Action.COOPERATE, Action.DEFECT): 0.2958205921725767, (Action.DEFECT, Action.COOPERATE): 0.8683066079392928, (Action.DEFECT, Action.DEFECT): 0.8379510490101051 }


class Stoc255(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5857284920116846, (Action.COOPERATE, Action.DEFECT): 0.6593612702863554, (Action.DEFECT, Action.COOPERATE): 0.9669929064642826, (Action.DEFECT, Action.DEFECT): 0.8574061001920368 }


class Stoc256(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.48221460480602596, (Action.COOPERATE, Action.DEFECT): 0.48715929338255604, (Action.DEFECT, Action.COOPERATE): 0.09451023799581382, (Action.DEFECT, Action.DEFECT): 0.4000843998117488 }


class Stoc257(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.3775820366553997, (Action.COOPERATE, Action.DEFECT): 0.9716943001559917, (Action.DEFECT, Action.COOPERATE): 0.8596418927368589, (Action.DEFECT, Action.DEFECT): 0.7635675381862128 }


class Stoc258(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.33623401932791386, (Action.COOPERATE, Action.DEFECT): 0.3232186548119872, (Action.DEFECT, Action.COOPERATE): 0.8319302416226783, (Action.DEFECT, Action.DEFECT): 0.44365798266997103 }


class Stoc259(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.4924156740614529, (Action.COOPERATE, Action.DEFECT): 0.622442359995641, (Action.DEFECT, Action.COOPERATE): 0.30966126753855605, (Action.DEFECT, Action.DEFECT): 0.7771126598403478 }


class Stoc260(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.8720030846611194, (Action.COOPERATE, Action.DEFECT): 0.7598737642902833, (Action.DEFECT, Action.COOPERATE): 0.25997635329628666, (Action.DEFECT, Action.DEFECT): 0.14231730246707708 }


class Stoc261(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.7412931380563685, (Action.COOPERATE, Action.DEFECT): 0.2996974174124363, (Action.DEFECT, Action.COOPERATE): 0.3779879287261424, (Action.DEFECT, Action.DEFECT): 0.4656105325517569 }


class Stoc262(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.03214483046290728, (Action.COOPERATE, Action.DEFECT): 0.42291163664134956, (Action.DEFECT, Action.COOPERATE): 0.6865027720394038, (Action.DEFECT, Action.DEFECT): 0.8606534631713667 }


class Stoc263(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.03434574105452748, (Action.COOPERATE, Action.DEFECT): 0.5163541284342545, (Action.DEFECT, Action.COOPERATE): 0.9327673483284136, (Action.DEFECT, Action.DEFECT): 0.03212057918774647 }


class Stoc264(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.48931080166535446, (Action.COOPERATE, Action.DEFECT): 0.1392903085274374, (Action.DEFECT, Action.COOPERATE): 0.6413795415084619, (Action.DEFECT, Action.DEFECT): 0.8089165767745196 }


class Stoc265(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.0705042991632161, (Action.COOPERATE, Action.DEFECT): 0.11561581227661277, (Action.DEFECT, Action.COOPERATE): 0.41464183998290116, (Action.DEFECT, Action.DEFECT): 0.3214268905986146 }


class Stoc266(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.3518833179610218, (Action.COOPERATE, Action.DEFECT): 0.5765842767006226, (Action.DEFECT, Action.COOPERATE): 0.6817043815768025, (Action.DEFECT, Action.DEFECT): 0.6500623979141521 }


class Stoc267(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.23607022136425682, (Action.COOPERATE, Action.DEFECT): 0.9921331844901752, (Action.DEFECT, Action.COOPERATE): 0.275283864280255, (Action.DEFECT, Action.DEFECT): 0.7052602024698956 }


class Stoc268(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.30673871638058814, (Action.COOPERATE, Action.DEFECT): 0.21334619591914972, (Action.DEFECT, Action.COOPERATE): 0.4740485461858691, (Action.DEFECT, Action.DEFECT): 0.6199698527379144 }


class Stoc269(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.8316336110137648, (Action.COOPERATE, Action.DEFECT): 0.1911354814631291, (Action.DEFECT, Action.COOPERATE): 0.7471369898398701, (Action.DEFECT, Action.DEFECT): 0.654022189992253 }


class Stoc270(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.0476225204825137, (Action.COOPERATE, Action.DEFECT): 0.32789913047178365, (Action.DEFECT, Action.COOPERATE): 0.276936827651188, (Action.DEFECT, Action.DEFECT): 0.003024896561764301 }


class Stoc271(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.6461804016919982, (Action.COOPERATE, Action.DEFECT): 0.8081016402206498, (Action.DEFECT, Action.COOPERATE): 0.19756736150766252, (Action.DEFECT, Action.DEFECT): 0.1737926288104087 }


class Stoc272(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.20224103656392456, (Action.COOPERATE, Action.DEFECT): 0.7538210536469935, (Action.DEFECT, Action.COOPERATE): 0.3599758953029739, (Action.DEFECT, Action.DEFECT): 0.38509347053062926 }


class Stoc273(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.8906977143825451, (Action.COOPERATE, Action.DEFECT): 0.6488588212531834, (Action.DEFECT, Action.COOPERATE): 0.004446782123973092, (Action.DEFECT, Action.DEFECT): 0.4030593182642376 }


class Stoc274(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.19715344124600154, (Action.COOPERATE, Action.DEFECT): 0.15904487850890348, (Action.DEFECT, Action.COOPERATE): 0.5853586487444558, (Action.DEFECT, Action.DEFECT): 0.19264577020542317 }


class Stoc275(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.7946980631830012, (Action.COOPERATE, Action.DEFECT): 0.38752068840505594, (Action.DEFECT, Action.COOPERATE): 0.9719526486991149, (Action.DEFECT, Action.DEFECT): 0.46332964535304955 }


class Stoc276(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.07260310314946139, (Action.COOPERATE, Action.DEFECT): 0.45469046171946925, (Action.DEFECT, Action.COOPERATE): 0.4102100627643587, (Action.DEFECT, Action.DEFECT): 0.8742160488624395 }


class Stoc277(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.9534407302185657, (Action.COOPERATE, Action.DEFECT): 0.14806663521044805, (Action.DEFECT, Action.COOPERATE): 0.15803215252013947, (Action.DEFECT, Action.DEFECT): 0.4269742133933293 }


class Stoc278(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.9353338280804195, (Action.COOPERATE, Action.DEFECT): 0.8075966378176686, (Action.DEFECT, Action.COOPERATE): 0.9542115059884196, (Action.DEFECT, Action.DEFECT): 0.19949414774281193 }


class Stoc279(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.6883437197812126, (Action.COOPERATE, Action.DEFECT): 0.9427348599515717, (Action.DEFECT, Action.COOPERATE): 0.21713565659340672, (Action.DEFECT, Action.DEFECT): 0.22571524902394902 }


class Stoc280(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.6471782612597423, (Action.COOPERATE, Action.DEFECT): 0.4243181394229081, (Action.DEFECT, Action.COOPERATE): 0.6956924877883455, (Action.DEFECT, Action.DEFECT): 0.8475533711540933 }


class Stoc281(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.9948280274659393, (Action.COOPERATE, Action.DEFECT): 0.023594840987384957, (Action.DEFECT, Action.COOPERATE): 0.922980541844254, (Action.DEFECT, Action.DEFECT): 0.9257032167054325 }


class Stoc282(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5911494939599358, (Action.COOPERATE, Action.DEFECT): 0.4333261551164894, (Action.DEFECT, Action.COOPERATE): 0.5878122525450212, (Action.DEFECT, Action.DEFECT): 0.17295679206781367 }


class Stoc283(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.6474278639531315, (Action.COOPERATE, Action.DEFECT): 0.27039923374607944, (Action.DEFECT, Action.COOPERATE): 0.07315477337098764, (Action.DEFECT, Action.DEFECT): 0.2658281689820039 }


class Stoc284(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.8158979653863039, (Action.COOPERATE, Action.DEFECT): 0.3076319755387472, (Action.DEFECT, Action.COOPERATE): 0.7305789693452078, (Action.DEFECT, Action.DEFECT): 0.7647177523031613 }


class Stoc285(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.466643418027643, (Action.COOPERATE, Action.DEFECT): 0.7155808676303053, (Action.DEFECT, Action.COOPERATE): 0.4707853975999644, (Action.DEFECT, Action.DEFECT): 0.22278972567124722 }


class Stoc286(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.9181264254431163, (Action.COOPERATE, Action.DEFECT): 0.8996861387710104, (Action.DEFECT, Action.COOPERATE): 0.036361057533338736, (Action.DEFECT, Action.DEFECT): 0.8337492404750049 }


class Stoc287(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5702499353653052, (Action.COOPERATE, Action.DEFECT): 0.32794406103116125, (Action.DEFECT, Action.COOPERATE): 0.170087021951139, (Action.DEFECT, Action.DEFECT): 0.07046820088268002 }


class Stoc288(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.6846833145107775, (Action.COOPERATE, Action.DEFECT): 0.9885245333971391, (Action.DEFECT, Action.COOPERATE): 0.4572032198030035, (Action.DEFECT, Action.DEFECT): 0.31369254729151863 }


class Stoc289(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.020364801448303216, (Action.COOPERATE, Action.DEFECT): 0.3988382098967267, (Action.DEFECT, Action.COOPERATE): 0.034174014588137624, (Action.DEFECT, Action.DEFECT): 0.5891504003771909 }


class Stoc290(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.6021624285725027, (Action.COOPERATE, Action.DEFECT): 0.7148339198884581, (Action.DEFECT, Action.COOPERATE): 0.9277070408797389, (Action.DEFECT, Action.DEFECT): 0.38038353371692035 }


class Stoc291(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.9406121045220156, (Action.COOPERATE, Action.DEFECT): 0.8736977713513112, (Action.DEFECT, Action.COOPERATE): 0.8151613129810137, (Action.DEFECT, Action.DEFECT): 0.31204677293107097 }


class Stoc292(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.09739047583701965, (Action.COOPERATE, Action.DEFECT): 0.5320201057625812, (Action.DEFECT, Action.COOPERATE): 0.04328674245967179, (Action.DEFECT, Action.DEFECT): 0.023511871542851503 }


class Stoc293(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.7924719280373579, (Action.COOPERATE, Action.DEFECT): 0.9587466650469174, (Action.DEFECT, Action.COOPERATE): 0.5782668572806838, (Action.DEFECT, Action.DEFECT): 0.5304287098653329 }


class Stoc294(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.17324585110538238, (Action.COOPERATE, Action.DEFECT): 0.9527227704991623, (Action.DEFECT, Action.COOPERATE): 0.7399737999060302, (Action.DEFECT, Action.DEFECT): 0.35349856525046364 }


class Stoc295(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.28996249956276576, (Action.COOPERATE, Action.DEFECT): 0.2711565189545563, (Action.DEFECT, Action.COOPERATE): 0.6430044712308939, (Action.DEFECT, Action.DEFECT): 0.18659818741066392 }


class Stoc296(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.8568659163339264, (Action.COOPERATE, Action.DEFECT): 0.6887454097942993, (Action.DEFECT, Action.COOPERATE): 0.6530701384624104, (Action.DEFECT, Action.DEFECT): 0.2601212993182187 }


class Stoc297(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.37666190904863783, (Action.COOPERATE, Action.DEFECT): 0.6255699716000086, (Action.DEFECT, Action.COOPERATE): 0.8971873542216405, (Action.DEFECT, Action.DEFECT): 0.37878141107567254 }


class Stoc298(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.27518419832221885, (Action.COOPERATE, Action.DEFECT): 0.18057514974134392, (Action.DEFECT, Action.COOPERATE): 0.5546933714004396, (Action.DEFECT, Action.DEFECT): 0.1623047521633293 }


class Stoc299(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.564169829892784, (Action.COOPERATE, Action.DEFECT): 0.591126160953063, (Action.DEFECT, Action.COOPERATE): 0.8174036849174511, (Action.DEFECT, Action.DEFECT): 0.15384017347647205 }


class Stoc300(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.6753836453290423, (Action.COOPERATE, Action.DEFECT): 0.5235602944250157, (Action.DEFECT, Action.COOPERATE): 0.28063685654405457, (Action.DEFECT, Action.DEFECT): 0.36321693262004984 }


class Stoc301(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5479170094450525, (Action.COOPERATE, Action.DEFECT): 0.13221452281106705, (Action.DEFECT, Action.COOPERATE): 0.563135823904553, (Action.DEFECT, Action.DEFECT): 0.5903255758715276 }


class Stoc302(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.24986520342649376, (Action.COOPERATE, Action.DEFECT): 0.6922384260169088, (Action.DEFECT, Action.COOPERATE): 0.15058533798671092, (Action.DEFECT, Action.DEFECT): 0.35184470796750655 }


class Stoc303(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.8512219938028035, (Action.COOPERATE, Action.DEFECT): 0.8812083722719543, (Action.DEFECT, Action.COOPERATE): 0.788720293712297, (Action.DEFECT, Action.DEFECT): 0.2690085440234009 }


class Stoc304(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.3465268587964063, (Action.COOPERATE, Action.DEFECT): 0.43978469342876336, (Action.DEFECT, Action.COOPERATE): 0.4869435064274067, (Action.DEFECT, Action.DEFECT): 0.14752481284051167 }


class Stoc305(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.7012647959010785, (Action.COOPERATE, Action.DEFECT): 0.8617788725433162, (Action.DEFECT, Action.COOPERATE): 0.5505032138212794, (Action.DEFECT, Action.DEFECT): 0.8298276279299269 }


class Stoc306(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.9124830712340178, (Action.COOPERATE, Action.DEFECT): 0.8851216199140869, (Action.DEFECT, Action.COOPERATE): 0.2492220303889574, (Action.DEFECT, Action.DEFECT): 0.7116186583675985 }


class Stoc307(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.3228446858449351, (Action.COOPERATE, Action.DEFECT): 0.4243717900160716, (Action.DEFECT, Action.COOPERATE): 0.27467728421169035, (Action.DEFECT, Action.DEFECT): 0.47956767658768973 }


class Stoc308(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5983990166615825, (Action.COOPERATE, Action.DEFECT): 0.8137407452762943, (Action.DEFECT, Action.COOPERATE): 0.8803437963059633, (Action.DEFECT, Action.DEFECT): 0.6946720182229092 }


class Stoc309(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.8025451740142121, (Action.COOPERATE, Action.DEFECT): 0.4085828060365413, (Action.DEFECT, Action.COOPERATE): 0.7166961470159215, (Action.DEFECT, Action.DEFECT): 0.5466439859901185 }


class Stoc310(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.8726975558237327, (Action.COOPERATE, Action.DEFECT): 0.4677564014943406, (Action.DEFECT, Action.COOPERATE): 0.8465119071826764, (Action.DEFECT, Action.DEFECT): 0.2352057388991432 }


class Stoc311(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.11200203686016108, (Action.COOPERATE, Action.DEFECT): 0.12647326546993143, (Action.DEFECT, Action.COOPERATE): 0.11241017283843335, (Action.DEFECT, Action.DEFECT): 0.9913563807326012 }


class Stoc312(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.620326112537129, (Action.COOPERATE, Action.DEFECT): 0.4011195789826071, (Action.DEFECT, Action.COOPERATE): 0.3469174322464943, (Action.DEFECT, Action.DEFECT): 0.5595693613367256 }


class Stoc313(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.984748164210471, (Action.COOPERATE, Action.DEFECT): 0.057550299672458616, (Action.DEFECT, Action.COOPERATE): 0.7835007222767938, (Action.DEFECT, Action.DEFECT): 0.15630191167325125 }


class Stoc314(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.25921881642349354, (Action.COOPERATE, Action.DEFECT): 0.3454123053380025, (Action.DEFECT, Action.COOPERATE): 0.9654401104473616, (Action.DEFECT, Action.DEFECT): 0.34126410883816816 }


class Stoc315(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.9179074341770694, (Action.COOPERATE, Action.DEFECT): 0.6487521513851314, (Action.DEFECT, Action.COOPERATE): 0.7991599095582199, (Action.DEFECT, Action.DEFECT): 0.8362431879248415 }


class Stoc316(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.8639996030778441, (Action.COOPERATE, Action.DEFECT): 0.5988854605692733, (Action.DEFECT, Action.COOPERATE): 0.8524710714854417, (Action.DEFECT, Action.DEFECT): 0.5627397310381235 }


class Stoc317(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.9722084853757303, (Action.COOPERATE, Action.DEFECT): 0.19372918439228293, (Action.DEFECT, Action.COOPERATE): 0.4097662574784874, (Action.DEFECT, Action.DEFECT): 0.4775274750928561 }


class Stoc318(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.44495398482195536, (Action.COOPERATE, Action.DEFECT): 0.26305927044440414, (Action.DEFECT, Action.COOPERATE): 0.8199904721247581, (Action.DEFECT, Action.DEFECT): 0.8681526056431197 }


class Stoc319(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.2584347373028699, (Action.COOPERATE, Action.DEFECT): 0.6142975390133544, (Action.DEFECT, Action.COOPERATE): 0.6294758495511814, (Action.DEFECT, Action.DEFECT): 0.04489663272619837 }


class Stoc320(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.7673304723975969, (Action.COOPERATE, Action.DEFECT): 0.10874216535577197, (Action.DEFECT, Action.COOPERATE): 0.09337421659694534, (Action.DEFECT, Action.DEFECT): 0.7028804447715352 }


class Stoc321(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.11409240119334874, (Action.COOPERATE, Action.DEFECT): 0.4240495940521022, (Action.DEFECT, Action.COOPERATE): 0.44354536867636274, (Action.DEFECT, Action.DEFECT): 0.12093440647676146 }


class Stoc322(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.39774596592824574, (Action.COOPERATE, Action.DEFECT): 0.4599580631407928, (Action.DEFECT, Action.COOPERATE): 0.5865577523968522, (Action.DEFECT, Action.DEFECT): 0.4455846714285999 }


class Stoc323(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.009654989723899998, (Action.COOPERATE, Action.DEFECT): 0.9637920934582478, (Action.DEFECT, Action.COOPERATE): 0.3229580312100919, (Action.DEFECT, Action.DEFECT): 0.6575487321445453 }


class Stoc324(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.6465705396436251, (Action.COOPERATE, Action.DEFECT): 0.3167715399319304, (Action.DEFECT, Action.COOPERATE): 0.6484406659119004, (Action.DEFECT, Action.DEFECT): 0.8977155047573929 }


class Stoc325(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.2177910562321307, (Action.COOPERATE, Action.DEFECT): 0.3908345053043344, (Action.DEFECT, Action.COOPERATE): 0.6577934079053683, (Action.DEFECT, Action.DEFECT): 0.6059222622670214 }


class Stoc326(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.9501381682928074, (Action.COOPERATE, Action.DEFECT): 0.9878223565459844, (Action.DEFECT, Action.COOPERATE): 0.8446068506038916, (Action.DEFECT, Action.DEFECT): 0.16464653642524318 }


class Stoc327(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.7189658839245642, (Action.COOPERATE, Action.DEFECT): 0.5315839164309238, (Action.DEFECT, Action.COOPERATE): 0.11862703497720672, (Action.DEFECT, Action.DEFECT): 0.36983586264705925 }


class Stoc328(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.6922745696254491, (Action.COOPERATE, Action.DEFECT): 0.6082359046681275, (Action.DEFECT, Action.COOPERATE): 0.16401642081793666, (Action.DEFECT, Action.DEFECT): 0.20105272780130556 }


class Stoc329(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5605069239211755, (Action.COOPERATE, Action.DEFECT): 0.0009695883588255461, (Action.DEFECT, Action.COOPERATE): 0.7046508563129597, (Action.DEFECT, Action.DEFECT): 0.6543044599436719 }


class Stoc330(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.46562895320671016, (Action.COOPERATE, Action.DEFECT): 0.9125203588084936, (Action.DEFECT, Action.COOPERATE): 0.5255843854183041, (Action.DEFECT, Action.DEFECT): 0.27696567683290474 }


class Stoc331(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.1296558504747446, (Action.COOPERATE, Action.DEFECT): 0.16265095325105494, (Action.DEFECT, Action.COOPERATE): 0.3847884661617641, (Action.DEFECT, Action.DEFECT): 0.7837165126292367 }


class Stoc332(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.1632810580843288, (Action.COOPERATE, Action.DEFECT): 0.5812791400348558, (Action.DEFECT, Action.COOPERATE): 0.24541364952559475, (Action.DEFECT, Action.DEFECT): 0.6899462826416287 }


class Stoc333(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.9497238658837002, (Action.COOPERATE, Action.DEFECT): 0.33988208283565435, (Action.DEFECT, Action.COOPERATE): 0.8815373720478051, (Action.DEFECT, Action.DEFECT): 0.31036917824097154 }


class Stoc334(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.6123952081915418, (Action.COOPERATE, Action.DEFECT): 0.2882384387292264, (Action.DEFECT, Action.COOPERATE): 0.4832230776643467, (Action.DEFECT, Action.DEFECT): 0.1520811661336241 }


class Stoc335(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.7908604456301471, (Action.COOPERATE, Action.DEFECT): 0.7063126230214885, (Action.DEFECT, Action.COOPERATE): 0.2631208167395507, (Action.DEFECT, Action.DEFECT): 0.5831383493740031 }


class Stoc336(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.27043795780417323, (Action.COOPERATE, Action.DEFECT): 0.4776162596322243, (Action.DEFECT, Action.COOPERATE): 0.08702925848863852, (Action.DEFECT, Action.DEFECT): 0.5900325630592397 }


class Stoc337(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.14038977215270376, (Action.COOPERATE, Action.DEFECT): 0.848147773409038, (Action.DEFECT, Action.COOPERATE): 0.46126408635870364, (Action.DEFECT, Action.DEFECT): 0.1623332160078197 }


class Stoc338(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.47829064358946227, (Action.COOPERATE, Action.DEFECT): 0.42043579620584015, (Action.DEFECT, Action.COOPERATE): 0.7966078105935169, (Action.DEFECT, Action.DEFECT): 0.12073327257538491 }


class Stoc339(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.20749315195284979, (Action.COOPERATE, Action.DEFECT): 0.24593137544302357, (Action.DEFECT, Action.COOPERATE): 0.5975350234835046, (Action.DEFECT, Action.DEFECT): 0.7180524062458224 }


class Stoc340(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.9266704108644661, (Action.COOPERATE, Action.DEFECT): 0.7022926092047418, (Action.DEFECT, Action.COOPERATE): 0.039878835937211754, (Action.DEFECT, Action.DEFECT): 0.08458469200235608 }


class Stoc341(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.2147401413721408, (Action.COOPERATE, Action.DEFECT): 0.38320957591718896, (Action.DEFECT, Action.COOPERATE): 0.9220464009293404, (Action.DEFECT, Action.DEFECT): 0.8396727347201375 }


class Stoc342(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.729132195422898, (Action.COOPERATE, Action.DEFECT): 0.4832759890999383, (Action.DEFECT, Action.COOPERATE): 0.8538144119611634, (Action.DEFECT, Action.DEFECT): 0.5212509339985669 }


class Stoc343(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.351270116850695, (Action.COOPERATE, Action.DEFECT): 0.7287627636845035, (Action.DEFECT, Action.COOPERATE): 0.7528066859262207, (Action.DEFECT, Action.DEFECT): 0.35040796735824997 }


class Stoc344(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.11205355586201327, (Action.COOPERATE, Action.DEFECT): 0.9426610503549898, (Action.DEFECT, Action.COOPERATE): 0.31454605470941166, (Action.DEFECT, Action.DEFECT): 0.23624173044174934 }


class Stoc345(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.9387230693176613, (Action.COOPERATE, Action.DEFECT): 0.5675743194094273, (Action.DEFECT, Action.COOPERATE): 0.31215767189205545, (Action.DEFECT, Action.DEFECT): 0.4809421184437044 }


class Stoc346(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.4968737091889105, (Action.COOPERATE, Action.DEFECT): 0.8890720291452806, (Action.DEFECT, Action.COOPERATE): 0.6239955380119155, (Action.DEFECT, Action.DEFECT): 0.7058149721814978 }


class Stoc347(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.8662454778339325, (Action.COOPERATE, Action.DEFECT): 0.15387418108078676, (Action.DEFECT, Action.COOPERATE): 0.48987914809839017, (Action.DEFECT, Action.DEFECT): 0.11700583034168044 }


class Stoc348(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.33824991401704674, (Action.COOPERATE, Action.DEFECT): 0.8285830258567869, (Action.DEFECT, Action.COOPERATE): 0.13178770928686723, (Action.DEFECT, Action.DEFECT): 0.7210570298080914 }


class Stoc349(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.3354719489115311, (Action.COOPERATE, Action.DEFECT): 0.19763145073953814, (Action.DEFECT, Action.COOPERATE): 0.04907185738645614, (Action.DEFECT, Action.DEFECT): 0.3860073995727483 }


class Stoc350(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.20620312103616623, (Action.COOPERATE, Action.DEFECT): 0.29756612974781127, (Action.DEFECT, Action.COOPERATE): 0.1874853651405204, (Action.DEFECT, Action.DEFECT): 0.3577766779828837 }


class Stoc351(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.39952751017682997, (Action.COOPERATE, Action.DEFECT): 0.6289906036693118, (Action.DEFECT, Action.COOPERATE): 0.7833706440558709, (Action.DEFECT, Action.DEFECT): 0.7166453413794471 }


class Stoc352(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.4130290707328921, (Action.COOPERATE, Action.DEFECT): 0.6047612107206736, (Action.DEFECT, Action.COOPERATE): 0.2785939578976635, (Action.DEFECT, Action.DEFECT): 0.0790919452217439 }


class Stoc353(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.05204128286277576, (Action.COOPERATE, Action.DEFECT): 0.3879830146315326, (Action.DEFECT, Action.COOPERATE): 0.8114841613471572, (Action.DEFECT, Action.DEFECT): 0.7132445216552165 }


class Stoc354(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5286632602310857, (Action.COOPERATE, Action.DEFECT): 0.5390407151474591, (Action.DEFECT, Action.COOPERATE): 0.4826420516192965, (Action.DEFECT, Action.DEFECT): 0.46859292032632993 }


class Stoc355(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.95181303798319, (Action.COOPERATE, Action.DEFECT): 0.9469812128873201, (Action.DEFECT, Action.COOPERATE): 0.07080965596166344, (Action.DEFECT, Action.DEFECT): 0.8081159648346221 }


class Stoc356(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.4206477819166271, (Action.COOPERATE, Action.DEFECT): 0.3953886243756183, (Action.DEFECT, Action.COOPERATE): 0.2854743270614021, (Action.DEFECT, Action.DEFECT): 0.6067806165657189 }


class Stoc357(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.2668622204471861, (Action.COOPERATE, Action.DEFECT): 0.3029368958345593, (Action.DEFECT, Action.COOPERATE): 0.4688341837572708, (Action.DEFECT, Action.DEFECT): 0.8929327096311291 }


class Stoc358(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.14516958462916207, (Action.COOPERATE, Action.DEFECT): 0.42202700899184176, (Action.DEFECT, Action.COOPERATE): 0.5340581103671492, (Action.DEFECT, Action.DEFECT): 0.47860179899251865 }


class Stoc359(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.11796270181049395, (Action.COOPERATE, Action.DEFECT): 0.41405110274752244, (Action.DEFECT, Action.COOPERATE): 0.6762184340485105, (Action.DEFECT, Action.DEFECT): 0.3330211500821427 }


class Stoc360(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.10576395997509602, (Action.COOPERATE, Action.DEFECT): 0.34203885500497533, (Action.DEFECT, Action.COOPERATE): 0.9159096906029313, (Action.DEFECT, Action.DEFECT): 0.4822660386826463 }


class Stoc361(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.04894443850976615, (Action.COOPERATE, Action.DEFECT): 0.1766147488321238, (Action.DEFECT, Action.COOPERATE): 0.8798510799237785, (Action.DEFECT, Action.DEFECT): 0.2247954463366716 }


class Stoc362(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.886665177787184, (Action.COOPERATE, Action.DEFECT): 0.473338905843524, (Action.DEFECT, Action.COOPERATE): 0.8902857213919846, (Action.DEFECT, Action.DEFECT): 0.8445003395046712 }


class Stoc363(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.3319917933746752, (Action.COOPERATE, Action.DEFECT): 0.8019611882697627, (Action.DEFECT, Action.COOPERATE): 0.8192481919175082, (Action.DEFECT, Action.DEFECT): 0.11170615155294539 }


class Stoc364(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.6844396270704239, (Action.COOPERATE, Action.DEFECT): 0.7156805533363296, (Action.DEFECT, Action.COOPERATE): 0.9304150694823288, (Action.DEFECT, Action.DEFECT): 0.4305944323670766 }


class Stoc365(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.7800059650196927, (Action.COOPERATE, Action.DEFECT): 0.03204729094705594, (Action.DEFECT, Action.COOPERATE): 0.6487173024232777, (Action.DEFECT, Action.DEFECT): 0.7821682159531201 }


class Stoc366(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.052008180967815454, (Action.COOPERATE, Action.DEFECT): 0.2055481363917091, (Action.DEFECT, Action.COOPERATE): 0.8713495067710512, (Action.DEFECT, Action.DEFECT): 0.9789414944449715 }


class Stoc367(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.7643892294628234, (Action.COOPERATE, Action.DEFECT): 0.26892447772986705, (Action.DEFECT, Action.COOPERATE): 0.010480842967718007, (Action.DEFECT, Action.DEFECT): 0.6810408010604623 }


class Stoc368(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.33063758754158334, (Action.COOPERATE, Action.DEFECT): 0.5542544924989752, (Action.DEFECT, Action.COOPERATE): 0.2390172213677949, (Action.DEFECT, Action.DEFECT): 0.9191364665859295 }


class Stoc369(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.3430099953731638, (Action.COOPERATE, Action.DEFECT): 0.9947439794104445, (Action.DEFECT, Action.COOPERATE): 0.2149279156469368, (Action.DEFECT, Action.DEFECT): 0.00528307952571605 }


class Stoc370(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.828983016521304, (Action.COOPERATE, Action.DEFECT): 0.6368028359850414, (Action.DEFECT, Action.COOPERATE): 0.7636957585155458, (Action.DEFECT, Action.DEFECT): 0.5699451676479428 }


class Stoc371(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.4605603883071223, (Action.COOPERATE, Action.DEFECT): 0.9097408386671356, (Action.DEFECT, Action.COOPERATE): 0.35567429130127004, (Action.DEFECT, Action.DEFECT): 0.5641630062935832 }


class Stoc372(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.9973758802855159, (Action.COOPERATE, Action.DEFECT): 0.8067824812094812, (Action.DEFECT, Action.COOPERATE): 0.7011407930703989, (Action.DEFECT, Action.DEFECT): 0.6486749823121861 }


class Stoc373(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.8883389435561501, (Action.COOPERATE, Action.DEFECT): 0.5268382334066198, (Action.DEFECT, Action.COOPERATE): 0.3359913996391012, (Action.DEFECT, Action.DEFECT): 0.24757885719558148 }


class Stoc374(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.7228001976888015, (Action.COOPERATE, Action.DEFECT): 0.9494720623266182, (Action.DEFECT, Action.COOPERATE): 0.5339116258678401, (Action.DEFECT, Action.DEFECT): 0.1900678470386249 }


class Stoc375(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.014686293305532394, (Action.COOPERATE, Action.DEFECT): 0.9124758304031013, (Action.DEFECT, Action.COOPERATE): 0.1761490005817169, (Action.DEFECT, Action.DEFECT): 0.49701720875600974 }


class Stoc376(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5994642750245772, (Action.COOPERATE, Action.DEFECT): 0.3426624451032282, (Action.DEFECT, Action.COOPERATE): 0.895916045811205, (Action.DEFECT, Action.DEFECT): 0.045296993480077985 }


class Stoc377(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.35261330736366414, (Action.COOPERATE, Action.DEFECT): 0.22985159625673135, (Action.DEFECT, Action.COOPERATE): 0.36727595542221503, (Action.DEFECT, Action.DEFECT): 0.9646674835031207 }


class Stoc378(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.6619751650833742, (Action.COOPERATE, Action.DEFECT): 0.8733201924958821, (Action.DEFECT, Action.COOPERATE): 0.8542994697508939, (Action.DEFECT, Action.DEFECT): 0.8313966653374342 }


class Stoc379(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.8763319033597261, (Action.COOPERATE, Action.DEFECT): 0.366138068920816, (Action.DEFECT, Action.COOPERATE): 0.5209747955716991, (Action.DEFECT, Action.DEFECT): 0.041904142243651576 }


class Stoc380(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.19515857198379782, (Action.COOPERATE, Action.DEFECT): 0.5500367006926908, (Action.DEFECT, Action.COOPERATE): 0.387187819378085, (Action.DEFECT, Action.DEFECT): 0.700153346268233 }


class Stoc381(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.9536940487599384, (Action.COOPERATE, Action.DEFECT): 0.9957982866169057, (Action.DEFECT, Action.COOPERATE): 0.17049780515955015, (Action.DEFECT, Action.DEFECT): 0.07654786090666621 }


class Stoc382(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.9496125440158685, (Action.COOPERATE, Action.DEFECT): 0.29176260142547594, (Action.DEFECT, Action.COOPERATE): 0.05854515257402715, (Action.DEFECT, Action.DEFECT): 0.6935815630736902 }


class Stoc383(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.1497135049871855, (Action.COOPERATE, Action.DEFECT): 0.6715453774144412, (Action.DEFECT, Action.COOPERATE): 0.9287664681156084, (Action.DEFECT, Action.DEFECT): 0.6289808765976762 }


class Stoc384(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.01723788600522158, (Action.COOPERATE, Action.DEFECT): 0.791697732210451, (Action.DEFECT, Action.COOPERATE): 0.835957314422136, (Action.DEFECT, Action.DEFECT): 0.9671868181415453 }


class Stoc385(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.01887706782851728, (Action.COOPERATE, Action.DEFECT): 0.8939622113792944, (Action.DEFECT, Action.COOPERATE): 0.5674386836467458, (Action.DEFECT, Action.DEFECT): 0.050043190153671535 }


class Stoc386(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.3001311574757326, (Action.COOPERATE, Action.DEFECT): 0.15833900339349039, (Action.DEFECT, Action.COOPERATE): 0.32200753001041393, (Action.DEFECT, Action.DEFECT): 0.06455806878523296 }


class Stoc387(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.8243495902062544, (Action.COOPERATE, Action.DEFECT): 0.7566926610082855, (Action.DEFECT, Action.COOPERATE): 0.9765766094010478, (Action.DEFECT, Action.DEFECT): 0.8122417446218383 }


class Stoc388(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.9298305657756639, (Action.COOPERATE, Action.DEFECT): 0.6009711821028906, (Action.DEFECT, Action.COOPERATE): 0.5615358363379744, (Action.DEFECT, Action.DEFECT): 0.3541743196242003 }


class Stoc389(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.04698077344792717, (Action.COOPERATE, Action.DEFECT): 0.6256358834939152, (Action.DEFECT, Action.COOPERATE): 0.1374053424999634, (Action.DEFECT, Action.DEFECT): 0.5490692103429672 }


class Stoc390(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.8885266936409734, (Action.COOPERATE, Action.DEFECT): 0.3886122904528394, (Action.DEFECT, Action.COOPERATE): 0.0678285820738318, (Action.DEFECT, Action.DEFECT): 0.6414004695840806 }


class Stoc391(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5697381370881628, (Action.COOPERATE, Action.DEFECT): 0.07570464820179568, (Action.DEFECT, Action.COOPERATE): 0.35543284285527166, (Action.DEFECT, Action.DEFECT): 0.09423893522691995 }


class Stoc392(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.3063590925645936, (Action.COOPERATE, Action.DEFECT): 0.13434647425524837, (Action.DEFECT, Action.COOPERATE): 0.26793410650910554, (Action.DEFECT, Action.DEFECT): 0.736558116268748 }


class Stoc393(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.41710938219652327, (Action.COOPERATE, Action.DEFECT): 0.8249513324662833, (Action.DEFECT, Action.COOPERATE): 0.13051223158012903, (Action.DEFECT, Action.DEFECT): 0.6502996465766138 }


class Stoc394(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.47757294776549064, (Action.COOPERATE, Action.DEFECT): 0.6886923319142119, (Action.DEFECT, Action.COOPERATE): 0.3834222013012041, (Action.DEFECT, Action.DEFECT): 0.6062930912641049 }


class Stoc395(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.47134764609913893, (Action.COOPERATE, Action.DEFECT): 0.09042962536653587, (Action.DEFECT, Action.COOPERATE): 0.48829079292077027, (Action.DEFECT, Action.DEFECT): 0.25021320749456355 }


class Stoc396(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.746692858160675, (Action.COOPERATE, Action.DEFECT): 0.9728620600563611, (Action.DEFECT, Action.COOPERATE): 0.6713206911342923, (Action.DEFECT, Action.DEFECT): 0.8105725613413406 }


class Stoc397(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.09147010744831185, (Action.COOPERATE, Action.DEFECT): 0.38530595157054703, (Action.DEFECT, Action.COOPERATE): 0.7591695081801342, (Action.DEFECT, Action.DEFECT): 0.09900584733595907 }


class Stoc398(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.7487073362586264, (Action.COOPERATE, Action.DEFECT): 0.19709724032027043, (Action.DEFECT, Action.COOPERATE): 0.4509500393744367, (Action.DEFECT, Action.DEFECT): 0.4946506243264176 }


class Stoc399(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.93346666399127, (Action.COOPERATE, Action.DEFECT): 0.5793618281966771, (Action.DEFECT, Action.COOPERATE): 0.35321813380080425, (Action.DEFECT, Action.DEFECT): 0.46095244659078405 }


class Stoc400(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5829615997617055, (Action.COOPERATE, Action.DEFECT): 0.0778838043338711, (Action.DEFECT, Action.COOPERATE): 0.6058796421640823, (Action.DEFECT, Action.DEFECT): 0.7651090603667261 }


class Stoc401(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.2676915684537259, (Action.COOPERATE, Action.DEFECT): 0.22699702477648198, (Action.DEFECT, Action.COOPERATE): 0.3740856485728443, (Action.DEFECT, Action.DEFECT): 0.3226518230910357 }


class Stoc402(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.6793442120758046, (Action.COOPERATE, Action.DEFECT): 0.08102080601221906, (Action.DEFECT, Action.COOPERATE): 0.41495472095030916, (Action.DEFECT, Action.DEFECT): 0.30961283316728083 }


class Stoc403(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.2957376469690016, (Action.COOPERATE, Action.DEFECT): 0.30868010600520934, (Action.DEFECT, Action.COOPERATE): 0.9757929077294687, (Action.DEFECT, Action.DEFECT): 0.7280991133647547 }


class Stoc404(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.04237036767639124, (Action.COOPERATE, Action.DEFECT): 0.3228889610259994, (Action.DEFECT, Action.COOPERATE): 0.5862703299766784, (Action.DEFECT, Action.DEFECT): 0.21079382683485937 }


class Stoc405(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.7186651128906368, (Action.COOPERATE, Action.DEFECT): 0.9139215671388892, (Action.DEFECT, Action.COOPERATE): 0.3456998064728879, (Action.DEFECT, Action.DEFECT): 0.4803149859248913 }


class Stoc406(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5243445810121531, (Action.COOPERATE, Action.DEFECT): 0.5939911518734693, (Action.DEFECT, Action.COOPERATE): 0.32864950894947176, (Action.DEFECT, Action.DEFECT): 0.6215259463578044 }


class Stoc407(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.3095099773150205, (Action.COOPERATE, Action.DEFECT): 0.18997042123104912, (Action.DEFECT, Action.COOPERATE): 0.7901907491121896, (Action.DEFECT, Action.DEFECT): 0.1753040817725302 }


class Stoc408(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.09303124243306227, (Action.COOPERATE, Action.DEFECT): 0.5664020690851158, (Action.DEFECT, Action.COOPERATE): 0.6659837860784181, (Action.DEFECT, Action.DEFECT): 0.33802130227150173 }


class Stoc409(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.4525389592809579, (Action.COOPERATE, Action.DEFECT): 0.6479023558009155, (Action.DEFECT, Action.COOPERATE): 0.046731207362432525, (Action.DEFECT, Action.DEFECT): 0.22870534834570844 }


class Stoc410(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.1561651165793816, (Action.COOPERATE, Action.DEFECT): 0.9576625985711686, (Action.DEFECT, Action.COOPERATE): 0.1108915989329643, (Action.DEFECT, Action.DEFECT): 0.23509296164505478 }


class Stoc411(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.43267461821290276, (Action.COOPERATE, Action.DEFECT): 0.8272779988249481, (Action.DEFECT, Action.COOPERATE): 0.3837372334754854, (Action.DEFECT, Action.DEFECT): 0.612878165534535 }


class Stoc412(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.389911245037729, (Action.COOPERATE, Action.DEFECT): 0.05949004811618852, (Action.DEFECT, Action.COOPERATE): 0.7825662958342179, (Action.DEFECT, Action.DEFECT): 0.15699810725667607 }


class Stoc413(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.4000168041176345, (Action.COOPERATE, Action.DEFECT): 0.7100286013035019, (Action.DEFECT, Action.COOPERATE): 0.18111450509870541, (Action.DEFECT, Action.DEFECT): 0.3851394860062608 }


class Stoc414(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.8241215334516554, (Action.COOPERATE, Action.DEFECT): 0.8027978728890931, (Action.DEFECT, Action.COOPERATE): 0.24201962548421152, (Action.DEFECT, Action.DEFECT): 0.9069566931633316 }


class Stoc415(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.7290323859882579, (Action.COOPERATE, Action.DEFECT): 0.1328407126535608, (Action.DEFECT, Action.COOPERATE): 0.18975535056453063, (Action.DEFECT, Action.DEFECT): 0.2255208418866722 }


class Stoc416(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.37235316192424583, (Action.COOPERATE, Action.DEFECT): 0.6073537786008746, (Action.DEFECT, Action.COOPERATE): 0.06167981462381511, (Action.DEFECT, Action.DEFECT): 0.20141736767335106 }


class Stoc417(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.9086357741938769, (Action.COOPERATE, Action.DEFECT): 0.6812203013752189, (Action.DEFECT, Action.COOPERATE): 0.780033007304254, (Action.DEFECT, Action.DEFECT): 0.9357505117245848 }


class Stoc418(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.6335883693448795, (Action.COOPERATE, Action.DEFECT): 0.10639525625250379, (Action.DEFECT, Action.COOPERATE): 0.8092444323652112, (Action.DEFECT, Action.DEFECT): 0.564260035109939 }


class Stoc419(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.6943315433424622, (Action.COOPERATE, Action.DEFECT): 0.8663929442682419, (Action.DEFECT, Action.COOPERATE): 0.9936282306562586, (Action.DEFECT, Action.DEFECT): 0.028456112024095148 }


class Stoc420(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.07970592060332382, (Action.COOPERATE, Action.DEFECT): 0.7485228173188069, (Action.DEFECT, Action.COOPERATE): 0.6829411392980101, (Action.DEFECT, Action.DEFECT): 0.3155882063406278 }


class Stoc421(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.07515500843056377, (Action.COOPERATE, Action.DEFECT): 0.6679659212278841, (Action.DEFECT, Action.COOPERATE): 0.6259926622570624, (Action.DEFECT, Action.DEFECT): 0.8583738384450622 }


class Stoc422(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.37914062086983824, (Action.COOPERATE, Action.DEFECT): 0.4896045846259468, (Action.DEFECT, Action.COOPERATE): 0.01852852376094538, (Action.DEFECT, Action.DEFECT): 0.9569515549790678 }


class Stoc423(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.17616807594648776, (Action.COOPERATE, Action.DEFECT): 0.18339487440623992, (Action.DEFECT, Action.COOPERATE): 0.8087585870584414, (Action.DEFECT, Action.DEFECT): 0.7721905631436679 }


class Stoc424(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.15382818877371884, (Action.COOPERATE, Action.DEFECT): 0.14104912404257708, (Action.DEFECT, Action.COOPERATE): 0.38587369323247955, (Action.DEFECT, Action.DEFECT): 0.9546876974777967 }


class Stoc425(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.7116521424350069, (Action.COOPERATE, Action.DEFECT): 0.3196703556366842, (Action.DEFECT, Action.COOPERATE): 0.37296084559263787, (Action.DEFECT, Action.DEFECT): 0.723050332647297 }


class Stoc426(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.07900199733138402, (Action.COOPERATE, Action.DEFECT): 0.33496870725331007, (Action.DEFECT, Action.COOPERATE): 0.551976624128651, (Action.DEFECT, Action.DEFECT): 0.9949865552151663 }


class Stoc427(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.004033946326644888, (Action.COOPERATE, Action.DEFECT): 0.47758258726634517, (Action.DEFECT, Action.COOPERATE): 0.8105867407839481, (Action.DEFECT, Action.DEFECT): 0.2951134000900061 }


class Stoc428(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.20837689929199554, (Action.COOPERATE, Action.DEFECT): 0.9461801041027208, (Action.DEFECT, Action.COOPERATE): 0.838305351546715, (Action.DEFECT, Action.DEFECT): 0.01940597786911269 }


class Stoc429(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.39608511489163045, (Action.COOPERATE, Action.DEFECT): 0.5199921418615009, (Action.DEFECT, Action.COOPERATE): 0.4748504680584682, (Action.DEFECT, Action.DEFECT): 0.48406503376432963 }


class Stoc430(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5215721350369716, (Action.COOPERATE, Action.DEFECT): 0.35056102941070455, (Action.DEFECT, Action.COOPERATE): 0.7336761763218755, (Action.DEFECT, Action.DEFECT): 0.21891150926399883 }


class Stoc431(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5624608248924043, (Action.COOPERATE, Action.DEFECT): 0.7484094193292558, (Action.DEFECT, Action.COOPERATE): 0.9587404500487978, (Action.DEFECT, Action.DEFECT): 0.6209957993768822 }


class Stoc432(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.7649097667250608, (Action.COOPERATE, Action.DEFECT): 0.3163904440451195, (Action.DEFECT, Action.COOPERATE): 0.32445832254444507, (Action.DEFECT, Action.DEFECT): 0.2842697136180897 }


class Stoc433(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.624948969945327, (Action.COOPERATE, Action.DEFECT): 0.46263145865725086, (Action.DEFECT, Action.COOPERATE): 0.3821349902099038, (Action.DEFECT, Action.DEFECT): 0.9325356360528511 }


class Stoc434(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.258002103377698, (Action.COOPERATE, Action.DEFECT): 0.8267320334518985, (Action.DEFECT, Action.COOPERATE): 0.8083673651256339, (Action.DEFECT, Action.DEFECT): 0.4622193305426596 }


class Stoc435(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.9248955905615108, (Action.COOPERATE, Action.DEFECT): 0.8532695008847361, (Action.DEFECT, Action.COOPERATE): 0.6623991487010684, (Action.DEFECT, Action.DEFECT): 0.7622161473834871 }


class Stoc436(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.7121660162681694, (Action.COOPERATE, Action.DEFECT): 0.5258967062930875, (Action.DEFECT, Action.COOPERATE): 0.10385341540698145, (Action.DEFECT, Action.DEFECT): 0.4581929535137901 }


class Stoc437(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.3362736593485307, (Action.COOPERATE, Action.DEFECT): 0.11548918953660958, (Action.DEFECT, Action.COOPERATE): 0.6185738585664265, (Action.DEFECT, Action.DEFECT): 0.2668116328489849 }


class Stoc438(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.570505918765586, (Action.COOPERATE, Action.DEFECT): 0.7373579464873249, (Action.DEFECT, Action.COOPERATE): 0.6284511918038549, (Action.DEFECT, Action.DEFECT): 0.15307303839159037 }


class Stoc439(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.9714698605748251, (Action.COOPERATE, Action.DEFECT): 0.39422008171144396, (Action.DEFECT, Action.COOPERATE): 0.15597092951020097, (Action.DEFECT, Action.DEFECT): 0.7771465528107806 }


class Stoc440(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.32758614588468404, (Action.COOPERATE, Action.DEFECT): 0.020085444894143434, (Action.DEFECT, Action.COOPERATE): 0.6165597732198401, (Action.DEFECT, Action.DEFECT): 0.5657346140141761 }


class Stoc441(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.9363354961055784, (Action.COOPERATE, Action.DEFECT): 0.6351105404553656, (Action.DEFECT, Action.COOPERATE): 0.09894949243487083, (Action.DEFECT, Action.DEFECT): 0.1131157931214235 }


class Stoc442(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.05072753496753657, (Action.COOPERATE, Action.DEFECT): 0.8769992774624548, (Action.DEFECT, Action.COOPERATE): 0.9060579997392034, (Action.DEFECT, Action.DEFECT): 0.6489939399593087 }


class Stoc443(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5406152740664097, (Action.COOPERATE, Action.DEFECT): 0.24072479859064777, (Action.DEFECT, Action.COOPERATE): 0.5084536999139159, (Action.DEFECT, Action.DEFECT): 0.3323857440167718 }


class Stoc444(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.3670696673441418, (Action.COOPERATE, Action.DEFECT): 0.3854389026145788, (Action.DEFECT, Action.COOPERATE): 0.5683215224132165, (Action.DEFECT, Action.DEFECT): 0.7331090131690354 }


class Stoc445(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.07559685731250221, (Action.COOPERATE, Action.DEFECT): 0.09669942021123468, (Action.DEFECT, Action.COOPERATE): 0.4417731430848397, (Action.DEFECT, Action.DEFECT): 0.050878785415534145 }


class Stoc446(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.3732085093178876, (Action.COOPERATE, Action.DEFECT): 0.9475298044641443, (Action.DEFECT, Action.COOPERATE): 0.7312277466359689, (Action.DEFECT, Action.DEFECT): 0.20039579700779375 }


class Stoc447(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.03192356049952105, (Action.COOPERATE, Action.DEFECT): 0.755814340436025, (Action.DEFECT, Action.COOPERATE): 0.20153008861636101, (Action.DEFECT, Action.DEFECT): 0.20896688609578085 }


class Stoc448(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.6787002911647785, (Action.COOPERATE, Action.DEFECT): 0.7835293447072074, (Action.DEFECT, Action.COOPERATE): 0.1749713205379838, (Action.DEFECT, Action.DEFECT): 0.9859183942949462 }


class Stoc449(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.09721563765719499, (Action.COOPERATE, Action.DEFECT): 0.7882531455287732, (Action.DEFECT, Action.COOPERATE): 0.9671182553465407, (Action.DEFECT, Action.DEFECT): 0.10188864221386418 }


class Stoc450(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.21114916605418121, (Action.COOPERATE, Action.DEFECT): 0.5135610255543165, (Action.DEFECT, Action.COOPERATE): 0.6022131173246976, (Action.DEFECT, Action.DEFECT): 0.1551756582699133 }


class Stoc451(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.11327655861984876, (Action.COOPERATE, Action.DEFECT): 0.7079267183365527, (Action.DEFECT, Action.COOPERATE): 0.7266765649791923, (Action.DEFECT, Action.DEFECT): 0.3106888762661123 }


class Stoc452(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.32696273121935504, (Action.COOPERATE, Action.DEFECT): 0.5394117990750045, (Action.DEFECT, Action.COOPERATE): 0.5015342067305714, (Action.DEFECT, Action.DEFECT): 0.10780799710039812 }


class Stoc453(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.27993170158012326, (Action.COOPERATE, Action.DEFECT): 0.7132512091275431, (Action.DEFECT, Action.COOPERATE): 0.5231827587445587, (Action.DEFECT, Action.DEFECT): 0.4019679115433513 }


class Stoc454(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.6980904480507557, (Action.COOPERATE, Action.DEFECT): 0.9150615976141994, (Action.DEFECT, Action.COOPERATE): 0.03926118541158208, (Action.DEFECT, Action.DEFECT): 0.15037149208573408 }


class Stoc455(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.6922243061315099, (Action.COOPERATE, Action.DEFECT): 0.18620510993888229, (Action.DEFECT, Action.COOPERATE): 0.11762485941821399, (Action.DEFECT, Action.DEFECT): 0.5489672455938476 }


class Stoc456(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.447638740963333, (Action.COOPERATE, Action.DEFECT): 0.19906215185740117, (Action.DEFECT, Action.COOPERATE): 0.4479150281415737, (Action.DEFECT, Action.DEFECT): 0.5633305450703568 }


class Stoc457(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.17908995122554727, (Action.COOPERATE, Action.DEFECT): 0.877447020379908, (Action.DEFECT, Action.COOPERATE): 0.5663542560385915, (Action.DEFECT, Action.DEFECT): 0.9249433832008778 }


class Stoc458(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.1400239272537357, (Action.COOPERATE, Action.DEFECT): 0.47097002459954496, (Action.DEFECT, Action.COOPERATE): 0.025680626593774902, (Action.DEFECT, Action.DEFECT): 0.4013147212927638 }


class Stoc459(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.6233257801960054, (Action.COOPERATE, Action.DEFECT): 0.8829116400537025, (Action.DEFECT, Action.COOPERATE): 0.6055998903815304, (Action.DEFECT, Action.DEFECT): 0.8632416321136018 }


class Stoc460(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.2740791212702316, (Action.COOPERATE, Action.DEFECT): 0.9715051233000644, (Action.DEFECT, Action.COOPERATE): 0.8440124617616325, (Action.DEFECT, Action.DEFECT): 0.6977491814416715 }


class Stoc461(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.9639338086320443, (Action.COOPERATE, Action.DEFECT): 0.23790017806087083, (Action.DEFECT, Action.COOPERATE): 0.6395544802658897, (Action.DEFECT, Action.DEFECT): 0.40349691967238754 }


class Stoc462(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5136224077513499, (Action.COOPERATE, Action.DEFECT): 0.919470227932431, (Action.DEFECT, Action.COOPERATE): 0.27919772541419063, (Action.DEFECT, Action.DEFECT): 0.8186116321866128 }


class Stoc463(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.13979032959079418, (Action.COOPERATE, Action.DEFECT): 0.3359576414444909, (Action.DEFECT, Action.COOPERATE): 0.10904487454355416, (Action.DEFECT, Action.DEFECT): 0.6554614589251058 }


class Stoc464(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.9570976366131111, (Action.COOPERATE, Action.DEFECT): 0.36258076775829773, (Action.DEFECT, Action.COOPERATE): 0.3794735075929878, (Action.DEFECT, Action.DEFECT): 0.8216880580396544 }


class Stoc465(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.07934181897582138, (Action.COOPERATE, Action.DEFECT): 0.9398302136799298, (Action.DEFECT, Action.COOPERATE): 0.03407175297910969, (Action.DEFECT, Action.DEFECT): 0.14739670265283888 }


class Stoc466(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.276877531626624, (Action.COOPERATE, Action.DEFECT): 0.005433105693836926, (Action.DEFECT, Action.COOPERATE): 0.45271272840629706, (Action.DEFECT, Action.DEFECT): 0.358504535903878 }


class Stoc467(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.06927685792675897, (Action.COOPERATE, Action.DEFECT): 0.743216831686374, (Action.DEFECT, Action.COOPERATE): 0.4836759793149772, (Action.DEFECT, Action.DEFECT): 0.282240720245826 }


class Stoc468(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5852592143560235, (Action.COOPERATE, Action.DEFECT): 0.06673799691794458, (Action.DEFECT, Action.COOPERATE): 0.3315320828650665, (Action.DEFECT, Action.DEFECT): 0.008928983073392738 }


class Stoc469(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.16786310875714605, (Action.COOPERATE, Action.DEFECT): 0.20519741979628958, (Action.DEFECT, Action.COOPERATE): 0.6887844971854993, (Action.DEFECT, Action.DEFECT): 0.8108469940203051 }


class Stoc470(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.662984611078308, (Action.COOPERATE, Action.DEFECT): 0.4957175930666792, (Action.DEFECT, Action.COOPERATE): 0.5115994886286672, (Action.DEFECT, Action.DEFECT): 0.39267971081489417 }


class Stoc471(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5995678868781047, (Action.COOPERATE, Action.DEFECT): 0.48663787511488643, (Action.DEFECT, Action.COOPERATE): 0.1821626012184695, (Action.DEFECT, Action.DEFECT): 0.49730211227441123 }


class Stoc472(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.45125032302793866, (Action.COOPERATE, Action.DEFECT): 0.19555980171262743, (Action.DEFECT, Action.COOPERATE): 0.4658485354191262, (Action.DEFECT, Action.DEFECT): 0.6942489368201598 }


class Stoc473(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.7492462376110577, (Action.COOPERATE, Action.DEFECT): 0.13981593176534424, (Action.DEFECT, Action.COOPERATE): 0.7677415012488011, (Action.DEFECT, Action.DEFECT): 0.5474088239759195 }


class Stoc474(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5779155646230522, (Action.COOPERATE, Action.DEFECT): 0.08582561671873945, (Action.DEFECT, Action.COOPERATE): 0.10314412000103124, (Action.DEFECT, Action.DEFECT): 0.7517696124476873 }


class Stoc475(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.36458998783008045, (Action.COOPERATE, Action.DEFECT): 0.8601789966043677, (Action.DEFECT, Action.COOPERATE): 0.34692221887521335, (Action.DEFECT, Action.DEFECT): 0.26256140209700807 }


class Stoc476(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.2059281461841389, (Action.COOPERATE, Action.DEFECT): 0.806090528116238, (Action.DEFECT, Action.COOPERATE): 0.00624651150253297, (Action.DEFECT, Action.DEFECT): 0.03297934122531598 }


class Stoc477(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.17590574657254732, (Action.COOPERATE, Action.DEFECT): 0.4899608840314923, (Action.DEFECT, Action.COOPERATE): 0.6982989181333258, (Action.DEFECT, Action.DEFECT): 0.8423810792241989 }


class Stoc478(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.9859534913651902, (Action.COOPERATE, Action.DEFECT): 0.5506806356179347, (Action.DEFECT, Action.COOPERATE): 0.5981917748160996, (Action.DEFECT, Action.DEFECT): 0.828793156394353 }


class Stoc479(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.6889350708750723, (Action.COOPERATE, Action.DEFECT): 0.7463334431089894, (Action.DEFECT, Action.COOPERATE): 0.5020952147348704, (Action.DEFECT, Action.DEFECT): 0.45310424985644593 }


class Stoc480(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.2545861806946188, (Action.COOPERATE, Action.DEFECT): 0.1881481368098955, (Action.DEFECT, Action.COOPERATE): 0.791026605522734, (Action.DEFECT, Action.DEFECT): 0.41269730086809286 }


class Stoc481(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.8345875690034625, (Action.COOPERATE, Action.DEFECT): 0.3570711900151329, (Action.DEFECT, Action.COOPERATE): 0.0014941605732023966, (Action.DEFECT, Action.DEFECT): 0.5395742240712016 }


class Stoc482(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.13822318645858, (Action.COOPERATE, Action.DEFECT): 0.6756579025638113, (Action.DEFECT, Action.COOPERATE): 0.5916759910014778, (Action.DEFECT, Action.DEFECT): 0.09992500326777298 }


class Stoc483(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.1465372788397563, (Action.COOPERATE, Action.DEFECT): 0.5468865926148396, (Action.DEFECT, Action.COOPERATE): 0.9566618128186695, (Action.DEFECT, Action.DEFECT): 0.7655046690762548 }


class Stoc484(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.7010987110786923, (Action.COOPERATE, Action.DEFECT): 0.1513939747858819, (Action.DEFECT, Action.COOPERATE): 0.04387703356046113, (Action.DEFECT, Action.DEFECT): 0.8830963290434322 }


class Stoc485(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.6784661079987754, (Action.COOPERATE, Action.DEFECT): 0.06360092015768493, (Action.DEFECT, Action.COOPERATE): 0.18210232625001976, (Action.DEFECT, Action.DEFECT): 0.9839851721942591 }


class Stoc486(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.9508181360932284, (Action.COOPERATE, Action.DEFECT): 0.5863384988126645, (Action.DEFECT, Action.COOPERATE): 0.3837162410308701, (Action.DEFECT, Action.DEFECT): 0.17154895656340774 }


class Stoc487(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.6119444378583883, (Action.COOPERATE, Action.DEFECT): 0.5436233439348409, (Action.DEFECT, Action.COOPERATE): 0.13179596274856964, (Action.DEFECT, Action.DEFECT): 0.2912083231927395 }


class Stoc488(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.1291360487566201, (Action.COOPERATE, Action.DEFECT): 0.995980120601403, (Action.DEFECT, Action.COOPERATE): 0.502786162583017, (Action.DEFECT, Action.DEFECT): 0.28204138630202136 }


class Stoc489(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.2631622661176558, (Action.COOPERATE, Action.DEFECT): 0.531473132682341, (Action.DEFECT, Action.COOPERATE): 0.6269080646797098, (Action.DEFECT, Action.DEFECT): 0.9645730421513107 }


class Stoc490(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5215625073193252, (Action.COOPERATE, Action.DEFECT): 0.5335507349870177, (Action.DEFECT, Action.COOPERATE): 0.3973446313079211, (Action.DEFECT, Action.DEFECT): 0.20819139030287226 }


class Stoc491(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.8289278932555306, (Action.COOPERATE, Action.DEFECT): 0.25589689940234084, (Action.DEFECT, Action.COOPERATE): 0.9835634754523142, (Action.DEFECT, Action.DEFECT): 0.3115235988993341 }


class Stoc492(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5409142731032739, (Action.COOPERATE, Action.DEFECT): 0.6239831931879083, (Action.DEFECT, Action.COOPERATE): 0.39858197061514744, (Action.DEFECT, Action.DEFECT): 0.9998470323640266 }


class Stoc493(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.19496187068674664, (Action.COOPERATE, Action.DEFECT): 0.3221775253575452, (Action.DEFECT, Action.COOPERATE): 0.6950716891746958, (Action.DEFECT, Action.DEFECT): 0.7672801047336525 }


class Stoc494(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.6836883267718047, (Action.COOPERATE, Action.DEFECT): 0.3434250982247187, (Action.DEFECT, Action.COOPERATE): 0.5993675210762494, (Action.DEFECT, Action.DEFECT): 0.014642224169485019 }


class Stoc495(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.46840804246477796, (Action.COOPERATE, Action.DEFECT): 0.9856596773484678, (Action.DEFECT, Action.COOPERATE): 0.571207648935163, (Action.DEFECT, Action.DEFECT): 0.8391973989559179 }


class Stoc496(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.43285769158084597, (Action.COOPERATE, Action.DEFECT): 0.34149114141840475, (Action.DEFECT, Action.COOPERATE): 0.24810985022451892, (Action.DEFECT, Action.DEFECT): 0.14811175285154132 }


class Stoc497(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.4603747599391267, (Action.COOPERATE, Action.DEFECT): 0.4210926439551236, (Action.DEFECT, Action.COOPERATE): 0.3811748663541632, (Action.DEFECT, Action.DEFECT): 0.40226099535483273 }


class Stoc498(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.29384011360689566, (Action.COOPERATE, Action.DEFECT): 0.8041170054752921, (Action.DEFECT, Action.COOPERATE): 0.8165428222689619, (Action.DEFECT, Action.DEFECT): 0.5026839059330561 }


class Stoc499(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.7088140269567735, (Action.COOPERATE, Action.DEFECT): 0.4332074443666569, (Action.DEFECT, Action.COOPERATE): 0.3999794905169183, (Action.DEFECT, Action.DEFECT): 0.03924310764640926 }




STOC_AGENTS = [ Stoc0,Stoc1,Stoc2,Stoc3,Stoc4,Stoc5,Stoc6,Stoc7,Stoc8,Stoc9,Stoc10,Stoc11,Stoc12,Stoc13,Stoc14,Stoc15,Stoc16,Stoc17,Stoc18,Stoc19,Stoc20,Stoc21,Stoc22,Stoc23,Stoc24,Stoc25,Stoc26,Stoc27,Stoc28,Stoc29,Stoc30,Stoc31,Stoc32,Stoc33,Stoc34,Stoc35,Stoc36,Stoc37,Stoc38,Stoc39,Stoc40,Stoc41,Stoc42,Stoc43,Stoc44,Stoc45,Stoc46,Stoc47,Stoc48,Stoc49,Stoc50,Stoc51,Stoc52,Stoc53,Stoc54,Stoc55,Stoc56,Stoc57,Stoc58,Stoc59,Stoc60,Stoc61,Stoc62,Stoc63,Stoc64,Stoc65,Stoc66,Stoc67,Stoc68,Stoc69,Stoc70,Stoc71,Stoc72,Stoc73,Stoc74,Stoc75,Stoc76,Stoc77,Stoc78,Stoc79,Stoc80,Stoc81,Stoc82,Stoc83,Stoc84,Stoc85,Stoc86,Stoc87,Stoc88,Stoc89,Stoc90,Stoc91,Stoc92,Stoc93,Stoc94,Stoc95,Stoc96,Stoc97,Stoc98,Stoc99,Stoc100,Stoc101,Stoc102,Stoc103,Stoc104,Stoc105,Stoc106,Stoc107,Stoc108,Stoc109,Stoc110,Stoc111,Stoc112,Stoc113,Stoc114,Stoc115,Stoc116,Stoc117,Stoc118,Stoc119,Stoc120,Stoc121,Stoc122,Stoc123,Stoc124,Stoc125,Stoc126,Stoc127,Stoc128,Stoc129,Stoc130,Stoc131,Stoc132,Stoc133,Stoc134,Stoc135,Stoc136,Stoc137,Stoc138,Stoc139,Stoc140,Stoc141,Stoc142,Stoc143,Stoc144,Stoc145,Stoc146,Stoc147,Stoc148,Stoc149,Stoc150,Stoc151,Stoc152,Stoc153,Stoc154,Stoc155,Stoc156,Stoc157,Stoc158,Stoc159,Stoc160,Stoc161,Stoc162,Stoc163,Stoc164,Stoc165,Stoc166,Stoc167,Stoc168,Stoc169,Stoc170,Stoc171,Stoc172,Stoc173,Stoc174,Stoc175,Stoc176,Stoc177,Stoc178,Stoc179,Stoc180,Stoc181,Stoc182,Stoc183,Stoc184,Stoc185,Stoc186,Stoc187,Stoc188,Stoc189,Stoc190,Stoc191,Stoc192,Stoc193,Stoc194,Stoc195,Stoc196,Stoc197,Stoc198,Stoc199,Stoc200,Stoc201,Stoc202,Stoc203,Stoc204,Stoc205,Stoc206,Stoc207,Stoc208,Stoc209,Stoc210,Stoc211,Stoc212,Stoc213,Stoc214,Stoc215,Stoc216,Stoc217,Stoc218,Stoc219,Stoc220,Stoc221,Stoc222,Stoc223,Stoc224,Stoc225,Stoc226,Stoc227,Stoc228,Stoc229,Stoc230,Stoc231,Stoc232,Stoc233,Stoc234,Stoc235,Stoc236,Stoc237,Stoc238,Stoc239,Stoc240,Stoc241,Stoc242,Stoc243,Stoc244,Stoc245,Stoc246,Stoc247,Stoc248,Stoc249,Stoc250,Stoc251,Stoc252,Stoc253,Stoc254,Stoc255,Stoc256,Stoc257,Stoc258,Stoc259,Stoc260,Stoc261,Stoc262,Stoc263,Stoc264,Stoc265,Stoc266,Stoc267,Stoc268,Stoc269,Stoc270,Stoc271,Stoc272,Stoc273,Stoc274,Stoc275,Stoc276,Stoc277,Stoc278,Stoc279,Stoc280,Stoc281,Stoc282,Stoc283,Stoc284,Stoc285,Stoc286,Stoc287,Stoc288,Stoc289,Stoc290,Stoc291,Stoc292,Stoc293,Stoc294,Stoc295,Stoc296,Stoc297,Stoc298,Stoc299,Stoc300,Stoc301,Stoc302,Stoc303,Stoc304,Stoc305,Stoc306,Stoc307,Stoc308,Stoc309,Stoc310,Stoc311,Stoc312,Stoc313,Stoc314,Stoc315,Stoc316,Stoc317,Stoc318,Stoc319,Stoc320,Stoc321,Stoc322,Stoc323,Stoc324,Stoc325,Stoc326,Stoc327,Stoc328,Stoc329,Stoc330,Stoc331,Stoc332,Stoc333,Stoc334,Stoc335,Stoc336,Stoc337,Stoc338,Stoc339,Stoc340,Stoc341,Stoc342,Stoc343,Stoc344,Stoc345,Stoc346,Stoc347,Stoc348,Stoc349,Stoc350,Stoc351,Stoc352,Stoc353,Stoc354,Stoc355,Stoc356,Stoc357,Stoc358,Stoc359,Stoc360,Stoc361,Stoc362,Stoc363,Stoc364,Stoc365,Stoc366,Stoc367,Stoc368,Stoc369,Stoc370,Stoc371,Stoc372,Stoc373,Stoc374,Stoc375,Stoc376,Stoc377,Stoc378,Stoc379,Stoc380,Stoc381,Stoc382,Stoc383,Stoc384,Stoc385,Stoc386,Stoc387,Stoc388,Stoc389,Stoc390,Stoc391,Stoc392,Stoc393,Stoc394,Stoc395,Stoc396,Stoc397,Stoc398,Stoc399,Stoc400,Stoc401,Stoc402,Stoc403,Stoc404,Stoc405,Stoc406,Stoc407,Stoc408,Stoc409,Stoc410,Stoc411,Stoc412,Stoc413,Stoc414,Stoc415,Stoc416,Stoc417,Stoc418,Stoc419,Stoc420,Stoc421,Stoc422,Stoc423,Stoc424,Stoc425,Stoc426,Stoc427,Stoc428,Stoc429,Stoc430,Stoc431,Stoc432,Stoc433,Stoc434,Stoc435,Stoc436,Stoc437,Stoc438,Stoc439,Stoc440,Stoc441,Stoc442,Stoc443,Stoc444,Stoc445,Stoc446,Stoc447,Stoc448,Stoc449,Stoc450,Stoc451,Stoc452,Stoc453,Stoc454,Stoc455,Stoc456,Stoc457,Stoc458,Stoc459,Stoc460,Stoc461,Stoc462,Stoc463,Stoc464,Stoc465,Stoc466,Stoc467,Stoc468,Stoc469,Stoc470,Stoc471,Stoc472,Stoc473,Stoc474,Stoc475,Stoc476,Stoc477,Stoc478,Stoc479,Stoc480,Stoc481,Stoc482,Stoc483,Stoc484,Stoc485,Stoc486,Stoc487,Stoc488,Stoc489,Stoc490,Stoc491,Stoc492,Stoc493,Stoc494,Stoc495,Stoc496,Stoc497,Stoc498,Stoc499]


STOC_HYPERPARAMS = {'Stoc0': {'p_cc': 0.24555198035154002, 'p_cd': 0.6689138330233754, 'p_dc': 0.9094055193691336, 'p_dd': 0.26130955248599574}, 'Stoc1': {'p_cc': 0.6434809118932705, 'p_cd': 0.9527022385704482, 'p_dc': 0.4594417812850451, 'p_dd': 0.004331505318258211}, 'Stoc2': {'p_cc': 0.03406234655659324, 'p_cd': 0.40364092588576295, 'p_dc': 0.03864841874161229, 'p_dd': 0.5635169885547961}, 'Stoc3': {'p_cc': 0.05797725066432835, 'p_cd': 0.5307121577458125, 'p_dc': 0.7134569862560709, 'p_dd': 0.9252681396944807}, 'Stoc4': {'p_cc': 0.578361877262347, 'p_cd': 0.2707399172747419, 'p_dc': 0.21018411337230425, 'p_dd': 0.32773055158260145}, 'Stoc5': {'p_cc': 0.355583073160022, 'p_cd': 0.03464048089584881, 'p_dc': 0.13294725132277496, 'p_dd': 0.38686517934879205}, 'Stoc6': {'p_cc': 0.29402799576762395, 'p_cd': 0.003994859666313966, 'p_dc': 0.7301750343209867, 'p_dd': 0.415405565937195}, 'Stoc7': {'p_cc': 0.9540068344357912, 'p_cd': 0.7306629776087092, 'p_dc': 0.2377325920387554, 'p_dd': 0.9624160929519162}, 'Stoc8': {'p_cc': 0.21997562090745038, 'p_cd': 0.6255389579965568, 'p_dc': 0.42137057855740634, 'p_dd': 0.12533079720298923}, 'Stoc9': {'p_cc': 0.903611483606926, 'p_cd': 0.033189560653139716, 'p_dc': 0.0060233543179002424, 'p_dd': 0.310862203708019}, 'Stoc10': {'p_cc': 0.13946570835704009, 'p_cd': 0.1003919881646822, 'p_dc': 0.564091687922157, 'p_dd': 0.2532799253068492}, 'Stoc11': {'p_cc': 0.46012691814910367, 'p_cd': 0.1093300250990209, 'p_dc': 0.92591398315716, 'p_dd': 0.02200221654825163}, 'Stoc12': {'p_cc': 0.7210984036536764, 'p_cd': 0.04159367129228875, 'p_dc': 0.48738141714211114, 'p_dd': 0.21732437233698443}, 'Stoc13': {'p_cc': 0.24431746948820543, 'p_cd': 0.7753693144337314, 'p_dc': 0.5996557759291836, 'p_dd': 0.45523512711674174}, 'Stoc14': {'p_cc': 0.9119542583670177, 'p_cd': 0.6197116293034924, 'p_dc': 0.29428007778197474, 'p_dd': 0.9802404369373245}, 'Stoc15': {'p_cc': 0.7482550796979737, 'p_cd': 0.6822703719120007, 'p_dc': 0.3131164676286381, 'p_dd': 0.3770904870628461}, 'Stoc16': {'p_cc': 0.9045280532988547, 'p_cd': 0.8096633200881911, 'p_dc': 0.0329491735247468, 'p_dd': 0.21514082033903226}, 'Stoc17': {'p_cc': 0.22973350689937877, 'p_cd': 0.5323738423256549, 'p_dc': 0.5342008277943291, 'p_dd': 0.3351262690918504}, 'Stoc18': {'p_cc': 0.29813063482557967, 'p_cd': 0.3550600527976512, 'p_dc': 0.6467637770765942, 'p_dd': 0.4720672526217117}, 'Stoc19': {'p_cc': 0.2787675885661589, 'p_cd': 0.5668150353632064, 'p_dc': 0.6574833922443439, 'p_dd': 0.0005273566626349258}, 'Stoc20': {'p_cc': 0.9679316532422065, 'p_cd': 0.9930375636577186, 'p_dc': 0.508908544595752, 'p_dd': 0.18337707610547804}, 'Stoc21': {'p_cc': 0.9146778714341666, 'p_cd': 0.5257068926711905, 'p_dc': 0.25068730477553114, 'p_dd': 0.26720943365278893}, 'Stoc22': {'p_cc': 0.10563578834193421, 'p_cd': 0.6552914430171511, 'p_dc': 0.5405886829639728, 'p_dd': 0.6994235056704322}, 'Stoc23': {'p_cc': 0.6266350618090202, 'p_cd': 0.5667493019611046, 'p_dc': 0.2235584188304428, 'p_dd': 0.04302550020449436}, 'Stoc24': {'p_cc': 0.8854261680432118, 'p_cd': 0.03276925187105484, 'p_dc': 0.7424817802270463, 'p_dd': 0.6432927700742592}, 'Stoc25': {'p_cc': 0.7033976953544395, 'p_cd': 0.41219111130440644, 'p_dc': 0.3246590337540034, 'p_dd': 0.6793043983318916}, 'Stoc26': {'p_cc': 0.9350139026527069, 'p_cd': 0.0622941374882644, 'p_dc': 0.4032650647948375, 'p_dd': 0.6528574613331762}, 'Stoc27': {'p_cc': 0.9457382844992196, 'p_cd': 0.040690510403396996, 'p_dc': 0.8381773133724917, 'p_dd': 0.25373931111705894}, 'Stoc28': {'p_cc': 0.8603215859547623, 'p_cd': 0.8706839095352594, 'p_dc': 0.9358367770107265, 'p_dd': 0.6230039665217292}, 'Stoc29': {'p_cc': 0.8257129349535292, 'p_cd': 0.8338080477154006, 'p_dc': 0.2222822430104101, 'p_dd': 0.6256851051822283}, 'Stoc30': {'p_cc': 0.4705018311846747, 'p_cd': 0.2042185075676568, 'p_dc': 0.5333814648418512, 'p_dd': 0.4230164751406347}, 'Stoc31': {'p_cc': 0.3524969099296412, 'p_cd': 0.3283173237972332, 'p_dc': 0.21880109250886182, 'p_dd': 0.09525980439984238}, 'Stoc32': {'p_cc': 0.5204467471797322, 'p_cd': 0.15814559115536242, 'p_dc': 0.2465953301742202, 'p_dd': 0.12354871444121518}, 'Stoc33': {'p_cc': 0.9569120568827945, 'p_cd': 0.755386614118337, 'p_dc': 0.09030046109880807, 'p_dd': 0.5049902359937181}, 'Stoc34': {'p_cc': 0.7725885995200135, 'p_cd': 0.2942030179660712, 'p_dc': 0.6464225645710301, 'p_dd': 0.589104306261808}, 'Stoc35': {'p_cc': 0.998421517890145, 'p_cd': 0.33589949241113803, 'p_dc': 0.7705577792876779, 'p_dd': 0.32455641466431595}, 'Stoc36': {'p_cc': 0.3930464700799473, 'p_cd': 0.9624769353904528, 'p_dc': 0.5009682830230255, 'p_dd': 0.009012082955532796}, 'Stoc37': {'p_cc': 0.08332593384227427, 'p_cd': 0.047817006187663824, 'p_dc': 0.9083031264915898, 'p_dd': 0.48506213964817924}, 'Stoc38': {'p_cc': 0.32858566204396966, 'p_cd': 0.30640947740278335, 'p_dc': 0.3680213322513205, 'p_dd': 0.2679709667289121}, 'Stoc39': {'p_cc': 0.455282791595386, 'p_cd': 0.2879060335889292, 'p_dc': 0.5100577228660369, 'p_dd': 0.7893714246141885}, 'Stoc40': {'p_cc': 0.4666177727031854, 'p_cd': 0.668142804673361, 'p_dc': 0.14503415612031167, 'p_dd': 0.06677940338412736}, 'Stoc41': {'p_cc': 0.28270098570757196, 'p_cd': 0.21692450137764585, 'p_dc': 0.10984081322712258, 'p_dd': 0.09868381179576224}, 'Stoc42': {'p_cc': 0.2831276262801, 'p_cd': 0.15197776342005542, 'p_dc': 0.9714354707077721, 'p_dd': 0.1271990348346702}, 'Stoc43': {'p_cc': 0.6101396970883693, 'p_cd': 0.47015455624417735, 'p_dc': 0.12183085209582922, 'p_dd': 0.2429038354223253}, 'Stoc44': {'p_cc': 0.52700294410562, 'p_cd': 0.9458075820588094, 'p_dc': 0.5363985311380839, 'p_dd': 0.21841106219891304}, 'Stoc45': {'p_cc': 0.6985148610825832, 'p_cd': 0.7349827916584952, 'p_dc': 0.24558833102197208, 'p_dd': 0.691311294448296}, 'Stoc46': {'p_cc': 0.888296962984728, 'p_cd': 0.620161513939621, 'p_dc': 0.71623030181864, 'p_dd': 0.37645868570494667}, 'Stoc47': {'p_cc': 0.761611703269811, 'p_cd': 0.6684942114208136, 'p_dc': 0.5208796156769303, 'p_dd': 0.4072758202080774}, 'Stoc48': {'p_cc': 0.46204325743075614, 'p_cd': 0.5233700221577949, 'p_dc': 0.6042599402233563, 'p_dd': 0.8552189650770854}, 'Stoc49': {'p_cc': 0.8485980677378232, 'p_cd': 0.5610300245915624, 'p_dc': 0.3218067961275354, 'p_dd': 0.877755304696451}, 'Stoc50': {'p_cc': 0.45032481511449596, 'p_cd': 0.35438052626254046, 'p_dc': 0.8752428696632496, 'p_dd': 0.021734179509899754}, 'Stoc51': {'p_cc': 0.5742697310681144, 'p_cd': 0.1758458728708655, 'p_dc': 0.08338419690705712, 'p_dd': 0.08595017427565033}, 'Stoc52': {'p_cc': 0.22544259762043906, 'p_cd': 0.9470792416398783, 'p_dc': 0.7417116707975098, 'p_dd': 0.5512967447548568}, 'Stoc53': {'p_cc': 0.9290565256945246, 'p_cd': 0.6080203515801893, 'p_dc': 0.48917885696282026, 'p_dd': 0.9230389474482616}, 'Stoc54': {'p_cc': 0.7616095868245583, 'p_cd': 0.7518457463334428, 'p_dc': 0.26136501962562264, 'p_dd': 0.4590547213448767}, 'Stoc55': {'p_cc': 0.8480192443027368, 'p_cd': 0.5964688637229312, 'p_dc': 0.4053258091924601, 'p_dd': 0.30808567680480015}, 'Stoc56': {'p_cc': 0.6574685801392158, 'p_cd': 0.3887776067219135, 'p_dc': 0.474348640384304, 'p_dd': 0.0963810597348187}, 'Stoc57': {'p_cc': 0.39790764330759754, 'p_cd': 0.9707582923072421, 'p_dc': 0.8150401649943101, 'p_dd': 0.9690663943897644}, 'Stoc58': {'p_cc': 0.8606451136990755, 'p_cd': 0.4065841471838426, 'p_dc': 0.7660951546614193, 'p_dd': 0.08027858227601925}, 'Stoc59': {'p_cc': 0.08849179743877933, 'p_cd': 0.18799045681181425, 'p_dc': 0.6716235343100901, 'p_dd': 0.7761108229345605}, 'Stoc60': {'p_cc': 0.1652267437825442, 'p_cd': 0.02199318055373678, 'p_dc': 0.5431307338682256, 'p_dd': 0.526288589836196}, 'Stoc61': {'p_cc': 0.8603920197575516, 'p_cd': 0.49744627715146605, 'p_dc': 0.8620255101454486, 'p_dd': 0.879992838545905}, 'Stoc62': {'p_cc': 0.4202546255697366, 'p_cd': 0.2552400973430141, 'p_dc': 0.6368888228242873, 'p_dd': 0.7247690332568114}, 'Stoc63': {'p_cc': 0.5539963451834998, 'p_cd': 0.31147507733657276, 'p_dc': 0.45136662205912903, 'p_dd': 0.5470007493085689}, 'Stoc64': {'p_cc': 0.8210496084223728, 'p_cd': 0.0007243756413928271, 'p_dc': 0.48732422002585474, 'p_dd': 0.8381320457223569}, 'Stoc65': {'p_cc': 0.7412765739435052, 'p_cd': 0.31820285002725934, 'p_dc': 0.7893451466533873, 'p_dd': 0.43747457425706415}, 'Stoc66': {'p_cc': 0.8982638637506498, 'p_cd': 0.826342935318325, 'p_dc': 0.36129268813842197, 'p_dd': 0.7811082049686151}, 'Stoc67': {'p_cc': 0.9793152085314719, 'p_cd': 0.9982479167661823, 'p_dc': 0.23868511139713966, 'p_dd': 0.7876874885387257}, 'Stoc68': {'p_cc': 0.20956368164674588, 'p_cd': 0.8932628242857878, 'p_dc': 0.9791768495917936, 'p_dd': 0.4642159819293644}, 'Stoc69': {'p_cc': 0.13119050769633034, 'p_cd': 0.46330350743150783, 'p_dc': 0.6874467778511003, 'p_dd': 0.9781088264663822}, 'Stoc70': {'p_cc': 0.4850994150342869, 'p_cd': 0.014022033113094912, 'p_dc': 0.40797306115276655, 'p_dd': 0.4479338750062186}, 'Stoc71': {'p_cc': 0.2613690538526825, 'p_cd': 0.44371536982328275, 'p_dc': 0.9342334643642877, 'p_dd': 0.6310258899146641}, 'Stoc72': {'p_cc': 0.06138986700229099, 'p_cd': 0.4547348577840884, 'p_dc': 0.033194304208610914, 'p_dd': 0.3728878938586636}, 'Stoc73': {'p_cc': 0.08965954269461607, 'p_cd': 0.6020345904184227, 'p_dc': 0.010021742583354087, 'p_dd': 0.15346998283316104}, 'Stoc74': {'p_cc': 0.5404863517193383, 'p_cd': 0.6507302859086906, 'p_dc': 0.9195997782822396, 'p_dd': 0.9186678080805907}, 'Stoc75': {'p_cc': 0.17700235488750016, 'p_cd': 0.941150134051194, 'p_dc': 0.32151063854825346, 'p_dd': 0.8229106174156999}, 'Stoc76': {'p_cc': 0.9724340883834263, 'p_cd': 0.10641730761256396, 'p_dc': 0.4025965854270537, 'p_dd': 0.5835175588024558}, 'Stoc77': {'p_cc': 0.48101050395335454, 'p_cd': 0.6275258919947833, 'p_dc': 0.5335027400326287, 'p_dd': 0.007416238260647412}, 'Stoc78': {'p_cc': 0.6941799391087348, 'p_cd': 0.8329487710050248, 'p_dc': 0.867052997209027, 'p_dd': 0.9599833553606051}, 'Stoc79': {'p_cc': 0.6667026283983063, 'p_cd': 0.8950050891063462, 'p_dc': 0.6848441407360306, 'p_dd': 0.6934232643844787}, 'Stoc80': {'p_cc': 0.5625024220216499, 'p_cd': 0.44566089406985676, 'p_dc': 0.8617108533403153, 'p_dd': 0.9245515668862584}, 'Stoc81': {'p_cc': 0.8377607199272427, 'p_cd': 0.906335596345318, 'p_dc': 0.7578220268847189, 'p_dd': 0.26128322928238257}, 'Stoc82': {'p_cc': 0.044250223871733274, 'p_cd': 0.23032458047848747, 'p_dc': 0.8026008150554612, 'p_dd': 0.3253588813038871}, 'Stoc83': {'p_cc': 0.6216074287837501, 'p_cd': 0.6232057506849089, 'p_dc': 0.930173517142538, 'p_dd': 0.11821267225882826}, 'Stoc84': {'p_cc': 0.1429556943569792, 'p_cd': 0.5236731069862467, 'p_dc': 0.692594365840037, 'p_dd': 0.2664474646632745}, 'Stoc85': {'p_cc': 0.36727564379553534, 'p_cd': 0.380976441008509, 'p_dc': 0.022151761769413802, 'p_dd': 0.7946840386196782}, 'Stoc86': {'p_cc': 0.8206420190406282, 'p_cd': 0.29263438196095226, 'p_dc': 0.32744789844056366, 'p_dd': 0.7407314735557265}, 'Stoc87': {'p_cc': 0.9213636968475741, 'p_cd': 0.8487602207415373, 'p_dc': 0.011744437236327121, 'p_dd': 0.3420233714797697}, 'Stoc88': {'p_cc': 0.12438712773272032, 'p_cd': 0.13872288045133863, 'p_dc': 0.3657736454669219, 'p_dd': 0.4166744164238593}, 'Stoc89': {'p_cc': 0.9412655490280184, 'p_cd': 0.1859541749966459, 'p_dc': 0.2249207331697861, 'p_dd': 0.8056605302166695}, 'Stoc90': {'p_cc': 0.18007313892418852, 'p_cd': 0.20078654985131716, 'p_dc': 0.01737491515027423, 'p_dd': 0.1958751188998772}, 'Stoc91': {'p_cc': 0.6611545067564258, 'p_cd': 0.2636807453387776, 'p_dc': 0.6314694453733073, 'p_dd': 0.34553892202934056}, 'Stoc92': {'p_cc': 0.19868222705844396, 'p_cd': 0.06966477198406429, 'p_dc': 0.5217293408075796, 'p_dd': 0.21117929346947018}, 'Stoc93': {'p_cc': 0.7277110254361271, 'p_cd': 0.8212514027659039, 'p_dc': 0.9245124817112804, 'p_dd': 0.7933399782270586}, 'Stoc94': {'p_cc': 0.8083994527542947, 'p_cd': 0.2190750858386843, 'p_dc': 0.9614236608903135, 'p_dd': 0.8932276386239763}, 'Stoc95': {'p_cc': 0.6287030125974655, 'p_cd': 0.7358220902603789, 'p_dc': 0.04888373978368499, 'p_dd': 0.3753361982930794}, 'Stoc96': {'p_cc': 0.3275827035947557, 'p_cd': 0.03326648571474489, 'p_dc': 0.6231457451756053, 'p_dd': 0.011586689481839496}, 'Stoc97': {'p_cc': 0.8338694002144922, 'p_cd': 0.873776986457856, 'p_dc': 0.9860323852584378, 'p_dd': 0.08101035719960814}, 'Stoc98': {'p_cc': 0.4585822967349379, 'p_cd': 0.2069885131459751, 'p_dc': 0.4355432038729018, 'p_dd': 0.7488323313518882}, 'Stoc99': {'p_cc': 0.9206100218211557, 'p_cd': 0.5808919405725447, 'p_dc': 0.32376037518564826, 'p_dd': 0.6307184167814762}, 'Stoc100': {'p_cc': 0.857417003298197, 'p_cd': 0.9169736644826626, 'p_dc': 0.5433534160801399, 'p_dd': 0.8316353443638754}, 'Stoc101': {'p_cc': 0.39568817154131997, 'p_cd': 0.6299365254457299, 'p_dc': 0.9811784628550668, 'p_dd': 0.9778870007791512}, 'Stoc102': {'p_cc': 0.3170815290337856, 'p_cd': 0.6542937168890385, 'p_dc': 0.08108127446919333, 'p_dd': 0.8880561820076129}, 'Stoc103': {'p_cc': 0.8453601028078177, 'p_cd': 0.8747665651166718, 'p_dc': 0.9149641554119852, 'p_dd': 0.41543662537248693}, 'Stoc104': {'p_cc': 0.3999591732296698, 'p_cd': 0.44881999648393167, 'p_dc': 0.11721966146508467, 'p_dd': 0.040151965202402495}, 'Stoc105': {'p_cc': 0.710084567117013, 'p_cd': 0.22816310460768718, 'p_dc': 0.009726591679690921, 'p_dd': 0.7495575776144153}, 'Stoc106': {'p_cc': 0.5865543424564661, 'p_cd': 0.5623967658105353, 'p_dc': 0.29747318060162364, 'p_dd': 0.6449246302534148}, 'Stoc107': {'p_cc': 0.4831442234736374, 'p_cd': 0.6677024300024682, 'p_dc': 0.06102521993825527, 'p_dd': 0.944240095404506}, 'Stoc108': {'p_cc': 0.4502156817126769, 'p_cd': 0.8918708977836246, 'p_dc': 0.06683948076441149, 'p_dd': 0.9009348640704858}, 'Stoc109': {'p_cc': 0.7544402625638046, 'p_cd': 0.15078175813339056, 'p_dc': 0.7614331758178212, 'p_dd': 0.5121379173349055}, 'Stoc110': {'p_cc': 0.568253607501865, 'p_cd': 0.46618846353117394, 'p_dc': 0.22345804617271847, 'p_dd': 0.6041274700478134}, 'Stoc111': {'p_cc': 0.18949091301702214, 'p_cd': 0.3304747586785187, 'p_dc': 0.6147737370744301, 'p_dd': 0.5960215204542911}, 'Stoc112': {'p_cc': 0.3819695216600637, 'p_cd': 0.3670837376546403, 'p_dc': 0.8418837219258939, 'p_dd': 0.15507098777180395}, 'Stoc113': {'p_cc': 0.18058557889871074, 'p_cd': 0.018925345077290268, 'p_dc': 0.8399197401856718, 'p_dd': 0.0757137549003124}, 'Stoc114': {'p_cc': 0.5823611797274225, 'p_cd': 0.6684420510600094, 'p_dc': 0.6714515315148842, 'p_dd': 0.19818035261517863}, 'Stoc115': {'p_cc': 0.255684949996981, 'p_cd': 0.30779247631649087, 'p_dc': 0.8747931250788279, 'p_dd': 0.028300569841126832}, 'Stoc116': {'p_cc': 0.7713410796947855, 'p_cd': 0.2480438790523375, 'p_dc': 0.21555589917466345, 'p_dd': 0.38960130566170625}, 'Stoc117': {'p_cc': 0.7699172848758024, 'p_cd': 0.7883022542146874, 'p_dc': 0.08046702834705632, 'p_dd': 0.12156842951193503}, 'Stoc118': {'p_cc': 0.8562782096067278, 'p_cd': 0.20133181948518053, 'p_dc': 0.1856740721992125, 'p_dd': 0.07113972289227022}, 'Stoc119': {'p_cc': 0.8917572989987822, 'p_cd': 0.7037151520314388, 'p_dc': 0.026362169207947983, 'p_dd': 0.4717798848468999}, 'Stoc120': {'p_cc': 0.7246807510034585, 'p_cd': 0.8695417757875359, 'p_dc': 0.886076235850941, 'p_dd': 0.09129232006287602}, 'Stoc121': {'p_cc': 0.16562185096164206, 'p_cd': 0.06241388285890426, 'p_dc': 0.5503116520678242, 'p_dd': 0.48955540513459306}, 'Stoc122': {'p_cc': 0.34805163884259505, 'p_cd': 0.03636154522417101, 'p_dc': 0.017524183409411753, 'p_dd': 0.7948846024112134}, 'Stoc123': {'p_cc': 0.6004205152088871, 'p_cd': 0.1357097063898095, 'p_dc': 0.333941249575998, 'p_dd': 0.9366937011819967}, 'Stoc124': {'p_cc': 0.07735025370694637, 'p_cd': 0.08835684289764989, 'p_dc': 0.9872878977895552, 'p_dd': 0.1612923971310667}, 'Stoc125': {'p_cc': 0.813595754050417, 'p_cd': 0.162837137945831, 'p_dc': 0.5622397512730358, 'p_dd': 0.1554522119942342}, 'Stoc126': {'p_cc': 0.7299030822648505, 'p_cd': 0.2162177006036512, 'p_dc': 0.6752197932387793, 'p_dd': 0.029597965318688302}, 'Stoc127': {'p_cc': 0.6814276352817246, 'p_cd': 0.5813269663863203, 'p_dc': 0.20112351407066353, 'p_dd': 0.8119993233278858}, 'Stoc128': {'p_cc': 0.1975957545171726, 'p_cd': 0.9767304907184792, 'p_dc': 0.09734123802572114, 'p_dd': 0.06721022978025049}, 'Stoc129': {'p_cc': 0.8047060844235847, 'p_cd': 0.9224275075508597, 'p_dc': 0.447027724949144, 'p_dd': 0.004114235063378158}, 'Stoc130': {'p_cc': 0.4620231893541895, 'p_cd': 0.37931195120490335, 'p_dc': 0.6095141841915002, 'p_dd': 0.9924938949420099}, 'Stoc131': {'p_cc': 0.5587843700143265, 'p_cd': 0.40346964967771626, 'p_dc': 0.952421642990698, 'p_dd': 0.7479571830106763}, 'Stoc132': {'p_cc': 0.12870960133470433, 'p_cd': 0.002725358852181281, 'p_dc': 0.9985492501090197, 'p_dd': 0.4836731638988423}, 'Stoc133': {'p_cc': 0.3408839393487577, 'p_cd': 0.9258924822901351, 'p_dc': 0.2576199133033472, 'p_dd': 0.5866478127995369}, 'Stoc134': {'p_cc': 0.20539881315504538, 'p_cd': 0.7457360320137859, 'p_dc': 0.9922457588562231, 'p_dd': 0.6883327430219893}, 'Stoc135': {'p_cc': 0.14656433761597665, 'p_cd': 0.1453280999804406, 'p_dc': 0.41766901989628147, 'p_dd': 0.31563274772924665}, 'Stoc136': {'p_cc': 0.419990086202647, 'p_cd': 0.9347940659517722, 'p_dc': 0.2571536872517497, 'p_dd': 0.9060609883403954}, 'Stoc137': {'p_cc': 0.9303511121296902, 'p_cd': 0.25654793008625776, 'p_dc': 0.9959304618461974, 'p_dd': 0.14328013835048703}, 'Stoc138': {'p_cc': 0.1550929736480735, 'p_cd': 0.5191358491140482, 'p_dc': 0.9672262541727852, 'p_dd': 0.42286488220333585}, 'Stoc139': {'p_cc': 0.1891113877842061, 'p_cd': 0.34780644827675156, 'p_dc': 0.24402046589477855, 'p_dd': 0.08506496102539074}, 'Stoc140': {'p_cc': 0.632138682525744, 'p_cd': 0.2901040819982701, 'p_dc': 0.7773287442197415, 'p_dd': 0.5043744284592299}, 'Stoc141': {'p_cc': 0.2091471831760925, 'p_cd': 0.5399307176624998, 'p_dc': 0.7802845493476444, 'p_dd': 0.23467945579798455}, 'Stoc142': {'p_cc': 0.5577926325857906, 'p_cd': 0.13852233984689943, 'p_dc': 0.4308243683351204, 'p_dd': 0.5425169688039843}, 'Stoc143': {'p_cc': 0.6737567480602543, 'p_cd': 0.001691391792417729, 'p_dc': 0.5505359754980116, 'p_dd': 0.18361320336677123}, 'Stoc144': {'p_cc': 0.4048662226844434, 'p_cd': 0.5123675001278434, 'p_dc': 0.29447917507292765, 'p_dd': 0.3747892218660275}, 'Stoc145': {'p_cc': 0.652676896925552, 'p_cd': 0.12772895508357074, 'p_dc': 0.6989377936959599, 'p_dd': 0.04488724384719667}, 'Stoc146': {'p_cc': 0.5955303311632774, 'p_cd': 0.4307827437264542, 'p_dc': 0.7280652334601175, 'p_dd': 0.8265231710604557}, 'Stoc147': {'p_cc': 0.2961389479269707, 'p_cd': 0.6404712011279073, 'p_dc': 0.3154691070050947, 'p_dd': 0.38984467120723176}, 'Stoc148': {'p_cc': 0.9589549086366645, 'p_cd': 0.7251329140670102, 'p_dc': 0.6988127489127165, 'p_dd': 0.4458125409545153}, 'Stoc149': {'p_cc': 0.44828252959833215, 'p_cd': 0.4062362284245584, 'p_dc': 0.8735511194724644, 'p_dd': 0.795692536224389}, 'Stoc150': {'p_cc': 0.9488583239481262, 'p_cd': 0.40799361164652326, 'p_dc': 0.7569963327058027, 'p_dd': 0.6077968199965219}, 'Stoc151': {'p_cc': 0.43970523241100856, 'p_cd': 0.228054804832304, 'p_dc': 0.14813419367695213, 'p_dd': 0.6229534709477285}, 'Stoc152': {'p_cc': 0.772620033510795, 'p_cd': 0.051025513520853494, 'p_dc': 0.3327099560137122, 'p_dd': 0.19720110468034469}, 'Stoc153': {'p_cc': 0.7698943717976668, 'p_cd': 0.4258876263321477, 'p_dc': 0.9986378333565193, 'p_dd': 0.15231752136393917}, 'Stoc154': {'p_cc': 0.4981735032032186, 'p_cd': 0.5736865247794659, 'p_dc': 0.8046769474820145, 'p_dd': 0.4677582005917432}, 'Stoc155': {'p_cc': 0.5904518947685312, 'p_cd': 0.7348036376202056, 'p_dc': 0.16072036175550208, 'p_dd': 0.9399694681028578}, 'Stoc156': {'p_cc': 0.279831371452954, 'p_cd': 0.07348706172067576, 'p_dc': 0.7861870726827401, 'p_dd': 0.18067977155454307}, 'Stoc157': {'p_cc': 0.8260436470978768, 'p_cd': 0.022276687464868883, 'p_dc': 0.3093265500445451, 'p_dd': 0.7526465201242889}, 'Stoc158': {'p_cc': 0.24919508486444208, 'p_cd': 0.11442262187571273, 'p_dc': 0.6358944713527717, 'p_dd': 0.42954560861540025}, 'Stoc159': {'p_cc': 0.8619221168032739, 'p_cd': 0.46761550346736735, 'p_dc': 0.11414853116944224, 'p_dd': 0.6537856820148448}, 'Stoc160': {'p_cc': 0.34297583443776813, 'p_cd': 0.9966388539123341, 'p_dc': 0.6949940887315059, 'p_dd': 0.9050147908605366}, 'Stoc161': {'p_cc': 0.11613121398763582, 'p_cd': 0.7392355746296284, 'p_dc': 0.48659646871760476, 'p_dd': 0.17770670416173184}, 'Stoc162': {'p_cc': 0.9026929891391141, 'p_cd': 0.8428026177669727, 'p_dc': 0.921280570623468, 'p_dd': 0.4953483114145918}, 'Stoc163': {'p_cc': 0.8107226842802944, 'p_cd': 0.22046972512994933, 'p_dc': 0.18995025103814855, 'p_dd': 0.5723591106782636}, 'Stoc164': {'p_cc': 0.4853008051369889, 'p_cd': 0.11006408555095182, 'p_dc': 0.961113599471648, 'p_dd': 0.09169488703450768}, 'Stoc165': {'p_cc': 0.9501945207999739, 'p_cd': 0.7700156320240217, 'p_dc': 0.8180750070420781, 'p_dd': 0.589705627570822}, 'Stoc166': {'p_cc': 0.3211548920716162, 'p_cd': 0.6869366996975843, 'p_dc': 0.26064910909913686, 'p_dd': 0.8616507886719359}, 'Stoc167': {'p_cc': 0.4480000223656727, 'p_cd': 0.5683143154900756, 'p_dc': 0.7861744632222557, 'p_dd': 0.35215404222875313}, 'Stoc168': {'p_cc': 0.8983137989891793, 'p_cd': 0.3543163032717409, 'p_dc': 0.3067437375867317, 'p_dd': 0.27271084949293034}, 'Stoc169': {'p_cc': 0.8115029119213887, 'p_cd': 0.4768298871026704, 'p_dc': 0.8533525942921136, 'p_dd': 0.17779057926483766}, 'Stoc170': {'p_cc': 0.5507840847129875, 'p_cd': 0.7145056848447372, 'p_dc': 0.8476991799038115, 'p_dd': 0.8039778232287456}, 'Stoc171': {'p_cc': 0.7262954935837634, 'p_cd': 0.09017682512662162, 'p_dc': 0.8273024100727986, 'p_dd': 0.278924545926559}, 'Stoc172': {'p_cc': 0.21327058129374676, 'p_cd': 0.9794383308170588, 'p_dc': 0.668847434208247, 'p_dd': 0.8451446130037231}, 'Stoc173': {'p_cc': 0.9634828835239486, 'p_cd': 0.39615150039023306, 'p_dc': 0.5494222127736949, 'p_dd': 0.6730743220992982}, 'Stoc174': {'p_cc': 0.25527637914469703, 'p_cd': 0.6141406344165836, 'p_dc': 0.37078568007583623, 'p_dd': 0.02692789698241249}, 'Stoc175': {'p_cc': 0.4812945387619636, 'p_cd': 0.4629400838905302, 'p_dc': 0.01747688845911699, 'p_dd': 0.2231638271499835}, 'Stoc176': {'p_cc': 0.8846066380892764, 'p_cd': 0.356601925940642, 'p_dc': 0.8232577428402712, 'p_dd': 0.18253385058354143}, 'Stoc177': {'p_cc': 0.9963522537952577, 'p_cd': 0.7596541926355868, 'p_dc': 0.938773305431125, 'p_dd': 0.43029074598951755}, 'Stoc178': {'p_cc': 0.9878412788453445, 'p_cd': 0.24619474921681306, 'p_dc': 0.41027194814904766, 'p_dd': 0.22973096275275073}, 'Stoc179': {'p_cc': 0.003845199901548413, 'p_cd': 0.3113970159194597, 'p_dc': 0.9339177799194052, 'p_dd': 0.8669226279643458}, 'Stoc180': {'p_cc': 0.9355982961288708, 'p_cd': 0.7938554823865337, 'p_dc': 0.08553692523025913, 'p_dd': 0.6758527828987002}, 'Stoc181': {'p_cc': 0.8399145304124972, 'p_cd': 0.6078657450628834, 'p_dc': 0.07283119033669183, 'p_dd': 0.40326146071338576}, 'Stoc182': {'p_cc': 0.8477395937674712, 'p_cd': 0.5118772588643101, 'p_dc': 0.7911480575603006, 'p_dd': 0.21657131152586062}, 'Stoc183': {'p_cc': 0.8314555211763852, 'p_cd': 0.3680528276813443, 'p_dc': 0.4707637268443725, 'p_dd': 0.24944267506994888}, 'Stoc184': {'p_cc': 0.26018450510864033, 'p_cd': 0.4199090857106923, 'p_dc': 0.6300997805246977, 'p_dd': 0.03334943669653234}, 'Stoc185': {'p_cc': 0.44998911541938014, 'p_cd': 0.7545394269502652, 'p_dc': 0.3380944929680394, 'p_dd': 0.639840814133092}, 'Stoc186': {'p_cc': 0.5870521919283843, 'p_cd': 0.5601027713306701, 'p_dc': 0.24960473939329042, 'p_dd': 0.7385912034798336}, 'Stoc187': {'p_cc': 0.02516132200661869, 'p_cd': 0.8641637003900535, 'p_dc': 0.8819225824282586, 'p_dd': 0.09586647363901712}, 'Stoc188': {'p_cc': 0.7107771275906398, 'p_cd': 0.12479628251703023, 'p_dc': 0.3190349510988312, 'p_dd': 0.28652247372855955}, 'Stoc189': {'p_cc': 0.8847257478341185, 'p_cd': 0.8116962981175663, 'p_dc': 0.08700239906462515, 'p_dd': 0.6726662505971562}, 'Stoc190': {'p_cc': 0.6921482304783564, 'p_cd': 0.6804378528716903, 'p_dc': 0.7201839713697389, 'p_dd': 0.39268338829711524}, 'Stoc191': {'p_cc': 0.31569397861590687, 'p_cd': 0.7824301296330597, 'p_dc': 0.7688459894520092, 'p_dd': 0.6608373972588414}, 'Stoc192': {'p_cc': 0.3276408037304155, 'p_cd': 0.11496454133111833, 'p_dc': 0.3838143729835767, 'p_dd': 0.8299136385300817}, 'Stoc193': {'p_cc': 0.2082580818540264, 'p_cd': 0.8483975828038258, 'p_dc': 0.19534115734614288, 'p_dd': 0.8767192698824358}, 'Stoc194': {'p_cc': 0.9257159752719133, 'p_cd': 0.6620884725135002, 'p_dc': 0.9178697153641663, 'p_dd': 0.09703368495159836}, 'Stoc195': {'p_cc': 0.36598848195631284, 'p_cd': 0.36771435608762193, 'p_dc': 0.6493779580308109, 'p_dd': 0.420127999028199}, 'Stoc196': {'p_cc': 0.9930180137266137, 'p_cd': 0.3493205744923358, 'p_dc': 0.17274939082680674, 'p_dd': 0.3726714546367368}, 'Stoc197': {'p_cc': 0.6309643825995851, 'p_cd': 0.6769401042360292, 'p_dc': 0.214318523563913, 'p_dd': 0.3853067729750487}, 'Stoc198': {'p_cc': 0.7270957262191917, 'p_cd': 0.935754071025023, 'p_dc': 0.6066149144013395, 'p_dd': 0.813838076209029}, 'Stoc199': {'p_cc': 0.0064150362107198156, 'p_cd': 0.37277783548293275, 'p_dc': 0.4679861754035114, 'p_dd': 0.976505042280034}, 'Stoc200': {'p_cc': 0.4597981001339084, 'p_cd': 0.522352659985699, 'p_dc': 0.4353407469732574, 'p_dd': 0.002383209971864364}, 'Stoc201': {'p_cc': 0.9716971747000137, 'p_cd': 0.9241125015640982, 'p_dc': 0.06381774186924494, 'p_dd': 0.6479542273754187}, 'Stoc202': {'p_cc': 0.33203100738988145, 'p_cd': 0.40085273778573527, 'p_dc': 0.7468105767263488, 'p_dd': 0.6824499632441884}, 'Stoc203': {'p_cc': 0.44047594321897565, 'p_cd': 0.7218169456215668, 'p_dc': 0.12444230420613589, 'p_dd': 0.2662787383145224}, 'Stoc204': {'p_cc': 0.981083300516125, 'p_cd': 0.1436415384547105, 'p_dc': 0.47686673908375765, 'p_dd': 0.38160839504127475}, 'Stoc205': {'p_cc': 0.7806050874607025, 'p_cd': 0.3229061445852389, 'p_dc': 0.17349443812900356, 'p_dd': 0.9918185277827707}, 'Stoc206': {'p_cc': 0.6991782991567564, 'p_cd': 0.9842977231213981, 'p_dc': 0.36617138908524116, 'p_dd': 0.5608744806825099}, 'Stoc207': {'p_cc': 0.5770635055063946, 'p_cd': 0.01139985799239962, 'p_dc': 0.7730354080660173, 'p_dd': 0.6964724705378669}, 'Stoc208': {'p_cc': 0.772546168124448, 'p_cd': 0.23355083856834935, 'p_dc': 0.5645371227148583, 'p_dd': 0.6041956041170807}, 'Stoc209': {'p_cc': 0.26724013643019895, 'p_cd': 0.7251731063104168, 'p_dc': 0.45033689406729316, 'p_dd': 0.1066795255803189}, 'Stoc210': {'p_cc': 0.11432655806711434, 'p_cd': 0.12268751495233765, 'p_dc': 0.5836848089396469, 'p_dd': 0.25284450251054424}, 'Stoc211': {'p_cc': 0.9361344450122981, 'p_cd': 0.9003804004113111, 'p_dc': 0.19121105636269686, 'p_dd': 0.5042211335695399}, 'Stoc212': {'p_cc': 0.43839655824448753, 'p_cd': 0.5517521723623503, 'p_dc': 0.8684711054910582, 'p_dd': 0.6933054914963676}, 'Stoc213': {'p_cc': 0.31304485648386904, 'p_cd': 0.01601350134694579, 'p_dc': 0.8630651910191379, 'p_dd': 0.03865406240929414}, 'Stoc214': {'p_cc': 0.6609630657495824, 'p_cd': 0.8750350410967231, 'p_dc': 0.5467299353965991, 'p_dd': 0.19168390254770584}, 'Stoc215': {'p_cc': 0.2066435561435881, 'p_cd': 0.13415506887054918, 'p_dc': 0.40583036149801655, 'p_dd': 0.871458478001958}, 'Stoc216': {'p_cc': 0.032888608632130056, 'p_cd': 0.7444011889788705, 'p_dc': 0.9121633627938821, 'p_dd': 0.0026847128030715872}, 'Stoc217': {'p_cc': 0.8937090148983616, 'p_cd': 0.05069946743402809, 'p_dc': 0.9333352889024078, 'p_dd': 0.3526790804561808}, 'Stoc218': {'p_cc': 0.0950648432224156, 'p_cd': 0.5902515558246588, 'p_dc': 0.019412820792732544, 'p_dd': 0.14149069465137531}, 'Stoc219': {'p_cc': 0.8232932152765559, 'p_cd': 0.18985923258827175, 'p_dc': 0.08485229196305555, 'p_dd': 0.5085797209693795}, 'Stoc220': {'p_cc': 0.03352729335099347, 'p_cd': 0.9771873851793977, 'p_dc': 0.49500093806163514, 'p_dd': 0.1689739848347095}, 'Stoc221': {'p_cc': 0.5456030577426262, 'p_cd': 0.23036656383157295, 'p_dc': 0.005463151904294472, 'p_dd': 0.7405253736274338}, 'Stoc222': {'p_cc': 0.9433090000218403, 'p_cd': 0.23631388349870042, 'p_dc': 0.372126919502917, 'p_dd': 0.00013560461089845433}, 'Stoc223': {'p_cc': 0.8144349059426327, 'p_cd': 0.09605224996784467, 'p_dc': 0.5031249317541696, 'p_dd': 0.1020145053237741}, 'Stoc224': {'p_cc': 0.6958952418496467, 'p_cd': 0.0526125675104373, 'p_dc': 0.6591731748386679, 'p_dd': 0.14505714150071936}, 'Stoc225': {'p_cc': 0.9903457546807807, 'p_cd': 0.2401754469206252, 'p_dc': 0.9381766546258152, 'p_dd': 0.029213107715732933}, 'Stoc226': {'p_cc': 0.23660582207301195, 'p_cd': 0.4953058102880431, 'p_dc': 0.4521865920493451, 'p_dd': 0.2747356130861065}, 'Stoc227': {'p_cc': 0.44275481559311125, 'p_cd': 0.7798839538921534, 'p_dc': 0.8884321980685065, 'p_dd': 0.5014358144115507}, 'Stoc228': {'p_cc': 0.9213456804197897, 'p_cd': 0.005488232718083186, 'p_dc': 0.8770464532823995, 'p_dd': 0.3998393408079969}, 'Stoc229': {'p_cc': 0.7652359409119001, 'p_cd': 0.6751463430458896, 'p_dc': 0.3962513358282047, 'p_dd': 0.445372462168548}, 'Stoc230': {'p_cc': 0.1686995741151851, 'p_cd': 0.15208358640078834, 'p_dc': 0.9431097478187482, 'p_dd': 0.7637848588131307}, 'Stoc231': {'p_cc': 0.42590598926858647, 'p_cd': 0.5647514953878758, 'p_dc': 0.39460301697294875, 'p_dd': 0.21679490081102115}, 'Stoc232': {'p_cc': 0.5156458647913603, 'p_cd': 0.04421834194142993, 'p_dc': 0.8566384291021267, 'p_dd': 0.5630482935121838}, 'Stoc233': {'p_cc': 0.7618954199903304, 'p_cd': 0.6479753645758224, 'p_dc': 0.5664201578094931, 'p_dd': 0.015031826728484243}, 'Stoc234': {'p_cc': 0.2088514939940762, 'p_cd': 0.9908475414543557, 'p_dc': 0.9945410861937951, 'p_dd': 0.20824982305649364}, 'Stoc235': {'p_cc': 0.3041203684637105, 'p_cd': 0.8568892793416555, 'p_dc': 0.8538034695053285, 'p_dd': 0.5543650295102207}, 'Stoc236': {'p_cc': 0.4016548111202758, 'p_cd': 0.8108253470939767, 'p_dc': 0.198449292630283, 'p_dd': 0.3982689753936556}, 'Stoc237': {'p_cc': 0.004690061523766942, 'p_cd': 0.12192700351191965, 'p_dc': 0.6557449281540202, 'p_dd': 0.8676202563413972}, 'Stoc238': {'p_cc': 0.6115398719943622, 'p_cd': 0.5654891308679053, 'p_dc': 0.8870386143308155, 'p_dd': 0.6719225147257644}, 'Stoc239': {'p_cc': 0.09848913285171645, 'p_cd': 0.8547412513906728, 'p_dc': 0.14984016098564967, 'p_dd': 0.8661865496671531}, 'Stoc240': {'p_cc': 0.17025597307818985, 'p_cd': 0.638895288900332, 'p_dc': 0.7324206730870877, 'p_dd': 0.20654066816381145}, 'Stoc241': {'p_cc': 0.7162882465906917, 'p_cd': 0.8505255171040726, 'p_dc': 0.2566691177114919, 'p_dd': 0.7350386810084978}, 'Stoc242': {'p_cc': 0.8867525045212468, 'p_cd': 0.8708934775186705, 'p_dc': 0.8551902010211182, 'p_dd': 0.026311959446002176}, 'Stoc243': {'p_cc': 0.341302671769373, 'p_cd': 0.8284587693280796, 'p_dc': 0.6614417679595489, 'p_dd': 0.5578187483033529}, 'Stoc244': {'p_cc': 0.684170898117988, 'p_cd': 0.4866837666826973, 'p_dc': 0.03642148617886343, 'p_dd': 0.03214237780434437}, 'Stoc245': {'p_cc': 0.6203065988474232, 'p_cd': 0.41512848615589315, 'p_dc': 0.866528722725183, 'p_dd': 0.42133064304683276}, 'Stoc246': {'p_cc': 0.11324092664229335, 'p_cd': 0.667285944383968, 'p_dc': 0.5749997743068721, 'p_dd': 0.8080094480843075}, 'Stoc247': {'p_cc': 0.3932105858300148, 'p_cd': 0.12974038918742326, 'p_dc': 0.9508290115078207, 'p_dd': 0.5478367784171563}, 'Stoc248': {'p_cc': 0.06686146643335678, 'p_cd': 0.5033608994020475, 'p_dc': 0.22795097537737619, 'p_dd': 0.947202706866822}, 'Stoc249': {'p_cc': 0.0376963314512998, 'p_cd': 0.8358457571723689, 'p_dc': 0.15729940226520067, 'p_dd': 0.5058148606705173}, 'Stoc250': {'p_cc': 0.5857590664218187, 'p_cd': 0.12012898337227229, 'p_dc': 0.2744937773595466, 'p_dd': 0.9366090091458971}, 'Stoc251': {'p_cc': 0.5493973879544941, 'p_cd': 0.7023534885447973, 'p_dc': 0.5968095874867753, 'p_dd': 0.6340040866559741}, 'Stoc252': {'p_cc': 0.15266607249497144, 'p_cd': 0.9992589242263014, 'p_dc': 0.760653547943587, 'p_dd': 0.8945409117382617}, 'Stoc253': {'p_cc': 0.86681166189041, 'p_cd': 0.9806261336649358, 'p_dc': 0.5248985330621088, 'p_dd': 0.9398514713597336}, 'Stoc254': {'p_cc': 0.7229570765738096, 'p_cd': 0.2958205921725767, 'p_dc': 0.8683066079392928, 'p_dd': 0.8379510490101051}, 'Stoc255': {'p_cc': 0.5857284920116846, 'p_cd': 0.6593612702863554, 'p_dc': 0.9669929064642826, 'p_dd': 0.8574061001920368}, 'Stoc256': {'p_cc': 0.48221460480602596, 'p_cd': 0.48715929338255604, 'p_dc': 0.09451023799581382, 'p_dd': 0.4000843998117488}, 'Stoc257': {'p_cc': 0.3775820366553997, 'p_cd': 0.9716943001559917, 'p_dc': 0.8596418927368589, 'p_dd': 0.7635675381862128}, 'Stoc258': {'p_cc': 0.33623401932791386, 'p_cd': 0.3232186548119872, 'p_dc': 0.8319302416226783, 'p_dd': 0.44365798266997103}, 'Stoc259': {'p_cc': 0.4924156740614529, 'p_cd': 0.622442359995641, 'p_dc': 0.30966126753855605, 'p_dd': 0.7771126598403478}, 'Stoc260': {'p_cc': 0.8720030846611194, 'p_cd': 0.7598737642902833, 'p_dc': 0.25997635329628666, 'p_dd': 0.14231730246707708}, 'Stoc261': {'p_cc': 0.7412931380563685, 'p_cd': 0.2996974174124363, 'p_dc': 0.3779879287261424, 'p_dd': 0.4656105325517569}, 'Stoc262': {'p_cc': 0.03214483046290728, 'p_cd': 0.42291163664134956, 'p_dc': 0.6865027720394038, 'p_dd': 0.8606534631713667}, 'Stoc263': {'p_cc': 0.03434574105452748, 'p_cd': 0.5163541284342545, 'p_dc': 0.9327673483284136, 'p_dd': 0.03212057918774647}, 'Stoc264': {'p_cc': 0.48931080166535446, 'p_cd': 0.1392903085274374, 'p_dc': 0.6413795415084619, 'p_dd': 0.8089165767745196}, 'Stoc265': {'p_cc': 0.0705042991632161, 'p_cd': 0.11561581227661277, 'p_dc': 0.41464183998290116, 'p_dd': 0.3214268905986146}, 'Stoc266': {'p_cc': 0.3518833179610218, 'p_cd': 0.5765842767006226, 'p_dc': 0.6817043815768025, 'p_dd': 0.6500623979141521}, 'Stoc267': {'p_cc': 0.23607022136425682, 'p_cd': 0.9921331844901752, 'p_dc': 0.275283864280255, 'p_dd': 0.7052602024698956}, 'Stoc268': {'p_cc': 0.30673871638058814, 'p_cd': 0.21334619591914972, 'p_dc': 0.4740485461858691, 'p_dd': 0.6199698527379144}, 'Stoc269': {'p_cc': 0.8316336110137648, 'p_cd': 0.1911354814631291, 'p_dc': 0.7471369898398701, 'p_dd': 0.654022189992253}, 'Stoc270': {'p_cc': 0.0476225204825137, 'p_cd': 0.32789913047178365, 'p_dc': 0.276936827651188, 'p_dd': 0.003024896561764301}, 'Stoc271': {'p_cc': 0.6461804016919982, 'p_cd': 0.8081016402206498, 'p_dc': 0.19756736150766252, 'p_dd': 0.1737926288104087}, 'Stoc272': {'p_cc': 0.20224103656392456, 'p_cd': 0.7538210536469935, 'p_dc': 0.3599758953029739, 'p_dd': 0.38509347053062926}, 'Stoc273': {'p_cc': 0.8906977143825451, 'p_cd': 0.6488588212531834, 'p_dc': 0.004446782123973092, 'p_dd': 0.4030593182642376}, 'Stoc274': {'p_cc': 0.19715344124600154, 'p_cd': 0.15904487850890348, 'p_dc': 0.5853586487444558, 'p_dd': 0.19264577020542317}, 'Stoc275': {'p_cc': 0.7946980631830012, 'p_cd': 0.38752068840505594, 'p_dc': 0.9719526486991149, 'p_dd': 0.46332964535304955}, 'Stoc276': {'p_cc': 0.07260310314946139, 'p_cd': 0.45469046171946925, 'p_dc': 0.4102100627643587, 'p_dd': 0.8742160488624395}, 'Stoc277': {'p_cc': 0.9534407302185657, 'p_cd': 0.14806663521044805, 'p_dc': 0.15803215252013947, 'p_dd': 0.4269742133933293}, 'Stoc278': {'p_cc': 0.9353338280804195, 'p_cd': 0.8075966378176686, 'p_dc': 0.9542115059884196, 'p_dd': 0.19949414774281193}, 'Stoc279': {'p_cc': 0.6883437197812126, 'p_cd': 0.9427348599515717, 'p_dc': 0.21713565659340672, 'p_dd': 0.22571524902394902}, 'Stoc280': {'p_cc': 0.6471782612597423, 'p_cd': 0.4243181394229081, 'p_dc': 0.6956924877883455, 'p_dd': 0.8475533711540933}, 'Stoc281': {'p_cc': 0.9948280274659393, 'p_cd': 0.023594840987384957, 'p_dc': 0.922980541844254, 'p_dd': 0.9257032167054325}, 'Stoc282': {'p_cc': 0.5911494939599358, 'p_cd': 0.4333261551164894, 'p_dc': 0.5878122525450212, 'p_dd': 0.17295679206781367}, 'Stoc283': {'p_cc': 0.6474278639531315, 'p_cd': 0.27039923374607944, 'p_dc': 0.07315477337098764, 'p_dd': 0.2658281689820039}, 'Stoc284': {'p_cc': 0.8158979653863039, 'p_cd': 0.3076319755387472, 'p_dc': 0.7305789693452078, 'p_dd': 0.7647177523031613}, 'Stoc285': {'p_cc': 0.466643418027643, 'p_cd': 0.7155808676303053, 'p_dc': 0.4707853975999644, 'p_dd': 0.22278972567124722}, 'Stoc286': {'p_cc': 0.9181264254431163, 'p_cd': 0.8996861387710104, 'p_dc': 0.036361057533338736, 'p_dd': 0.8337492404750049}, 'Stoc287': {'p_cc': 0.5702499353653052, 'p_cd': 0.32794406103116125, 'p_dc': 0.170087021951139, 'p_dd': 0.07046820088268002}, 'Stoc288': {'p_cc': 0.6846833145107775, 'p_cd': 0.9885245333971391, 'p_dc': 0.4572032198030035, 'p_dd': 0.31369254729151863}, 'Stoc289': {'p_cc': 0.020364801448303216, 'p_cd': 0.3988382098967267, 'p_dc': 0.034174014588137624, 'p_dd': 0.5891504003771909}, 'Stoc290': {'p_cc': 0.6021624285725027, 'p_cd': 0.7148339198884581, 'p_dc': 0.9277070408797389, 'p_dd': 0.38038353371692035}, 'Stoc291': {'p_cc': 0.9406121045220156, 'p_cd': 0.8736977713513112, 'p_dc': 0.8151613129810137, 'p_dd': 0.31204677293107097}, 'Stoc292': {'p_cc': 0.09739047583701965, 'p_cd': 0.5320201057625812, 'p_dc': 0.04328674245967179, 'p_dd': 0.023511871542851503}, 'Stoc293': {'p_cc': 0.7924719280373579, 'p_cd': 0.9587466650469174, 'p_dc': 0.5782668572806838, 'p_dd': 0.5304287098653329}, 'Stoc294': {'p_cc': 0.17324585110538238, 'p_cd': 0.9527227704991623, 'p_dc': 0.7399737999060302, 'p_dd': 0.35349856525046364}, 'Stoc295': {'p_cc': 0.28996249956276576, 'p_cd': 0.2711565189545563, 'p_dc': 0.6430044712308939, 'p_dd': 0.18659818741066392}, 'Stoc296': {'p_cc': 0.8568659163339264, 'p_cd': 0.6887454097942993, 'p_dc': 0.6530701384624104, 'p_dd': 0.2601212993182187}, 'Stoc297': {'p_cc': 0.37666190904863783, 'p_cd': 0.6255699716000086, 'p_dc': 0.8971873542216405, 'p_dd': 0.37878141107567254}, 'Stoc298': {'p_cc': 0.27518419832221885, 'p_cd': 0.18057514974134392, 'p_dc': 0.5546933714004396, 'p_dd': 0.1623047521633293}, 'Stoc299': {'p_cc': 0.564169829892784, 'p_cd': 0.591126160953063, 'p_dc': 0.8174036849174511, 'p_dd': 0.15384017347647205}, 'Stoc300': {'p_cc': 0.6753836453290423, 'p_cd': 0.5235602944250157, 'p_dc': 0.28063685654405457, 'p_dd': 0.36321693262004984}, 'Stoc301': {'p_cc': 0.5479170094450525, 'p_cd': 0.13221452281106705, 'p_dc': 0.563135823904553, 'p_dd': 0.5903255758715276}, 'Stoc302': {'p_cc': 0.24986520342649376, 'p_cd': 0.6922384260169088, 'p_dc': 0.15058533798671092, 'p_dd': 0.35184470796750655}, 'Stoc303': {'p_cc': 0.8512219938028035, 'p_cd': 0.8812083722719543, 'p_dc': 0.788720293712297, 'p_dd': 0.2690085440234009}, 'Stoc304': {'p_cc': 0.3465268587964063, 'p_cd': 0.43978469342876336, 'p_dc': 0.4869435064274067, 'p_dd': 0.14752481284051167}, 'Stoc305': {'p_cc': 0.7012647959010785, 'p_cd': 0.8617788725433162, 'p_dc': 0.5505032138212794, 'p_dd': 0.8298276279299269}, 'Stoc306': {'p_cc': 0.9124830712340178, 'p_cd': 0.8851216199140869, 'p_dc': 0.2492220303889574, 'p_dd': 0.7116186583675985}, 'Stoc307': {'p_cc': 0.3228446858449351, 'p_cd': 0.4243717900160716, 'p_dc': 0.27467728421169035, 'p_dd': 0.47956767658768973}, 'Stoc308': {'p_cc': 0.5983990166615825, 'p_cd': 0.8137407452762943, 'p_dc': 0.8803437963059633, 'p_dd': 0.6946720182229092}, 'Stoc309': {'p_cc': 0.8025451740142121, 'p_cd': 0.4085828060365413, 'p_dc': 0.7166961470159215, 'p_dd': 0.5466439859901185}, 'Stoc310': {'p_cc': 0.8726975558237327, 'p_cd': 0.4677564014943406, 'p_dc': 0.8465119071826764, 'p_dd': 0.2352057388991432}, 'Stoc311': {'p_cc': 0.11200203686016108, 'p_cd': 0.12647326546993143, 'p_dc': 0.11241017283843335, 'p_dd': 0.9913563807326012}, 'Stoc312': {'p_cc': 0.620326112537129, 'p_cd': 0.4011195789826071, 'p_dc': 0.3469174322464943, 'p_dd': 0.5595693613367256}, 'Stoc313': {'p_cc': 0.984748164210471, 'p_cd': 0.057550299672458616, 'p_dc': 0.7835007222767938, 'p_dd': 0.15630191167325125}, 'Stoc314': {'p_cc': 0.25921881642349354, 'p_cd': 0.3454123053380025, 'p_dc': 0.9654401104473616, 'p_dd': 0.34126410883816816}, 'Stoc315': {'p_cc': 0.9179074341770694, 'p_cd': 0.6487521513851314, 'p_dc': 0.7991599095582199, 'p_dd': 0.8362431879248415}, 'Stoc316': {'p_cc': 0.8639996030778441, 'p_cd': 0.5988854605692733, 'p_dc': 0.8524710714854417, 'p_dd': 0.5627397310381235}, 'Stoc317': {'p_cc': 0.9722084853757303, 'p_cd': 0.19372918439228293, 'p_dc': 0.4097662574784874, 'p_dd': 0.4775274750928561}, 'Stoc318': {'p_cc': 0.44495398482195536, 'p_cd': 0.26305927044440414, 'p_dc': 0.8199904721247581, 'p_dd': 0.8681526056431197}, 'Stoc319': {'p_cc': 0.2584347373028699, 'p_cd': 0.6142975390133544, 'p_dc': 0.6294758495511814, 'p_dd': 0.04489663272619837}, 'Stoc320': {'p_cc': 0.7673304723975969, 'p_cd': 0.10874216535577197, 'p_dc': 0.09337421659694534, 'p_dd': 0.7028804447715352}, 'Stoc321': {'p_cc': 0.11409240119334874, 'p_cd': 0.4240495940521022, 'p_dc': 0.44354536867636274, 'p_dd': 0.12093440647676146}, 'Stoc322': {'p_cc': 0.39774596592824574, 'p_cd': 0.4599580631407928, 'p_dc': 0.5865577523968522, 'p_dd': 0.4455846714285999}, 'Stoc323': {'p_cc': 0.009654989723899998, 'p_cd': 0.9637920934582478, 'p_dc': 0.3229580312100919, 'p_dd': 0.6575487321445453}, 'Stoc324': {'p_cc': 0.6465705396436251, 'p_cd': 0.3167715399319304, 'p_dc': 0.6484406659119004, 'p_dd': 0.8977155047573929}, 'Stoc325': {'p_cc': 0.2177910562321307, 'p_cd': 0.3908345053043344, 'p_dc': 0.6577934079053683, 'p_dd': 0.6059222622670214}, 'Stoc326': {'p_cc': 0.9501381682928074, 'p_cd': 0.9878223565459844, 'p_dc': 0.8446068506038916, 'p_dd': 0.16464653642524318}, 'Stoc327': {'p_cc': 0.7189658839245642, 'p_cd': 0.5315839164309238, 'p_dc': 0.11862703497720672, 'p_dd': 0.36983586264705925}, 'Stoc328': {'p_cc': 0.6922745696254491, 'p_cd': 0.6082359046681275, 'p_dc': 0.16401642081793666, 'p_dd': 0.20105272780130556}, 'Stoc329': {'p_cc': 0.5605069239211755, 'p_cd': 0.0009695883588255461, 'p_dc': 0.7046508563129597, 'p_dd': 0.6543044599436719}, 'Stoc330': {'p_cc': 0.46562895320671016, 'p_cd': 0.9125203588084936, 'p_dc': 0.5255843854183041, 'p_dd': 0.27696567683290474}, 'Stoc331': {'p_cc': 0.1296558504747446, 'p_cd': 0.16265095325105494, 'p_dc': 0.3847884661617641, 'p_dd': 0.7837165126292367}, 'Stoc332': {'p_cc': 0.1632810580843288, 'p_cd': 0.5812791400348558, 'p_dc': 0.24541364952559475, 'p_dd': 0.6899462826416287}, 'Stoc333': {'p_cc': 0.9497238658837002, 'p_cd': 0.33988208283565435, 'p_dc': 0.8815373720478051, 'p_dd': 0.31036917824097154}, 'Stoc334': {'p_cc': 0.6123952081915418, 'p_cd': 0.2882384387292264, 'p_dc': 0.4832230776643467, 'p_dd': 0.1520811661336241}, 'Stoc335': {'p_cc': 0.7908604456301471, 'p_cd': 0.7063126230214885, 'p_dc': 0.2631208167395507, 'p_dd': 0.5831383493740031}, 'Stoc336': {'p_cc': 0.27043795780417323, 'p_cd': 0.4776162596322243, 'p_dc': 0.08702925848863852, 'p_dd': 0.5900325630592397}, 'Stoc337': {'p_cc': 0.14038977215270376, 'p_cd': 0.848147773409038, 'p_dc': 0.46126408635870364, 'p_dd': 0.1623332160078197}, 'Stoc338': {'p_cc': 0.47829064358946227, 'p_cd': 0.42043579620584015, 'p_dc': 0.7966078105935169, 'p_dd': 0.12073327257538491}, 'Stoc339': {'p_cc': 0.20749315195284979, 'p_cd': 0.24593137544302357, 'p_dc': 0.5975350234835046, 'p_dd': 0.7180524062458224}, 'Stoc340': {'p_cc': 0.9266704108644661, 'p_cd': 0.7022926092047418, 'p_dc': 0.039878835937211754, 'p_dd': 0.08458469200235608}, 'Stoc341': {'p_cc': 0.2147401413721408, 'p_cd': 0.38320957591718896, 'p_dc': 0.9220464009293404, 'p_dd': 0.8396727347201375}, 'Stoc342': {'p_cc': 0.729132195422898, 'p_cd': 0.4832759890999383, 'p_dc': 0.8538144119611634, 'p_dd': 0.5212509339985669}, 'Stoc343': {'p_cc': 0.351270116850695, 'p_cd': 0.7287627636845035, 'p_dc': 0.7528066859262207, 'p_dd': 0.35040796735824997}, 'Stoc344': {'p_cc': 0.11205355586201327, 'p_cd': 0.9426610503549898, 'p_dc': 0.31454605470941166, 'p_dd': 0.23624173044174934}, 'Stoc345': {'p_cc': 0.9387230693176613, 'p_cd': 0.5675743194094273, 'p_dc': 0.31215767189205545, 'p_dd': 0.4809421184437044}, 'Stoc346': {'p_cc': 0.4968737091889105, 'p_cd': 0.8890720291452806, 'p_dc': 0.6239955380119155, 'p_dd': 0.7058149721814978}, 'Stoc347': {'p_cc': 0.8662454778339325, 'p_cd': 0.15387418108078676, 'p_dc': 0.48987914809839017, 'p_dd': 0.11700583034168044}, 'Stoc348': {'p_cc': 0.33824991401704674, 'p_cd': 0.8285830258567869, 'p_dc': 0.13178770928686723, 'p_dd': 0.7210570298080914}, 'Stoc349': {'p_cc': 0.3354719489115311, 'p_cd': 0.19763145073953814, 'p_dc': 0.04907185738645614, 'p_dd': 0.3860073995727483}, 'Stoc350': {'p_cc': 0.20620312103616623, 'p_cd': 0.29756612974781127, 'p_dc': 0.1874853651405204, 'p_dd': 0.3577766779828837}, 'Stoc351': {'p_cc': 0.39952751017682997, 'p_cd': 0.6289906036693118, 'p_dc': 0.7833706440558709, 'p_dd': 0.7166453413794471}, 'Stoc352': {'p_cc': 0.4130290707328921, 'p_cd': 0.6047612107206736, 'p_dc': 0.2785939578976635, 'p_dd': 0.0790919452217439}, 'Stoc353': {'p_cc': 0.05204128286277576, 'p_cd': 0.3879830146315326, 'p_dc': 0.8114841613471572, 'p_dd': 0.7132445216552165}, 'Stoc354': {'p_cc': 0.5286632602310857, 'p_cd': 0.5390407151474591, 'p_dc': 0.4826420516192965, 'p_dd': 0.46859292032632993}, 'Stoc355': {'p_cc': 0.95181303798319, 'p_cd': 0.9469812128873201, 'p_dc': 0.07080965596166344, 'p_dd': 0.8081159648346221}, 'Stoc356': {'p_cc': 0.4206477819166271, 'p_cd': 0.3953886243756183, 'p_dc': 0.2854743270614021, 'p_dd': 0.6067806165657189}, 'Stoc357': {'p_cc': 0.2668622204471861, 'p_cd': 0.3029368958345593, 'p_dc': 0.4688341837572708, 'p_dd': 0.8929327096311291}, 'Stoc358': {'p_cc': 0.14516958462916207, 'p_cd': 0.42202700899184176, 'p_dc': 0.5340581103671492, 'p_dd': 0.47860179899251865}, 'Stoc359': {'p_cc': 0.11796270181049395, 'p_cd': 0.41405110274752244, 'p_dc': 0.6762184340485105, 'p_dd': 0.3330211500821427}, 'Stoc360': {'p_cc': 0.10576395997509602, 'p_cd': 0.34203885500497533, 'p_dc': 0.9159096906029313, 'p_dd': 0.4822660386826463}, 'Stoc361': {'p_cc': 0.04894443850976615, 'p_cd': 0.1766147488321238, 'p_dc': 0.8798510799237785, 'p_dd': 0.2247954463366716}, 'Stoc362': {'p_cc': 0.886665177787184, 'p_cd': 0.473338905843524, 'p_dc': 0.8902857213919846, 'p_dd': 0.8445003395046712}, 'Stoc363': {'p_cc': 0.3319917933746752, 'p_cd': 0.8019611882697627, 'p_dc': 0.8192481919175082, 'p_dd': 0.11170615155294539}, 'Stoc364': {'p_cc': 0.6844396270704239, 'p_cd': 0.7156805533363296, 'p_dc': 0.9304150694823288, 'p_dd': 0.4305944323670766}, 'Stoc365': {'p_cc': 0.7800059650196927, 'p_cd': 0.03204729094705594, 'p_dc': 0.6487173024232777, 'p_dd': 0.7821682159531201}, 'Stoc366': {'p_cc': 0.052008180967815454, 'p_cd': 0.2055481363917091, 'p_dc': 0.8713495067710512, 'p_dd': 0.9789414944449715}, 'Stoc367': {'p_cc': 0.7643892294628234, 'p_cd': 0.26892447772986705, 'p_dc': 0.010480842967718007, 'p_dd': 0.6810408010604623}, 'Stoc368': {'p_cc': 0.33063758754158334, 'p_cd': 0.5542544924989752, 'p_dc': 0.2390172213677949, 'p_dd': 0.9191364665859295}, 'Stoc369': {'p_cc': 0.3430099953731638, 'p_cd': 0.9947439794104445, 'p_dc': 0.2149279156469368, 'p_dd': 0.00528307952571605}, 'Stoc370': {'p_cc': 0.828983016521304, 'p_cd': 0.6368028359850414, 'p_dc': 0.7636957585155458, 'p_dd': 0.5699451676479428}, 'Stoc371': {'p_cc': 0.4605603883071223, 'p_cd': 0.9097408386671356, 'p_dc': 0.35567429130127004, 'p_dd': 0.5641630062935832}, 'Stoc372': {'p_cc': 0.9973758802855159, 'p_cd': 0.8067824812094812, 'p_dc': 0.7011407930703989, 'p_dd': 0.6486749823121861}, 'Stoc373': {'p_cc': 0.8883389435561501, 'p_cd': 0.5268382334066198, 'p_dc': 0.3359913996391012, 'p_dd': 0.24757885719558148}, 'Stoc374': {'p_cc': 0.7228001976888015, 'p_cd': 0.9494720623266182, 'p_dc': 0.5339116258678401, 'p_dd': 0.1900678470386249}, 'Stoc375': {'p_cc': 0.014686293305532394, 'p_cd': 0.9124758304031013, 'p_dc': 0.1761490005817169, 'p_dd': 0.49701720875600974}, 'Stoc376': {'p_cc': 0.5994642750245772, 'p_cd': 0.3426624451032282, 'p_dc': 0.895916045811205, 'p_dd': 0.045296993480077985}, 'Stoc377': {'p_cc': 0.35261330736366414, 'p_cd': 0.22985159625673135, 'p_dc': 0.36727595542221503, 'p_dd': 0.9646674835031207}, 'Stoc378': {'p_cc': 0.6619751650833742, 'p_cd': 0.8733201924958821, 'p_dc': 0.8542994697508939, 'p_dd': 0.8313966653374342}, 'Stoc379': {'p_cc': 0.8763319033597261, 'p_cd': 0.366138068920816, 'p_dc': 0.5209747955716991, 'p_dd': 0.041904142243651576}, 'Stoc380': {'p_cc': 0.19515857198379782, 'p_cd': 0.5500367006926908, 'p_dc': 0.387187819378085, 'p_dd': 0.700153346268233}, 'Stoc381': {'p_cc': 0.9536940487599384, 'p_cd': 0.9957982866169057, 'p_dc': 0.17049780515955015, 'p_dd': 0.07654786090666621}, 'Stoc382': {'p_cc': 0.9496125440158685, 'p_cd': 0.29176260142547594, 'p_dc': 0.05854515257402715, 'p_dd': 0.6935815630736902}, 'Stoc383': {'p_cc': 0.1497135049871855, 'p_cd': 0.6715453774144412, 'p_dc': 0.9287664681156084, 'p_dd': 0.6289808765976762}, 'Stoc384': {'p_cc': 0.01723788600522158, 'p_cd': 0.791697732210451, 'p_dc': 0.835957314422136, 'p_dd': 0.9671868181415453}, 'Stoc385': {'p_cc': 0.01887706782851728, 'p_cd': 0.8939622113792944, 'p_dc': 0.5674386836467458, 'p_dd': 0.050043190153671535}, 'Stoc386': {'p_cc': 0.3001311574757326, 'p_cd': 0.15833900339349039, 'p_dc': 0.32200753001041393, 'p_dd': 0.06455806878523296}, 'Stoc387': {'p_cc': 0.8243495902062544, 'p_cd': 0.7566926610082855, 'p_dc': 0.9765766094010478, 'p_dd': 0.8122417446218383}, 'Stoc388': {'p_cc': 0.9298305657756639, 'p_cd': 0.6009711821028906, 'p_dc': 0.5615358363379744, 'p_dd': 0.3541743196242003}, 'Stoc389': {'p_cc': 0.04698077344792717, 'p_cd': 0.6256358834939152, 'p_dc': 0.1374053424999634, 'p_dd': 0.5490692103429672}, 'Stoc390': {'p_cc': 0.8885266936409734, 'p_cd': 0.3886122904528394, 'p_dc': 0.0678285820738318, 'p_dd': 0.6414004695840806}, 'Stoc391': {'p_cc': 0.5697381370881628, 'p_cd': 0.07570464820179568, 'p_dc': 0.35543284285527166, 'p_dd': 0.09423893522691995}, 'Stoc392': {'p_cc': 0.3063590925645936, 'p_cd': 0.13434647425524837, 'p_dc': 0.26793410650910554, 'p_dd': 0.736558116268748}, 'Stoc393': {'p_cc': 0.41710938219652327, 'p_cd': 0.8249513324662833, 'p_dc': 0.13051223158012903, 'p_dd': 0.6502996465766138}, 'Stoc394': {'p_cc': 0.47757294776549064, 'p_cd': 0.6886923319142119, 'p_dc': 0.3834222013012041, 'p_dd': 0.6062930912641049}, 'Stoc395': {'p_cc': 0.47134764609913893, 'p_cd': 0.09042962536653587, 'p_dc': 0.48829079292077027, 'p_dd': 0.25021320749456355}, 'Stoc396': {'p_cc': 0.746692858160675, 'p_cd': 0.9728620600563611, 'p_dc': 0.6713206911342923, 'p_dd': 0.8105725613413406}, 'Stoc397': {'p_cc': 0.09147010744831185, 'p_cd': 0.38530595157054703, 'p_dc': 0.7591695081801342, 'p_dd': 0.09900584733595907}, 'Stoc398': {'p_cc': 0.7487073362586264, 'p_cd': 0.19709724032027043, 'p_dc': 0.4509500393744367, 'p_dd': 0.4946506243264176}, 'Stoc399': {'p_cc': 0.93346666399127, 'p_cd': 0.5793618281966771, 'p_dc': 0.35321813380080425, 'p_dd': 0.46095244659078405}, 'Stoc400': {'p_cc': 0.5829615997617055, 'p_cd': 0.0778838043338711, 'p_dc': 0.6058796421640823, 'p_dd': 0.7651090603667261}, 'Stoc401': {'p_cc': 0.2676915684537259, 'p_cd': 0.22699702477648198, 'p_dc': 0.3740856485728443, 'p_dd': 0.3226518230910357}, 'Stoc402': {'p_cc': 0.6793442120758046, 'p_cd': 0.08102080601221906, 'p_dc': 0.41495472095030916, 'p_dd': 0.30961283316728083}, 'Stoc403': {'p_cc': 0.2957376469690016, 'p_cd': 0.30868010600520934, 'p_dc': 0.9757929077294687, 'p_dd': 0.7280991133647547}, 'Stoc404': {'p_cc': 0.04237036767639124, 'p_cd': 0.3228889610259994, 'p_dc': 0.5862703299766784, 'p_dd': 0.21079382683485937}, 'Stoc405': {'p_cc': 0.7186651128906368, 'p_cd': 0.9139215671388892, 'p_dc': 0.3456998064728879, 'p_dd': 0.4803149859248913}, 'Stoc406': {'p_cc': 0.5243445810121531, 'p_cd': 0.5939911518734693, 'p_dc': 0.32864950894947176, 'p_dd': 0.6215259463578044}, 'Stoc407': {'p_cc': 0.3095099773150205, 'p_cd': 0.18997042123104912, 'p_dc': 0.7901907491121896, 'p_dd': 0.1753040817725302}, 'Stoc408': {'p_cc': 0.09303124243306227, 'p_cd': 0.5664020690851158, 'p_dc': 0.6659837860784181, 'p_dd': 0.33802130227150173}, 'Stoc409': {'p_cc': 0.4525389592809579, 'p_cd': 0.6479023558009155, 'p_dc': 0.046731207362432525, 'p_dd': 0.22870534834570844}, 'Stoc410': {'p_cc': 0.1561651165793816, 'p_cd': 0.9576625985711686, 'p_dc': 0.1108915989329643, 'p_dd': 0.23509296164505478}, 'Stoc411': {'p_cc': 0.43267461821290276, 'p_cd': 0.8272779988249481, 'p_dc': 0.3837372334754854, 'p_dd': 0.612878165534535}, 'Stoc412': {'p_cc': 0.389911245037729, 'p_cd': 0.05949004811618852, 'p_dc': 0.7825662958342179, 'p_dd': 0.15699810725667607}, 'Stoc413': {'p_cc': 0.4000168041176345, 'p_cd': 0.7100286013035019, 'p_dc': 0.18111450509870541, 'p_dd': 0.3851394860062608}, 'Stoc414': {'p_cc': 0.8241215334516554, 'p_cd': 0.8027978728890931, 'p_dc': 0.24201962548421152, 'p_dd': 0.9069566931633316}, 'Stoc415': {'p_cc': 0.7290323859882579, 'p_cd': 0.1328407126535608, 'p_dc': 0.18975535056453063, 'p_dd': 0.2255208418866722}, 'Stoc416': {'p_cc': 0.37235316192424583, 'p_cd': 0.6073537786008746, 'p_dc': 0.06167981462381511, 'p_dd': 0.20141736767335106}, 'Stoc417': {'p_cc': 0.9086357741938769, 'p_cd': 0.6812203013752189, 'p_dc': 0.780033007304254, 'p_dd': 0.9357505117245848}, 'Stoc418': {'p_cc': 0.6335883693448795, 'p_cd': 0.10639525625250379, 'p_dc': 0.8092444323652112, 'p_dd': 0.564260035109939}, 'Stoc419': {'p_cc': 0.6943315433424622, 'p_cd': 0.8663929442682419, 'p_dc': 0.9936282306562586, 'p_dd': 0.028456112024095148}, 'Stoc420': {'p_cc': 0.07970592060332382, 'p_cd': 0.7485228173188069, 'p_dc': 0.6829411392980101, 'p_dd': 0.3155882063406278}, 'Stoc421': {'p_cc': 0.07515500843056377, 'p_cd': 0.6679659212278841, 'p_dc': 0.6259926622570624, 'p_dd': 0.8583738384450622}, 'Stoc422': {'p_cc': 0.37914062086983824, 'p_cd': 0.4896045846259468, 'p_dc': 0.01852852376094538, 'p_dd': 0.9569515549790678}, 'Stoc423': {'p_cc': 0.17616807594648776, 'p_cd': 0.18339487440623992, 'p_dc': 0.8087585870584414, 'p_dd': 0.7721905631436679}, 'Stoc424': {'p_cc': 0.15382818877371884, 'p_cd': 0.14104912404257708, 'p_dc': 0.38587369323247955, 'p_dd': 0.9546876974777967}, 'Stoc425': {'p_cc': 0.7116521424350069, 'p_cd': 0.3196703556366842, 'p_dc': 0.37296084559263787, 'p_dd': 0.723050332647297}, 'Stoc426': {'p_cc': 0.07900199733138402, 'p_cd': 0.33496870725331007, 'p_dc': 0.551976624128651, 'p_dd': 0.9949865552151663}, 'Stoc427': {'p_cc': 0.004033946326644888, 'p_cd': 0.47758258726634517, 'p_dc': 0.8105867407839481, 'p_dd': 0.2951134000900061}, 'Stoc428': {'p_cc': 0.20837689929199554, 'p_cd': 0.9461801041027208, 'p_dc': 0.838305351546715, 'p_dd': 0.01940597786911269}, 'Stoc429': {'p_cc': 0.39608511489163045, 'p_cd': 0.5199921418615009, 'p_dc': 0.4748504680584682, 'p_dd': 0.48406503376432963}, 'Stoc430': {'p_cc': 0.5215721350369716, 'p_cd': 0.35056102941070455, 'p_dc': 0.7336761763218755, 'p_dd': 0.21891150926399883}, 'Stoc431': {'p_cc': 0.5624608248924043, 'p_cd': 0.7484094193292558, 'p_dc': 0.9587404500487978, 'p_dd': 0.6209957993768822}, 'Stoc432': {'p_cc': 0.7649097667250608, 'p_cd': 0.3163904440451195, 'p_dc': 0.32445832254444507, 'p_dd': 0.2842697136180897}, 'Stoc433': {'p_cc': 0.624948969945327, 'p_cd': 0.46263145865725086, 'p_dc': 0.3821349902099038, 'p_dd': 0.9325356360528511}, 'Stoc434': {'p_cc': 0.258002103377698, 'p_cd': 0.8267320334518985, 'p_dc': 0.8083673651256339, 'p_dd': 0.4622193305426596}, 'Stoc435': {'p_cc': 0.9248955905615108, 'p_cd': 0.8532695008847361, 'p_dc': 0.6623991487010684, 'p_dd': 0.7622161473834871}, 'Stoc436': {'p_cc': 0.7121660162681694, 'p_cd': 0.5258967062930875, 'p_dc': 0.10385341540698145, 'p_dd': 0.4581929535137901}, 'Stoc437': {'p_cc': 0.3362736593485307, 'p_cd': 0.11548918953660958, 'p_dc': 0.6185738585664265, 'p_dd': 0.2668116328489849}, 'Stoc438': {'p_cc': 0.570505918765586, 'p_cd': 0.7373579464873249, 'p_dc': 0.6284511918038549, 'p_dd': 0.15307303839159037}, 'Stoc439': {'p_cc': 0.9714698605748251, 'p_cd': 0.39422008171144396, 'p_dc': 0.15597092951020097, 'p_dd': 0.7771465528107806}, 'Stoc440': {'p_cc': 0.32758614588468404, 'p_cd': 0.020085444894143434, 'p_dc': 0.6165597732198401, 'p_dd': 0.5657346140141761}, 'Stoc441': {'p_cc': 0.9363354961055784, 'p_cd': 0.6351105404553656, 'p_dc': 0.09894949243487083, 'p_dd': 0.1131157931214235}, 'Stoc442': {'p_cc': 0.05072753496753657, 'p_cd': 0.8769992774624548, 'p_dc': 0.9060579997392034, 'p_dd': 0.6489939399593087}, 'Stoc443': {'p_cc': 0.5406152740664097, 'p_cd': 0.24072479859064777, 'p_dc': 0.5084536999139159, 'p_dd': 0.3323857440167718}, 'Stoc444': {'p_cc': 0.3670696673441418, 'p_cd': 0.3854389026145788, 'p_dc': 0.5683215224132165, 'p_dd': 0.7331090131690354}, 'Stoc445': {'p_cc': 0.07559685731250221, 'p_cd': 0.09669942021123468, 'p_dc': 0.4417731430848397, 'p_dd': 0.050878785415534145}, 'Stoc446': {'p_cc': 0.3732085093178876, 'p_cd': 0.9475298044641443, 'p_dc': 0.7312277466359689, 'p_dd': 0.20039579700779375}, 'Stoc447': {'p_cc': 0.03192356049952105, 'p_cd': 0.755814340436025, 'p_dc': 0.20153008861636101, 'p_dd': 0.20896688609578085}, 'Stoc448': {'p_cc': 0.6787002911647785, 'p_cd': 0.7835293447072074, 'p_dc': 0.1749713205379838, 'p_dd': 0.9859183942949462}, 'Stoc449': {'p_cc': 0.09721563765719499, 'p_cd': 0.7882531455287732, 'p_dc': 0.9671182553465407, 'p_dd': 0.10188864221386418}, 'Stoc450': {'p_cc': 0.21114916605418121, 'p_cd': 0.5135610255543165, 'p_dc': 0.6022131173246976, 'p_dd': 0.1551756582699133}, 'Stoc451': {'p_cc': 0.11327655861984876, 'p_cd': 0.7079267183365527, 'p_dc': 0.7266765649791923, 'p_dd': 0.3106888762661123}, 'Stoc452': {'p_cc': 0.32696273121935504, 'p_cd': 0.5394117990750045, 'p_dc': 0.5015342067305714, 'p_dd': 0.10780799710039812}, 'Stoc453': {'p_cc': 0.27993170158012326, 'p_cd': 0.7132512091275431, 'p_dc': 0.5231827587445587, 'p_dd': 0.4019679115433513}, 'Stoc454': {'p_cc': 0.6980904480507557, 'p_cd': 0.9150615976141994, 'p_dc': 0.03926118541158208, 'p_dd': 0.15037149208573408}, 'Stoc455': {'p_cc': 0.6922243061315099, 'p_cd': 0.18620510993888229, 'p_dc': 0.11762485941821399, 'p_dd': 0.5489672455938476}, 'Stoc456': {'p_cc': 0.447638740963333, 'p_cd': 0.19906215185740117, 'p_dc': 0.4479150281415737, 'p_dd': 0.5633305450703568}, 'Stoc457': {'p_cc': 0.17908995122554727, 'p_cd': 0.877447020379908, 'p_dc': 0.5663542560385915, 'p_dd': 0.9249433832008778}, 'Stoc458': {'p_cc': 0.1400239272537357, 'p_cd': 0.47097002459954496, 'p_dc': 0.025680626593774902, 'p_dd': 0.4013147212927638}, 'Stoc459': {'p_cc': 0.6233257801960054, 'p_cd': 0.8829116400537025, 'p_dc': 0.6055998903815304, 'p_dd': 0.8632416321136018}, 'Stoc460': {'p_cc': 0.2740791212702316, 'p_cd': 0.9715051233000644, 'p_dc': 0.8440124617616325, 'p_dd': 0.6977491814416715}, 'Stoc461': {'p_cc': 0.9639338086320443, 'p_cd': 0.23790017806087083, 'p_dc': 0.6395544802658897, 'p_dd': 0.40349691967238754}, 'Stoc462': {'p_cc': 0.5136224077513499, 'p_cd': 0.919470227932431, 'p_dc': 0.27919772541419063, 'p_dd': 0.8186116321866128}, 'Stoc463': {'p_cc': 0.13979032959079418, 'p_cd': 0.3359576414444909, 'p_dc': 0.10904487454355416, 'p_dd': 0.6554614589251058}, 'Stoc464': {'p_cc': 0.9570976366131111, 'p_cd': 0.36258076775829773, 'p_dc': 0.3794735075929878, 'p_dd': 0.8216880580396544}, 'Stoc465': {'p_cc': 0.07934181897582138, 'p_cd': 0.9398302136799298, 'p_dc': 0.03407175297910969, 'p_dd': 0.14739670265283888}, 'Stoc466': {'p_cc': 0.276877531626624, 'p_cd': 0.005433105693836926, 'p_dc': 0.45271272840629706, 'p_dd': 0.358504535903878}, 'Stoc467': {'p_cc': 0.06927685792675897, 'p_cd': 0.743216831686374, 'p_dc': 0.4836759793149772, 'p_dd': 0.282240720245826}, 'Stoc468': {'p_cc': 0.5852592143560235, 'p_cd': 0.06673799691794458, 'p_dc': 0.3315320828650665, 'p_dd': 0.008928983073392738}, 'Stoc469': {'p_cc': 0.16786310875714605, 'p_cd': 0.20519741979628958, 'p_dc': 0.6887844971854993, 'p_dd': 0.8108469940203051}, 'Stoc470': {'p_cc': 0.662984611078308, 'p_cd': 0.4957175930666792, 'p_dc': 0.5115994886286672, 'p_dd': 0.39267971081489417}, 'Stoc471': {'p_cc': 0.5995678868781047, 'p_cd': 0.48663787511488643, 'p_dc': 0.1821626012184695, 'p_dd': 0.49730211227441123}, 'Stoc472': {'p_cc': 0.45125032302793866, 'p_cd': 0.19555980171262743, 'p_dc': 0.4658485354191262, 'p_dd': 0.6942489368201598}, 'Stoc473': {'p_cc': 0.7492462376110577, 'p_cd': 0.13981593176534424, 'p_dc': 0.7677415012488011, 'p_dd': 0.5474088239759195}, 'Stoc474': {'p_cc': 0.5779155646230522, 'p_cd': 0.08582561671873945, 'p_dc': 0.10314412000103124, 'p_dd': 0.7517696124476873}, 'Stoc475': {'p_cc': 0.36458998783008045, 'p_cd': 0.8601789966043677, 'p_dc': 0.34692221887521335, 'p_dd': 0.26256140209700807}, 'Stoc476': {'p_cc': 0.2059281461841389, 'p_cd': 0.806090528116238, 'p_dc': 0.00624651150253297, 'p_dd': 0.03297934122531598}, 'Stoc477': {'p_cc': 0.17590574657254732, 'p_cd': 0.4899608840314923, 'p_dc': 0.6982989181333258, 'p_dd': 0.8423810792241989}, 'Stoc478': {'p_cc': 0.9859534913651902, 'p_cd': 0.5506806356179347, 'p_dc': 0.5981917748160996, 'p_dd': 0.828793156394353}, 'Stoc479': {'p_cc': 0.6889350708750723, 'p_cd': 0.7463334431089894, 'p_dc': 0.5020952147348704, 'p_dd': 0.45310424985644593}, 'Stoc480': {'p_cc': 0.2545861806946188, 'p_cd': 0.1881481368098955, 'p_dc': 0.791026605522734, 'p_dd': 0.41269730086809286}, 'Stoc481': {'p_cc': 0.8345875690034625, 'p_cd': 0.3570711900151329, 'p_dc': 0.0014941605732023966, 'p_dd': 0.5395742240712016}, 'Stoc482': {'p_cc': 0.13822318645858, 'p_cd': 0.6756579025638113, 'p_dc': 0.5916759910014778, 'p_dd': 0.09992500326777298}, 'Stoc483': {'p_cc': 0.1465372788397563, 'p_cd': 0.5468865926148396, 'p_dc': 0.9566618128186695, 'p_dd': 0.7655046690762548}, 'Stoc484': {'p_cc': 0.7010987110786923, 'p_cd': 0.1513939747858819, 'p_dc': 0.04387703356046113, 'p_dd': 0.8830963290434322}, 'Stoc485': {'p_cc': 0.6784661079987754, 'p_cd': 0.06360092015768493, 'p_dc': 0.18210232625001976, 'p_dd': 0.9839851721942591}, 'Stoc486': {'p_cc': 0.9508181360932284, 'p_cd': 0.5863384988126645, 'p_dc': 0.3837162410308701, 'p_dd': 0.17154895656340774}, 'Stoc487': {'p_cc': 0.6119444378583883, 'p_cd': 0.5436233439348409, 'p_dc': 0.13179596274856964, 'p_dd': 0.2912083231927395}, 'Stoc488': {'p_cc': 0.1291360487566201, 'p_cd': 0.995980120601403, 'p_dc': 0.502786162583017, 'p_dd': 0.28204138630202136}, 'Stoc489': {'p_cc': 0.2631622661176558, 'p_cd': 0.531473132682341, 'p_dc': 0.6269080646797098, 'p_dd': 0.9645730421513107}, 'Stoc490': {'p_cc': 0.5215625073193252, 'p_cd': 0.5335507349870177, 'p_dc': 0.3973446313079211, 'p_dd': 0.20819139030287226}, 'Stoc491': {'p_cc': 0.8289278932555306, 'p_cd': 0.25589689940234084, 'p_dc': 0.9835634754523142, 'p_dd': 0.3115235988993341}, 'Stoc492': {'p_cc': 0.5409142731032739, 'p_cd': 0.6239831931879083, 'p_dc': 0.39858197061514744, 'p_dd': 0.9998470323640266}, 'Stoc493': {'p_cc': 0.19496187068674664, 'p_cd': 0.3221775253575452, 'p_dc': 0.6950716891746958, 'p_dd': 0.7672801047336525}, 'Stoc494': {'p_cc': 0.6836883267718047, 'p_cd': 0.3434250982247187, 'p_dc': 0.5993675210762494, 'p_dd': 0.014642224169485019}, 'Stoc495': {'p_cc': 0.46840804246477796, 'p_cd': 0.9856596773484678, 'p_dc': 0.571207648935163, 'p_dd': 0.8391973989559179}, 'Stoc496': {'p_cc': 0.43285769158084597, 'p_cd': 0.34149114141840475, 'p_dc': 0.24810985022451892, 'p_dd': 0.14811175285154132}, 'Stoc497': {'p_cc': 0.4603747599391267, 'p_cd': 0.4210926439551236, 'p_dc': 0.3811748663541632, 'p_dd': 0.40226099535483273}, 'Stoc498': {'p_cc': 0.29384011360689566, 'p_cd': 0.8041170054752921, 'p_dc': 0.8165428222689619, 'p_dd': 0.5026839059330561}, 'Stoc499': {'p_cc': 0.7088140269567735, 'p_cd': 0.4332074443666569, 'p_dc': 0.3999794905169183, 'p_dd': 0.03924310764640926}}
