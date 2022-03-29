from tournament.action import Action
from tournament.agents.random import ProbabilisticLB2

class Stoc0(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.25, (Action.COOPERATE, Action.DEFECT): 0.25, (Action.DEFECT, Action.COOPERATE): 0.25, (Action.DEFECT, Action.DEFECT): 0.25 }


class Stoc1(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.25, (Action.COOPERATE, Action.DEFECT): 0.25, (Action.DEFECT, Action.COOPERATE): 0.25, (Action.DEFECT, Action.DEFECT): 0.5 }


class Stoc2(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.25, (Action.COOPERATE, Action.DEFECT): 0.25, (Action.DEFECT, Action.COOPERATE): 0.25, (Action.DEFECT, Action.DEFECT): 0.75 }


class Stoc3(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.25, (Action.COOPERATE, Action.DEFECT): 0.25, (Action.DEFECT, Action.COOPERATE): 0.25, (Action.DEFECT, Action.DEFECT): 1 }


class Stoc4(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.25, (Action.COOPERATE, Action.DEFECT): 0.25, (Action.DEFECT, Action.COOPERATE): 0.5, (Action.DEFECT, Action.DEFECT): 0.25 }


class Stoc5(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.25, (Action.COOPERATE, Action.DEFECT): 0.25, (Action.DEFECT, Action.COOPERATE): 0.5, (Action.DEFECT, Action.DEFECT): 0.5 }


class Stoc6(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.25, (Action.COOPERATE, Action.DEFECT): 0.25, (Action.DEFECT, Action.COOPERATE): 0.5, (Action.DEFECT, Action.DEFECT): 0.75 }


class Stoc7(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.25, (Action.COOPERATE, Action.DEFECT): 0.25, (Action.DEFECT, Action.COOPERATE): 0.5, (Action.DEFECT, Action.DEFECT): 1 }


class Stoc8(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.25, (Action.COOPERATE, Action.DEFECT): 0.25, (Action.DEFECT, Action.COOPERATE): 0.75, (Action.DEFECT, Action.DEFECT): 0.25 }


class Stoc9(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.25, (Action.COOPERATE, Action.DEFECT): 0.25, (Action.DEFECT, Action.COOPERATE): 0.75, (Action.DEFECT, Action.DEFECT): 0.5 }


class Stoc10(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.25, (Action.COOPERATE, Action.DEFECT): 0.25, (Action.DEFECT, Action.COOPERATE): 0.75, (Action.DEFECT, Action.DEFECT): 0.75 }


class Stoc11(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.25, (Action.COOPERATE, Action.DEFECT): 0.25, (Action.DEFECT, Action.COOPERATE): 0.75, (Action.DEFECT, Action.DEFECT): 1 }


class Stoc12(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.25, (Action.COOPERATE, Action.DEFECT): 0.25, (Action.DEFECT, Action.COOPERATE): 1, (Action.DEFECT, Action.DEFECT): 0.25 }


class Stoc13(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.25, (Action.COOPERATE, Action.DEFECT): 0.25, (Action.DEFECT, Action.COOPERATE): 1, (Action.DEFECT, Action.DEFECT): 0.5 }


class Stoc14(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.25, (Action.COOPERATE, Action.DEFECT): 0.25, (Action.DEFECT, Action.COOPERATE): 1, (Action.DEFECT, Action.DEFECT): 0.75 }


class Stoc15(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.25, (Action.COOPERATE, Action.DEFECT): 0.25, (Action.DEFECT, Action.COOPERATE): 1, (Action.DEFECT, Action.DEFECT): 1 }


class Stoc16(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.25, (Action.COOPERATE, Action.DEFECT): 0.5, (Action.DEFECT, Action.COOPERATE): 0.25, (Action.DEFECT, Action.DEFECT): 0.25 }


class Stoc17(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.25, (Action.COOPERATE, Action.DEFECT): 0.5, (Action.DEFECT, Action.COOPERATE): 0.25, (Action.DEFECT, Action.DEFECT): 0.5 }


class Stoc18(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.25, (Action.COOPERATE, Action.DEFECT): 0.5, (Action.DEFECT, Action.COOPERATE): 0.25, (Action.DEFECT, Action.DEFECT): 0.75 }


class Stoc19(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.25, (Action.COOPERATE, Action.DEFECT): 0.5, (Action.DEFECT, Action.COOPERATE): 0.25, (Action.DEFECT, Action.DEFECT): 1 }


class Stoc20(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.25, (Action.COOPERATE, Action.DEFECT): 0.5, (Action.DEFECT, Action.COOPERATE): 0.5, (Action.DEFECT, Action.DEFECT): 0.25 }


class Stoc21(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.25, (Action.COOPERATE, Action.DEFECT): 0.5, (Action.DEFECT, Action.COOPERATE): 0.5, (Action.DEFECT, Action.DEFECT): 0.5 }


class Stoc22(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.25, (Action.COOPERATE, Action.DEFECT): 0.5, (Action.DEFECT, Action.COOPERATE): 0.5, (Action.DEFECT, Action.DEFECT): 0.75 }


class Stoc23(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.25, (Action.COOPERATE, Action.DEFECT): 0.5, (Action.DEFECT, Action.COOPERATE): 0.5, (Action.DEFECT, Action.DEFECT): 1 }


class Stoc24(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.25, (Action.COOPERATE, Action.DEFECT): 0.5, (Action.DEFECT, Action.COOPERATE): 0.75, (Action.DEFECT, Action.DEFECT): 0.25 }


class Stoc25(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.25, (Action.COOPERATE, Action.DEFECT): 0.5, (Action.DEFECT, Action.COOPERATE): 0.75, (Action.DEFECT, Action.DEFECT): 0.5 }


class Stoc26(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.25, (Action.COOPERATE, Action.DEFECT): 0.5, (Action.DEFECT, Action.COOPERATE): 0.75, (Action.DEFECT, Action.DEFECT): 0.75 }


class Stoc27(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.25, (Action.COOPERATE, Action.DEFECT): 0.5, (Action.DEFECT, Action.COOPERATE): 0.75, (Action.DEFECT, Action.DEFECT): 1 }


class Stoc28(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.25, (Action.COOPERATE, Action.DEFECT): 0.5, (Action.DEFECT, Action.COOPERATE): 1, (Action.DEFECT, Action.DEFECT): 0.25 }


class Stoc29(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.25, (Action.COOPERATE, Action.DEFECT): 0.5, (Action.DEFECT, Action.COOPERATE): 1, (Action.DEFECT, Action.DEFECT): 0.5 }


class Stoc30(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.25, (Action.COOPERATE, Action.DEFECT): 0.5, (Action.DEFECT, Action.COOPERATE): 1, (Action.DEFECT, Action.DEFECT): 0.75 }


class Stoc31(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.25, (Action.COOPERATE, Action.DEFECT): 0.5, (Action.DEFECT, Action.COOPERATE): 1, (Action.DEFECT, Action.DEFECT): 1 }


class Stoc32(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.25, (Action.COOPERATE, Action.DEFECT): 0.75, (Action.DEFECT, Action.COOPERATE): 0.25, (Action.DEFECT, Action.DEFECT): 0.25 }


class Stoc33(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.25, (Action.COOPERATE, Action.DEFECT): 0.75, (Action.DEFECT, Action.COOPERATE): 0.25, (Action.DEFECT, Action.DEFECT): 0.5 }


class Stoc34(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.25, (Action.COOPERATE, Action.DEFECT): 0.75, (Action.DEFECT, Action.COOPERATE): 0.25, (Action.DEFECT, Action.DEFECT): 0.75 }


class Stoc35(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.25, (Action.COOPERATE, Action.DEFECT): 0.75, (Action.DEFECT, Action.COOPERATE): 0.25, (Action.DEFECT, Action.DEFECT): 1 }


class Stoc36(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.25, (Action.COOPERATE, Action.DEFECT): 0.75, (Action.DEFECT, Action.COOPERATE): 0.5, (Action.DEFECT, Action.DEFECT): 0.25 }


class Stoc37(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.25, (Action.COOPERATE, Action.DEFECT): 0.75, (Action.DEFECT, Action.COOPERATE): 0.5, (Action.DEFECT, Action.DEFECT): 0.5 }


class Stoc38(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.25, (Action.COOPERATE, Action.DEFECT): 0.75, (Action.DEFECT, Action.COOPERATE): 0.5, (Action.DEFECT, Action.DEFECT): 0.75 }


class Stoc39(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.25, (Action.COOPERATE, Action.DEFECT): 0.75, (Action.DEFECT, Action.COOPERATE): 0.5, (Action.DEFECT, Action.DEFECT): 1 }


class Stoc40(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.25, (Action.COOPERATE, Action.DEFECT): 0.75, (Action.DEFECT, Action.COOPERATE): 0.75, (Action.DEFECT, Action.DEFECT): 0.25 }


class Stoc41(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.25, (Action.COOPERATE, Action.DEFECT): 0.75, (Action.DEFECT, Action.COOPERATE): 0.75, (Action.DEFECT, Action.DEFECT): 0.5 }


class Stoc42(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.25, (Action.COOPERATE, Action.DEFECT): 0.75, (Action.DEFECT, Action.COOPERATE): 0.75, (Action.DEFECT, Action.DEFECT): 0.75 }


class Stoc43(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.25, (Action.COOPERATE, Action.DEFECT): 0.75, (Action.DEFECT, Action.COOPERATE): 0.75, (Action.DEFECT, Action.DEFECT): 1 }


class Stoc44(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.25, (Action.COOPERATE, Action.DEFECT): 0.75, (Action.DEFECT, Action.COOPERATE): 1, (Action.DEFECT, Action.DEFECT): 0.25 }


class Stoc45(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.25, (Action.COOPERATE, Action.DEFECT): 0.75, (Action.DEFECT, Action.COOPERATE): 1, (Action.DEFECT, Action.DEFECT): 0.5 }


class Stoc46(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.25, (Action.COOPERATE, Action.DEFECT): 0.75, (Action.DEFECT, Action.COOPERATE): 1, (Action.DEFECT, Action.DEFECT): 0.75 }


class Stoc47(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.25, (Action.COOPERATE, Action.DEFECT): 0.75, (Action.DEFECT, Action.COOPERATE): 1, (Action.DEFECT, Action.DEFECT): 1 }


class Stoc48(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.25, (Action.COOPERATE, Action.DEFECT): 1, (Action.DEFECT, Action.COOPERATE): 0.25, (Action.DEFECT, Action.DEFECT): 0.25 }


class Stoc49(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.25, (Action.COOPERATE, Action.DEFECT): 1, (Action.DEFECT, Action.COOPERATE): 0.25, (Action.DEFECT, Action.DEFECT): 0.5 }


class Stoc50(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.25, (Action.COOPERATE, Action.DEFECT): 1, (Action.DEFECT, Action.COOPERATE): 0.25, (Action.DEFECT, Action.DEFECT): 0.75 }


class Stoc51(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.25, (Action.COOPERATE, Action.DEFECT): 1, (Action.DEFECT, Action.COOPERATE): 0.25, (Action.DEFECT, Action.DEFECT): 1 }


class Stoc52(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.25, (Action.COOPERATE, Action.DEFECT): 1, (Action.DEFECT, Action.COOPERATE): 0.5, (Action.DEFECT, Action.DEFECT): 0.25 }


class Stoc53(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.25, (Action.COOPERATE, Action.DEFECT): 1, (Action.DEFECT, Action.COOPERATE): 0.5, (Action.DEFECT, Action.DEFECT): 0.5 }


