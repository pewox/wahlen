import pandas as pd
import os
import matplotlib.pyplot as plt

pfad_dat = 'dat/csv/stimmen_laender.csv'
pfad_dem = 'dat/csv/demokrafie.csv'
part = ["AfD", "CDU", "FDP", "SPD", "Linke", "Grüne", "Andere"]
idx = ['sh', 'hh', 'hb', 'mv', 'ni', 'be', 'bb', 'st', 'sn', 'th',
                    'he', 'nw', 'rp', 'sl', 'bw', 'by']
farben = ['#2688d4', '#484a4a', '#f2ef1b', '#f21b8a', '#f21b34', '#1dad33', '#1dada9']

def bund():
    
    if os.path.exists(pfad_dat):
        dat = pd.read_csv(pfad_dat, index_col=[0])
    else: print(f'Datei {pfad_dat} nicht vorhanden.')    

    if os.path.exists(pfad_dem):
        dem = pd.read_csv(pfad_dem, index_col=[0])
    else: print(f'Datei {pfad_dem} nicht vorhanden.')

    try:   
        wahlbet_bund = 100 * dat.sum().sum() / dem.wahlberechtigt.sum()
        
        
        df = pd.read_csv(pfad_dat, index_col=[0])
        arr = df.sum().to_numpy()
        
        fig, achse = plt.subplots(figsize=(8, 8))

        achse.pie(arr, labels=part, autopct="%.1f%%", colors=farben)
        fig.suptitle('Zwischenergebnisse Bundestagswahlen')
        achse.set_title(f"Wahlbeteiligung {wahlbet_bund:.1f} %")
        plt.show()
    except Exception as e:
        print('Fehler:', e)

def land():
    if os.path.exists(pfad_dat):
        dat = pd.read_csv(pfad_dat, index_col=[0])
    else: print(f'Datei {pfad_dat} nicht vorhanden.')    

    if os.path.exists(pfad_dem):
        dem = pd.read_csv(pfad_dem, index_col=[0])
    else: print(f'Datei {pfad_dem} nicht vorhanden.')
    
    try:
        inp = input('\nLand: ')

        if inp.lower() in dem.laender_id.values:
            suche = dem.index[dem.laender_id == inp.lower()]
            bland = dem.at[suche[0], 'bundesland']
            wahlber_land = dem.at[suche[0], 'wahlberechtigt']
            wahlbet_land = dat.iloc[suche[0]].sum() / wahlber_land

        df = pd.read_csv(pfad_dat, index_col=[0])
        arr = df.loc[inp].to_numpy()
        fig, achse = plt.subplots(figsize=(8, 8))

        achse.pie(arr, labels=part, autopct="%.1f%%", colors=farben)
        fig.suptitle(f'Zwischenergebnisse Bundestagswahlen\nLand {bland}')
        achse.set_title(f"Wahlbeteiligung {wahlbet_land:.1f} %")
        plt.show()
    except Exception as e:
        print('Fehler:', e)





