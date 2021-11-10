import csv
<<<<<<< HEAD
from numpy import nan
=======
>>>>>>> 0f28a2f (null)
import requests
import os
import re
import random
import matplotlib.pyplot as plt
import pandas as pd

def WrithListToCsvFile(linkedList,filename="new_csv_file",Season=""):
    newpath = r'C:\Users\USER\NewDoc\La_Liga' 
    if(re.match(r"\d{4,4}_\d{4,4}",Season)):
         newpath+=str.format(r'\{}',Season)    
    if not os.path.exists(newpath):
     os.makedirs(newpath)
    f=open(newpath+ str.format(r'\{}',filename) +".csv",'w') 
    # using csv.writer method from CSV package
    write = csv.writer(f)
      
    write.writerow(linkedList[0])
    write.writerows(linkedList[1:])
def openCsvFile(path):
     with open(path,'r') as file: 
      file.seek(0) 
      reader=csv.reader(file)
<<<<<<< HEAD
      return list(reader)
=======
      return reader
>>>>>>> 0f28a2f (null)

def exportTeamsLeague(reader):      
     LeugeTeams=[]  
     i=0
     for line in reader:
<<<<<<< HEAD
      if(line[2] not in LeugeTeams):           
          if(i==0):
              i=1               
              continue
          else:
               LeugeTeams.append(line[2])
    
     for x in LeugeTeams:
         if(type(x) != str):
            LeugeTeams.remove(x)
=======
      if(line[2] not in LeugeTeams):
          if(i==0):
               i=1
               continue
          else:
               LeugeTeams.append(line[2])
>>>>>>> 0f28a2f (null)
     LeugeTeams.sort()
     return LeugeTeams
def VictoryParcent(reader):
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
def HomeAwayDataExport(reader):
    BondesligaTeams18_19=exportTeamsLeague(reader)  
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
def buildTableFromCsv(reader,gamesNumber=38):
<<<<<<< HEAD
    leagueTeams=exportTeamsLeague(reader) 
=======
    BondesligaTeams18_19=exportTeamsLeague(reader) 
>>>>>>> 0f28a2f (null)
    table=[]    
    for team in leagueTeams:
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
<<<<<<< HEAD
def WriteAllBundesligaSeason(): 
  a=22
  for filename in range(15):
    b=a-1
    url=str.format("https://www.football-data.co.uk/mmz4281/{}{}/D1.csv",b,a)
    data = pd.read_csv(url)
    if(data.columns[2]=="Time"):
            data.pop('Time')
    Data=list(data.values)
    WrithListToCsvFile(buildTableFromCsv(Data,gamesNumber=34),str.format("GermanLeageTable-{}_{}",a,b),str.format("20{}_20{}",a,str(b).zfill(2)))
    WrithListToCsvFile(HomeAwayDataExport(Data),str.format("GermanHomeAwayStats-{}_{}",a,b),str.format("20{}_20{}",a,str(b).zfill(2)))
    a-=1
def WriteAllLa_LigaSeason():
    a=22
    for i in range(15):
     b=a-1
     url=str.format("https://www.football-data.co.uk/mmz4281/{}{}/SP1.csv",str(b).zfill(2),str(a).zfill(2))
     data = pd.read_csv(url)
     if(data.columns[2]=="Time"):
            data.pop('Time')
     Data=list(data.values)
     WrithListToCsvFile(buildTableFromCsv(Data),str.format("SpainLeageTable-{}_{}",a,b),str.format("20{}_20{}",str(a).zfill(2),str(b).zfill(2)))
     WrithListToCsvFile(HomeAwayDataExport(Data),str.format("SpainHomeAwayStats-{}_{}",a,b),str.format("20{}_20{}",str(a).zfill(2),str(b).zfill(2)))
     a-=1

#WrithListToCsvFile(HomeAwayDataExport(r"C:\Users\USER\Downloads\D1 (1).csv"),str.format("GermanLeageHomeAwayStats-{}_{}",20,21),str.format("{}_{}",2020,2021))
def write_All_primerLegaueData():   
    url = 'https://www.football-data.co.uk/mmz4281/1011/E0.csv'
    a=11
    b=12
    for x in range(10):
         data = pd.read_csv(url)
         if(data.columns[2]=="Time"):
            data.pop('Time')
         Data=list(data.values)
         WrithListToCsvFile(HomeAwayDataExport(Data),str.format("EngelandLeageHomeAwayData-20{}_20{}",a,b),str.format("{}_{}",a,b))      
         WrithListToCsvFile(buildTableFromCsv(Data,gamesNumber=38),str.format("EngelandLeageTable-20{}_20{}",a,b),str.format("{}_{}",a,b))               
         a+=1
         b+=1
         url= str.format('https://www.football-data.co.uk/mmz4281/{}{}/E0.csv',a,b)
=======
def WriteAllSeason():
  a_directory = r"C:\Users\USER\data\data"
  a=2009
  for filename in os.listdir(a_directory):
    filepath = os.path.join(a_directory, filename)
    WrithListToCsvFile(buildTableFromCsv(openCsvFile(path=filepath),gamesNumber=34),str.format("GermanLeageTable-{}_{}",a%100,(a+1)%100),str.format("{}_{}",a,a+1))
    a+=1
#WrithListToCsvFile(HomeAwayDataExport(r"C:\Users\USER\Downloads\D1 (1).csv"),str.format("GermanLeageHomeAwayStats-{}_{}",20,21),str.format("{}_{}",2020,2021))
def write_All_primerLegaueData():   
    url = 'https://www.football-data.co.uk/mmz4281/1011/E0.csv'
    r = requests.get(url)
    text = r.iter_lines()   
    a=1112
    for x in range(10):
         WrithListToCsvFile(buildTableFromCsv(text,gamesNumber=38),str.format("EngelandLeageTable-{}_{}",a%100,(a+1)),str.format("{}_{}",a,a+1))
         a+=101
         url=str.format('https://www.football-data.co.uk/mmz4281/{}/E0.csv',a)
>>>>>>> 0f28a2f (null)




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
<<<<<<< HEAD
WriteAllLa_LigaSeason()
=======
#write_All_primerLegaueData()
>>>>>>> 0f28a2f (null)




            
    
    
      

            

                
    

   
    


    


    
