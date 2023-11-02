import csv
from datetime import datetime, timedelta  # Import timedelta from the datetime module
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import numpy as np


# Check available styles
# print(plt.style.available):

#['Solarize_Light2', '_classic_test_patch', '_mpl-gallery', '_mpl-gallery-nogrid', 'bmh', 'classic', 'dark_background',
# 'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn-v0_8', 'seaborn-v0_8-bright', 'seaborn-v0_8-colorblind', '
# seaborn-v0_8-dark', 'seaborn-v0_8-dark-palette', 'seaborn-v0_8-darkgrid', 'seaborn-v0_8-deep', 'seaborn-v0_8-muted',
# 'seaborn-v0_8-notebook', 'seaborn-v0_8-paper', 'seaborn-v0_8-pastel', 'seaborn-v0_8-poster', 'seaborn-v0_8-talk',
# 'seaborn-v0_8-ticks', 'seaborn-v0_8-white', 'seaborn-v0_8-whitegrid', 'tableau-colorblind10']


# Data obtained from: https://www.ncei.noaa.gov/access/past-weather/75039
# Open the CSV file and read the header row
filename = 'data/Weather_ZIP_75039.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

# for index, column_header in enumerate(header_row):
#     print(index, column_header)
    # 0
    # STATION
    # 1
    # NAME
    # 2
    # DATE
    # 3
    # AWND
    # 4
    # DAPR
    # 5
    # EVAP
    # 6
    # MDPR
    # 7
    # MNPN
    # 8
    # MXPN
    # 9
    # PRCP
    # 10
    # SNOW
    # 11
    # SNWD
    # 12
    # TAVG
    # 13
    # TMAX
    # 14
    # TMIN
    # 15
    # TOBS
    # 16
    # WDF2
    # 17
    # WDF5
    # 18
    # WDMV
    # 19
    # WESD
    # 20
    # WESF
    # 21
    # WSF2
    # 22
    # WSF5
    # 23
    # WT01
    # 24
    # WT02
    # 25
    # WT03
    # 26
    # WT04
    # 27
    # WT05
    # 28
    # WT06
    # 29
    # WT08

    # Create empty lists to store temperature data
    highs = []  # To store high temperatures
    lows = []  # To store low temperatures
    dates = []  # To store dates

    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        for row in reader:
            # Check if the row has at least 14 elements (including the 0-based index)
            if len(row) > 13 and row[13]:
                high = int(row[13])
                highs.append(high)
                if len(row) > 14 and row[14]:
                    low = int(row[14])
                    lows.append(low)
                    # Check if the row has at least 3 elements (including the 0-based index)
                    if len(row) > 2:
                        date = datetime.strptime(row[2], '%Y-%m-%d')
                        dates.append(date)

# Handle the case when the value is empty (e.g., you can skip it or assign a default value)

# # Now you can work with the 'highs' list
# print(highs)
# # # [77, 76, 67, 56, 60, 69, 64, 60, 68, 81, 82, 67, 55, 62, 69, 74, 76, 70, 58, 61, 56, 52, 53, 47, 42, 53, 60, 66, 60, 29,
# # #  27, 30, 33, 51, 57, 70, 72, 63, 48, 63, 48, 53, 65, 65, 70, 77, 63, 49, 53, 69, 78, 87, 79, 67, 48, 48, 76, 74, 83, 72,
# # #  81,.............]
#

# print(lows)
#
# [53, 63, 47, 38, 36, 46, 48, 38, 42, 51, 57, 42, 34, 38, 46, 60, 51, 56, 42, 42, 45, 38, 34, 33, 35, 31, 36, 46, 29, 24,
#  24, 26, 30, 29, 33, 39, 53, 47, 38, 34, 36, 34, 35, 46, 51, 48, 34, 30, 34, 45, 55, 61, 58, 43, 39, 37, 47, 53, 52, 59,
#  53, 45, 46, 54, 57, 60, 51, 53, 45, 56, 50, 45, 42, 46, 42, 38, 39, 33, 39, 49, 66, 68, 60, 52, 50, 46, 47, 49, 59, 65,
#  57, 59, 64, 71, 50, 49, 51, 54, 54, 56, 53, 57, .........

# print(dates)
#
# #[datetime.datetime(2023, 1, 1, 0, 0), datetime.datetime(2023, 1, 2, 0, 0), datetime.datetime(2023, 1, 3, 0, 0),......




# Convert the lists to NumPy arrays for efficient processing
dates = np.array(dates)
highs = np.array(highs)
lows = np.array(lows)


# Create a mask to select dates from January 1, 2023, to September 30, 2023
mask = (dates >= datetime(2023, 1, 1)) & (dates <= datetime(2023, 9, 30))

# Calculate the numerical representation of dates
start_date = datetime(2023, 1, 1)
numerical_dates = np.array([(date - start_date).days for date in dates[mask]])

# Create a smooth range of numerical dates with High Temp
smooth_numerical_dates_high = np.linspace(0, (datetime(2023, 9, 30) - start_date).days, len(highs[mask]))

# Create a smooth range of numerical dates with Low Temp
smooth_numerical_dates_low = np.linspace(0, (datetime(2023, 9, 30) - start_date).days, len(lows[mask]))

# Interpolate high temperatures
smooth_highs = np.interp(smooth_numerical_dates_high, numerical_dates, highs[mask])

# Interpolate low temperatures
smooth_lows = np.interp(smooth_numerical_dates_low, numerical_dates, lows[mask])

# Convert numerical dates back to datetime with High Temp
smooth_dates_high = [start_date + timedelta(days=int(date)) for date in smooth_numerical_dates_high]

# Convert numerical dates back to datetime with Low Temp
smooth_dates_low = [start_date + timedelta(days=int(date)) for date in smooth_numerical_dates_low]


# Create a smooth line plot of high and low temperatures from January 1, 2023, to September 30, 2023
plt.style.use('ggplot')

# Define the figure size (width, height) in inches
fig, ax = plt.subplots(figsize=(12, 8))  # Adjust the width and height as needed

# Plot high and low temperatures
ax.plot(smooth_dates_high, smooth_highs, color='r', alpha=0.5, label='High')
ax.plot(smooth_dates_low, smooth_lows, color='b', alpha=0.5, label='Low')

# Fill the shaded region between high and low temperatures
ax.fill_between(smooth_dates_high, smooth_highs, smooth_lows, color='gray', alpha=0.1, label='High-Low Range')

# Set plot title, labels, and grid
plt.title('Temperatures Irving, TX 2023', fontsize=24)
plt.xlabel('Dates',  fontsize=20)
fig.autofmt_xdate()
plt.ylabel('Temperatures (°F)',  fontsize=20)
plt.grid(True)

# Format the x-axis to display dates in the "YYYY-MM-DD" format
date_formatter = DateFormatter('%Y-%m-%d')
plt.gca().xaxis.set_major_formatter(date_formatter)
plt.xticks(rotation=45)

# Add a legend to the plot
plt.legend(loc='upper right')

plt.show()