class Stoc54(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.25, (Action.COOPERATE, Action.DEFECT): 1, (Action.DEFECT, Action.COOPERATE): 0.5, (Action.DEFECT, Action.DEFECT): 0.75 }


class Stoc55(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.25, (Action.COOPERATE, Action.DEFECT): 1, (Action.DEFECT, Action.COOPERATE): 0.5, (Action.DEFECT, Action.DEFECT): 1 }


class Stoc56(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.25, (Action.COOPERATE, Action.DEFECT): 1, (Action.DEFECT, Action.COOPERATE): 0.75, (Action.DEFECT, Action.DEFECT): 0.25 }


class Stoc57(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.25, (Action.COOPERATE, Action.DEFECT): 1, (Action.DEFECT, Action.COOPERATE): 0.75, (Action.DEFECT, Action.DEFECT): 0.5 }


class Stoc58(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.25, (Action.COOPERATE, Action.DEFECT): 1, (Action.DEFECT, Action.COOPERATE): 0.75, (Action.DEFECT, Action.DEFECT): 0.75 }


class Stoc59(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.25, (Action.COOPERATE, Action.DEFECT): 1, (Action.DEFECT, Action.COOPERATE): 0.75, (Action.DEFECT, Action.DEFECT): 1 }


class Stoc60(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.25, (Action.COOPERATE, Action.DEFECT): 1, (Action.DEFECT, Action.COOPERATE): 1, (Action.DEFECT, Action.DEFECT): 0.25 }


class Stoc61(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.25, (Action.COOPERATE, Action.DEFECT): 1, (Action.DEFECT, Action.COOPERATE): 1, (Action.DEFECT, Action.DEFECT): 0.5 }


class Stoc62(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.25, (Action.COOPERATE, Action.DEFECT): 1, (Action.DEFECT, Action.COOPERATE): 1, (Action.DEFECT, Action.DEFECT): 0.75 }


class Stoc63(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.25, (Action.COOPERATE, Action.DEFECT): 1, (Action.DEFECT, Action.COOPERATE): 1, (Action.DEFECT, Action.DEFECT): 1 }


class Stoc64(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5, (Action.COOPERATE, Action.DEFECT): 0.25, (Action.DEFECT, Action.COOPERATE): 0.25, (Action.DEFECT, Action.DEFECT): 0.25 }


class Stoc65(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5, (Action.COOPERATE, Action.DEFECT): 0.25, (Action.DEFECT, Action.COOPERATE): 0.25, (Action.DEFECT, Action.DEFECT): 0.5 }


class Stoc66(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5, (Action.COOPERATE, Action.DEFECT): 0.25, (Action.DEFECT, Action.COOPERATE): 0.25, (Action.DEFECT, Action.DEFECT): 0.75 }


class Stoc67(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5, (Action.COOPERATE, Action.DEFECT): 0.25, (Action.DEFECT, Action.COOPERATE): 0.25, (Action.DEFECT, Action.DEFECT): 1 }


class Stoc68(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5, (Action.COOPERATE, Action.DEFECT): 0.25, (Action.DEFECT, Action.COOPERATE): 0.5, (Action.DEFECT, Action.DEFECT): 0.25 }


class Stoc69(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5, (Action.COOPERATE, Action.DEFECT): 0.25, (Action.DEFECT, Action.COOPERATE): 0.5, (Action.DEFECT, Action.DEFECT): 0.5 }


class Stoc70(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5, (Action.COOPERATE, Action.DEFECT): 0.25, (Action.DEFECT, Action.COOPERATE): 0.5, (Action.DEFECT, Action.DEFECT): 0.75 }


class Stoc71(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5, (Action.COOPERATE, Action.DEFECT): 0.25, (Action.DEFECT, Action.COOPERATE): 0.5, (Action.DEFECT, Action.DEFECT): 1 }


class Stoc72(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5, (Action.COOPERATE, Action.DEFECT): 0.25, (Action.DEFECT, Action.COOPERATE): 0.75, (Action.DEFECT, Action.DEFECT): 0.25 }


class Stoc73(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5, (Action.COOPERATE, Action.DEFECT): 0.25, (Action.DEFECT, Action.COOPERATE): 0.75, (Action.DEFECT, Action.DEFECT): 0.5 }


class Stoc74(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5, (Action.COOPERATE, Action.DEFECT): 0.25, (Action.DEFECT, Action.COOPERATE): 0.75, (Action.DEFECT, Action.DEFECT): 0.75 }


class Stoc75(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5, (Action.COOPERATE, Action.DEFECT): 0.25, (Action.DEFECT, Action.COOPERATE): 0.75, (Action.DEFECT, Action.DEFECT): 1 }


class Stoc76(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5, (Action.COOPERATE, Action.DEFECT): 0.25, (Action.DEFECT, Action.COOPERATE): 1, (Action.DEFECT, Action.DEFECT): 0.25 }


class Stoc77(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5, (Action.COOPERATE, Action.DEFECT): 0.25, (Action.DEFECT, Action.COOPERATE): 1, (Action.DEFECT, Action.DEFECT): 0.5 }


class Stoc78(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5, (Action.COOPERATE, Action.DEFECT): 0.25, (Action.DEFECT, Action.COOPERATE): 1, (Action.DEFECT, Action.DEFECT): 0.75 }


class Stoc79(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5, (Action.COOPERATE, Action.DEFECT): 0.25, (Action.DEFECT, Action.COOPERATE): 1, (Action.DEFECT, Action.DEFECT): 1 }


class Stoc80(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5, (Action.COOPERATE, Action.DEFECT): 0.5, (Action.DEFECT, Action.COOPERATE): 0.25, (Action.DEFECT, Action.DEFECT): 0.25 }


class Stoc81(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5, (Action.COOPERATE, Action.DEFECT): 0.5, (Action.DEFECT, Action.COOPERATE): 0.25, (Action.DEFECT, Action.DEFECT): 0.5 }


class Stoc82(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5, (Action.COOPERATE, Action.DEFECT): 0.5, (Action.DEFECT, Action.COOPERATE): 0.25, (Action.DEFECT, Action.DEFECT): 0.75 }


class Stoc83(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5, (Action.COOPERATE, Action.DEFECT): 0.5, (Action.DEFECT, Action.COOPERATE): 0.25, (Action.DEFECT, Action.DEFECT): 1 }


class Stoc84(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5, (Action.COOPERATE, Action.DEFECT): 0.5, (Action.DEFECT, Action.COOPERATE): 0.5, (Action.DEFECT, Action.DEFECT): 0.25 }


class Stoc85(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5, (Action.COOPERATE, Action.DEFECT): 0.5, (Action.DEFECT, Action.COOPERATE): 0.5, (Action.DEFECT, Action.DEFECT): 0.5 }


class Stoc86(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5, (Action.COOPERATE, Action.DEFECT): 0.5, (Action.DEFECT, Action.COOPERATE): 0.5, (Action.DEFECT, Action.DEFECT): 0.75 }


class Stoc87(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5, (Action.COOPERATE, Action.DEFECT): 0.5, (Action.DEFECT, Action.COOPERATE): 0.5, (Action.DEFECT, Action.DEFECT): 1 }


class Stoc88(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5, (Action.COOPERATE, Action.DEFECT): 0.5, (Action.DEFECT, Action.COOPERATE): 0.75, (Action.DEFECT, Action.DEFECT): 0.25 }


class Stoc89(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5, (Action.COOPERATE, Action.DEFECT): 0.5, (Action.DEFECT, Action.COOPERATE): 0.75, (Action.DEFECT, Action.DEFECT): 0.5 }


class Stoc90(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5, (Action.COOPERATE, Action.DEFECT): 0.5, (Action.DEFECT, Action.COOPERATE): 0.75, (Action.DEFECT, Action.DEFECT): 0.75 }


class Stoc91(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5, (Action.COOPERATE, Action.DEFECT): 0.5, (Action.DEFECT, Action.COOPERATE): 0.75, (Action.DEFECT, Action.DEFECT): 1 }


class Stoc92(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5, (Action.COOPERATE, Action.DEFECT): 0.5, (Action.DEFECT, Action.COOPERATE): 1, (Action.DEFECT, Action.DEFECT): 0.25 }


class Stoc93(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5, (Action.COOPERATE, Action.DEFECT): 0.5, (Action.DEFECT, Action.COOPERATE): 1, (Action.DEFECT, Action.DEFECT): 0.5 }


class Stoc94(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5, (Action.COOPERATE, Action.DEFECT): 0.5, (Action.DEFECT, Action.COOPERATE): 1, (Action.DEFECT, Action.DEFECT): 0.75 }


class Stoc95(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5, (Action.COOPERATE, Action.DEFECT): 0.5, (Action.DEFECT, Action.COOPERATE): 1, (Action.DEFECT, Action.DEFECT): 1 }


class Stoc96(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5, (Action.COOPERATE, Action.DEFECT): 0.75, (Action.DEFECT, Action.COOPERATE): 0.25, (Action.DEFECT, Action.DEFECT): 0.25 }


class Stoc97(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5, (Action.COOPERATE, Action.DEFECT): 0.75, (Action.DEFECT, Action.COOPERATE): 0.25, (Action.DEFECT, Action.DEFECT): 0.5 }


class Stoc98(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5, (Action.COOPERATE, Action.DEFECT): 0.75, (Action.DEFECT, Action.COOPERATE): 0.25, (Action.DEFECT, Action.DEFECT): 0.75 }


class Stoc99(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5, (Action.COOPERATE, Action.DEFECT): 0.75, (Action.DEFECT, Action.COOPERATE): 0.25, (Action.DEFECT, Action.DEFECT): 1 }


class Stoc100(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5, (Action.COOPERATE, Action.DEFECT): 0.75, (Action.DEFECT, Action.COOPERATE): 0.5, (Action.DEFECT, Action.DEFECT): 0.25 }


class Stoc101(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5, (Action.COOPERATE, Action.DEFECT): 0.75, (Action.DEFECT, Action.COOPERATE): 0.5, (Action.DEFECT, Action.DEFECT): 0.5 }


class Stoc102(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5, (Action.COOPERATE, Action.DEFECT): 0.75, (Action.DEFECT, Action.COOPERATE): 0.5, (Action.DEFECT, Action.DEFECT): 0.75 }


class Stoc103(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5, (Action.COOPERATE, Action.DEFECT): 0.75, (Action.DEFECT, Action.COOPERATE): 0.5, (Action.DEFECT, Action.DEFECT): 1 }


class Stoc104(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5, (Action.COOPERATE, Action.DEFECT): 0.75, (Action.DEFECT, Action.COOPERATE): 0.75, (Action.DEFECT, Action.DEFECT): 0.25 }


class Stoc105(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5, (Action.COOPERATE, Action.DEFECT): 0.75, (Action.DEFECT, Action.COOPERATE): 0.75, (Action.DEFECT, Action.DEFECT): 0.5 }


class Stoc106(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5, (Action.COOPERATE, Action.DEFECT): 0.75, (Action.DEFECT, Action.COOPERATE): 0.75, (Action.DEFECT, Action.DEFECT): 0.75 }


class Stoc107(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5, (Action.COOPERATE, Action.DEFECT): 0.75, (Action.DEFECT, Action.COOPERATE): 0.75, (Action.DEFECT, Action.DEFECT): 1 }


class Stoc108(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5, (Action.COOPERATE, Action.DEFECT): 0.75, (Action.DEFECT, Action.COOPERATE): 1, (Action.DEFECT, Action.DEFECT): 0.25 }


class Stoc109(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5, (Action.COOPERATE, Action.DEFECT): 0.75, (Action.DEFECT, Action.COOPERATE): 1, (Action.DEFECT, Action.DEFECT): 0.5 }


