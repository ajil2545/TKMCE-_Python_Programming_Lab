read=open('Testing/text.txt','r+')
test=True
while test:
    list=read.readline()
    firstletter=list.split(" ")
    if(len(firstletter)>5):
        word=firstletter[0]
        if(word[0].isupper()):
            print(list)
    if not list:
        test=False