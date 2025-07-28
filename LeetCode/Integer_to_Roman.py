class Solution(object):
    def intToRoman(self, num):
        l=[[1,'I'],[4,'IV'],[5,'V'],[9,'IX'],[10,'X'],[40,'XL'],[50,'L'],[90,'XC'],[100,'C'],[400,'CD'],[500,'D'],[900,'CM'],[1000,'M']]
        s=''
        for i in range(len(l)-1,-1,-1):
            if num/l[i][0]:
                cnt=num/l[i][0]
                s=s+cnt*l[i][1]
                num=num%l[i][0]
        return s
