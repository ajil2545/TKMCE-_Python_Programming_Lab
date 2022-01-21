class Time:
    def __init__(self,hour,minute,second):
        self.__hour=hour
        self.__minute=minute
        self.__second=second
    def __add__(self,obj):
        h=self.__hour+obj.__hour
        m=self.__minute+obj.__minute
        s=self.__second+obj.__second
        if m>=60:
            h+=1
            m-=60
        if s>=60:
            m+=1
            s-=60
        return str(h)+":"+str(m)+":"+str(s)
t1=Time(12,30,10)
t2=Time(10,30,10)
print(t1 + t2)