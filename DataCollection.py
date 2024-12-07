#Purpose - To collect data of all races from 2018 to 2023
import fastf1 as ff1
import pandas as pd
import os

#Load data from cache if already present
ff1.Cache.enable_cache('/path/to/the/cache/')

#Merc drivers over the seasons
merc_drivers = [['HAM', 'BOT'], ['HAM', 'BOT'], ['HAM', 'BOT'], ['HAM', 'RUS'], ['HAM', 'RUS']]  #Base index considered as 2018 season
merc_driver_numbers = [[44, 77], [44, 77], [44, 77], [44, 63], [44, 63]]

#Redbull drivers over the seasons
rb_drivers = [['RIC', 'VER'], ['VER', 'GAS', 'ALB'], ['VER', 'PER'], ['VER', 'PER'], ['VER', 'PER']]  #Base index consider as 2018 season
rb_driver_numbers = [[3, 33], [33, 10, 23], [33, 11], [1, 11], [1, 11]]

#Scuderia Ferarri drivers over the season
ferrari_drivers = [['RAI', 'VET'], ['RAI', 'VET'],['LEC', 'SAI'], ['LEC', 'SAI'], ['LEC', 'SAI']]   #Base index consider as 2018 season
ferrari_driver_numbers = [[5, 7], [5, 16], [16, 55], [16, 55], [16, 55]]

print("Data collection [START].................")

seasons = [2018, 2019, 2021, 2022, 2023]

#Paths where the csv files need to be saved
merc_data_path = '/mercedes/save/path/'
rb_data_path = '/redbull/save/path/'
ferrari_data_path = '/ferrari/save/path/'

print("Collecting data for Mercedes Petronas AMG formula team, Redbull Racing formula, Scuderia Ferrari formula team for seasons: ", seasons)

numRaces = [21, 21, 22, 22, 22]   #Base index considered as 2018 season

#Driver Info Collection

#Collect Mercedes Petronas AMG formula team data
for sno, season in enumerate(seasons):
    for i in range(1, numRaces[sno] + 1):   #Get the number of races for that season from the numRaces list
        try:
            #Get session and load it
            session = ff1.get_session(season, i, 'R')
            session.load(telemetry=True, laps=True, weather=True, messages = True)
            
            #Create the driver session info folder if it doesn't already exist
            driverSessionInfo_folder = merc_data_path + 'DriverSessionInfo'
            if not os.path.exists(driverSessionInfo_folder):
                os.makedirs(driverSessionInfo_folder)
            
            #Create the folder structure if it doesn't already exist
            season_folder = driverSessionInfo_folder + '/' + str(season)
            if not os.path.exists(season_folder):
                os.makedirs(season_folder)
            
            session_folder = season_folder + '/' + str(i)
            if not os.path.exists(session_folder):
                os.makedirs(session_folder)
            
            #Collect driver session data
            print("Drivers: ", merc_drivers[sno])
            for driver in merc_drivers[sno]: #Iterate over all the drivers for the particular season
                
                print("Collecting {} info for {} session.".format(driver, session))
                
                driverInfo_df = pd.DataFrame(session.get_driver(driver))
                driverInfo_df = driverInfo_df.T  #Transpose the dataframe
                driverInfo_df.to_csv(session_folder + '/' + driver + '_info.csv', index=False)
        except:
            continue
        

#Collect Redbull Racing formula team data
for sno, season in enumerate(seasons):
    for i in range(1, numRaces[sno] + 1):   #Get the number of races for that season from the numRaces list
        try:
            #Get session and load it
            session = ff1.get_session(season, i, 'R')
            session.load(telemetry=True, laps=True, weather=True, messages = True)
            
            #Create the driver session info folder if it doesn't already exist
            driverSessionInfo_folder = rb_data_path + 'DriverSessionInfo'
            if not os.path.exists(driverSessionInfo_folder):
                os.makedirs(driverSessionInfo_folder)
            
            #Create the folder structure if it doesn't already exist
            season_folder = driverSessionInfo_folder + '/' + str(season)
            if not os.path.exists(season_folder):
                os.makedirs(season_folder)
            
            session_folder = season_folder + '/' + str(i)
            if not os.path.exists(session_folder):
                os.makedirs(session_folder)
            
            #Collect driver session data
            print("Drivers: ", rb_drivers[sno])
            for driver in rb_drivers[sno]: #Iterate over all the drivers for the particular season
                
                print("Collecting {} info for {} session.".format(driver, session))
                
                driverInfo_df = pd.DataFrame(session.get_driver(driver))
                driverInfo_df = driverInfo_df.T  #Transpose the dataframe
                driverInfo_df.to_csv(session_folder + '/' + driver + '_info.csv', index=False)
        except:
            continue
     