class Stoc110(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5, (Action.COOPERATE, Action.DEFECT): 0.75, (Action.DEFECT, Action.COOPERATE): 1, (Action.DEFECT, Action.DEFECT): 0.75 }


class Stoc111(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5, (Action.COOPERATE, Action.DEFECT): 0.75, (Action.DEFECT, Action.COOPERATE): 1, (Action.DEFECT, Action.DEFECT): 1 }


class Stoc112(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5, (Action.COOPERATE, Action.DEFECT): 1, (Action.DEFECT, Action.COOPERATE): 0.25, (Action.DEFECT, Action.DEFECT): 0.25 }


class Stoc113(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5, (Action.COOPERATE, Action.DEFECT): 1, (Action.DEFECT, Action.COOPERATE): 0.25, (Action.DEFECT, Action.DEFECT): 0.5 }


class Stoc114(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5, (Action.COOPERATE, Action.DEFECT): 1, (Action.DEFECT, Action.COOPERATE): 0.25, (Action.DEFECT, Action.DEFECT): 0.75 }


class Stoc115(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5, (Action.COOPERATE, Action.DEFECT): 1, (Action.DEFECT, Action.COOPERATE): 0.25, (Action.DEFECT, Action.DEFECT): 1 }


class Stoc116(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5, (Action.COOPERATE, Action.DEFECT): 1, (Action.DEFECT, Action.COOPERATE): 0.5, (Action.DEFECT, Action.DEFECT): 0.25 }


class Stoc117(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5, (Action.COOPERATE, Action.DEFECT): 1, (Action.DEFECT, Action.COOPERATE): 0.5, (Action.DEFECT, Action.DEFECT): 0.5 }


class Stoc118(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5, (Action.COOPERATE, Action.DEFECT): 1, (Action.DEFECT, Action.COOPERATE): 0.5, (Action.DEFECT, Action.DEFECT): 0.75 }


class Stoc119(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5, (Action.COOPERATE, Action.DEFECT): 1, (Action.DEFECT, Action.COOPERATE): 0.5, (Action.DEFECT, Action.DEFECT): 1 }


class Stoc120(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5, (Action.COOPERATE, Action.DEFECT): 1, (Action.DEFECT, Action.COOPERATE): 0.75, (Action.DEFECT, Action.DEFECT): 0.25 }


class Stoc121(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5, (Action.COOPERATE, Action.DEFECT): 1, (Action.DEFECT, Action.COOPERATE): 0.75, (Action.DEFECT, Action.DEFECT): 0.5 }


class Stoc122(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5, (Action.COOPERATE, Action.DEFECT): 1, (Action.DEFECT, Action.COOPERATE): 0.75, (Action.DEFECT, Action.DEFECT): 0.75 }


class Stoc123(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5, (Action.COOPERATE, Action.DEFECT): 1, (Action.DEFECT, Action.COOPERATE): 0.75, (Action.DEFECT, Action.DEFECT): 1 }


class Stoc124(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5, (Action.COOPERATE, Action.DEFECT): 1, (Action.DEFECT, Action.COOPERATE): 1, (Action.DEFECT, Action.DEFECT): 0.25 }


class Stoc125(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5, (Action.COOPERATE, Action.DEFECT): 1, (Action.DEFECT, Action.COOPERATE): 1, (Action.DEFECT, Action.DEFECT): 0.5 }


class Stoc126(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5, (Action.COOPERATE, Action.DEFECT): 1, (Action.DEFECT, Action.COOPERATE): 1, (Action.DEFECT, Action.DEFECT): 0.75 }


class Stoc127(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.5, (Action.COOPERATE, Action.DEFECT): 1, (Action.DEFECT, Action.COOPERATE): 1, (Action.DEFECT, Action.DEFECT): 1 }


class Stoc128(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.75, (Action.COOPERATE, Action.DEFECT): 0.25, (Action.DEFECT, Action.COOPERATE): 0.25, (Action.DEFECT, Action.DEFECT): 0.25 }


class Stoc129(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.75, (Action.COOPERATE, Action.DEFECT): 0.25, (Action.DEFECT, Action.COOPERATE): 0.25, (Action.DEFECT, Action.DEFECT): 0.5 }


class Stoc130(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.75, (Action.COOPERATE, Action.DEFECT): 0.25, (Action.DEFECT, Action.COOPERATE): 0.25, (Action.DEFECT, Action.DEFECT): 0.75 }


class Stoc131(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.75, (Action.COOPERATE, Action.DEFECT): 0.25, (Action.DEFECT, Action.COOPERATE): 0.25, (Action.DEFECT, Action.DEFECT): 1 }


class Stoc132(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.75, (Action.COOPERATE, Action.DEFECT): 0.25, (Action.DEFECT, Action.COOPERATE): 0.5, (Action.DEFECT, Action.DEFECT): 0.25 }


class Stoc133(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.75, (Action.COOPERATE, Action.DEFECT): 0.25, (Action.DEFECT, Action.COOPERATE): 0.5, (Action.DEFECT, Action.DEFECT): 0.5 }


class Stoc134(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.75, (Action.COOPERATE, Action.DEFECT): 0.25, (Action.DEFECT, Action.COOPERATE): 0.5, (Action.DEFECT, Action.DEFECT): 0.75 }


class Stoc135(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.75, (Action.COOPERATE, Action.DEFECT): 0.25, (Action.DEFECT, Action.COOPERATE): 0.5, (Action.DEFECT, Action.DEFECT): 1 }


class Stoc136(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.75, (Action.COOPERATE, Action.DEFECT): 0.25, (Action.DEFECT, Action.COOPERATE): 0.75, (Action.DEFECT, Action.DEFECT): 0.25 }


class Stoc137(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.75, (Action.COOPERATE, Action.DEFECT): 0.25, (Action.DEFECT, Action.COOPERATE): 0.75, (Action.DEFECT, Action.DEFECT): 0.5 }


class Stoc138(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.75, (Action.COOPERATE, Action.DEFECT): 0.25, (Action.DEFECT, Action.COOPERATE): 0.75, (Action.DEFECT, Action.DEFECT): 0.75 }


class Stoc139(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.75, (Action.COOPERATE, Action.DEFECT): 0.25, (Action.DEFECT, Action.COOPERATE): 0.75, (Action.DEFECT, Action.DEFECT): 1 }


class Stoc140(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.75, (Action.COOPERATE, Action.DEFECT): 0.25, (Action.DEFECT, Action.COOPERATE): 1, (Action.DEFECT, Action.DEFECT): 0.25 }


class Stoc141(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.75, (Action.COOPERATE, Action.DEFECT): 0.25, (Action.DEFECT, Action.COOPERATE): 1, (Action.DEFECT, Action.DEFECT): 0.5 }


class Stoc142(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.75, (Action.COOPERATE, Action.DEFECT): 0.25, (Action.DEFECT, Action.COOPERATE): 1, (Action.DEFECT, Action.DEFECT): 0.75 }


class Stoc143(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.75, (Action.COOPERATE, Action.DEFECT): 0.25, (Action.DEFECT, Action.COOPERATE): 1, (Action.DEFECT, Action.DEFECT): 1 }


class Stoc144(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.75, (Action.COOPERATE, Action.DEFECT): 0.5, (Action.DEFECT, Action.COOPERATE): 0.25, (Action.DEFECT, Action.DEFECT): 0.25 }


class Stoc145(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.75, (Action.COOPERATE, Action.DEFECT): 0.5, (Action.DEFECT, Action.COOPERATE): 0.25, (Action.DEFECT, Action.DEFECT): 0.5 }


class Stoc146(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.75, (Action.COOPERATE, Action.DEFECT): 0.5, (Action.DEFECT, Action.COOPERATE): 0.25, (Action.DEFECT, Action.DEFECT): 0.75 }


class Stoc147(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.75, (Action.COOPERATE, Action.DEFECT): 0.5, (Action.DEFECT, Action.COOPERATE): 0.25, (Action.DEFECT, Action.DEFECT): 1 }


class Stoc148(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.75, (Action.COOPERATE, Action.DEFECT): 0.5, (Action.DEFECT, Action.COOPERATE): 0.5, (Action.DEFECT, Action.DEFECT): 0.25 }


class Stoc149(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.75, (Action.COOPERATE, Action.DEFECT): 0.5, (Action.DEFECT, Action.COOPERATE): 0.5, (Action.DEFECT, Action.DEFECT): 0.5 }


class Stoc150(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.75, (Action.COOPERATE, Action.DEFECT): 0.5, (Action.DEFECT, Action.COOPERATE): 0.5, (Action.DEFECT, Action.DEFECT): 0.75 }


class Stoc151(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.75, (Action.COOPERATE, Action.DEFECT): 0.5, (Action.DEFECT, Action.COOPERATE): 0.5, (Action.DEFECT, Action.DEFECT): 1 }


class Stoc152(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.75, (Action.COOPERATE, Action.DEFECT): 0.5, (Action.DEFECT, Action.COOPERATE): 0.75, (Action.DEFECT, Action.DEFECT): 0.25 }


class Stoc153(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.75, (Action.COOPERATE, Action.DEFECT): 0.5, (Action.DEFECT, Action.COOPERATE): 0.75, (Action.DEFECT, Action.DEFECT): 0.5 }


class Stoc154(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.75, (Action.COOPERATE, Action.DEFECT): 0.5, (Action.DEFECT, Action.COOPERATE): 0.75, (Action.DEFECT, Action.DEFECT): 0.75 }


class Stoc155(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.75, (Action.COOPERATE, Action.DEFECT): 0.5, (Action.DEFECT, Action.COOPERATE): 0.75, (Action.DEFECT, Action.DEFECT): 1 }


class Stoc156(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.75, (Action.COOPERATE, Action.DEFECT): 0.5, (Action.DEFECT, Action.COOPERATE): 1, (Action.DEFECT, Action.DEFECT): 0.25 }


class Stoc157(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.75, (Action.COOPERATE, Action.DEFECT): 0.5, (Action.DEFECT, Action.COOPERATE): 1, (Action.DEFECT, Action.DEFECT): 0.5 }


class Stoc158(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.75, (Action.COOPERATE, Action.DEFECT): 0.5, (Action.DEFECT, Action.COOPERATE): 1, (Action.DEFECT, Action.DEFECT): 0.75 }


class Stoc159(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.75, (Action.COOPERATE, Action.DEFECT): 0.5, (Action.DEFECT, Action.COOPERATE): 1, (Action.DEFECT, Action.DEFECT): 1 }


class Stoc160(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.75, (Action.COOPERATE, Action.DEFECT): 0.75, (Action.DEFECT, Action.COOPERATE): 0.25, (Action.DEFECT, Action.DEFECT): 0.25 }


class Stoc161(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.75, (Action.COOPERATE, Action.DEFECT): 0.75, (Action.DEFECT, Action.COOPERATE): 0.25, (Action.DEFECT, Action.DEFECT): 0.5 }


class Stoc162(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.75, (Action.COOPERATE, Action.DEFECT): 0.75, (Action.DEFECT, Action.COOPERATE): 0.25, (Action.DEFECT, Action.DEFECT): 0.75 }


class Stoc163(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.75, (Action.COOPERATE, Action.DEFECT): 0.75, (Action.DEFECT, Action.COOPERATE): 0.25, (Action.DEFECT, Action.DEFECT): 1 }


class Stoc164(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.75, (Action.COOPERATE, Action.DEFECT): 0.75, (Action.DEFECT, Action.COOPERATE): 0.5, (Action.DEFECT, Action.DEFECT): 0.25 }


