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
    def is_duck(self,n):
        self.n = n
        l = self.integer_to_list(self.n)
        if 0 in l:
            if l[(l.index(0)-1)] != 0:
                return True
        return False

math_obj = math_fucntions()
print(math_obj.is_duck(int(input("X:"))))