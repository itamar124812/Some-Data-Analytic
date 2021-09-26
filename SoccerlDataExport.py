import csv
import os
import re
import random
import matplotlib.pyplot as plt
import pandas as pd
def WrithListToCsvFile(linkedList,filename="new_csv_file",Season=""):
    newpath = r'C:\Users\USER\NewDoc' 
    if(re.match(r"\d{4,4}_\d{4,4}",Season)):
         newpath+=str.format(r'\{}',Season)    
    if not os.path.exists(newpath):
     os.makedirs(newpath)
    f=open(newpath+ str.format(r'\{}',filename) +".csv",'w') 
    # using csv.writer method from CSV package
    write = csv.writer(f)
      
    write.writerow(linkedList[0])
    write.writerows(linkedList[1:])
def exportTeamsLeague(path):
    with open(path,'r') as file:  
     reader=csv.reader(file)
     BondesligaTeams18_19=[]  
     for line in reader:
      if(line[2] not in BondesligaTeams18_19):
        BondesligaTeams18_19.append(line[2])
     BondesligaTeams18_19.remove('HomeTeam')
     BondesligaTeams18_19.sort()
     return BondesligaTeams18_19
def VictoryParcent(path):
 with open(path,'r') as file:  
    reader=csv.reader(file)
    HowWines=[]
    for line in reader:
       HowWines.append(line[6])
    HowWines.remove('FTR')
    sumHomeWins=0
    sumAwayWins=0
    sumDrew=0
    for a in HowWines:
        if(a=='H'):sumHomeWins+=1
        elif(a=='A'):sumAwayWins+=1
        else:sumDrew+=1
    return [sumHomeWins/len(HowWines),sumAwayWins/len(HowWines),sumDrew/len(HowWines)]
def HomeAwayDataExport(path):
 with open(path,'r') as file:
    BondesligaTeams18_19=exportTeamsLeague(path)
    reader=csv.reader(file)   
    file.seek(0)
    analyze=[]
    analyze.append(["Team","Home Wins","Away Wins","Drew","Home Losses","Away Losess","Home Goals","Away Goals","goals against H","goals against A"])
    for team in BondesligaTeams18_19:
        analyze.append([team,0,0,0,0,0,0,0,0,0])
    for line in reader:
        for lis in analyze:
            if(line[2]==lis[0]):
                if(line[6]=='H'):
                    lis[1]+=1
                elif(line[6]=='D'):lis[3]+=1
                elif(line[6]=='A'):lis[4]+=1
                lis[6]+=int(line[4])
                lis[8]+=int(line[5])
            elif(line[3]==lis[0]):
              if(line[6]=='H'):lis[5]+=1
              elif(line[6]=='D'):lis[3]+=1
              elif(line[6]=='A'):lis[2]+=1
              lis[7]+=int(line[5])
              lis[9]+=int(line[4])   
    return analyze
def takeSecond(elem):
    return elem[1]
def buildTableFromCsv(path,gamesNumber=38):
   with open(path,'r') as file:  
    reader=csv.reader(file)
    BondesligaTeams18_19=exportTeamsLeague(path) 
    table=[]    
    for team in BondesligaTeams18_19:
       table.append([team,0,0,0,0,0,0,0,0,0,0])
    for line in reader:
        for lis in table:
            if(line[2]==lis[0]):
                if(line[6]=='H'):
                    lis[1]+=3
                    lis[2]+=1
                elif(line[6]=='D'):
                    lis[1]+=1
                    lis[4]+=1
                else:
                    lis[3]+=1
                lis[5]+=int(line[4])
                lis[6]+=int(line[5])
            elif(line[3]==lis[0]):
                if(line[6]=='A'):
                    lis[1]+=3
                    lis[2]+=1
                elif(line[6]=='D'):
                    lis[1]+=1
                    lis[4]+=1
                else:
                    lis[3]+=1
                lis[5]+=int(line[5])
                lis[6]+=int(line[4])
    for lis in table:
        lis[7]=lis[5]-lis[6]
        lis[8]=lis[5]/gamesNumber
        lis[9]=lis[6]/gamesNumber
        lis[10]=lis[5]/lis[1]
    table.sort(key=takeSecond,reverse=True)
    table.insert(0,["Team","Points","wins","Losess","Drew","Goals Scored","Goals Against","Goal Difference","Goals per game","Goals Against per game","Goals per point"])
    return table
def WriteAllSeason():
  a_directory = r"C:\Users\USER\data\data"
  a=2009
  for filename in os.listdir(a_directory):
    filepath = os.path.join(a_directory, filename)
    WrithListToCsvFile(buildTableFromCsv(filepath,34),str.format("GermanLeageTable-{}_{}",a%100,(a+1)%100),str.format("{}_{}",a,a+1))
    a+=1
#WrithListToCsvFile(HomeAwayDataExport(r"C:\Users\USER\Downloads\D1 (1).csv"),str.format("GermanLeageHomeAwayStats-{}_{}",20,21),str.format("{}_{}",2020,2021))
def buildNeuralNetwork(exeptedOutput,**inputs):
    weights=[]
    for i in range(0,len(input)):
      weights.append(random.random())
    
def R(X,Y):
  aveX=sum(X)/len(X) 
  aveY=sum(Y)/len(Y) 
  A=0
  B=sum(map(lambda x:(x-aveX)**2,X))
  C=sum(map(lambda y:(y-aveY)**2,Y))
  for i in range(len(Y)):
   A+=(X[i]-aveX)*(Y[i]-aveY)
  return A/((B*C)**(1/2))
def ALinearRegression(X,Y):
  aveX=sum(X)/len(X) 
  aveY=sum(Y)/len(Y) 
  A=0
  B=0
  for i in range(len(Y)):
   A+=X[i]*(Y[i]-aveY)
   B+=X[i]*(X[i]-aveX)
  return [float(A)/B,aveY-aveX*float(A)/B]
with open(r"C:\Users\USER\Downloads\D1 (2).csv","r")  as f:
    R_HomeFauls_HomeBet=-0.045477074114620236
    reader=csv.reader(f)
    L=[]
    P=[]
    i=0
    for line in reader:
          if(i!=0):
           L.append(float(line[5]))
           P.append(float(line[23]))
          i+=1
   # L.remove("HF")
    #P.remove("B365H")
    print(ALinearRegression(L,P))
    plt.plot(P, L, color = 'g', linestyle = 'dashed',
         marker = 'o',label = "BetRelationGoals")
    u=0
    for x in range(0,len(L)-1):
     u+=P[x]
    print(u/len(P))
plt.xticks(rotation = 25)
plt.xlabel('Bet')
plt.ylabel('Goals')
plt.title('BetRelationGoals', fontsize = 20)
plt.grid()
plt.legend()
plt.show()




            
    
    
      

            

                
    

   
    


    


    