class Stoc165(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.75, (Action.COOPERATE, Action.DEFECT): 0.75, (Action.DEFECT, Action.COOPERATE): 0.5, (Action.DEFECT, Action.DEFECT): 0.5 }


class Stoc166(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.75, (Action.COOPERATE, Action.DEFECT): 0.75, (Action.DEFECT, Action.COOPERATE): 0.5, (Action.DEFECT, Action.DEFECT): 0.75 }


class Stoc167(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.75, (Action.COOPERATE, Action.DEFECT): 0.75, (Action.DEFECT, Action.COOPERATE): 0.5, (Action.DEFECT, Action.DEFECT): 1 }


class Stoc168(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.75, (Action.COOPERATE, Action.DEFECT): 0.75, (Action.DEFECT, Action.COOPERATE): 0.75, (Action.DEFECT, Action.DEFECT): 0.25 }


class Stoc169(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.75, (Action.COOPERATE, Action.DEFECT): 0.75, (Action.DEFECT, Action.COOPERATE): 0.75, (Action.DEFECT, Action.DEFECT): 0.5 }


class Stoc170(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.75, (Action.COOPERATE, Action.DEFECT): 0.75, (Action.DEFECT, Action.COOPERATE): 0.75, (Action.DEFECT, Action.DEFECT): 0.75 }


class Stoc171(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.75, (Action.COOPERATE, Action.DEFECT): 0.75, (Action.DEFECT, Action.COOPERATE): 0.75, (Action.DEFECT, Action.DEFECT): 1 }


class Stoc172(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.75, (Action.COOPERATE, Action.DEFECT): 0.75, (Action.DEFECT, Action.COOPERATE): 1, (Action.DEFECT, Action.DEFECT): 0.25 }


class Stoc173(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.75, (Action.COOPERATE, Action.DEFECT): 0.75, (Action.DEFECT, Action.COOPERATE): 1, (Action.DEFECT, Action.DEFECT): 0.5 }


class Stoc174(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.75, (Action.COOPERATE, Action.DEFECT): 0.75, (Action.DEFECT, Action.COOPERATE): 1, (Action.DEFECT, Action.DEFECT): 0.75 }


class Stoc175(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.75, (Action.COOPERATE, Action.DEFECT): 0.75, (Action.DEFECT, Action.COOPERATE): 1, (Action.DEFECT, Action.DEFECT): 1 }


class Stoc176(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.75, (Action.COOPERATE, Action.DEFECT): 1, (Action.DEFECT, Action.COOPERATE): 0.25, (Action.DEFECT, Action.DEFECT): 0.25 }


class Stoc177(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.75, (Action.COOPERATE, Action.DEFECT): 1, (Action.DEFECT, Action.COOPERATE): 0.25, (Action.DEFECT, Action.DEFECT): 0.5 }


class Stoc178(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.75, (Action.COOPERATE, Action.DEFECT): 1, (Action.DEFECT, Action.COOPERATE): 0.25, (Action.DEFECT, Action.DEFECT): 0.75 }


class Stoc179(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.75, (Action.COOPERATE, Action.DEFECT): 1, (Action.DEFECT, Action.COOPERATE): 0.25, (Action.DEFECT, Action.DEFECT): 1 }


class Stoc180(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.75, (Action.COOPERATE, Action.DEFECT): 1, (Action.DEFECT, Action.COOPERATE): 0.5, (Action.DEFECT, Action.DEFECT): 0.25 }


class Stoc181(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.75, (Action.COOPERATE, Action.DEFECT): 1, (Action.DEFECT, Action.COOPERATE): 0.5, (Action.DEFECT, Action.DEFECT): 0.5 }


class Stoc182(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.75, (Action.COOPERATE, Action.DEFECT): 1, (Action.DEFECT, Action.COOPERATE): 0.5, (Action.DEFECT, Action.DEFECT): 0.75 }


class Stoc183(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.75, (Action.COOPERATE, Action.DEFECT): 1, (Action.DEFECT, Action.COOPERATE): 0.5, (Action.DEFECT, Action.DEFECT): 1 }


class Stoc184(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.75, (Action.COOPERATE, Action.DEFECT): 1, (Action.DEFECT, Action.COOPERATE): 0.75, (Action.DEFECT, Action.DEFECT): 0.25 }


class Stoc185(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.75, (Action.COOPERATE, Action.DEFECT): 1, (Action.DEFECT, Action.COOPERATE): 0.75, (Action.DEFECT, Action.DEFECT): 0.5 }


class Stoc186(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.75, (Action.COOPERATE, Action.DEFECT): 1, (Action.DEFECT, Action.COOPERATE): 0.75, (Action.DEFECT, Action.DEFECT): 0.75 }


class Stoc187(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.75, (Action.COOPERATE, Action.DEFECT): 1, (Action.DEFECT, Action.COOPERATE): 0.75, (Action.DEFECT, Action.DEFECT): 1 }


class Stoc188(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.75, (Action.COOPERATE, Action.DEFECT): 1, (Action.DEFECT, Action.COOPERATE): 1, (Action.DEFECT, Action.DEFECT): 0.25 }


class Stoc189(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.75, (Action.COOPERATE, Action.DEFECT): 1, (Action.DEFECT, Action.COOPERATE): 1, (Action.DEFECT, Action.DEFECT): 0.5 }


class Stoc190(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.75, (Action.COOPERATE, Action.DEFECT): 1, (Action.DEFECT, Action.COOPERATE): 1, (Action.DEFECT, Action.DEFECT): 0.75 }


class Stoc191(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 0.75, (Action.COOPERATE, Action.DEFECT): 1, (Action.DEFECT, Action.COOPERATE): 1, (Action.DEFECT, Action.DEFECT): 1 }


class Stoc192(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 1, (Action.COOPERATE, Action.DEFECT): 0.25, (Action.DEFECT, Action.COOPERATE): 0.25, (Action.DEFECT, Action.DEFECT): 0.25 }


class Stoc193(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 1, (Action.COOPERATE, Action.DEFECT): 0.25, (Action.DEFECT, Action.COOPERATE): 0.25, (Action.DEFECT, Action.DEFECT): 0.5 }


class Stoc194(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 1, (Action.COOPERATE, Action.DEFECT): 0.25, (Action.DEFECT, Action.COOPERATE): 0.25, (Action.DEFECT, Action.DEFECT): 0.75 }


class Stoc195(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 1, (Action.COOPERATE, Action.DEFECT): 0.25, (Action.DEFECT, Action.COOPERATE): 0.25, (Action.DEFECT, Action.DEFECT): 1 }


class Stoc196(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 1, (Action.COOPERATE, Action.DEFECT): 0.25, (Action.DEFECT, Action.COOPERATE): 0.5, (Action.DEFECT, Action.DEFECT): 0.25 }


class Stoc197(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 1, (Action.COOPERATE, Action.DEFECT): 0.25, (Action.DEFECT, Action.COOPERATE): 0.5, (Action.DEFECT, Action.DEFECT): 0.5 }


class Stoc198(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 1, (Action.COOPERATE, Action.DEFECT): 0.25, (Action.DEFECT, Action.COOPERATE): 0.5, (Action.DEFECT, Action.DEFECT): 0.75 }


class Stoc199(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 1, (Action.COOPERATE, Action.DEFECT): 0.25, (Action.DEFECT, Action.COOPERATE): 0.5, (Action.DEFECT, Action.DEFECT): 1 }


class Stoc200(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 1, (Action.COOPERATE, Action.DEFECT): 0.25, (Action.DEFECT, Action.COOPERATE): 0.75, (Action.DEFECT, Action.DEFECT): 0.25 }


class Stoc201(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 1, (Action.COOPERATE, Action.DEFECT): 0.25, (Action.DEFECT, Action.COOPERATE): 0.75, (Action.DEFECT, Action.DEFECT): 0.5 }


class Stoc202(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 1, (Action.COOPERATE, Action.DEFECT): 0.25, (Action.DEFECT, Action.COOPERATE): 0.75, (Action.DEFECT, Action.DEFECT): 0.75 }


class Stoc203(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 1, (Action.COOPERATE, Action.DEFECT): 0.25, (Action.DEFECT, Action.COOPERATE): 0.75, (Action.DEFECT, Action.DEFECT): 1 }


class Stoc204(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 1, (Action.COOPERATE, Action.DEFECT): 0.25, (Action.DEFECT, Action.COOPERATE): 1, (Action.DEFECT, Action.DEFECT): 0.25 }


class Stoc205(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 1, (Action.COOPERATE, Action.DEFECT): 0.25, (Action.DEFECT, Action.COOPERATE): 1, (Action.DEFECT, Action.DEFECT): 0.5 }


class Stoc206(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 1, (Action.COOPERATE, Action.DEFECT): 0.25, (Action.DEFECT, Action.COOPERATE): 1, (Action.DEFECT, Action.DEFECT): 0.75 }


class Stoc207(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 1, (Action.COOPERATE, Action.DEFECT): 0.25, (Action.DEFECT, Action.COOPERATE): 1, (Action.DEFECT, Action.DEFECT): 1 }


class Stoc208(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 1, (Action.COOPERATE, Action.DEFECT): 0.5, (Action.DEFECT, Action.COOPERATE): 0.25, (Action.DEFECT, Action.DEFECT): 0.25 }


class Stoc209(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 1, (Action.COOPERATE, Action.DEFECT): 0.5, (Action.DEFECT, Action.COOPERATE): 0.25, (Action.DEFECT, Action.DEFECT): 0.5 }


class Stoc210(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 1, (Action.COOPERATE, Action.DEFECT): 0.5, (Action.DEFECT, Action.COOPERATE): 0.25, (Action.DEFECT, Action.DEFECT): 0.75 }


class Stoc211(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 1, (Action.COOPERATE, Action.DEFECT): 0.5, (Action.DEFECT, Action.COOPERATE): 0.25, (Action.DEFECT, Action.DEFECT): 1 }


class Stoc212(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 1, (Action.COOPERATE, Action.DEFECT): 0.5, (Action.DEFECT, Action.COOPERATE): 0.5, (Action.DEFECT, Action.DEFECT): 0.25 }


class Stoc213(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 1, (Action.COOPERATE, Action.DEFECT): 0.5, (Action.DEFECT, Action.COOPERATE): 0.5, (Action.DEFECT, Action.DEFECT): 0.5 }


class Stoc214(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 1, (Action.COOPERATE, Action.DEFECT): 0.5, (Action.DEFECT, Action.COOPERATE): 0.5, (Action.DEFECT, Action.DEFECT): 0.75 }


class Stoc215(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 1, (Action.COOPERATE, Action.DEFECT): 0.5, (Action.DEFECT, Action.COOPERATE): 0.5, (Action.DEFECT, Action.DEFECT): 1 }


class Stoc216(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 1, (Action.COOPERATE, Action.DEFECT): 0.5, (Action.DEFECT, Action.COOPERATE): 0.75, (Action.DEFECT, Action.DEFECT): 0.25 }


class Stoc217(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 1, (Action.COOPERATE, Action.DEFECT): 0.5, (Action.DEFECT, Action.COOPERATE): 0.75, (Action.DEFECT, Action.DEFECT): 0.5 }


class Stoc218(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 1, (Action.COOPERATE, Action.DEFECT): 0.5, (Action.DEFECT, Action.COOPERATE): 0.75, (Action.DEFECT, Action.DEFECT): 0.75 }


class Stoc219(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 1, (Action.COOPERATE, Action.DEFECT): 0.5, (Action.DEFECT, Action.COOPERATE): 0.75, (Action.DEFECT, Action.DEFECT): 1 }


