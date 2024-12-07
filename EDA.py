import numpy as np
import os
import pandas as pd
from natsort import natsorted
import matplotlib.pyplot as plt

data_path = '/path/to/the/root/data/folder/'

team_names = ['Ferrari', 'Mercedes', 'Redbull']

seshInfoFolderName = 'DriverSessionInfo'

seasons = ['2018', '2019', '2021', '2022', '2023']

# Define team-specific colors
team_colors = {
    'ferrari': {'final': '#FF0000', 'grid': '#FFA500'},  # Red and Orange for Ferrari
    'mercedes': {'final': '#00D2BE', 'grid': '#AAAAAA'},  # Teal and Silver for Mercedes
    'redbull': {'final': '#1E41FF', 'grid': '#FFB800'},  # Blue and Yellow for Red Bull
}

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

        # Get colors for the current team
        final_color = team_colors[team.lower()]['final']
        grid_color = team_colors[team.lower()]['grid']

        # Set F1-inspired theme
        plt.style.use('dark_background')
        plt.figure(figsize=(15, 10))

        # Plot data
        plt.plot(range(1, len(final_position)//2 + 1), final_position[:len(final_position)//2], 
                color=final_color, linewidth=2.5, label='D1 Final Position')
        plt.plot(range(1, len(grid_position)//2 + 1), grid_position[:len(grid_position)//2], 
                color=grid_color, linewidth=2.5, linestyle='--', label='D1 Grid Position')
        plt.plot(range(1, len(final_position)//2 + 1), final_position[len(final_position)//2:], 
                color=final_color, linewidth=2.5, label='D2 Final Position', alpha=0.7)
        plt.plot(range(1, len(grid_position)//2 + 1), grid_position[len(grid_position)//2:], 
                color=grid_color, linewidth=2.5, linestyle='--', label='D2 Grid Position', alpha=0.7)

        # Add labels and title
        plt.xlabel('Race Number', fontsize=14, fontweight='bold', color='white')
        plt.ylabel('Position', fontsize=14, fontweight='bold', color='white')
        plt.title(f"{team.capitalize()} Drivers' Grid vs Finish Positions - {season} Season", 
                fontsize=18, fontweight='bold', color='white')

        # Add gridlines and legend
        plt.grid(color='#555555', linestyle='--', linewidth=0.7)
        plt.legend(fontsize=12, loc='upper right', frameon=True, framealpha=0.8, edgecolor='white')

        # Adjust layout and save the plot
        plt.autoscale()
        plt.savefig(f"{team}_{season}_grid_vs_finish_F1_theme.jpg", dpi=300)
        
        #Calculate position gain percentage and position loss percentage
        gain_count, loss_count = 0, 0
        
        for i in range(len(final_position)):
            if final_position[i] < grid_position[i]:
                gain_count += 1
            
            if final_position[i] > grid_position[i]:
                loss_count += 1
                
        season_gain_percent.append(gain_count/len(final_position) * 100)
        season_loss_percent.append(loss_count/len(final_position) * 100)

    plt.style.use('dark_background')

    # Define bar width and positions
    bar_width = 0.4  # Width of each bar
    x = np.arange(len(seasons))  # Positions for the first set of bars

    # Create the grouped bar plot
    plt.figure(figsize=(10, 7))
    plt.bar(x - bar_width / 2, season_gain_percent, width=bar_width, label='Position Gain Percentage',
            color='#32CD32', edgecolor='black')  # Lime Green for gains
    plt.bar(x + bar_width / 2, season_loss_percent, width=bar_width, label='Position Loss Percentage',
            color='#FF4500', edgecolor='black')  # Orange Red for losses

    # Add labels, title, and legend
    plt.xlabel('Seasons', fontsize=14, fontweight='bold', color='white')
    plt.ylabel('Percentages (%)', fontsize=14, fontweight='bold', color='white')
    plt.title(f"{team.capitalize()} Position Gain vs Loss Percentage Across Seasons", 
            fontsize=16, fontweight='bold', color='white')
    plt.xticks(x, seasons, fontsize=12, color='white')  # Set category labels at the center of the bars
    plt.yticks(fontsize=12, color='white')
    plt.legend(fontsize=12, frameon=True, framealpha=0.8, edgecolor='white')

    # Add gridlines for better readability
    plt.grid(axis='y', color='#555555', linestyle='--', linewidth=0.7)

    # Adjust layout and save the plot
    plt.tight_layout()
    plt.savefig(f"{team}_pos_gain_vs_loss_percentages_across_seasons_F1_theme.jpg", dpi=300)