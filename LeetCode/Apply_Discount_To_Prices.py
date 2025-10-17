class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        l= sentence.split(" ")
        discount= round(discount/100,2)
        l1={"$"}
        for char in range(0,len(l)):
            if l[char][0]=="$":
                s=l[char][1:]
                if s.isdigit():
                    res=format(int(s)-(int(s)*discount),".2f")
                    l[char]= "$"+str(res)
        return " ".join(l)
