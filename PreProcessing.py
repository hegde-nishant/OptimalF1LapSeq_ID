import pandas as pd
from datetime import timedelta
import numpy as np
import warnings
from natsort import natsorted
import os

warnings.filterwarnings("ignore")

def convertTimes(time_str):
    # Parse the time string into a timedelta object
    # Since the input string is in a non-standard format, we'll manually extract and convert it
    if pd.isna(time_str):
        return 0
    else:
        days, time_part = time_str.split(" days ")
        time_components = time_part.split(":")
        hours, minutes, seconds_micro = int(time_components[0]), int(time_components[1]), time_components[2]

        if "." in seconds_micro: 
            seconds, microseconds = seconds_micro.split(".") 
            microseconds = int(microseconds) 
        else: 
            seconds = seconds_micro 
            microseconds = 0

        td = timedelta(
        days=int(days),
        hours=int(hours),
        minutes=int(minutes),
        seconds=int(seconds),
        microseconds=int(microseconds))

        return int(td.total_seconds() * 1000)

data_path = '/home/nhegde2/Data-Mining-Project/Data/'
transformed_data_path = '/home/nhegde2/Data-Mining-Project/TransformedData/'
team_names = ['Ferrari', 'Mercedes', 'Redbull']
seshInfoFolderName = 'DriverLapTimes'
seasons = ['2018', '2019', '2021', '2022', '2023']

