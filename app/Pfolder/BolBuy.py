# Calculate 5% of LowerBol
dt_Pan['LowerBol_5perc'] = dt_Pan['LowerBol'] * 0.05

# Determine the upper and lower bounds
dt_Pan['LowerBol_upper'] = dt_Pan['LowerBol'] + dt_Pan['LowerBol_5perc']
dt_Pan['LowerBol_lower'] = dt_Pan['LowerBol'] - dt_Pan['LowerBol_5perc']

# Check if Close is within ±5% of LowerBol
dt_Pan['Close_within_5perc_LowerBol'] = (dt_Pan['Close'] <= dt_Pan['LowerBol_upper']) & (dt_Pan['Close'] >= dt_Pan['LowerBol_lower'])



#second part
# Assuming dt_Pan has a DateTimeIndex or a similar time-based index

# Calculate 5% of LowerBol
dt_Pan['LowerBol_5perc'] = dt_Pan['LowerBol'] * 0.05

# Determine the upper and lower bounds
dt_Pan['LowerBol_upper'] = dt_Pan['LowerBol'] + dt_Pan['LowerBol_5perc']
dt_Pan['LowerBol_lower'] = dt_Pan['LowerBol'] - dt_Pan['LowerBol_5perc']

# Identify rows where Close is within ±5% of LowerBol
dt_Pan['Close_within_5perc_LowerBol'] = (dt_Pan['Close'] <= dt_Pan['LowerBol_upper']) & (dt_Pan['Close'] >= dt_Pan['LowerBol_lower'])

# Initialize an empty list to store the time references
time_references = []

# Iterate through the DataFrame to find when Close goes above MA20 after being within ±5% of LowerBol
for index, row in dt_Pan.iterrows():
    if row['Close_within_5perc_LowerBol']:
        # Look ahead to see if Close goes above MA20
        future_rows = dt_Pan.loc[index:]
        for future_index, future_row in future_rows.iterrows():
            if future_row['Close'] > future_row['MA20']:
                time_references.append((index, future_index))  # Store the initial and crossing time references
                break  # Stop looking ahead once the condition is met

# time_references now contains tuples of (initial_time, crossing_time)

# calculate slope of MA20 over the last 5 days
dt_Pan['MA20_Slope_5Day'] = dt_Pan['MA20'].diff(periods=5) / 5
