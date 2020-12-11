class Solow:
    def __init__(self,params):
        """
        Exogenous parameters in Solow growth model:
        n = population growth rate
        s = saving rate
        d = depreciation rate
        alpha = share of capital, alpha
        g = technological growth rate
        """
        self.params = params

    def cobb_douglas(self):
        return True if self.params['alpha'] !=1 else False

    def calc_k_star(self):
        n = self.params['n']
        s = self.params['s']
        d = self.params['d']
        alpha = self.params['alpha']
        g = self.params['g']
        k_star = (s/(n+g+d))**(1/(1-alpha)) if self.cobb_douglas() else s/(n+g+d)
        return k_star

    def calc_y_star(self):
        return self.calc_k_star()**self.params['alpha']

    def calc_c_star(self):
        return (1-self.params['s'])*self.calc_y_star()

    def predict_k(self,init_k):
        k = [init_k]
        for t in range(1,200):
            k.append((self.params['s']*(k[t-1]**self.params['alpha'])+(1-self.params['d'])*k[t-1])/(1+self.params['n']))
        return k

# params = {
#     'n': 0.01,
#     's': 0.2,
#     'g': 0.02,
#     'alpha': 1/3,
#     'd':0.04
# }
# model = Solow(params)
# print(model.calc_k_star())
# print(model.predict_k(init_k=6))
# print(model.calc_y_star())
# print(model.calc_c_star())