#Collect Scuderia Ferrari formula team data
for sno, season in enumerate(seasons):
    for i in range(1, numRaces[sno] + 1):   #Get the number of races for that season from the numRaces list
        try:
            #Get session and load it
            session = ff1.get_session(season, i, 'R')
            session.load(telemetry=True, laps=True, weather=True, messages = True)
            
            #Create the driver session info folder if it doesn't already exist
            driverSessionInfo_folder = ferrari_data_path + 'DriverSessionInfo'
            if not os.path.exists(driverSessionInfo_folder):
                os.makedirs(driverSessionInfo_folder)
            
            #Create the folder structure if it doesn't already exist
            season_folder = driverSessionInfo_folder + '/' + str(season)
            if not os.path.exists(season_folder):
                os.makedirs(season_folder)
            
            #Create session folder
            session_folder = season_folder + '/' + str(i)
            if not os.path.exists(session_folder):
                os.makedirs(session_folder)
            
            #Collect driver session data
            print("Drivers: ", ferrari_drivers[sno])
            for driver in ferrari_drivers[sno]: #Iterate over all the drivers for the particular season
                
                print("Collecting {} info for {} session.".format(driver, session))
                
                driverInfo_df = pd.DataFrame(session.get_driver(driver))
                driverInfo_df = driverInfo_df.T  #Transpose the dataframe
                driverInfo_df.to_csv(session_folder + '/' + driver + '_info.csv', index=False)
        except:
            continue

#Collect Merc drivers lap times
for sno, season in enumerate(seasons):
    for i in range(1, numRaces[sno] + 1):   #Get the number of races for that season from the numRaces list
        try:
            session = ff1.get_session(season, i, 'R')
            session.load(telemetry=True, laps=True, weather=True, messages = True)
            
            driverLapTimes_folder = merc_data_path + 'DriverLapTimes'
            if not os.path.exists(driverLapTimes_folder):
                os.makedirs(driverLapTimes_folder)
                
            #Create the folder structure if it doesn't already exist
            season_folder = driverLapTimes_folder + '/' + str(season)
            if not os.path.exists(season_folder):
                os.makedirs(season_folder)
                
            #Create session folder
            session_folder = season_folder + '/' + str(i)
            if not os.path.exists(session_folder):
                os.makedirs(session_folder)
                
            print("Drivers: ", merc_drivers[sno])
            for driver in merc_drivers[sno]: #Iterate over all the drivers for the particular season
                print("Collecting lap times of {} for {} session.".format(driver, session))
                
                driverLapTimes_df = pd.DataFrame(session.laps.pick_driver(driver))
                driverLapTimes_df.to_csv(session_folder + '/' + driver + '_LapTimes.csv', index=False)
            
        except:
            continue

#Collect Redbull driver lap times
for sno, season in enumerate(seasons):
    for i in range(1, numRaces[sno] + 1):   #Get the number of races for that season from the numRaces list
        try:
            session = ff1.get_session(season, i, 'R')
            session.load(telemetry=True, laps=True, weather=True, messages = True)
            
            driverLapTimes_folder = rb_data_path + 'DriverLapTimes'
            if not os.path.exists(driverLapTimes_folder):
                os.makedirs(driverLapTimes_folder)
                
            #Create the folder structure if it doesn't already exist
            season_folder = driverLapTimes_folder + '/' + str(season)
            if not os.path.exists(season_folder):
                os.makedirs(season_folder)
                
            #Create session folder
            session_folder = season_folder + '/' + str(i)
            if not os.path.exists(session_folder):
                os.makedirs(session_folder)
                
            print("Drivers: ", rb_drivers[sno])
            for driver in rb_drivers[sno]: #Iterate over all the drivers for the particular season
                print("Collecting lap times of {} for {} session.".format(driver, session))
                
                driverLapTimes_df = pd.DataFrame(session.laps.pick_driver(driver))
                driverLapTimes_df.to_csv(session_folder + '/' + driver + '_LapTimes.csv', index=False)
            
        except:
            continue

    
