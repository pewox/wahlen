from dat import plotbwahl
import pandas as pd

class Statistik:
    
    def menue(self):
        self.__str__("""\nBundestagswahlen
                     \nStatistik:    (1)-Stimmenverteilung Bund  (2)-Stimmenverteilung Länder
              (3)-Abbruch  """)
        self.inp = input('Auswahl: ')
        
        if self.inp == "1":
            plotbwahl.bund()
        elif self.inp == "2":
            self.__str__('\n---Länderauswahl---\n (Kurzbezeichnung eingeben)\n')
            try:
                self.liste = pd.read_csv('dat/csv/demokrafie.csv', index_col=[0])
                [print(i, sep='\n') for i in self.liste.loc[:, "bundesland"]]
                plotbwahl.land()
            except Exception as e:
                print('Fehler:', e)
    
    def __str__(self, x):
        print(x)
    
new = Statistik()
new.menue()