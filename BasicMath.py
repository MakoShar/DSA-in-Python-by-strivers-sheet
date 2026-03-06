class solution:
    def DigitsInNumber(self,N)-> int:
        count = 0
        while N>0:
            N=N//10
            count +=1
        return count
    def ReverseDigits(self,N)-> int:
        rev =0
        if N>0: 
            sign = 1
        else:
            sign = -1
        N=abs(N)
        while N>0:
            ld = N%10
            N=N//10
            rev = (rev*10) + ld
        return sign*rev
    def Palindrome(self,N)->bool:
        rev = 0
        if N<0:
            return False
        else:
            x=N
            while N>0:
                ld = N%10
                N=N//10
                rev = rev*10 + ld
            if rev == x:
                return True
            else:
                return False
    def ArmstrongNumber(self,x: int)->bool:
        y = len(str(x))
        arm = 0
        N = x
        while x > 0:
            arm += (x % 10) ** y
            x //= 10
        return N == arm
    def Divisor(self,N):
        for i in range (1,N+1):
            if N % i == 0:
                print(i," ",end='')
    def GCD(self,N1,N2):
        if N1>N2:
            y = N1
        else:
            y = N2
        for i in range(1,y+1):
            if N1 % i == 0 and N2 % i == 0:
                print(i," ",end='')
    def PrimeNum(self,N)-> bool:
        c = 0
        for i in range(1,N+1):
            if N % i == 0:
                c += 1
        if c != 2:
            return False
        else:
            return True

if __name__ == '__main__':
    obj = solution()
    print(obj.PrimeNum(5))