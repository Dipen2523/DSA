class math_fucntions:
    def length_of_int(self,n):
        self.n = n
        i = int(0)
        if self.n == 0:
            return 1
        if self.n < 0:
            self.n *= -1
        while self.n:
            self.n //= 10
            i += 1
        return i
    def integer_to_list(self,n):
        self.n = n
        len_ = self.length_of_int(n)
        l = [0] * len_
        for j in range(0,self.length_of_int(n)):
            l[len_ - j - 1] = n % 10
            n //= 10
        return l
    def factors(self,n):
        l = [1,]
        for j in range(2,int((n/2)+1)):
            if n % j == 0:
                l.append(j)
        return l
    def is_friendly(self, n,m):
        self.n = n
        self.m = m
        ln = self.factors(n)
        lm = self.factors(m)
        sum_nf = 0
        sum_mf = 0
        for i in ln:
            sum_nf = sum_nf + i
        for i in lm:
            sum_mf = sum_mf + i
        return sum_nf/n == sum_mf/m
        
math_object = math_fucntions()
print(math_object.is_friendly(int(input("N:")),int(input("M:")))),