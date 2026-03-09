class rec:
    def nTimes(self,N: int, S):
        if N == 0:
            return
        self.nTimes(N-1,S)
        print(S,' ',end='')
    def numberPrinting(self,N):
        if N == 0:
            return
        self.numberPrinting(N-1)
        print(N)
    def RevNumPrint(self,N):
        if N==0:
            return
        print(N)
        self.RevNumPrint(N-1)
    def SumNum(self,N,sum=0):
        if N != 0:
            sum += N
            self.SumNum(N-1,sum)
        else:
            print('sum =',sum)
            return
    def Fact(self,N,sum = 1):
        if N == 1:
            print('Factorial =',sum)  
            return      
        sum *= N
        self.Fact(N-1,sum)
    def RevArr(self,arr):
        arr[:] = arr[::-1]
        return arr
    def Palindrom(self,s)->bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
    def Palindrom(self,s)->bool:
        rev=""
        for i in range(len(s),0,-1):
            rev += s[i-1]
        print(rev)
        if s == rev:
            return True
        else:
            return False
    def Fibonacci(self,n,sum=0,prev=0,next1=1,N=0):
        if N == n:
            return
        print(sum) 
        sum = prev + next1 
        prev = next1 
        next1 = sum 
        self.Fibonacci(n,sum,prev,next1,N+1)    
    def FibonacciTerm(self,n):
        if n <= 1:
            return n
        return self.FibonacciTerm(n-1) + self.FibonacciTerm(n-2)

if __name__ == '__main__':
    obj = rec()
    print(obj.FibonacciTerm(4))