#Collect Ferrari driver lap times
for sno, season in enumerate(seasons):
    for i in range(1, numRaces[sno] + 1):   #Get the number of races for that season from the numRaces list
        try:
            session = ff1.get_session(season, i, 'R')
            session.load(telemetry=True, laps=True, weather=True, messages = True)
            
            driverLapTimes_folder = ferrari_data_path + 'DriverLapTimes'
            if not os.path.exists(driverLapTimes_folder):
                os.makedirs(driverLapTimes_folder)
                
            #Create the folder structure if it doesn't already exist
            season_folder = driverLapTimes_folder + '/' + str(season)
            if not os.path.exists(season_folder):
                os.makedirs(season_folder)
                
            #Create session folder
            session_folder = season_folder + '/' + str(i)
            if not os.path.exists(session_folder):
                os.makedirs(session_folder)
                
            print("Drivers: ", ferrari_drivers[sno])
            for driver in ferrari_drivers[sno]: #Iterate over all the drivers for the particular season
                print("Collecting lap times of {} for {} session.".format(driver, session))
                
                driverLapTimes_df = pd.DataFrame(session.laps.pick_driver(driver))
                driverLapTimes_df.to_csv(session_folder + '/' + driver + '_LapTimes.csv', index=False)
            
        except:
            continue

  
#Collect Merc driver telemetry data
for sno, season in enumerate(seasons):
    for i in range(1, numRaces[sno] + 1):   #Get the number of races for that season from the numRaces list
        try:
            session = ff1.get_session(season, i, 'R')
            session.load(telemetry=True, laps=True, weather=True, messages = True)
            
            telemetryData_folder = merc_data_path + 'TelemetryData'
            if not os.path.exists(telemetryData_folder):
                os.makedirs(telemetryData_folder)
                
            #Create the folder structure if it doesn't already exist
            season_folder = telemetryData_folder + '/' + str(season)
            if not os.path.exists(season_folder):
                os.makedirs(season_folder)
                
            #Create session folder
            session_folder = season_folder + '/' + str(i)
            if not os.path.exists(session_folder):
                os.makedirs(session_folder)
                
            print("Drivers: ", merc_drivers[sno])
            for driver in merc_drivers[sno]: #Iterate over all the drivers for the particular season
                print("Collecting lap times of {} for {} session.".format(driver, session))
                
                driverLapTimes_df = pd.DataFrame(session.laps.pick_driver(driver).get_telemetry())
                driverLapTimes_df.to_csv(session_folder + '/' + driver + '_SessionTelemetry.csv', index=False)
            
        except:
            continue
  
#Collect Redbull driver telemetry data
for sno, season in enumerate(seasons):
    for i in range(1, numRaces[sno] + 1):   #Get the number of races for that season from the numRaces list
        try:
            session = ff1.get_session(season, i, 'R')
            session.load(telemetry=True, laps=True, weather=True, messages = True)
            
            telemetryData_folder = rb_data_path + 'TelemetryData'
            if not os.path.exists(telemetryData_folder):
                os.makedirs(telemetryData_folder)
                
            #Create the folder structure if it doesn't already exist
            season_folder = telemetryData_folder + '/' + str(season)
            if not os.path.exists(season_folder):
                os.makedirs(season_folder)
                
            #Create session folder
            session_folder = season_folder + '/' + str(i)
            if not os.path.exists(session_folder):
                os.makedirs(session_folder)
                
            print("Drivers: ", rb_drivers[sno])
            for driver in rb_drivers[sno]: #Iterate over all the drivers for the particular season
                print("Collecting lap times of {} for {} session.".format(driver, session))
                
                driverLapTimes_df = pd.DataFrame(session.laps.pick_driver(driver).get_telemetry())
                driverLapTimes_df.to_csv(session_folder + '/' + driver + '_SessionTelemetry.csv', index=False)
            
        except:
            continue

#Collect Ferrari driver telemetry data
for sno, season in enumerate(seasons):
    for i in range(1, numRaces[sno] + 1):   #Get the number of races for that season from the numRaces list
        try:
            session = ff1.get_session(season, i, 'R')
            session.load(telemetry=True, laps=True, weather=True, messages = True)
            
            telemetryData_folder = ferrari_data_path + 'TelemetryData'
            if not os.path.exists(telemetryData_folder):
                os.makedirs(telemetryData_folder)
                
            #Create the folder structure if it doesn't already exist
            season_folder = telemetryData_folder + '/' + str(season)
            if not os.path.exists(season_folder):
                os.makedirs(season_folder)
                
            #Create session folder
            session_folder = season_folder + '/' + str(i)
            if not os.path.exists(session_folder):
                os.makedirs(session_folder)
                
            print("Drivers: ", ferrari_drivers[sno])
            for driver in ferrari_drivers[sno]: #Iterate over all the drivers for the particular season
                print("Collecting lap times of {} for {} session.".format(driver, session))
                
                driverLapTimes_df = pd.DataFrame(session.laps.pick_driver(driver).get_telemetry())
                driverLapTimes_df.to_csv(session_folder + '/' + driver + '_SessionTelemetry.csv', index=False)            
        except:
            continue