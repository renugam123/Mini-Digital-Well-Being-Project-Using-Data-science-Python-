import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("digital_usage.csv")

# Convert Date column
data["Date"] = pd.to_datetime(data["Date"])

print("Missing values check:")
print(data.isnull().sum())

# Average screen time
avg_screen = data["ScreenTime"].mean()
print("\nAverage Screen Time:", avg_screen)

# High screen time days
high_screen = data[data["ScreenTime"] > 7]
print("\nHigh Screen Time Days:")
print(high_screen[["Date", "SleepHours", "Mood"]])

# Category-wise usage
category_avg = data[["SocialMedia", "Education", "Entertainment"]].mean()
print("\nCategory-wise Average Usage:")
print(category_avg)

# Burnout days
burnout = data[(data["ScreenTime"] > 7) & (data["SleepHours"] < 6)]
print("\nPotential Digital Burnout Days:")
print(burnout[["Date", "Mood"]])

# Graph 1: Screen time trend
plt.plot(data["Date"], data["ScreenTime"], marker="o")
plt.title("Daily Screen Time Trend")
plt.xlabel("Date")
plt.ylabel("Screen Time (Hours)")
plt.show()

# Graph 2: Screen time vs sleep
plt.scatter(data["ScreenTime"], data["SleepHours"])
plt.title("Screen Time vs Sleep Hours")
plt.xlabel("Screen Time (Hours)")
plt.ylabel("Sleep Hours")
plt.show()
