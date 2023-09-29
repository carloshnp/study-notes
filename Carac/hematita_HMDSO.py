import pandas as pd
import matplotlib.pyplot as plt

# Read the Excel file into a Pandas DataFrame
df = pd.read_excel('hematita_recobrimento_HMDSO.xlsx', header=None)

# Extract the X and Y data columns from the DataFrame
x_data = df.iloc[:, 0]  # Assuming X data is in the first column
y_data = df.iloc[:, 1]  # Assuming Y data is in the second column

x_data = x_data.apply(lambda x: float(x))
y_data = y_data.apply(lambda x: float(x))

# Convert absorbance values from range 0-1 to 0-100
y_data = y_data * 100

plt.figure(figsize=(32, 18)) 

# Plot the data using Matplotlib
plt.plot(x_data, y_data)
plt.xlabel('Wavenumber (cm^-1)', fontsize=28)
plt.ylabel('Absorbance (%)', fontsize=28)
plt.title('Hematita recoberta com HMDSO - análise FTIR', fontsize=36)
plt.grid(True)

# Adjust the y-axis limits to invert the graph
plt.ylim(15, 75)
plt.xlim(3800, 650)
plt.xticks(range(3800, 650, -100))

plt.savefig('hematita_HMDSO.png')