class Stoc220(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 1, (Action.COOPERATE, Action.DEFECT): 0.5, (Action.DEFECT, Action.COOPERATE): 1, (Action.DEFECT, Action.DEFECT): 0.25 }


class Stoc221(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 1, (Action.COOPERATE, Action.DEFECT): 0.5, (Action.DEFECT, Action.COOPERATE): 1, (Action.DEFECT, Action.DEFECT): 0.5 }


class Stoc222(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 1, (Action.COOPERATE, Action.DEFECT): 0.5, (Action.DEFECT, Action.COOPERATE): 1, (Action.DEFECT, Action.DEFECT): 0.75 }


class Stoc223(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 1, (Action.COOPERATE, Action.DEFECT): 0.5, (Action.DEFECT, Action.COOPERATE): 1, (Action.DEFECT, Action.DEFECT): 1 }


class Stoc224(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 1, (Action.COOPERATE, Action.DEFECT): 0.75, (Action.DEFECT, Action.COOPERATE): 0.25, (Action.DEFECT, Action.DEFECT): 0.25 }


class Stoc225(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 1, (Action.COOPERATE, Action.DEFECT): 0.75, (Action.DEFECT, Action.COOPERATE): 0.25, (Action.DEFECT, Action.DEFECT): 0.5 }


class Stoc226(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 1, (Action.COOPERATE, Action.DEFECT): 0.75, (Action.DEFECT, Action.COOPERATE): 0.25, (Action.DEFECT, Action.DEFECT): 0.75 }


class Stoc227(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 1, (Action.COOPERATE, Action.DEFECT): 0.75, (Action.DEFECT, Action.COOPERATE): 0.25, (Action.DEFECT, Action.DEFECT): 1 }


class Stoc228(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 1, (Action.COOPERATE, Action.DEFECT): 0.75, (Action.DEFECT, Action.COOPERATE): 0.5, (Action.DEFECT, Action.DEFECT): 0.25 }


class Stoc229(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 1, (Action.COOPERATE, Action.DEFECT): 0.75, (Action.DEFECT, Action.COOPERATE): 0.5, (Action.DEFECT, Action.DEFECT): 0.5 }


class Stoc230(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 1, (Action.COOPERATE, Action.DEFECT): 0.75, (Action.DEFECT, Action.COOPERATE): 0.5, (Action.DEFECT, Action.DEFECT): 0.75 }


class Stoc231(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 1, (Action.COOPERATE, Action.DEFECT): 0.75, (Action.DEFECT, Action.COOPERATE): 0.5, (Action.DEFECT, Action.DEFECT): 1 }


class Stoc232(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 1, (Action.COOPERATE, Action.DEFECT): 0.75, (Action.DEFECT, Action.COOPERATE): 0.75, (Action.DEFECT, Action.DEFECT): 0.25 }


class Stoc233(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 1, (Action.COOPERATE, Action.DEFECT): 0.75, (Action.DEFECT, Action.COOPERATE): 0.75, (Action.DEFECT, Action.DEFECT): 0.5 }


class Stoc234(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 1, (Action.COOPERATE, Action.DEFECT): 0.75, (Action.DEFECT, Action.COOPERATE): 0.75, (Action.DEFECT, Action.DEFECT): 0.75 }


class Stoc235(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 1, (Action.COOPERATE, Action.DEFECT): 0.75, (Action.DEFECT, Action.COOPERATE): 0.75, (Action.DEFECT, Action.DEFECT): 1 }


class Stoc236(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 1, (Action.COOPERATE, Action.DEFECT): 0.75, (Action.DEFECT, Action.COOPERATE): 1, (Action.DEFECT, Action.DEFECT): 0.25 }


class Stoc237(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 1, (Action.COOPERATE, Action.DEFECT): 0.75, (Action.DEFECT, Action.COOPERATE): 1, (Action.DEFECT, Action.DEFECT): 0.5 }


class Stoc238(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 1, (Action.COOPERATE, Action.DEFECT): 0.75, (Action.DEFECT, Action.COOPERATE): 1, (Action.DEFECT, Action.DEFECT): 0.75 }


class Stoc239(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 1, (Action.COOPERATE, Action.DEFECT): 0.75, (Action.DEFECT, Action.COOPERATE): 1, (Action.DEFECT, Action.DEFECT): 1 }


class Stoc240(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 1, (Action.COOPERATE, Action.DEFECT): 1, (Action.DEFECT, Action.COOPERATE): 0.25, (Action.DEFECT, Action.DEFECT): 0.25 }


class Stoc241(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 1, (Action.COOPERATE, Action.DEFECT): 1, (Action.DEFECT, Action.COOPERATE): 0.25, (Action.DEFECT, Action.DEFECT): 0.5 }


class Stoc242(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 1, (Action.COOPERATE, Action.DEFECT): 1, (Action.DEFECT, Action.COOPERATE): 0.25, (Action.DEFECT, Action.DEFECT): 0.75 }


class Stoc243(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 1, (Action.COOPERATE, Action.DEFECT): 1, (Action.DEFECT, Action.COOPERATE): 0.25, (Action.DEFECT, Action.DEFECT): 1 }


class Stoc244(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 1, (Action.COOPERATE, Action.DEFECT): 1, (Action.DEFECT, Action.COOPERATE): 0.5, (Action.DEFECT, Action.DEFECT): 0.25 }


class Stoc245(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 1, (Action.COOPERATE, Action.DEFECT): 1, (Action.DEFECT, Action.COOPERATE): 0.5, (Action.DEFECT, Action.DEFECT): 0.5 }


class Stoc246(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 1, (Action.COOPERATE, Action.DEFECT): 1, (Action.DEFECT, Action.COOPERATE): 0.5, (Action.DEFECT, Action.DEFECT): 0.75 }


class Stoc247(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 1, (Action.COOPERATE, Action.DEFECT): 1, (Action.DEFECT, Action.COOPERATE): 0.5, (Action.DEFECT, Action.DEFECT): 1 }


class Stoc248(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 1, (Action.COOPERATE, Action.DEFECT): 1, (Action.DEFECT, Action.COOPERATE): 0.75, (Action.DEFECT, Action.DEFECT): 0.25 }


class Stoc249(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 1, (Action.COOPERATE, Action.DEFECT): 1, (Action.DEFECT, Action.COOPERATE): 0.75, (Action.DEFECT, Action.DEFECT): 0.5 }


class Stoc250(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 1, (Action.COOPERATE, Action.DEFECT): 1, (Action.DEFECT, Action.COOPERATE): 0.75, (Action.DEFECT, Action.DEFECT): 0.75 }


class Stoc251(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 1, (Action.COOPERATE, Action.DEFECT): 1, (Action.DEFECT, Action.COOPERATE): 0.75, (Action.DEFECT, Action.DEFECT): 1 }


class Stoc252(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 1, (Action.COOPERATE, Action.DEFECT): 1, (Action.DEFECT, Action.COOPERATE): 1, (Action.DEFECT, Action.DEFECT): 0.25 }


class Stoc253(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 1, (Action.COOPERATE, Action.DEFECT): 1, (Action.DEFECT, Action.COOPERATE): 1, (Action.DEFECT, Action.DEFECT): 0.5 }


class Stoc254(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 1, (Action.COOPERATE, Action.DEFECT): 1, (Action.DEFECT, Action.COOPERATE): 1, (Action.DEFECT, Action.DEFECT): 0.75 }


class Stoc255(ProbabilisticLB2):
    def __init__(self):
        super().__init__()

        self.p = {(Action.COOPERATE, Action.COOPERATE): 1, (Action.COOPERATE, Action.DEFECT): 1, (Action.DEFECT, Action.COOPERATE): 1, (Action.DEFECT, Action.DEFECT): 1 }




STOC_AGENTS = [ Stoc0,Stoc1,Stoc2,Stoc3,Stoc4,Stoc5,Stoc6,Stoc7,Stoc8,Stoc9,Stoc10,Stoc11,Stoc12,Stoc13,Stoc14,Stoc15,Stoc16,Stoc17,Stoc18,Stoc19,Stoc20,Stoc21,Stoc22,Stoc23,Stoc24,Stoc25,Stoc26,Stoc27,Stoc28,Stoc29,Stoc30,Stoc31,Stoc32,Stoc33,Stoc34,Stoc35,Stoc36,Stoc37,Stoc38,Stoc39,Stoc40,Stoc41,Stoc42,Stoc43,Stoc44,Stoc45,Stoc46,Stoc47,Stoc48,Stoc49,Stoc50,Stoc51,Stoc52,Stoc53,Stoc54,Stoc55,Stoc56,Stoc57,Stoc58,Stoc59,Stoc60,Stoc61,Stoc62,Stoc63,Stoc64,Stoc65,Stoc66,Stoc67,Stoc68,Stoc69,Stoc70,Stoc71,Stoc72,Stoc73,Stoc74,Stoc75,Stoc76,Stoc77,Stoc78,Stoc79,Stoc80,Stoc81,Stoc82,Stoc83,Stoc84,Stoc85,Stoc86,Stoc87,Stoc88,Stoc89,Stoc90,Stoc91,Stoc92,Stoc93,Stoc94,Stoc95,Stoc96,Stoc97,Stoc98,Stoc99,Stoc100,Stoc101,Stoc102,Stoc103,Stoc104,Stoc105,Stoc106,Stoc107,Stoc108,Stoc109,Stoc110,Stoc111,Stoc112,Stoc113,Stoc114,Stoc115,Stoc116,Stoc117,Stoc118,Stoc119,Stoc120,Stoc121,Stoc122,Stoc123,Stoc124,Stoc125,Stoc126,Stoc127,Stoc128,Stoc129,Stoc130,Stoc131,Stoc132,Stoc133,Stoc134,Stoc135,Stoc136,Stoc137,Stoc138,Stoc139,Stoc140,Stoc141,Stoc142,Stoc143,Stoc144,Stoc145,Stoc146,Stoc147,Stoc148,Stoc149,Stoc150,Stoc151,Stoc152,Stoc153,Stoc154,Stoc155,Stoc156,Stoc157,Stoc158,Stoc159,Stoc160,Stoc161,Stoc162,Stoc163,Stoc164,Stoc165,Stoc166,Stoc167,Stoc168,Stoc169,Stoc170,Stoc171,Stoc172,Stoc173,Stoc174,Stoc175,Stoc176,Stoc177,Stoc178,Stoc179,Stoc180,Stoc181,Stoc182,Stoc183,Stoc184,Stoc185,Stoc186,Stoc187,Stoc188,Stoc189,Stoc190,Stoc191,Stoc192,Stoc193,Stoc194,Stoc195,Stoc196,Stoc197,Stoc198,Stoc199,Stoc200,Stoc201,Stoc202,Stoc203,Stoc204,Stoc205,Stoc206,Stoc207,Stoc208,Stoc209,Stoc210,Stoc211,Stoc212,Stoc213,Stoc214,Stoc215,Stoc216,Stoc217,Stoc218,Stoc219,Stoc220,Stoc221,Stoc222,Stoc223,Stoc224,Stoc225,Stoc226,Stoc227,Stoc228,Stoc229,Stoc230,Stoc231,Stoc232,Stoc233,Stoc234,Stoc235,Stoc236,Stoc237,Stoc238,Stoc239,Stoc240,Stoc241,Stoc242,Stoc243,Stoc244,Stoc245,Stoc246,Stoc247,Stoc248,Stoc249,Stoc250,Stoc251,Stoc252,Stoc253,Stoc254,Stoc255]


