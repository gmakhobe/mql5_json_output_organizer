import datetime

# Define two date and time objects
start_date = datetime.datetime(2023, 10, 1, 12, 0)  # Example start date and time
end_date = datetime.datetime(2023, 10, 5, 14, 30)   # Example end date and time

# Calculate the duration
duration = end_date - start_date

# Extract days and seconds from the duration
days = duration.days
seconds = duration.seconds

# Calculate the number of hours
hours = seconds // 3600  # 3600 seconds in an hour

# Format the output
if days > 0:
    duration_str = f"{days} days"
elif hours > 0:
    duration_str = f"{hours} hours"
else:
    duration_str = "Less than 1 hour"

print(f"The duration between the two dates is approximately {duration_str}.")