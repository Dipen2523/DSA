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
    def is_neonnumber(self,num):
        self.x = num
        y = self.x*self.x
        l = self.integer_to_list(y)
        numsum = 0
        for i in l:
            numsum += i
        return numsum == self.x
    #def is_range_neonnumber(self,a,b):
        #self.a = a
        #self.b = b
        #for i in range(a, b + 1):
            #if(self.is_neonnumber(i)):
                #print(f"{i} is neonnumber number")
    def is_nth_neonnumber(self, n):
        count = 0
        i = 1
        while True:
            if self.is_neonnumber(i):
                count += 1
            if count == n:
                print(f"The {n} position neonnumber number is: {i}")
                break
            i += 1

                

math_object = math_fucntions()
#math_object.is_range_neonnumber(int(input("S:")),int(input("E:")))
math_object.is_nth_neonnumber(int(input("Nth:")))