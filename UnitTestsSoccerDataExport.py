from SoccerlDataExport import exportTeamsLeague, openCsvFile
import unittest
import csv
import requests
class Uint_test(unittest.TestCase):
   def testexportTeamsLeague(self):
    teams=exportTeamsLeague(openCsvFile(r"C:\Users\USER\Downloads\E0.csv"))
    print(teams)
    self.assertListEqual(teams,["Aston Villa","Blackburn","Bolton","Chelsea","Sunderland","Tottenham","Wigan","Wolves","Liverpool","Man United","Arsenal"
,"Birmingham","Everton","Stoke","West Brom","West Ham","Wigan","Fulham","Newcastle","Man City"])
    url = 'https://www.football-data.co.uk/mmz4281/1011/E0.csv'
    r = requests.get(url)
    text = r.iter_lines() 
    reader =csv.reader(text)
    teams=exportTeamsLeague(reader)
    self.assertListEqual(teams,["Aston Villa","Blackburn","Bolton","Chelsea","Sunderland","Tottenham","Wigan","Wolves","Liverpool","Man United","Arsenal"
,"Birmingham","Everton","Stoke","West Brom","West Ham","Wigan","Fulham","Newcastle","Man City"])



#if __name__ == '__main__':
unittest.main()
