import csv
import os
import re
def WrithListToCsvFile(linkedList,filename="new_csv_file"):
    newpath = r'C:\Users\USER\NewDoc' 
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
    table.insert(0,["Team","Points","wins","Losess","Drew","Goals Scored","Goals Against","Goal Difference","Goals per game","Goals Against per game","Goals Against points"])
    return table

  
    
                



            
    
    
      

            

                
    

   
    


    


    
