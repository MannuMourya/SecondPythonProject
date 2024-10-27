#EventScope: Visualizing History

## Overview

The Historical Events Visualization project aims to provide insights into significant historical events through data visualization. By analyzing a dataset containing key historical milestones, this project allows users to explore trends and patterns in historical occurrences across different centuries.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Output](#output)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Understanding history helps us learn from the past and shape our future. This project visualizes historical events to highlight their distribution over time, making it easier to identify trends and significant periods in history.

## Features

- **Data Loading**: Reads historical event data from a CSV file.
- **Data Cleaning**: Processes and formats the data for analysis, including handling years and creating century bins.
- **Visualization**: Generates a bar chart displaying the number of historical events per century, providing a clear visual representation of trends over time.

## Technologies Used

- **Python**: The primary programming language for data manipulation and visualization.
- **Pandas**: A library used for data manipulation and analysis.
- **NumPy**: A library for numerical operations, used for handling data arrays.
- **Matplotlib**: A plotting library used for creating static, animated, and interactive visualizations in Python.

## Dataset

The dataset used in this project consists of significant historical events. Each entry includes:

- **Year**: The year the event took place.
- **Event**: A brief description of the event.

The dataset is stored in a CSV file named `historical_events.csv`.

## Installation

To run this project, you need to have Python installed on your machine. You can download Python from the official website: [python.org](https://www.python.org/downloads/).

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/historical-events-visualization.git
   cd historical-events-visualization
