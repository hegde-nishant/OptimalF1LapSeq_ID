import fastf1 as ff1
import pandas as pd

ff1.Cache.enable_cache('/path/to/the/cached/file/')

rb_seasons = [2018, 2019, 2021, 2022, 2023] #2020 was COVID Year

numRaces = numRaces = [21, 21, 22, 22, 22]  #Base index considered as 2010 season

rb_drivers = [['RIC', 'VER'], ['VER', 'GAS', 'ALB'], ['VER', 'PER'], ['VER', 'PER'], ['VER', 'PER']]  #Base index consider as 2018 season

for sno, season in enumerate(rb_seasons):
    for i in range(1, numRaces[sno] + 1):  #Get the number of races for that season from the numRaces list
        #Get session and load it
        print("Season {} session {}".format(season, i))
        session = ff1.get_session(season, i, 'R')
        session.load(telemetry=True, laps=True, weather=True, messages = True)
        print(session.total_laps)
        df1 = pd.DataFrame(session.laps.pick_driver("HAM"))
        print(df1.columns)
        print(df1.head())
        print(len(df1['Driver']))
        print("-------------------------------------------------------------------------------------------")