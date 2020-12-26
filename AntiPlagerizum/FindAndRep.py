import random
class FindAndRep:
    def __init__(self,fileIn,fileOut):
        self.nameR = fileIn
        self.nameW = fileOut
    def createList(self,strog):
        st = strog
        wordList =[]
        while(st.find(',')!=-1):
            tempSt=st[:st.find(',')]
            st= st[st.find(',')+1:len(st)]
            wordList.append(tempSt)
        wordList.append(st)
        return wordList
    
    def findWork(self):
        with open(self.nameR, 'r') as FI:
            filedata = FI.read()
        FD = open("dic.txt","r")
        dicData = FD.read()
        FD.close()
        FD = open('dic.txt')
        #how to check for upper case and correct respectively
        for line in FD:
            spaceNum = line.find(';')
            s1 = line[:spaceNum].lower()
            s2 = line[(spaceNum + 1):(len(line)-1)].lower()
            wL1 = self.createList(s2)
            s3 = wL1[random.randint(0,(len(wL1)-1))]
            filedata = filedata.replace(s1,s3)
            
        with open(self.nameW, 'w') as FO:
            FO.write(filedata)
        FD.close()
            
run = FindAndRep("InFile.txt","OutFile.txt")
run.findWork()
        
