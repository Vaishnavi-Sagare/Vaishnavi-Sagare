class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1,n2=0,0
        for i in num1:
            digit=ord(i)-48
            n1=(n1*10)+digit
        for i in num2:
            digit=ord(i)-48
            n2=(n2*10)+digit
        res=n1*n2
        if n1==0 or n2==0:
            return "0"
        FinalResult=[]
        while res>0:
            rem= res%10
            n=chr(48+rem)
            FinalResult.append(n)
            res = res//10
        FinalResult=FinalResult[::-1]
        return "".join(FinalResult)
