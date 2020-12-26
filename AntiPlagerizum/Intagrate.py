class Intigrate:
    def __init__(self,fileToBe):
        self.str1 = fileToBe
        self.str2 = "dic.txt"
    def form (self,sepChar):
        FD = open(self.str1)
        FI = open("tempout.txt",'w')
        fileData = ""
        for line in FD:
            sft = line.lower()
            sft = sft.replace(" ","")
            sft = sft.replace(sepChar,";")
            sft = sft[:(len(line)-1)]
            fileData = fileData + sft
        FI.write(fileData)
        FI.close()
        FD.close()
    def alph (self,inputTxt):
        FI = open(inputTxt)
        listy = []
        for line in FI:
            listy.append(line)
        gList = sorted(listy)
        FI.close()
        FI = open(inputTxt,'w')
        for x in gList:
            FI.write(x)
        FI.close()
        
run = Intigrate("toBeIntD.txt")
run.alph("dic.txt")
