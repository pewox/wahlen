import numpy as np
import pandas as pd

#print("\nDemokrafie BRD: Einwohnerzahl Bundeslaender\n")
class Wahlen():
    
    def __init__(self):
        self.struktur = np.dtype([("bundesland", str, 24),
                             ("laender_id", str, 5),
                             ("einwohner", np.int32),
                             ("wahlberechtigt", np.int32)
                             ])

        self.population_l = np.array([("Schleswig-Holstein(SH)", 'sh', 2810000, 2200000),
                                 ("Hamburg(HH)", 'hh', 1750000, 1300000),
                                 ("Bremen(HB)", 'hb', 650000, 500000),
                                 ("Mecklenb.-Vorpommern(MV)", 'mv', 1590000, 1300000),
                                 ("Niedersachsen(NI)", 'ni', 7790000, 6000000),
                                 ("Berlin(BE)", 'be', 3520000, 2400000),
                                 ("Brandenburg(BB)", 'bb', 2440000, 2000000),
                                 ("Sachsen-Anhalt(ST)", 'st', 2240000, 1800000),
                                 ("Sachsen(SN)", 'sn', 4040000, 3200000),
                                 ("Thüringen(TH)", 'th', 2160000, 1700000),
                                 ("Hessen(HE)", 'he',6040000, 4300000),
                                 ("Nordrhein-Westfalen(NW)", 'nw', 17570000, 12800000),
                                 ("Rheinland-Pfalz(RP)", 'rp', 3990000, 3000000),
                                 ("Saarland(SL)", 'sl',  990000, 700000),
                                 ("Baden-Württemberg(BW)", 'bw', 10630000, 7700000),
                                 ("Bayern(BY)", 'by', 12560000, 9400000)], self.struktur)
        
        self.pfad = 'dat/csv/demokrafie.csv'
        self.pop = np.sum(self.population_l["einwohner"])
        self.wahlber = np.sum(self.population_l["wahlberechtigt"])
        self.df = pd.DataFrame(self.population_l)
        self.df.columns = ["bundesland", "laender_id", "einwohner", "wahlberechtigt"]
        self.df.to_csv(self.pfad)
        
    def __str__(self):
        return (f"{self.pop * 1e-6:.2f} Mio. Einwohner bundesweit\n" +
              f"{self.wahlber * 1e-6:.2f} Mio. Wahlberechtigte bundesweit")

x, y, z = "--Bundesland--", "--Einwohnerzahl(Mio.)--", "--Wahlberechtigte(Mio.)--"

new = Wahlen()
print(new)
print()
pfad = 'dat/csv/demokrafie.csv'
demokrafie = pd.read_csv(pfad, index_col=[0])
print(demokrafie)


