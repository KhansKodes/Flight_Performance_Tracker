# Flight Data Analysis Project

## Overview
This project analyzes flight delay patterns and performance metrics using the 2013 flight delays dataset. The analysis includes various visualizations and statistical measures to understand delay distributions, carrier performance, hourly patterns, and route efficiency.

## Dataset
The project uses the Flight Delays Dataset from Kaggle, which contains flight information from 2013:
- [Flight Delays Dataset](https://www.kaggle.com/code/farzadnekouei/flight-data-eda-to-preprocessing/input)

### Dataset Features:
- `year`, `month`, `day`: Date of the flight
- `dep_time`, `sched_dep_time`: Actual and scheduled departure times
- `dep_delay`: Departure delays (in minutes)
- `arr_time`, `sched_arr_time`: Actual and scheduled arrival times
- `arr_delay`: Arrival delays (in minutes)
- `carrier`: Two letter carrier abbreviation
- `flight`: Flight number
- `tailnum`: Plane tail number
- `origin`, `dest`: Origin and destination airports
- `air_time`: Amount of time spent in the air
- `distance`: Distance between airports
- `hour`, `minute`: Time components
- `name`: Full name of the carrier

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/flight-data-analysis.git
cd flight-data-analysis
```

2. Install required packages:
```bash
pip install pandas matplotlib seaborn
```

3. Download the dataset from Kaggle and place it in the project directory as `flights.csv`

## Project Structure
```
flight-data-analysis/
│
├── README.md
├── main.py
├── requirements.txt
```

## Features
- Delay distribution analysis
- Carrier performance comparison
- Hourly delay patterns
- Route efficiency analysis
- Monthly trend visualization
- Comprehensive summary statistics

## Usage Examples

```python
from flight_analyzer import FlightAnalyzer

# Initialize the analyzer
analyzer = FlightAnalyzer('flights.csv')

# Get summary statistics
stats = analyzer.generate_summary_statistics()
print(stats)

# Plot delay distribution for a specific carrier
analyzer.plot_delay_distribution(carrier='United Air Lines Inc.')

# Generate carrier performance visualization
analyzer.plot_carrier_performance()

# Analyze route delays
analyzer.plot_route_analysis(top_n=10)
```

## Visualizations
The project includes several types of visualizations:
1. Delay Distribution: Histogram showing the distribution of flight delays
2. Carrier Performance: Bar chart comparing different airlines' delay rates
3. Hourly Delays: Line plot showing average delays by hour of day
4. Route Analysis: Bar chart of routes with highest average delays
5. Monthly Trends: Comparison of departure and arrival delays by month

## Contributing
1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a Pull Request


## Contact
Project Link: [https://github.com/yourusername/flight-data-analysis](https://github.com/yourusername/flight-data-analysis)

## Acknowledgments
- Dataset provided by Kaggle
- Inspired by real-world flight delay analysis needs
