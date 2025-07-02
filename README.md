# OptimalF1LapSeq_ID

### Title  
**F1 Optimal Lap Sequence Identification Using Self-Organizing Maps (SOMs) and the Apriori Algorithm**

**Report**: [`ProjectReport.pdf`](./ProjectReport.pdf)

---

## Abstract

This project aims to **identify optimal laps in Formula One racing** using:

- **Self-Organizing Maps (SOMs)** for clustering high-dimensional telemetry data  
- **The Apriori Algorithm** for discovering hidden associations

We leverage telemetry data—such as lap times, tire wear, and fuel load—sourced from the **FastF1 API** to uncover patterns that can enhance race strategy.

Our method offers actionable insights into:

- Lap pacing  
- Tire management  
- Pit stop timing  

While our focus is motorsport, the same principles apply to other fields requiring **dynamic optimization**, such as logistics and supply chain management.

---

## Introduction

Artificial intelligence (AI) has become indispensable in motorsport analytics, especially in Formula One. Teams use AI systems to:

- Analyze vast amounts of telemetry data  
- Predict competitor behavior  
- Improve car simulations  
- Optimize real-time strategic decisions

This project introduces an innovative framework that combines:

### Self-Organizing Maps (SOMs)  
To cluster and visualize complex, high-dimensional telemetry data.

### The Apriori Algorithm  
To mine association rules within those clusters, revealing patterns and correlations.

Our goals are to:

- Identify optimal lap sequences that improve race outcomes  
- Provide insights into lap pacing, tire degradation, and pit stop strategies  
- Enable teams to make better data-driven decisions on race day

---

## Broader Applications

Beyond Formula One, this methodology can be applied to domains such as:

- **Logistics**: Optimize delivery routes and schedules  
- **Supply Chain Management**: Improve resource allocation and inventory control

---

## Repository Contents

### Code and Analysis

- **`DataCollection.py`**  
  Connects to the FastF1 API to collect telemetry data for Mercedes, Red Bull, and Ferrari from the 2018, 2019, 2021, 2022, and 2023 seasons. Data is stored in the `Data/` folder.

- **`TelemetryAvailabilityCheck.py`**  
  Checks for the availability of telemetry data across all sessions and seasons.

- **`EDA.py`**  
  Performs exploratory data analysis on the collected data. Outputs performance-related plots stored in the `Plots/` folder.

- **`PreProcessing.py`**  
  Cleans, transforms, and performs feature engineering on the raw telemetry data. The output is stored in the `Transformed Data/` folder.

- **`combining_files.py`**  
  Merges each season’s race data into a single CSV per team. Uses the `Transformed Data/` folder and saves combined files in team-specific subfolders.

- **`encoding_combined_files.py`**  
  Applies one-hot and binary encoding to selected features. Outputs are saved in each team’s `Transformed Data/` subfolder.

- **`soms_apriori.py`**  
  Runs the SOM algorithm to identify optimal laps via heatmaps and plots. These are saved in a new `plots/` folder. Also applies the Apriori algorithm to generate association rules saved under `association_rules/`.

- **`apriori_topk.py`**  
  Filters and extracts the top-k association rules based on configurable criteria. Output is stored in the `association_rules/` folder.

---
