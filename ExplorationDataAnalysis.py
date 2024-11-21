import numpy as np
import os
import pandas as pd
from natsort import natsorted
import matplotlib.pyplot as plt

data_path = '/home/nhegde2/Data-Mining-Project/Data/'

team_names = ['Ferrari', 'Mercedes', 'Redbull']

seshInfoFolderName = 'DriverSessionInfo'

seasons = ['2018', '2019', '2021', '2022', '2023']

for team in team_names:
    fp1 = data_path + team + '/'
    
    season_gain_percent, season_loss_percent = [], []

    for season in seasons:
        
        #New for every season
        final_position, grid_position, status, points = [],[],[],[]
        
        fp2 = fp1 + seshInfoFolderName + '/' + season
        races = os.listdir(fp2)
        
        for race in natsorted(races):
            driver_files = os.listdir(fp2 + '/' + race)
            
            for driver in driver_files[:2]:
                df = pd.read_csv(fp2 + '/' + race + '/' + driver)
                
                final_position.append(df['Position'].values[0])
                grid_position.append(df['GridPosition'].values[0])
                status.append(df['Status'].values[0])
                points.append(df['Points'].values[0])
        
        #Processing the final position list
        for i in range(len(final_position)):
            if np.isnan(final_position[i]):
                final_position[i] = 20  #Last position (only 20 teams participate)
            else:
                final_position[i] = int(final_position[i])
            
            if np.isnan(grid_position[i]):
                grid_position[i] = 20 #Last position (only 20 teams participate)
            else:
                grid_position[i] = int(grid_position[i])

            if np.isnan(points[i]):
                points[i] = 0     #No points
            else:
                points[i] = int(points[i])
             
        plt.figure(figsize=(15, 10))
        plt.plot(range(1, len(final_position)//2 + 1), final_position[:len(final_position)//2], color='red', label = 'D1 Final Position')
        plt.plot(range(1, len(grid_position)//2 + 1), grid_position[:len(grid_position)//2], color='orange', label = 'D1 Grid Position')
        plt.plot(range(1, len(final_position)//2 + 1), final_position[len(final_position)//2:], color='blue', label = 'D2 Final Position')
        plt.plot(range(1, len(grid_position)//2 + 1), grid_position[len(grid_position)//2:], color='green', label = 'D2 Grid Position')
        plt.xlabel('Race Number')
        plt.ylabel('Position')
        plt.title("{} drivers grid position vs finish position for {} season".format(team, season))
        plt.legend()
        plt.autoscale()
        plt.savefig("{}_{}_grid_vs_finish.jpg".format(team, season))
        
        #Calculate position gain percentage and position loss percentage
        gain_count, loss_count = 0, 0
        
        for i in range(len(final_position)):
            if final_position[i] < grid_position[i]:
                gain_count += 1
            
            if final_position[i] > grid_position[i]:
                loss_count += 1
                
        season_gain_percent.append(gain_count/len(final_position) * 100)
        season_loss_percent.append(loss_count/len(final_position) * 100)
        
    #Plot the gain percentage vs loss percentage stacked bar plots for all seasons the team participated in.
    # Create the bar plot
    plt.figure(figsize=(8, 6))
    
    print("Gain Percent: ", season_gain_percent)
    print("Loss Percent: ", season_loss_percent)

    # Define bar width and positions
    bar_width = 0.4  # Width of each bar
    x = np.arange(len(seasons))  # Positions for the first set of bars

    # Create the grouped bar plot
    plt.figure(figsize=(8, 6))
    plt.bar(x - bar_width / 2, season_gain_percent, width=bar_width, label='Position Gain Percentage', color='Green', edgecolor='black')
    plt.bar(x + bar_width / 2, season_loss_percent, width=bar_width, label='Position Loss Percentage', color='Red', edgecolor='black')

    # Add labels, title, and legend
    plt.xlabel('Seasons')
    plt.ylabel('Percentages')
    plt.title('{} Position gain vs loss percentage across seasons'.format(team))
    plt.xticks(x, seasons)  # Set category labels at the center of the bars
    plt.legend()

    # Save the plot
    plt.savefig("{}_pos_gain_vs_loss_percentages_across_seasons.jpg".format(team))