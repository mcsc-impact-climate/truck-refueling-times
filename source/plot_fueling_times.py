import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.transforms import BlendedGenericTransform
from common_tools import get_top_dir

def load_data(file_path):
    """Load data from a CSV file."""
    return pd.read_csv(file_path)

def plot_fueling_times(df, top_dir):
    fig, (ax, ax2) = plt.subplots(2, 1, sharex=True, figsize=(10, 8), gridspec_kw={'height_ratios': [1, 3]})
    
    # Set up y-limits for the broken axis
    ax.set_ylim(800, 900)  # Upper axis for high fueling times
    ax2.set_ylim(0, 50)    # Lower axis for regular fueling times
    
    # Hide the spines between the two axes
    ax.spines['bottom'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax2.spines['top'].set_visible(False)
    
    # Hide right and bottom spines for both axes
    ax.spines['right'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    ax2.spines['bottom'].set_visible(False)
    
    # Define colors for each fuel type
    colors = ['blue', 'green', 'red']
    
    # Plot bars for each fuel type with min-max fueling times
    for i, fuel in enumerate(df['Fuel']):
        min_time = df.loc[i, 'Min Fueling Time (minutes)']
        max_time = df.loc[i, 'Max Fueling Time (minutes)']
        
        # Plotting bars and setting text labels for each fuel type
        if fuel == 'Battery Electric':
            # Split the bar for Battery Electric across both axes
            ax2.bar(i, 50 - min_time, bottom=min_time, color=colors[i], width=0.8, edgecolor='black')  # Lower part
            ax.bar(i, max_time - 800, bottom=800, color=colors[i], width=0.8, edgecolor='black')  # Upper part
        else:
            # Plot for other fuels on the lower axis only from min_time to max_time
            ax2.bar(i, max_time - min_time, bottom=min_time, color=colors[i], width=0.8, edgecolor='black')
        
        # Add fuel type label in the middle of each bar
        label_y_position = (min_time + max_time) / 2  # Center of the bar
        if max_time > 100:
            ax2.text(i, 25, fuel, ha='center', va='center', fontsize=15, fontweight='bold', color='white')  # Lower axis for Battery Electric
        else:
            ax2.text(i, label_y_position, fuel, ha='center', va='center', fontsize=15, fontweight='bold', color='white')  # Lower axis for other fuels
        
        # Add annotations below and above each bar
        min_capacity = df.loc[i, 'Min Fuel Capacity']
        max_capacity = df.loc[i, 'Max Fuel Capacity']
        capacity_units = df.loc[i, 'Fuel Capacity Units']
        min_refuel_rate = df.loc[i, 'Min Refueling Rate']
        max_refuel_rate = df.loc[i, 'Max Refueling Rate']
        refuel_units = df.loc[i, 'Refueling Rate Units']

        # Text below the bar on the lower axis
        ax2.text(i, min_time - 2,
                 f"{min_capacity} {capacity_units}\nat {max_refuel_rate} {refuel_units}",
                 ha='center', va='top', fontsize=14)
        
        # Text above the bar on the correct axis
        if fuel == 'Battery Electric':
            ax.text(i, max_time + 10,  # Small offset to ensure text is visible above the bar
                    f"{max_capacity} {capacity_units}\nat {min_refuel_rate} {refuel_units}",
                    ha='center', va='bottom', fontsize=14)
        else:
            ax2.text(i, max_time + 2,
                     f"{max_capacity} {capacity_units}\nat {min_refuel_rate} {refuel_units}",
                     ha='center', va='bottom', fontsize=14)

    # Make all ticks and labels invisible except for the left y-axis
    ax.tick_params(left=True, labelleft=True, bottom=False, labelbottom=False, labelsize=14)
    ax2.tick_params(left=True, labelleft=True, bottom=False, labelbottom=False, labelsize=14)
    
    # Set y-axis label
    ax2.set_ylabel('Fueling Time (minutes)', fontsize=16)
    
    # Show plot
    plt.tight_layout()
    plt.savefig(f"{top_dir}/plots/refueling_info.png", dpi=300)
    
def main():
    top_dir = get_top_dir()
    file_path = f"{top_dir}/data/refueling_info.csv"
    df = load_data(file_path)
    plot_fueling_times(df, top_dir)

if __name__ == '__main__':
    main()

