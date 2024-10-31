import matplotlib.pyplot as plt
import numpy as np
import os

# Create directory if it doesn't exist
os.makedirs('plots', exist_ok=True)

# Data
sources = ['Electricity', 'Biomass', 'Natural Gas']
transport = np.asarray([0.02, 1.79, 1.32])
total = np.asarray([13.3, 5, 33.4])
other = total - transport
total_transport_demand = 28  # Quadrillion BTUs

# Custom colors
colors_other = [(219/255, 158/255, 68/255),  # Electricity
                (104/255, 189/255, 78/255),  # Biomass
                (98/255, 167/255, 242/255)]  # Natural Gas
color_transport = 'red'  # Red for transport

# Plot
fig, ax = plt.subplots(figsize=(8, 6))

# Create a stacked bar chart with specified colors
for i, source in enumerate(sources):
    ax.bar(source, other[i], color=colors_other[i])
    ax.bar(source, transport[i], label='Goes to Transport (Quads)' if i == 0 else "", color=color_transport, bottom=other[i])

# Add dashed line for demand threshold
ax.axhline(total_transport_demand, color='black', linestyle='--')

# Customize tick sizes
ax.tick_params(axis='both', which='major', labelsize=16)

# Labels and legend
ax.set_ylabel('Energy (Quads)', fontsize=20)
ax.legend(loc='upper left', fontsize=16)

# Make only the left-hand y-axis visible, hide others
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(True)

# Remove x-axis ticks and labels
ax.set_xticks([])

# Add source labels in the middle of each bar with bold font and matching colors
for i, source in enumerate(sources):
    ax.text(i, -1, source, ha='center', va='top', fontsize=20, fontweight='bold', color=colors_other[i])  # Bold font for labels

# Label line
ax.text(1, total_transport_demand - 2, 'Current Transport Demand', ha='right', va='bottom', color='black', fontsize=16)

# Save the figure
plt.savefig('plots/transport_flows.png', dpi=300)