for team in team_names:
    fp1 = data_path + team + '/'
    tfp1 = transformed_data_path + team + '/'
    
    for season in seasons:        
        fp2 = fp1 + seshInfoFolderName + '/' + season
        tfp2 = tfp1 + seshInfoFolderName + '/' + season
        
        races = os.listdir(fp2)

        for race in natsorted(races):
            driver_files = os.listdir(fp2 + '/' + race)
            
            for driver in driver_files[:2]:
                print(fp2 + '/' + race + '/' + driver)
                df = pd.read_csv(fp2 + '/' + race + '/' + driver)
                
                if len(df[(df.columns)[0]]) <= 5:   #Skipping files that have less than 5 laps data
                    continue
                
                columns_to_be_dropped = ['Time', 'Driver', 'DriverNumber', 'Stint', 'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime', 'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'Team', 'LapStartTime', 'LapStartDate', 'DeletedReason', 'FastF1Generated', 'IsAccurate', 'TrackStatus']

                df.drop(columns_to_be_dropped, axis = 1, inplace = True)

                #Data processing of columns
                # 1. Converting Lap time = str (time in days, hours, minutes, seconds, and microseconds) to float (milliseconds)
                laptimes = []
                for i, value in enumerate(df['LapTime'].values):
                    laptimes.append(convertTimes(value))
                    
                df['LapTime'] = laptimes

                # 2. Based on pit in and pit out time, add new columns that populates 0 for that lap where pit in and pit out  = nan and 1 for any time in pit in or pit out

                if_pit_in = [1] * len(df['PitInTime'])
                if_pit_out = [1] * len(df['PitOutTime'])

                for i in range(len(df['PitInTime'])):
                    if pd.isna(df['PitInTime'][i]):
                        if_pit_in[i] = 0

                    if pd.isna(df['PitOutTime'][i]):
                        if_pit_out[i] = 0

                df['If_PitIn'] = if_pit_in
                df['If_PitOut'] = if_pit_out

                #Drop PitInTime and PitOutTime columns
                df.drop(['PitInTime', 'PitOutTime'], axis = 1, inplace = True)

                #Processing sector 1, sector 2 and sector 3 times.
                sector1_times, sector2_times, sector3_times = [], [], []
                for i, value in enumerate(df['Sector1Time'].values):

                    #when data is nan
                    if pd.isna(value):
                        if (not pd.isna(df['Sector2Time'][i])) and (not pd.isna(df['Sector3Time'][i])) and (not pd.isna(df['LapTime'][i])):
                            s1_time = df['LapTime'][i] - (convertTimes(df['Sector2Time'][i]) + convertTimes(df['Sector3Time'][i]))   #sector1 time = lap time - (sector2 time + sector3 time)
                            sector1_times.append(s1_time)
                        else:
                            sector1_times.append(0)    #Just append zero. Can't be calculated
                    else:
                        #When
                        sector1_times.append(convertTimes(value))

                for i, value in enumerate(df['Sector2Time'].values):

                    #when data is nan
                    if pd.isna(value):
                        if (not pd.isna(df['Sector1Time'][i])) and (not pd.isna(df['Sector3Time'][i])) and (not pd.isna(df['LapTime'][i])):
                            s2_time = df['LapTime'][i] - (convertTimes(df['Sector1Time'][i]) + convertTimes(df['Sector3Time'][i]))   #sector2 time = lap time - (sector1 time + sector3 time)
                            sector2_times.append(s2_time)
                        else:
                            sector2_times.append(0)    #Just append zero. Can't be calculated
                    else:
                        #When
                        sector2_times.append(convertTimes(value))

                for i, value in enumerate(df['Sector3Time'].values):

                    #when data is nan
                    if pd.isna(value):
                        if (not pd.isna(df['Sector2Time'][i])) and (not pd.isna(df['Sector1Time'][i])) and (not pd.isna(df['LapTime'][i])):
                            s3_time = df['LapTime'][i] - (convertTimes(df['Sector2Time'][i]) + convertTimes(df['Sector1Time'][i]))   #sector3 time = lap time - (sector1 time + sector2 time)
                            sector3_times.append(s3_time)
                        else:
                            sector3_times.append(0)    #Just append zero. Can't be calculated
                    else:
                        #When
                        sector3_times.append(convertTimes(value))
                  
                df['Sector1Time'] = sector1_times
                df['Sector2Time'] = sector2_times
                df['Sector3Time'] = sector3_times

                #Converting numpy boolean features to to boolean data
                for i, value in enumerate(df['IsPersonalBest'].values):
                    if value == True:
                        df['IsPersonalBest'][i] = 1
                    else:
                        df['IsPersonalBest'][i] = 0

                for i, value in enumerate(df['FreshTyre'].values):
                    if value == True:
                        df['FreshTyre'][i] = 1
                    else:
                        df['FreshTyre'][i] = 0

                for i, value in enumerate(df['Deleted'].values):
                    if value == True:
                        df['Deleted'][i] = 1
                    else:
                        df['Deleted'][i] = 0

                #Handling null/nan values

                #Laptimes
                for i, time in enumerate(df['LapTime']):
                    if pd.isna(time):
                        df['LapTime'][i] = df['LapTime'].mean()

                #SectorTimes
                for i in range(len(df['Sector1Time'])):
                    if pd.isna(df['Sector1Time'][i]):
                        df['Sector1Time'][i] = df['Sector1Time'].mean()

                    if pd.isna(df['Sector2Time'][i]):
                        df['Sector2Time'][i] = df['Sector2Time'].mean()

                    if pd.isna(df['Sector3Time'][i]):
                        df['Sector3Time'][i] = df['Sector3Time'].mean()

                #Personal best
                for i in range(len(df['IsPersonalBest'])):
                    if pd.isna(df['IsPersonalBest'][i]):
                        df['IsPersonalBest'][i] = 0     #Set binary False

                #Deleted
                for i in range(len(df['FreshTyre'])):
                    if pd.isna(df['FreshTyre'][i]):
                        df['FreshTyre'][i] = 0     #Set binary False

                #Compound
                for i in range(len(df['Compound'])):
                    if pd.isna(df['Compound'][i]):
                        if i == 0:
                            df['Compound'][i] = df['Compound'][i: 5].mode()[0]  #mode of the next 5 values (since the i + 1) value can be none
                        elif i == len(df['Compound']) - 1:
                            df['Compound'][i] = df['Compound'][i - 5: i].mode()[0]  #mode of the last 5 values (since the i - 1) value can be none
                        else:
                            df['Compound'][i] = df['Compound'][i - 1: i + 1].mode()[0] #kernel of size 3

                #TyreLife
                for i in range(len(df['TyreLife'])):
                    if pd.isna(df['TyreLife'][i]):
                        if i == 0:
                            df['TyreLife'][i] = df['TyreLife'][i + 1]
                        elif i == len(df['TyreLife']) - 1:
                            df['TyreLife'][i] = df['TyreLife'][i - 1]
                        else:
                            df['TyreLife'][i] = df['TyreLife'][i - 1]


                #Feature engineering
                #Creating avg sector feature for all three sectors
                avg_sector_time = []
                for i in range(len(df['Sector1Time'])):
                    avg_sector_time.append((df['Sector1Time'][i] + df['Sector2Time'][i] + df['Sector3Time'][i])/3)

                df['AvgSectorTime'] = avg_sector_time

                #One hot encoding for positions gained, lost or unchanged
                # Calculate the change in position
                position_diff = np.diff(df['Position'], prepend=df['Position'][0])  # Prepend first value for alignment

                # Create columns for position gained or lost
                position_status = np.where(position_diff < 0, 'Gained',
                                np.where(position_diff > 0, 'Lost', 'Unchanged'))

                # Create DataFrame
                df1 = pd.DataFrame({
                    'Position': df['Position'],
                    'Position_Status': position_status
                })

                # One-hot encode the 'Position_Status' column
                df_one_hot = pd.get_dummies(df1, columns=['Position_Status'], prefix='', prefix_sep='')
                
                # Ensure all expected columns exist, adding them if missing
                expected_columns = ['Gained', 'Lost', 'Unchanged']
                for col in expected_columns:
                    if col not in df_one_hot:
                        df_one_hot[col] = 0  # Initialize missing columns with 0

                print(df_one_hot.columns)

                df['PositionGained'], df['PositionLost'], df['PositionUnchanged'] = df_one_hot['Gained'].astype(int), df_one_hot['Lost'].astype(int), df_one_hot['Unchanged'].astype(int)

                #Compound type one-hot encoding
                categories = ['soft', 'medium', 'hard', 'intermediate', 'wet']

                df['Soft'] = [0] * len(df['LapTime'])
                df['Medium'] = [0] * len(df['LapTime'])
                df['Hard'] = [0] * len(df['LapTime'])
                df['Intermediate'] = [0] * len(df['LapTime'])
                df['Wet'] = [0] * len(df['LapTime'])

                for i, c_val in enumerate(df['Compound'].values):
                    if c_val.lower() == 'soft':
                        df['Soft'][i] = 1
                    elif c_val.lower() == 'medium':
                        df['Medium'][i] = 1
                    elif c_val.lower() == 'hard':
                        df['Hard'][i] = 1
                    elif c_val.lower() == 'intermediate':
                        df['Intermediate'][i] = 1
                    elif c_val.lower() == 'wet':
                        df['Wet'][i] = 1
                    else:
                        df['Soft'] = 1

                #Drop the compound column
                df.drop(['Compound'], axis = 1, inplace = True)


                #Fuel Load
                base_fl = 110                                       #Every car starts with 110kg of fuel every race
                inspection_fl = 1                                   #At the end of the race a minimum of 1kg fuel must remain in the car for inspection
                num_laps = len(df['LapTime'])

                decay_rate = (base_fl - inspection_fl)/num_laps

                fuelLoad_decay = [0] * num_laps

                for i in range(len(fuelLoad_decay)):
                    fuelLoad_decay[i] = base_fl
                    base_fl = base_fl - decay_rate
                    
                bin_edges = np.linspace(min(fuelLoad_decay), max(fuelLoad_decay), 4)  # 3 categories => 4 edges

                # Define categories using bin edges
                def categorize_auto(value):
                    if value >= bin_edges[2]:  # Upper third (High)
                        return 'High'
                    elif (value <= bin_edges[2]) and (value >= bin_edges[1]):  # Middle third (Medium)
                        return 'Medium'
                    else:  # Lower third (Low)
                        return 'Low'

                # Apply categorization
                categories = [categorize_auto(val) for val in fuelLoad_decay]

                # Create a DataFrame
                df1 = pd.DataFrame({
                    'Fuel Load Decay': fuelLoad_decay,
                    'Category': categories
                })

                # Perform one-hot encoding
                df_one_hot = pd.get_dummies(df1, columns=['Category'], prefix='', prefix_sep='')
                
                # Ensure all expected columns exist, adding them if missing
                expected_columns = ['High', 'Medium', 'Low']
                for col in expected_columns:
                    if col not in df_one_hot:
                        df_one_hot[col] = 0  # Initialize missing columns with 0

                df['HighFuelLoad'] = df_one_hot['High'].astype(int)
                df['MediumFuelLoad'] = df_one_hot['Medium'].astype(int)
                df['LowFuelLoad'] = df_one_hot['Low'].astype(int)
                
                if not os.path.exists(tfp2 + '/' + race + '/'):
                    os.makedirs(tfp2 + '/' + race + '/')
                
                df.to_csv(tfp2 + '/' + race + '/' + driver)