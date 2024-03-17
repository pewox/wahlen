import pandas as pd
import numpy as np
import os

idx = ['sh', 'hh', 'hb', 'mv', 'ni', 'be', 'bb', 'st', 'sn', 'th',
                    'he', 'nw', 'rp', 'sl', 'bw', 'by'] 
cols = ["afd", "cdu", "fdp", "spd", "linke", "grüne", "andere"] 
pfad = 'dat/csv/stimmen_laender.csv'

class Daten():
    def __init__(self):
        self.idx = idx
        self.cols = cols
        self.pfad = pfad

    def lesen(self, pfad):
        if os.path.exists(self.pfad):
            # index_col=[0] setzen, um erste Spalte als Index zu setzen
            # (Heft PTH08 S. 61)
            self.stimmen_l = pd.read_csv(self.pfad, index_col=[0])
            return self.stimmen_l
        else:
            self.arr = np.ones(len(self.idx) * len(self.cols)).reshape(len(self.idx), len(self.cols))
            self.stimmen_l = pd.DataFrame(self.arr, columns=self.cols, index=self.idx, dtype=int)
            return self.stimmen_l

    def __str__(self, obj):
        print(obj)

    def schreiben(self, la, pa, st):
        try:
            self.stimmen_l = self.lesen(self.pfad)
            self.stimmen_l.loc[la, pa] += st
            self.stimmen_l.to_csv(self.pfad)
        except Exception as e:
            return self.__str__('Fehler: {e}')

    def eingeben(self):
        self.__str__('\n---Länderauswahl---\n (Kurzbezeichnung eingeben)\n')
        try:
            self.liste = pd.read_csv('dat/csv/demokrafie.csv', index_col=[0])
            [print(i, sep='\n') for i in self.liste.loc[:, "bundesland"]]
            self.la = input('\nBundesland: ')
            self.pa = input('Partei: ')
            if self.la.lower() not in self.idx or self.pa.lower() not in self.cols:
                self.__str__('Bundesland oder Partei nicht vorhanden.')
                menue.menue_eingabe()
            self.st = int(input('Stimmen: '))
            self.schreiben(self.la.lower(), self.pa.lower(), self.st)
        except Exception as e:
            return self.__str__(f'Fehler Stimmeneingabe: {e}')
        
class Menue():
    def hauptmenue(self):
        print("""\nHauptmenü:    (1)-Stimmeneingabe 
              (2)-Abbruch""")
        self.inp = input('\nAuswahl: ')
        while self.inp != '2':
            if self.inp == '1':
                self.menue_eingabe()
            else: self.hauptmenue()

    def menue_eingabe(self):
        # mit Instanz von Daten Funktion eingeben() aus Klasse Daten aufrufen
        daten.eingeben()
        self.inp = input('\nweiter ? ([j]/n): ')
        if self.inp.lower() == 'j' or self.inp == '':
            self.menue_eingabe()
        else: self.hauptmenue()

daten = Daten()       
menue = Menue()
menue.hauptmenue()
