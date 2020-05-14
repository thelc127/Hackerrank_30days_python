# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())

for j in range(0,T):
        s = input()
        a,b = s[::2] , s[1::2]
        print(a,b)
