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
        """
        Check if the function is in Cobb-Douglas form
        """
        return True if self.params['alpha'] !=1 else False

    def calc_k_star(self):
        """
        Calculate golden rule level of capital
        """
        n = self.params['n']
        s = self.params['s']
        d = self.params['d']
        alpha = self.params['alpha']
        g = self.params['g']
        k_star = (s/(n+g+d))**(1/(1-alpha)) if self.cobb_douglas() else s/(n+g+d)
        return k_star

    def calc_y_star(self):
        """
        Caluclate golden rule level of output
        """
        return self.calc_k_star()**self.params['alpha']

    def calc_c_star(self):
        """
        Calculate golden rule level of consumption
        """
        return (1-self.params['s'])*self.calc_y_star()

    def predict_k(self, init_k,t):
        """
        Simulate next capital for time t based on initial value of k
        """
        k = [init_k]
        for t in range(1,t):
            k.append((self.params['s']*(k[t-1]**self.params['alpha'])+(1-self.params['d'])*k[t-1])/(1+self.params['n']))
        return k

    def cobb_douglas_output(self, k):
        """
        Cobb-Douglas production function.
        """
        alpha = self.params['alpha']
        return k ** alpha

    def marginal_prod_capital(self, k):
        """
        Marginal product of capital k
        """
        alpha = self.params['alpha']
        mpk = alpha * k ** (alpha - 1)
        return mpk

    def equation_of_motion_k(self, k):
        """
        Equation of motion of kapital (k_dot)
        """
        s = self.params['s']
        n = self.params['n']
        g = self.params['g']
        delta = self.params['delta']

        k_dot = s * self.cobb_douglas_output(k) - (n + g + delta) * k
        return k_dot

    def growth_rate_of_k(self, k):
        """
        Growth rate of k (derivative of k_dot with respect to k)
        """
        s = self.params['s']
        n = self.params['n']
        g = self.params['g']
        delta = self.params['delta']
        k_dot_d = s * self.marginal_prod_capital(k) - (n + g + delta)
        return k_dot_d








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