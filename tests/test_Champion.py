'''run by python -m pytest'''

import pytest
from tournament.agents.axelrod_second import Champion
from tournament.agents.constant import AllC, AllD
from tournament.action import Action
from tournament.agent import Agent
from tournament.match import PAYOFF_MATRIX, Match

C, D = Action.COOPERATE, Action.DEFECT

class Test_Champion:

    def test_first_ten_round(self):
        a = Champion()
        b = AllD()
        w = Match(a, b).play_moves(1,10,0)
        for i in range(10):
            assert next(w)[0][0] == C
    
    def test_next_fifty_round(self):
        a = Champion()
        b = AllD()
        w = Match(a, b).play_moves(1, 25, 0)
        for i in range(25):
            ans = next(w)[0][0]
            if i >= 15:
                assert ans == D

    def test_after_25_coop1(self):
        a = Champion()
        opp_history = []
        for i in range(50):
            opp_history.append(C)

        assert a.play_move(opp_history,opp_history) == C

    def test_after_25_coop2(self):
        a = Champion()
        opp_history = []
        for i in range(100):
            if i < 61:
                opp_history.append(C)
            else:
                opp_history.append(D)

        assert a.play_move(opp_history,opp_history) == C

    def test_after_25_coop2(self):
        a = Champion()
        opp_history = []
        for i in range(50):
            opp_history.append(D)
        assert a.play_move(opp_history, opp_history) == D




