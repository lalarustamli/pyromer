class Solow:
    def __str__(self):
        return str(self.params)
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
        k_dot = [0]
        k_growth = [0]
        for t in range(1,t):
            k.append((self.params['s']*(k[t-1]**self.params['alpha'])+(1-self.params['d'])*k[t-1])/(1+self.params['n']))
            k_dot.append(k[t]-k[t-1])
            k_growth.append(k_dot[t]/k[t])
        return k_dot

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
        For small k, sk^alpha > (n+g+delta)k and k_dot > 0
        For large k, k_dot < 0
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

    def calculate_convergence(self):
        n = self.params['n']
        g = self.params['g']
        delta = self.params['d']
        alpha = self.params['alpha']
        convergence = (1-alpha)*(n+g+delta)
        return convergence


    def update_model(self, p):
        old_k_star = self.calc_k_star()
        old_y_star = self.calc_y_star()
        old_c_star = self.calc_c_star()
        self.params = p
        new_k_star = self.calc_k_star()
        new_y_star = self.calc_y_star()
        new_c_star = self.calc_c_star()

        new_vals = {
            "old k star": old_k_star,
            "old y star": old_y_star,
            "old c star": old_c_star,
            "new k star" : new_k_star,
            "new y star" : new_y_star,
            "new c star" : new_c_star,
            "change in k star %": (new_k_star-old_k_star)/old_k_star,
            "change in k star": new_k_star/ old_k_star,
            "change in y star": new_y_star / old_y_star,
            "change in c star": new_c_star / old_c_star,

        }
        return new_vals

a = []
params = {
    'n': 0.01,
    's': 0.24,
    'g': 0.01,
    'alpha': 1/3,
    'd':0.04
}
model = Solow(params)
print(model.calc_k_star())
# print(model.predict_k(init_k=6))
print(model.calc_y_star())
print(model.calc_c_star())
print(model)
a = model.predict_k(init_k=4,t =10)
print(a)
params2 = {
    'n': 0.01,
    's': 0.33,
    'g': 0.01,
    'alpha': 1/3,
    'd': 0.04
}
print(model.update_model(params2))
print(model)
print(model.predict_k(init_k=4,t =10))
print(model.calculate_convergence())