STOC_HYPERPARAMS = {'Stoc0': {'p_cc': 0.25, 'p_cd': 0.25, 'p_dc': 0.25, 'p_dd': 0.25}, 'Stoc1': {'p_cc': 0.25, 'p_cd': 0.25, 'p_dc': 0.25, 'p_dd': 0.5}, 'Stoc2': {'p_cc': 0.25, 'p_cd': 0.25, 'p_dc': 0.25, 'p_dd': 0.75}, 'Stoc3': {'p_cc': 0.25, 'p_cd': 0.25, 'p_dc': 0.25, 'p_dd': 1}, 'Stoc4': {'p_cc': 0.25, 'p_cd': 0.25, 'p_dc': 0.5, 'p_dd': 0.25}, 'Stoc5': {'p_cc': 0.25, 'p_cd': 0.25, 'p_dc': 0.5, 'p_dd': 0.5}, 'Stoc6': {'p_cc': 0.25, 'p_cd': 0.25, 'p_dc': 0.5, 'p_dd': 0.75}, 'Stoc7': {'p_cc': 0.25, 'p_cd': 0.25, 'p_dc': 0.5, 'p_dd': 1}, 'Stoc8': {'p_cc': 0.25, 'p_cd': 0.25, 'p_dc': 0.75, 'p_dd': 0.25}, 'Stoc9': {'p_cc': 0.25, 'p_cd': 0.25, 'p_dc': 0.75, 'p_dd': 0.5}, 'Stoc10': {'p_cc': 0.25, 'p_cd': 0.25, 'p_dc': 0.75, 'p_dd': 0.75}, 'Stoc11': {'p_cc': 0.25, 'p_cd': 0.25, 'p_dc': 0.75, 'p_dd': 1}, 'Stoc12': {'p_cc': 0.25, 'p_cd': 0.25, 'p_dc': 1, 'p_dd': 0.25}, 'Stoc13': {'p_cc': 0.25, 'p_cd': 0.25, 'p_dc': 1, 'p_dd': 0.5}, 'Stoc14': {'p_cc': 0.25, 'p_cd': 0.25, 'p_dc': 1, 'p_dd': 0.75}, 'Stoc15': {'p_cc': 0.25, 'p_cd': 0.25, 'p_dc': 1, 'p_dd': 1}, 'Stoc16': {'p_cc': 0.25, 'p_cd': 0.5, 'p_dc': 0.25, 'p_dd': 0.25}, 'Stoc17': {'p_cc': 0.25, 'p_cd': 0.5, 'p_dc': 0.25, 'p_dd': 0.5}, 'Stoc18': {'p_cc': 0.25, 'p_cd': 0.5, 'p_dc': 0.25, 'p_dd': 0.75}, 'Stoc19': {'p_cc': 0.25, 'p_cd': 0.5, 'p_dc': 0.25, 'p_dd': 1}, 'Stoc20': {'p_cc': 0.25, 'p_cd': 0.5, 'p_dc': 0.5, 'p_dd': 0.25}, 'Stoc21': {'p_cc': 0.25, 'p_cd': 0.5, 'p_dc': 0.5, 'p_dd': 0.5}, 'Stoc22': {'p_cc': 0.25, 'p_cd': 0.5, 'p_dc': 0.5, 'p_dd': 0.75}, 'Stoc23': {'p_cc': 0.25, 'p_cd': 0.5, 'p_dc': 0.5, 'p_dd': 1}, 'Stoc24': {'p_cc': 0.25, 'p_cd': 0.5, 'p_dc': 0.75, 'p_dd': 0.25}, 'Stoc25': {'p_cc': 0.25, 'p_cd': 0.5, 'p_dc': 0.75, 'p_dd': 0.5}, 'Stoc26': {'p_cc': 0.25, 'p_cd': 0.5, 'p_dc': 0.75, 'p_dd': 0.75}, 'Stoc27': {'p_cc': 0.25, 'p_cd': 0.5, 'p_dc': 0.75, 'p_dd': 1}, 'Stoc28': {'p_cc': 0.25, 'p_cd': 0.5, 'p_dc': 1, 'p_dd': 0.25}, 'Stoc29': {'p_cc': 0.25, 'p_cd': 0.5, 'p_dc': 1, 'p_dd': 0.5}, 'Stoc30': {'p_cc': 0.25, 'p_cd': 0.5, 'p_dc': 1, 'p_dd': 0.75}, 'Stoc31': {'p_cc': 0.25, 'p_cd': 0.5, 'p_dc': 1, 'p_dd': 1}, 'Stoc32': {'p_cc': 0.25, 'p_cd': 0.75, 'p_dc': 0.25, 'p_dd': 0.25}, 'Stoc33': {'p_cc': 0.25, 'p_cd': 0.75, 'p_dc': 0.25, 'p_dd': 0.5}, 'Stoc34': {'p_cc': 0.25, 'p_cd': 0.75, 'p_dc': 0.25, 'p_dd': 0.75}, 'Stoc35': {'p_cc': 0.25, 'p_cd': 0.75, 'p_dc': 0.25, 'p_dd': 1}, 'Stoc36': {'p_cc': 0.25, 'p_cd': 0.75, 'p_dc': 0.5, 'p_dd': 0.25}, 'Stoc37': {'p_cc': 0.25, 'p_cd': 0.75, 'p_dc': 0.5, 'p_dd': 0.5}, 'Stoc38': {'p_cc': 0.25, 'p_cd': 0.75, 'p_dc': 0.5, 'p_dd': 0.75}, 'Stoc39': {'p_cc': 0.25, 'p_cd': 0.75, 'p_dc': 0.5, 'p_dd': 1}, 'Stoc40': {'p_cc': 0.25, 'p_cd': 0.75, 'p_dc': 0.75, 'p_dd': 0.25}, 'Stoc41': {'p_cc': 0.25, 'p_cd': 0.75, 'p_dc': 0.75, 'p_dd': 0.5}, 'Stoc42': {'p_cc': 0.25, 'p_cd': 0.75, 'p_dc': 0.75, 'p_dd': 0.75}, 'Stoc43': {'p_cc': 0.25, 'p_cd': 0.75, 'p_dc': 0.75, 'p_dd': 1}, 'Stoc44': {'p_cc': 0.25, 'p_cd': 0.75, 'p_dc': 1, 'p_dd': 0.25}, 'Stoc45': {'p_cc': 0.25, 'p_cd': 0.75, 'p_dc': 1, 'p_dd': 0.5}, 'Stoc46': {'p_cc': 0.25, 'p_cd': 0.75, 'p_dc': 1, 'p_dd': 0.75}, 'Stoc47': {'p_cc': 0.25, 'p_cd': 0.75, 'p_dc': 1, 'p_dd': 1}, 'Stoc48': {'p_cc': 0.25, 'p_cd': 1, 'p_dc': 0.25, 'p_dd': 0.25}, 'Stoc49': {'p_cc': 0.25, 'p_cd': 1, 'p_dc': 0.25, 'p_dd': 0.5}, 'Stoc50': {'p_cc': 0.25, 'p_cd': 1, 'p_dc': 0.25, 'p_dd': 0.75}, 'Stoc51': {'p_cc': 0.25, 'p_cd': 1, 'p_dc': 0.25, 'p_dd': 1}, 'Stoc52': {'p_cc': 0.25, 'p_cd': 1, 'p_dc': 0.5, 'p_dd': 0.25}, 'Stoc53': {'p_cc': 0.25, 'p_cd': 1, 'p_dc': 0.5, 'p_dd': 0.5}, 'Stoc54': {'p_cc': 0.25, 'p_cd': 1, 'p_dc': 0.5, 'p_dd': 0.75}, 'Stoc55': {'p_cc': 0.25, 'p_cd': 1, 'p_dc': 0.5, 'p_dd': 1}, 'Stoc56': {'p_cc': 0.25, 'p_cd': 1, 'p_dc': 0.75, 'p_dd': 0.25}, 'Stoc57': {'p_cc': 0.25, 'p_cd': 1, 'p_dc': 0.75, 'p_dd': 0.5}, 'Stoc58': {'p_cc': 0.25, 'p_cd': 1, 'p_dc': 0.75, 'p_dd': 0.75}, 'Stoc59': {'p_cc': 0.25, 'p_cd': 1, 'p_dc': 0.75, 'p_dd': 1}, 'Stoc60': {'p_cc': 0.25, 'p_cd': 1, 'p_dc': 1, 'p_dd': 0.25}, 'Stoc61': {'p_cc': 0.25, 'p_cd': 1, 'p_dc': 1, 'p_dd': 0.5}, 'Stoc62': {'p_cc': 0.25, 'p_cd': 1, 'p_dc': 1, 'p_dd': 0.75}, 'Stoc63': {'p_cc': 0.25, 'p_cd': 1, 'p_dc': 1, 'p_dd': 1}, 'Stoc64': {'p_cc': 0.5, 'p_cd': 0.25, 'p_dc': 0.25, 'p_dd': 0.25}, 'Stoc65': {'p_cc': 0.5, 'p_cd': 0.25, 'p_dc': 0.25, 'p_dd': 0.5}, 'Stoc66': {'p_cc': 0.5, 'p_cd': 0.25, 'p_dc': 0.25, 'p_dd': 0.75}, 'Stoc67': {'p_cc': 0.5, 'p_cd': 0.25, 'p_dc': 0.25, 'p_dd': 1}, 'Stoc68': {'p_cc': 0.5, 'p_cd': 0.25, 'p_dc': 0.5, 'p_dd': 0.25}, 'Stoc69': {'p_cc': 0.5, 'p_cd': 0.25, 'p_dc': 0.5, 'p_dd': 0.5}, 'Stoc70': {'p_cc': 0.5, 'p_cd': 0.25, 'p_dc': 0.5, 'p_dd': 0.75}, 'Stoc71': {'p_cc': 0.5, 'p_cd': 0.25, 'p_dc': 0.5, 'p_dd': 1}, 'Stoc72': {'p_cc': 0.5, 'p_cd': 0.25, 'p_dc': 0.75, 'p_dd': 0.25}, 'Stoc73': {'p_cc': 0.5, 'p_cd': 0.25, 'p_dc': 0.75, 'p_dd': 0.5}, 'Stoc74': {'p_cc': 0.5, 'p_cd': 0.25, 'p_dc': 0.75, 'p_dd': 0.75}, 'Stoc75': {'p_cc': 0.5, 'p_cd': 0.25, 'p_dc': 0.75, 'p_dd': 1}, 'Stoc76': {'p_cc': 0.5, 'p_cd': 0.25, 'p_dc': 1, 'p_dd': 0.25}, 'Stoc77': {'p_cc': 0.5, 'p_cd': 0.25, 'p_dc': 1, 'p_dd': 0.5}, 'Stoc78': {'p_cc': 0.5, 'p_cd': 0.25, 'p_dc': 1, 'p_dd': 0.75}, 'Stoc79': {'p_cc': 0.5, 'p_cd': 0.25, 'p_dc': 1, 'p_dd': 1}, 'Stoc80': {'p_cc': 0.5, 'p_cd': 0.5, 'p_dc': 0.25, 'p_dd': 0.25}, 'Stoc81': {'p_cc': 0.5, 'p_cd': 0.5, 'p_dc': 0.25, 'p_dd': 0.5}, 'Stoc82': {'p_cc': 0.5, 'p_cd': 0.5, 'p_dc': 0.25, 'p_dd': 0.75}, 'Stoc83': {'p_cc': 0.5, 'p_cd': 0.5, 'p_dc': 0.25, 'p_dd': 1}, 'Stoc84': {'p_cc': 0.5, 'p_cd': 0.5, 'p_dc': 0.5, 'p_dd': 0.25}, 'Stoc85': {'p_cc': 0.5, 'p_cd': 0.5, 'p_dc': 0.5, 'p_dd': 0.5}, 'Stoc86': {'p_cc': 0.5, 'p_cd': 0.5, 'p_dc': 0.5, 'p_dd': 0.75}, 'Stoc87': {'p_cc': 0.5, 'p_cd': 0.5, 'p_dc': 0.5, 'p_dd': 1}, 'Stoc88': {'p_cc': 0.5, 'p_cd': 0.5, 'p_dc': 0.75, 'p_dd': 0.25}, 'Stoc89': {'p_cc': 0.5, 'p_cd': 0.5, 'p_dc': 0.75, 'p_dd': 0.5}, 'Stoc90': {'p_cc': 0.5, 'p_cd': 0.5, 'p_dc': 0.75, 'p_dd': 0.75}, 'Stoc91': {'p_cc': 0.5, 'p_cd': 0.5, 'p_dc': 0.75, 'p_dd': 1}, 'Stoc92': {'p_cc': 0.5, 'p_cd': 0.5, 'p_dc': 1, 'p_dd': 0.25}, 'Stoc93': {'p_cc': 0.5, 'p_cd': 0.5, 'p_dc': 1, 'p_dd': 0.5}, 'Stoc94': {'p_cc': 0.5, 'p_cd': 0.5, 'p_dc': 1, 'p_dd': 0.75}, 'Stoc95': {'p_cc': 0.5, 'p_cd': 0.5, 'p_dc': 1, 'p_dd': 1}, 'Stoc96': {'p_cc': 0.5, 'p_cd': 0.75, 'p_dc': 0.25, 'p_dd': 0.25}, 'Stoc97': {'p_cc': 0.5, 'p_cd': 0.75, 'p_dc': 0.25, 'p_dd': 0.5}, 'Stoc98': {'p_cc': 0.5, 'p_cd': 0.75, 'p_dc': 0.25, 'p_dd': 0.75}, 'Stoc99': {'p_cc': 0.5, 'p_cd': 0.75, 'p_dc': 0.25, 'p_dd': 1}, 'Stoc100': {'p_cc': 0.5, 'p_cd': 0.75, 'p_dc': 0.5, 'p_dd': 0.25}, 'Stoc101': {'p_cc': 0.5, 'p_cd': 0.75, 'p_dc': 0.5, 'p_dd': 0.5}, 'Stoc102': {'p_cc': 0.5, 'p_cd': 0.75, 'p_dc': 0.5, 'p_dd': 0.75}, 'Stoc103': {'p_cc': 0.5, 'p_cd': 0.75, 'p_dc': 0.5, 'p_dd': 1}, 'Stoc104': {'p_cc': 0.5, 'p_cd': 0.75, 'p_dc': 0.75, 'p_dd': 0.25}, 'Stoc105': {'p_cc': 0.5, 'p_cd': 0.75, 'p_dc': 0.75, 'p_dd': 0.5}, 'Stoc106': {'p_cc': 0.5, 'p_cd': 0.75, 'p_dc': 0.75, 'p_dd': 0.75}, 'Stoc107': {'p_cc': 0.5, 'p_cd': 0.75, 'p_dc': 0.75, 'p_dd': 1}, 'Stoc108': {'p_cc': 0.5, 'p_cd': 0.75, 'p_dc': 1, 'p_dd': 0.25}, 'Stoc109': {'p_cc': 0.5, 'p_cd': 0.75, 'p_dc': 1, 'p_dd': 0.5}, 'Stoc110': {'p_cc': 0.5, 'p_cd': 0.75, 'p_dc': 1, 'p_dd': 0.75}, 'Stoc111': {'p_cc': 0.5, 'p_cd': 0.75, 'p_dc': 1, 'p_dd': 1}, 'Stoc112': {'p_cc': 0.5, 'p_cd': 1, 'p_dc': 0.25, 'p_dd': 0.25}, 'Stoc113': {'p_cc': 0.5, 'p_cd': 1, 'p_dc': 0.25, 'p_dd': 0.5}, 'Stoc114': {'p_cc': 0.5, 'p_cd': 1, 'p_dc': 0.25, 'p_dd': 0.75}, 'Stoc115': {'p_cc': 0.5, 'p_cd': 1, 'p_dc': 0.25, 'p_dd': 1}, 'Stoc116': {'p_cc': 0.5, 'p_cd': 1, 'p_dc': 0.5, 'p_dd': 0.25}, 'Stoc117': {'p_cc': 0.5, 'p_cd': 1, 'p_dc': 0.5, 'p_dd': 0.5}, 'Stoc118': {'p_cc': 0.5, 'p_cd': 1, 'p_dc': 0.5, 'p_dd': 0.75}, 'Stoc119': {'p_cc': 0.5, 'p_cd': 1, 'p_dc': 0.5, 'p_dd': 1}, 'Stoc120': {'p_cc': 0.5, 'p_cd': 1, 'p_dc': 0.75, 'p_dd': 0.25}, 'Stoc121': {'p_cc': 0.5, 'p_cd': 1, 'p_dc': 0.75, 'p_dd': 0.5}, 'Stoc122': {'p_cc': 0.5, 'p_cd': 1, 'p_dc': 0.75, 'p_dd': 0.75}, 'Stoc123': {'p_cc': 0.5, 'p_cd': 1, 'p_dc': 0.75, 'p_dd': 1}, 'Stoc124': {'p_cc': 0.5, 'p_cd': 1, 'p_dc': 1, 'p_dd': 0.25}, 'Stoc125': {'p_cc': 0.5, 'p_cd': 1, 'p_dc': 1, 'p_dd': 0.5}, 'Stoc126': {'p_cc': 0.5, 'p_cd': 1, 'p_dc': 1, 'p_dd': 0.75}, 'Stoc127': {'p_cc': 0.5, 'p_cd': 1, 'p_dc': 1, 'p_dd': 1}, 'Stoc128': {'p_cc': 0.75, 'p_cd': 0.25, 'p_dc': 0.25, 'p_dd': 0.25}, 'Stoc129': {'p_cc': 0.75, 'p_cd': 0.25, 'p_dc': 0.25, 'p_dd': 0.5}, 'Stoc130': {'p_cc': 0.75, 'p_cd': 0.25, 'p_dc': 0.25, 'p_dd': 0.75}, 'Stoc131': {'p_cc': 0.75, 'p_cd': 0.25, 'p_dc': 0.25, 'p_dd': 1}, 'Stoc132': {'p_cc': 0.75, 'p_cd': 0.25, 'p_dc': 0.5, 'p_dd': 0.25}, 'Stoc133': {'p_cc': 0.75, 'p_cd': 0.25, 'p_dc': 0.5, 'p_dd': 0.5}, 'Stoc134': {'p_cc': 0.75, 'p_cd': 0.25, 'p_dc': 0.5, 'p_dd': 0.75}, 'Stoc135': {'p_cc': 0.75, 'p_cd': 0.25, 'p_dc': 0.5, 'p_dd': 1}, 'Stoc136': {'p_cc': 0.75, 'p_cd': 0.25, 'p_dc': 0.75, 'p_dd': 0.25}, 'Stoc137': {'p_cc': 0.75, 'p_cd': 0.25, 'p_dc': 0.75, 'p_dd': 0.5}, 'Stoc138': {'p_cc': 0.75, 'p_cd': 0.25, 'p_dc': 0.75, 'p_dd': 0.75}, 'Stoc139': {'p_cc': 0.75, 'p_cd': 0.25, 'p_dc': 0.75, 'p_dd': 1}, 'Stoc140': {'p_cc': 0.75, 'p_cd': 0.25, 'p_dc': 1, 'p_dd': 0.25}, 'Stoc141': {'p_cc': 0.75, 'p_cd': 0.25, 'p_dc': 1, 'p_dd': 0.5}, 'Stoc142': {'p_cc': 0.75, 'p_cd': 0.25, 'p_dc': 1, 'p_dd': 0.75}, 'Stoc143': {'p_cc': 0.75, 'p_cd': 0.25, 'p_dc': 1, 'p_dd': 1}, 'Stoc144': {'p_cc': 0.75, 'p_cd': 0.5, 'p_dc': 0.25, 'p_dd': 0.25}, 'Stoc145': {'p_cc': 0.75, 'p_cd': 0.5, 'p_dc': 0.25, 'p_dd': 0.5}, 'Stoc146': {'p_cc': 0.75, 'p_cd': 0.5, 'p_dc': 0.25, 'p_dd': 0.75}, 'Stoc147': {'p_cc': 0.75, 'p_cd': 0.5, 'p_dc': 0.25, 'p_dd': 1}, 'Stoc148': {'p_cc': 0.75, 'p_cd': 0.5, 'p_dc': 0.5, 'p_dd': 0.25}, 'Stoc149': {'p_cc': 0.75, 'p_cd': 0.5, 'p_dc': 0.5, 'p_dd': 0.5}, 'Stoc150': {'p_cc': 0.75, 'p_cd': 0.5, 'p_dc': 0.5, 'p_dd': 0.75}, 'Stoc151': {'p_cc': 0.75, 'p_cd': 0.5, 'p_dc': 0.5, 'p_dd': 1}, 'Stoc152': {'p_cc': 0.75, 'p_cd': 0.5, 'p_dc': 0.75, 'p_dd': 0.25}, 'Stoc153': {'p_cc': 0.75, 'p_cd': 0.5, 'p_dc': 0.75, 'p_dd': 0.5}, 'Stoc154': {'p_cc': 0.75, 'p_cd': 0.5, 'p_dc': 0.75, 'p_dd': 0.75}, 'Stoc155': {'p_cc': 0.75, 'p_cd': 0.5, 'p_dc': 0.75, 'p_dd': 1}, 'Stoc156': {'p_cc': 0.75, 'p_cd': 0.5, 'p_dc': 1, 'p_dd': 0.25}, 'Stoc157': {'p_cc': 0.75, 'p_cd': 0.5, 'p_dc': 1, 'p_dd': 0.5}, 'Stoc158': {'p_cc': 0.75, 'p_cd': 0.5, 'p_dc': 1, 'p_dd': 0.75}, 'Stoc159': {'p_cc': 0.75, 'p_cd': 0.5, 'p_dc': 1, 'p_dd': 1}, 'Stoc160': {'p_cc': 0.75, 'p_cd': 0.75, 'p_dc': 0.25, 'p_dd': 0.25}, 'Stoc161': {'p_cc': 0.75, 'p_cd': 0.75, 'p_dc': 0.25, 'p_dd': 0.5}, 'Stoc162': {'p_cc': 0.75, 'p_cd': 0.75, 'p_dc': 0.25, 'p_dd': 0.75}, 'Stoc163': {'p_cc': 0.75, 'p_cd': 0.75, 'p_dc': 0.25, 'p_dd': 1}, 'Stoc164': {'p_cc': 0.75, 'p_cd': 0.75, 'p_dc': 0.5, 'p_dd': 0.25}, 'Stoc165': {'p_cc': 0.75, 'p_cd': 0.75, 'p_dc': 0.5, 'p_dd': 0.5}, 'Stoc166': {'p_cc': 0.75, 'p_cd': 0.75, 'p_dc': 0.5, 'p_dd': 0.75}, 'Stoc167': {'p_cc': 0.75, 'p_cd': 0.75, 'p_dc': 0.5, 'p_dd': 1}, 'Stoc168': {'p_cc': 0.75, 'p_cd': 0.75, 'p_dc': 0.75, 'p_dd': 0.25}, 'Stoc169': {'p_cc': 0.75, 'p_cd': 0.75, 'p_dc': 0.75, 'p_dd': 0.5}, 'Stoc170': {'p_cc': 0.75, 'p_cd': 0.75, 'p_dc': 0.75, 'p_dd': 0.75}, 'Stoc171': {'p_cc': 0.75, 'p_cd': 0.75, 'p_dc': 0.75, 'p_dd': 1}, 'Stoc172': {'p_cc': 0.75, 'p_cd': 0.75, 'p_dc': 1, 'p_dd': 0.25}, 'Stoc173': {'p_cc': 0.75, 'p_cd': 0.75, 'p_dc': 1, 'p_dd': 0.5}, 'Stoc174': {'p_cc': 0.75, 'p_cd': 0.75, 'p_dc': 1, 'p_dd': 0.75}, 'Stoc175': {'p_cc': 0.75, 'p_cd': 0.75, 'p_dc': 1, 'p_dd': 1}, 'Stoc176': {'p_cc': 0.75, 'p_cd': 1, 'p_dc': 0.25, 'p_dd': 0.25}, 'Stoc177': {'p_cc': 0.75, 'p_cd': 1, 'p_dc': 0.25, 'p_dd': 0.5}, 'Stoc178': {'p_cc': 0.75, 'p_cd': 1, 'p_dc': 0.25, 'p_dd': 0.75}, 'Stoc179': {'p_cc': 0.75, 'p_cd': 1, 'p_dc': 0.25, 'p_dd': 1}, 'Stoc180': {'p_cc': 0.75, 'p_cd': 1, 'p_dc': 0.5, 'p_dd': 0.25}, 'Stoc181': {'p_cc': 0.75, 'p_cd': 1, 'p_dc': 0.5, 'p_dd': 0.5}, 'Stoc182': {'p_cc': 0.75, 'p_cd': 1, 'p_dc': 0.5, 'p_dd': 0.75}, 'Stoc183': {'p_cc': 0.75, 'p_cd': 1, 'p_dc': 0.5, 'p_dd': 1}, 'Stoc184': {'p_cc': 0.75, 'p_cd': 1, 'p_dc': 0.75, 'p_dd': 0.25}, 'Stoc185': {'p_cc': 0.75, 'p_cd': 1, 'p_dc': 0.75, 'p_dd': 0.5}, 'Stoc186': {'p_cc': 0.75, 'p_cd': 1, 'p_dc': 0.75, 'p_dd': 0.75}, 'Stoc187': {'p_cc': 0.75, 'p_cd': 1, 'p_dc': 0.75, 'p_dd': 1}, 'Stoc188': {'p_cc': 0.75, 'p_cd': 1, 'p_dc': 1, 'p_dd': 0.25}, 'Stoc189': {'p_cc': 0.75, 'p_cd': 1, 'p_dc': 1, 'p_dd': 0.5}, 'Stoc190': {'p_cc': 0.75, 'p_cd': 1, 'p_dc': 1, 'p_dd': 0.75}, 'Stoc191': {'p_cc': 0.75, 'p_cd': 1, 'p_dc': 1, 'p_dd': 1}, 'Stoc192': {'p_cc': 1, 'p_cd': 0.25, 'p_dc': 0.25, 'p_dd': 0.25}, 'Stoc193': {'p_cc': 1, 'p_cd': 0.25, 'p_dc': 0.25, 'p_dd': 0.5}, 'Stoc194': {'p_cc': 1, 'p_cd': 0.25, 'p_dc': 0.25, 'p_dd': 0.75}, 'Stoc195': {'p_cc': 1, 'p_cd': 0.25, 'p_dc': 0.25, 'p_dd': 1}, 'Stoc196': {'p_cc': 1, 'p_cd': 0.25, 'p_dc': 0.5, 'p_dd': 0.25}, 'Stoc197': {'p_cc': 1, 'p_cd': 0.25, 'p_dc': 0.5, 'p_dd': 0.5}, 'Stoc198': {'p_cc': 1, 'p_cd': 0.25, 'p_dc': 0.5, 'p_dd': 0.75}, 'Stoc199': {'p_cc': 1, 'p_cd': 0.25, 'p_dc': 0.5, 'p_dd': 1}, 'Stoc200': {'p_cc': 1, 'p_cd': 0.25, 'p_dc': 0.75, 'p_dd': 0.25}, 'Stoc201': {'p_cc': 1, 'p_cd': 0.25, 'p_dc': 0.75, 'p_dd': 0.5}, 'Stoc202': {'p_cc': 1, 'p_cd': 0.25, 'p_dc': 0.75, 'p_dd': 0.75}, 'Stoc203': {'p_cc': 1, 'p_cd': 0.25, 'p_dc': 0.75, 'p_dd': 1}, 'Stoc204': {'p_cc': 1, 'p_cd': 0.25, 'p_dc': 1, 'p_dd': 0.25}, 'Stoc205': {'p_cc': 1, 'p_cd': 0.25, 'p_dc': 1, 'p_dd': 0.5}, 'Stoc206': {'p_cc': 1, 'p_cd': 0.25, 'p_dc': 1, 'p_dd': 0.75}, 'Stoc207': {'p_cc': 1, 'p_cd': 0.25, 'p_dc': 1, 'p_dd': 1}, 'Stoc208': {'p_cc': 1, 'p_cd': 0.5, 'p_dc': 0.25, 'p_dd': 0.25}, 'Stoc209': {'p_cc': 1, 'p_cd': 0.5, 'p_dc': 0.25, 'p_dd': 0.5}, 'Stoc210': {'p_cc': 1, 'p_cd': 0.5, 'p_dc': 0.25, 'p_dd': 0.75}, 'Stoc211': {'p_cc': 1, 'p_cd': 0.5, 'p_dc': 0.25, 'p_dd': 1}, 'Stoc212': {'p_cc': 1, 'p_cd': 0.5, 'p_dc': 0.5, 'p_dd': 0.25}, 'Stoc213': {'p_cc': 1, 'p_cd': 0.5, 'p_dc': 0.5, 'p_dd': 0.5}, 'Stoc214': {'p_cc': 1, 'p_cd': 0.5, 'p_dc': 0.5, 'p_dd': 0.75}, 'Stoc215': {'p_cc': 1, 'p_cd': 0.5, 'p_dc': 0.5, 'p_dd': 1}, 'Stoc216': {'p_cc': 1, 'p_cd': 0.5, 'p_dc': 0.75, 'p_dd': 0.25}, 'Stoc217': {'p_cc': 1, 'p_cd': 0.5, 'p_dc': 0.75, 'p_dd': 0.5}, 'Stoc218': {'p_cc': 1, 'p_cd': 0.5, 'p_dc': 0.75, 'p_dd': 0.75}, 'Stoc219': {'p_cc': 1, 'p_cd': 0.5, 'p_dc': 0.75, 'p_dd': 1}, 'Stoc220': {'p_cc': 1, 'p_cd': 0.5, 'p_dc': 1, 'p_dd': 0.25}, 'Stoc221': {'p_cc': 1, 'p_cd': 0.5, 'p_dc': 1, 'p_dd': 0.5}, 'Stoc222': {'p_cc': 1, 'p_cd': 0.5, 'p_dc': 1, 'p_dd': 0.75}, 'Stoc223': {'p_cc': 1, 'p_cd': 0.5, 'p_dc': 1, 'p_dd': 1}, 'Stoc224': {'p_cc': 1, 'p_cd': 0.75, 'p_dc': 0.25, 'p_dd': 0.25}, 'Stoc225': {'p_cc': 1, 'p_cd': 0.75, 'p_dc': 0.25, 'p_dd': 0.5}, 'Stoc226': {'p_cc': 1, 'p_cd': 0.75, 'p_dc': 0.25, 'p_dd': 0.75}, 'Stoc227': {'p_cc': 1, 'p_cd': 0.75, 'p_dc': 0.25, 'p_dd': 1}, 'Stoc228': {'p_cc': 1, 'p_cd': 0.75, 'p_dc': 0.5, 'p_dd': 0.25}, 'Stoc229': {'p_cc': 1, 'p_cd': 0.75, 'p_dc': 0.5, 'p_dd': 0.5}, 'Stoc230': {'p_cc': 1, 'p_cd': 0.75, 'p_dc': 0.5, 'p_dd': 0.75}, 'Stoc231': {'p_cc': 1, 'p_cd': 0.75, 'p_dc': 0.5, 'p_dd': 1}, 'Stoc232': {'p_cc': 1, 'p_cd': 0.75, 'p_dc': 0.75, 'p_dd': 0.25}, 'Stoc233': {'p_cc': 1, 'p_cd': 0.75, 'p_dc': 0.75, 'p_dd': 0.5}, 'Stoc234': {'p_cc': 1, 'p_cd': 0.75, 'p_dc': 0.75, 'p_dd': 0.75}, 'Stoc235': {'p_cc': 1, 'p_cd': 0.75, 'p_dc': 0.75, 'p_dd': 1}, 'Stoc236': {'p_cc': 1, 'p_cd': 0.75, 'p_dc': 1, 'p_dd': 0.25}, 'Stoc237': {'p_cc': 1, 'p_cd': 0.75, 'p_dc': 1, 'p_dd': 0.5}, 'Stoc238': {'p_cc': 1, 'p_cd': 0.75, 'p_dc': 1, 'p_dd': 0.75}, 'Stoc239': {'p_cc': 1, 'p_cd': 0.75, 'p_dc': 1, 'p_dd': 1}, 'Stoc240': {'p_cc': 1, 'p_cd': 1, 'p_dc': 0.25, 'p_dd': 0.25}, 'Stoc241': {'p_cc': 1, 'p_cd': 1, 'p_dc': 0.25, 'p_dd': 0.5}, 'Stoc242': {'p_cc': 1, 'p_cd': 1, 'p_dc': 0.25, 'p_dd': 0.75}, 'Stoc243': {'p_cc': 1, 'p_cd': 1, 'p_dc': 0.25, 'p_dd': 1}, 'Stoc244': {'p_cc': 1, 'p_cd': 1, 'p_dc': 0.5, 'p_dd': 0.25}, 'Stoc245': {'p_cc': 1, 'p_cd': 1, 'p_dc': 0.5, 'p_dd': 0.5}, 'Stoc246': {'p_cc': 1, 'p_cd': 1, 'p_dc': 0.5, 'p_dd': 0.75}, 'Stoc247': {'p_cc': 1, 'p_cd': 1, 'p_dc': 0.5, 'p_dd': 1}, 'Stoc248': {'p_cc': 1, 'p_cd': 1, 'p_dc': 0.75, 'p_dd': 0.25}, 'Stoc249': {'p_cc': 1, 'p_cd': 1, 'p_dc': 0.75, 'p_dd': 0.5}, 'Stoc250': {'p_cc': 1, 'p_cd': 1, 'p_dc': 0.75, 'p_dd': 0.75}, 'Stoc251': {'p_cc': 1, 'p_cd': 1, 'p_dc': 0.75, 'p_dd': 1}, 'Stoc252': {'p_cc': 1, 'p_cd': 1, 'p_dc': 1, 'p_dd': 0.25}, 'Stoc253': {'p_cc': 1, 'p_cd': 1, 'p_dc': 1, 'p_dd': 0.5}, 'Stoc254': {'p_cc': 1, 'p_cd': 1, 'p_dc': 1, 'p_dd': 0.75}, 'Stoc255': {'p_cc': 1, 'p_cd': 1, 'p_dc': 1, 'p_dd': 1}}
