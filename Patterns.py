
class sol:

    def patt1(self,N):
        for i in range(N):
            print('*'*N,end='\n')
    def patt2(self,N):
        for i in range(N):
            for j in range(i+1):
                print('*',end='')
            print()
    def patt3(self,N):
        for i in range(N):
            for j in range(i+1):
                print(j+1,end='')
            print()
    def patt4(self,N):
        for i in range(N):
            for j in range(i+1):
                print(i+1,end='')
            print()
    def patt5(self,N):
        for i in range(N):
            for j in range(N-i):
                print('*',end='')
            print()
    def patt6(self,N):
        for i in range(N):
            for j in range(N-i):
                print(j+1,end='')
            print()
    def patt7(self,N):
        for i in range(N):
            for j in range(N-i-1):
                print(' ',end='')
            for j in range(2*i+1):
                print('*',end='')
            for j in range(N-i-1):
                print(' ',end='')
            print()
    def patt8(self,N):
        for i in range(N):
            for j in range(i):
                print(' ',end='')
            for j in range(2*(N-i)-1):
                print('*',end='')
            for j in range(i):
                print(' ',end='')
            print()
    def patt9(self,N):
        for i in range(N):
            for j in range(N-i-1):
                print(' ',end='')
            for j in range(2*i+1):
                print('*',end='')
            for j in range(N-i-1):
                print(' ',end='')
            print()
        for i in range(N):
            for j in range(i):
                print(' ',end='')
            for j in range(2*(N-i)-1):
                print('*',end='')
            for j in range(i):
                print(' ',end='')
            print()
    def patt10(self,N):
        for i in range(N):
            for j in range(i+1):
                print('*',end='')
            print()
        for i in range(N-1):
            for j in range(N-1-i):
                print('*',end='')
            print()
    def patt11(self,N):
        for i in range(N):
            for j in range(i+1):
                if((i+j) % 2 == 0):
                    print('1',end='')
                elif((i+j) % 2 == 1):
                    print('0',end='')
            print()
    def patt12(self,N):
        for i in range(N):
            for j in range(i+1):
                print(j+1,end='')
            for j in range(2*(N-i-1)):
                print(' ',end='')
            for j in range(i+1):
                print(i-j+1,end='')
            print()
    def patt13(self,N):
        x=1
        for i in range(N):
            for j in range(i+1):
                print(x,' ',end='')
                x += 1
            print()
    def patt14(self,N):
        for i in range(N):
            x=65
            for j in range(i+1):
                print(chr(x),end='')
                x+=1
            print()
    def patt15(self,N):
        for i in range(N):
            x=65
            for j in range(N-i):
                print(chr(x),end='')
                x+=1
            print()
    def patt16(self,N):
        x=65
        for i in range(N):
            for j in range(i+1):
                print(chr(x),end='')
            x+=1
            print()
    def patt17(self,N):
        for i in range(N):
            x=65
            for j in range(N-i-1):
                print(' ',end='')
            for j in range(i+1):
                print(chr(x),end='')
                x+=1
            x-=1
            for j in range(i):
                x-=1
                print(chr(x),end='')
            print()
    def patt18(self,N):
        for i in range(N):
            x = 64+N
            for j in range(i+1):
                print(chr(x-i),end='')
                x+=1
            print()
    def patt19(self,N):
        for i in range(N):
            for j in range(N-i):
                print('*',end='')
            for j in range(2*i):
                print(' ',end='')
            for j in range(N-i):
                print('*',end='')
            print()  
        for i in range(N):
            for j in range(i+1):
                print('*',end='')  
            for j in range(2*(N-i-1)):
                print(' ',end='')
            for j in range(i+1):
                print('*',end='') 
            print()  
    def patt20(self,N):
        for i in range(N-1):
            for j in range(i+1):
                print('*',end='')
            for j in range(2*(N-i-2)+1):
                print(' ',end='')
            for j in range(i+1):
                print('*',end='')
            print()
        print('*'*(2*N-1))
        for i in range(N-1):
            for j in range(N-i-1):
                print('*',end='')
            for j in range(2*i+1):
                print(' ',end='')
            for j in range(N-i-1):
                print('*',end='')
            print()
    def patt21(self,N):
        print('*'*N)
        for i in range(N-2):
            for j in range(1):
                print('*',end='')
            for j in range(N-2):
                print(' ',end='')
            for j in range(1):
                print('*',end='')
            print()
        print('*'*N)
    def patt22(self,N):

        for i in range(N):
            for j in range(i):
                print(N-j,end='')
            for j in range(2*(N-i)-1):
                print(N-i,end='')
            for j in range(i):
                print(N-i+j+1,end='')
            print()
        for i in range(2,N+1):
            for j in range(N-i):
                print(N-j,end='')
            for j in range(2*i-1):
                print(i,end='')
            for j in range(N-i):
                print(i+j+1,end='')
            print()


if __name__ == "__main__":
    obj = sol()
    obj.patt22(5)