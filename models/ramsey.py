class Ramsey:
    """
    The Ramsey-Cass-Koopmans Infinite Horizon Model
    ro: discount rate
    theta : coefficient of relative risk aversion
    """
    def __init__(self,params):
        self.params = params

    def get_instant_utility(self):
        theta = self.params['theta']
        C = self.params['C']
        uti = (C^(1-theta))/(1-theta)
        return uti

    def household_utility(self, Lt, H):
        ro = self.params['ro']
        theta = self.params['theta']
        u = self.get_instant_utility()
        C = self.params['C']
        return # will add