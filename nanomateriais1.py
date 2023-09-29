import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define the nanoparticle sizes and surface layer thicknesses
sizes = np.arange(1, 101) # nanoparticle sizes from 1 to 100 nm
layer_thicknesses = [0.5, 1.0, 2.0] # surface layer thicknesses in nm

# Initialize an empty list to store the dispersion values
dispersion_values = []

# Calculate the dispersion values for each combination of size and layer thickness
for size in sizes:
    for layer_thickness in layer_thicknesses:
        surface_area = 4 * np.pi * (size + layer_thickness)**2
        volume = (4/3) * np.pi * (size + layer_thickness)**3
        dispersion = surface_area / volume
        dispersion_values.append([size, layer_thickness, dispersion])

# Create a Pandas DataFrame to store the dispersion values
df = pd.DataFrame(dispersion_values, columns=['Size (nm)', 'Layer Thickness (nm)', 'Dispersion'])

# Print the DataFrame to the console
print(df)
table_string = df.to_string(index=False)
with open('table.txt', 'w') as f:
    f.write(table_string)
df.to_csv('nanoparticle_dispersion.csv', index=False)

# Define the number of atoms in the nanoparticle as a function of size
# (this example assumes a face-centered cubic (FCC) crystal structure)
n_atoms = (4/3) * np.pi * (sizes / 2)**3 * 4 + sizes**3

# Create a scatter plot of the dispersion values versus the number of atoms
fig, ax = plt.subplots()
for layer_thickness in layer_thicknesses:
    data = df[df['Layer Thickness (nm)'] == layer_thickness]
    ax.plot(n_atoms, data['Dispersion'], label=f'{layer_thickness} nm')
ax.set_xlabel('Number of Atoms in the Cluster (n)')
ax.set_ylabel('Dispersion')
ax.set_xlim(0, 1e6) # set the x-axis limits
ax.set_ylim(0, 2) # set the y-axis limits
ax.legend()

plt.savefig('nanoparticle_dispersion.png', dpi=300, bbox_inches='tight')
plt.show()
