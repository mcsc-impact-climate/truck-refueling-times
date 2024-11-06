import matplotlib.pyplot as plt

# Define cost data
diesel_price_range = (0.27, 0.34)   # $/gal converted to ($/kWh to drivetrain) assuming 30% efficiency. Range of average US diesel prices over the past year from https://www.eia.gov/petroleum/gasdiesel/
electricity_price_range = (0.12, 1.23)  # $/kWh converted to ($/kWh to drivetrain) assuming 81% efficiency. Range of DCFC charging prices from https://www.nrel.gov/docs/fy19osti/72326.pdf
h2_price_range = (0.98, 2.04)     # $/kg converted to ($/kWh to drivetrain) assuming 49% efficiency (https://www.spglobal.com/commodityinsights/en/market-insights/latest-news/energy-transition/012324-logistical-woes-and-high-pump-prices-stall-california-h2-market-development)

# Define positions for the categories on the x-axis
categories = ['Diesel\n(ICE)', 'Electricity\n(BEV)', 'H$_2$\n(FCEV)']
x_positions = range(len(categories))

# Plot
fig, ax = plt.subplots(figsize=(10, 6))

# Plot blue and green hydrogen cost ranges as bars
ax.bar(0, diesel_price_range[1] - diesel_price_range[0], bottom=diesel_price_range[0],
       color='lightgrey', edgecolor='black', width=0.4)
ax.bar(1, electricity_price_range[1] - electricity_price_range[0], bottom=electricity_price_range[0],
       color='lightcoral', edgecolor='black', width=0.4)
ax.bar(2, h2_price_range[1] - h2_price_range[0], bottom=h2_price_range[0],
       color='skyblue', edgecolor='black', width=0.4)

# Customize plot
ax.set_ylim(0, 2.1)
ax.set_xlim(-0.5, 2.5)
ax.set_xticks(x_positions)
ax.set_xticklabels(categories, fontsize=24)
ax.set_ylabel('USD per kWh to the Drivetrain', fontsize=22)
ax.tick_params(axis='y', labelsize=18)

# Show plot
plt.tight_layout()
plt.savefig('plots/energy_price.png', dpi=300)
