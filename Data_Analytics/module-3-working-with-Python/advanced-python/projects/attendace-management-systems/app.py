# create a data frames 
import pandas as pd 
import matplotlib.pyplot as plt 

data = {
    "studentname": ["Faiz", "Jay", "Meet", "forum", "rutwick", "brijesh"],
    "attendance": [0, 0, 1, 1, 1, 1]
}

# Create DataFrame
df = pd.DataFrame(data)

# Count present and absent students
present = (df["attendance"] == 1).sum()
absent = (df["attendance"] == 0).sum()

# Data for pie chart
labels = ["Present", "Absent"]
values = [present, absent]
colors = ["green", "red"]

# Create pie chart
plt.figure(figsize=(8, 8))

plt.pie(
    values,
    labels=labels,
    colors=colors,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Student Attendance Management System")
plt.show()

# Display counts
print("Present Students:", present)
print("Absent Students:", absent)
