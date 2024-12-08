# F1_OptimalLap_Seq_ID
Title - F1 Optimal Lap Sequence Identification Using Self-Organizing Maps (SOMs) and Apriori Algorithm.

Report - ProjectReport.pdf

**Abstract**
This project aims to identify optimal laps in Formula One racing by leveraging Self-Organizing Maps (SOMs) and the Apriori algorithm. Using telemetry data—such as lap times, tire wear, and fuel load—obtained from the Fast F1 API, we uncover patterns that enhance race strategies.

Our approach enables the discovery of actionable insights into key performance factors like lap pacing, tire management, and pit stop timing. These findings not only benefit motorsport but also have broader applications in fields requiring dynamic optimization, such as logistics and supply chain management.

**Introduction**
Artificial intelligence (AI) has become an indispensable tool in motorsport analytics, particularly in Formula One. Advanced AI systems are employed by F1 teams to analyze vast amounts of telemetry data, automate strategic decisions, and improve real-time race performance. These systems help predict competitors’ behavior, enhance car simulations, and optimize decision-making during races.

This project introduces an innovative framework combining:

**Self-Organizing Maps (SOMs)**: To cluster and visualize high-dimensional telemetry data.
**The Apriori Algorithm**: To extract meaningful associations within these clusters.
By integrating these methodologies, we aim to:

Identify optimal lap sequences for improved race outcomes.
Provide insights into lap pacing, tire wear patterns, and pit stop timing.
Equip teams with data-driven strategies to enhance decision-making during races.

**Broader Applications**
While the focus is on Formula One, this approach extends to other domains requiring dynamic optimization, such as:

Logistics: Efficiently managing delivery routes and schedules.
Supply Chain Management: Optimizing resource allocation and inventory strategies.
This repository includes:

Code: Implementation of SOMs and the Apriori algorithm using Python.
Data: Example telemetry data sourced from the Fast F1 API.
Analysis: Visualizations and insights derived from the analysis.
Explore the repository to discover how AI is revolutionizing motorsport analytics! 🚀


**Files and their purpose**:
1. DataCollection.py - Connects with FastF1 API and collects data for Mercedes, Redbull and Ferrari teams for 5 seasons {2018, 2019, 2021, 2022, 2023}. The collected data is committed in the repo with folder name - Data.

2. TelemetryAvailaibilityCheck.py - Code to check if enough telemetry data is avaialable for every session. Not all seasons have telemetry data made available.

3. EDA.py - Exploratory Data Analysis on collected data. Data is explored to analyze general performance of teams and plot performance related plots. The plots are committed in the repo with the folder name - Plots

4. PreProcessing.py - Code to clean, transform and feature engineer data to be sent to Self Organized Maps. The clean and transformed data present in Transformed Data folder committed to the repo.

5. combining_files.py - Script combines each season's (year) race data into one combined CSV file. This data comes from the Transformed Data folder and the combined files get saved under each team's folder of Transformed Data.

6. encoding_combined_files.py - Script to one-hot encode and binary encode particular features from the combined dataset above. This file is also saved under each team's folder of Transformed Data.

7. soms_apriori.py - Script that includes SOMs code to find the optimal lap by generating HeatMaps and plots. These plots are saved under a newly created folder (when script runs) "plots". Second half of the code gives out association rules using Apriori, and these rules are saved under a newly created folder "association_rules".

8. apriori_topk.py - Script to extract top-k association rules from entire set of rules created, using filteration criterias (can be changed according to preference).  These rules, when script runs, can be viewed under the folder "association_rules".
