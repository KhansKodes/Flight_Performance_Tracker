import matplotlib
matplotlib.use('Agg')  # Use Agg backend instead of Tk

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

class FlightAnalyzer:
    def __init__(self, file_path):
        """Initialize the analyzer with the data file"""
        self.load_data(file_path)
        self.setup_plot_style()
        
    def load_data(self, file_path):
        """Load and preprocess the flight data"""
        # Read the CSV file
        self.df = pd.read_csv(file_path)
        
        # Convert time columns to datetime
        self.df['time_hour'] = pd.to_datetime(self.df['time_hour'])
        
        # Create month and hour names for better labels
        self.df['month_name'] = pd.to_datetime(self.df['time_hour']).dt.strftime('%B')
        self.df['hour_formatted'] = self.df['hour'].map(lambda x: f"{x:02d}:00")
        
        # Calculate additional metrics
        self.df['is_delayed'] = self.df['dep_delay'] > 15  # Flights delayed more than 15 minutes
        self.df['total_delay'] = self.df['dep_delay'] + self.df['arr_delay']
        
    def setup_plot_style(self):
        """Set up the default plotting style"""
        sns.set_theme()
        self.colors = sns.color_palette("husl", 8)
        
    def plot_delay_distribution(self, carrier=None):
        """Plot the distribution of departure delays"""
        plt.figure(figsize=(12, 6))
        
        data = self.df if carrier is None else self.df[self.df['name'] == carrier]
        
        sns.histplot(data=data[data['dep_delay'] > 0], 
                    x='dep_delay', bins=50)
        plt.title('Distribution of Departure Delays')
        plt.xlabel('Delay Minutes')
        plt.ylabel('Number of Flights')
        plt.savefig('delay_distribution.png')  # Save instead of show
        plt.close()  # Close the figure to free memory
        
    def plot_carrier_performance(self):
        """Plot performance metrics for each carrier"""
        plt.figure(figsize=(12, 6))
        
        carrier_stats = self.df.groupby('name').agg({
            'is_delayed': 'mean',
            'dep_delay': 'mean'
        }).sort_values('is_delayed', ascending=False)
        
        ax = carrier_stats['is_delayed'].plot(kind='bar', color=self.colors[0])
        plt.title('Carrier Delay Performance')
        plt.xlabel('Carrier')
        plt.ylabel('Percentage of Delayed Flights')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig('carrier_performance.png')  # Save instead of show
        plt.close()  # Close the figure
        
        return carrier_stats
        
    def plot_hourly_delays(self):
        """Plot average delays by hour of day"""
        plt.figure(figsize=(12, 6))
        
        hourly_delays = self.df.groupby('hour_formatted')['dep_delay'].mean()
        hourly_delays.plot(kind='line', marker='o', color=self.colors[2])
        plt.title('Average Delays by Hour of Day')
        plt.xlabel('Hour')
        plt.ylabel('Average Delay (minutes)')
        plt.grid(True)
        plt.tight_layout()
        plt.savefig('hourly_delays.png')  # Save instead of show
        plt.close()  # Close the figure
        
    def plot_route_analysis(self, top_n=15):
        """Plot average delays for top routes"""
        plt.figure(figsize=(12, 6))
        
        route_delays = (self.df.groupby(['origin', 'dest'])['dep_delay']
                       .agg(['mean', 'count'])
                       .sort_values('mean', ascending=False)
                       .head(top_n))
        
        ax = route_delays['mean'].plot(kind='bar', color=self.colors[3])
        plt.title(f'Top {top_n} Routes by Average Delay')
        plt.xlabel('Route (Origin-Destination)')
        plt.ylabel('Average Delay (minutes)')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig('route_analysis.png')  # Save instead of show
        plt.close()  # Close the figure
        
        return route_delays
        
    def plot_monthly_trends(self):
        """Plot monthly delay trends"""
        plt.figure(figsize=(12, 6))
        
        monthly_stats = self.df.groupby('month_name').agg({
            'dep_delay': 'mean',
            'arr_delay': 'mean'
        })
        
        # Reorder months chronologically
        month_order = ['January', 'February', 'March', 'April', 'May', 'June',
                      'July', 'August', 'September', 'October', 'November', 'December']
        monthly_stats = monthly_stats.reindex(month_order)
        
        monthly_stats.plot(kind='bar', color=[self.colors[4], self.colors[5]])
        plt.title('Monthly Delay Trends')
        plt.xlabel('Month')
        plt.ylabel('Average Delay (minutes)')
        plt.legend(['Departure Delay', 'Arrival Delay'])
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig('monthly_trends.png')  # Save instead of show
        plt.close()  # Close the figure
        
        return monthly_stats
    
    def generate_summary_statistics(self):
        """Generate summary statistics for the dataset"""
        summary = {
            'Total Flights': len(self.df),
            'Average Departure Delay': self.df['dep_delay'].mean(),
            'Average Arrival Delay': self.df['arr_delay'].mean(),
            'Percentage Delayed Flights': (self.df['is_delayed'].mean() * 100),
            'Most Common Origin': self.df['origin'].mode().iloc[0],
            'Most Common Destination': self.df['dest'].mode().iloc[0],
            'Carrier with Most Delays': self.df.groupby('name')['is_delayed'].mean().idxmax(),
            'Average Flight Distance': self.df['distance'].mean()
        }
        return pd.Series(summary)

# Example usage
if __name__ == "__main__":
    # Initialize the analyzer
    analyzer = FlightAnalyzer('flights.csv')
    
    # Generate and print summary statistics
    print("Flight Data Summary:")
    print(analyzer.generate_summary_statistics())
    print("\n")
    
    # Generate all visualizations
    analyzer.plot_delay_distribution()
    analyzer.plot_carrier_performance()
    analyzer.plot_hourly_delays()
    analyzer.plot_route_analysis()
    analyzer.plot_monthly_trends()
    
    # Open the generated plots (on Windows)
    os.system('start delay_distribution.png')
    os.system('start carrier_performance.png')
    os.system('start hourly_delays.png')
    os.system('start route_analysis.png')
    os.system('start monthly_trends.png')