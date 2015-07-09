
import random
A,B=(0,0)
Answer=[0,0,0,0] 
AttemptTimes=0 

def BuildAnswer():  
    global Answer    
    random.seed() 
    while 1: 
        digit = random.randint(0, 9999) 
        Answer[0]=digit/1000 #取千位数字
        Answer[1]=digit%1000/100 #取白位数字
        Answer[2]=digit%100/10 #取十位数字
        Answer[3]=digit%10 #取个位数字
        if Answer[0]!=Answer[1] and Answer[0]!=Answer[2] and Answer[0]!=Answer[3] and Answer[1]!=Answer[2] and Answer[1]!=Answer[3] and Answer[2]!=Answer[3]: 
            Answer=[1,2,3,4]
            return 
        
def IsTryStringOK(TryString): 
    if TryString.isdigit() and len(TryString)==4: 
        if TryString[0]!=TryString[1] and TryString[0]!=TryString[2] and TryString[0]!=TryString[3] and TryString[1]!=TryString[2] and TryString[1]!=TryString[3] and TryString[2]!=TryString[3]: 
            return 1 
    return 0   
def Judge(TryString): 
    global A, B,Answer
    for i in range(4): 
        if(TryString[i]==str(Answer[i])): 
            A=A+1 
        else: 
            for j in range(4): 
                if(TryString[i]==str(Answer[j])): 
                    B=B+1 
    ReturnStr = "%dA%dB"%(A,B) 
    A=0 
    B=0 
    return ReturnStr 	
def Play(): 
    global  AttemptTimes  
    while AttemptTimes: 
        TryString = input("%d:    "%AttemptTimes)  
        if IsTryStringOK(TryString):                          
            TryResult=Judge(TryString) 
            if TryResult=="4A0B": 
                print ("You are winer!" )
                break 
            else: 
                print (TryResult )
                AttemptTimes=AttemptTimes-1 
        else: 
            print ("Input error! Type again,",)
            continue 
   
    print ("Attempt times is Eight./nThe finily answer is: %s/nGame Over!"%Answer )				
if __name__=="__main__":       
    Try=1 
    global A, B,Answer
    while Try: 
        A,B=(0,0)   #Match falg 
        AttemptTimes=8  #Geuss times 
        Answer=[0,0,0,0]   #The Answer 
    
        BuildAnswer() 
        print ("I've ready,please guess me.")
        Play()   

        Data=input( "Do you want to try again? /nType [0] for 'No' and others for [Yes]/n") 
        if Data.isdigit(): 
            Try=int(Data) 
        else: 
            Try=1  
    else: 
        print ("Game exited!")