"""
Contains subclasses of TabluarQLearner with varying hyperparameters.
"""

from tournament.agents.tabluar_q_learner import TabluarQLearner


class TDoubleLookBack(TabluarQLearner):
    def __init__(self):
        super().init()
        self._len_history = 2


class TTripleLookBack(TabluarQLearner):
    def __init__(self):
        super().init()
        self._len_history = 3


class THighExplorationRate(TabluarQLearner):
    def __init__(self):
        super().init()
        self._epsilon = 0.25


class TLowExplorationRate(TabluarQLearner):
    def __init__(self):
        super().init()
        self._epsilon = self._decay_limit


class TLowDiscountRate(TabluarQLearner):
    def __init__(self):
        super().init()
        self._discount_rate = 0.75
