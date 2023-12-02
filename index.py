# Rohit Ranjan
# 2001CS56
# rohit_2001cs56@iitp.ac.in

'''
	Question 1: Write a computer program to deduce the total number of atoms and surface atoms 
	for different shells of cuboctahedral/spherical shape. Plot % of atoms in bulk/surface versus 
	particle size. The user should get ideas to generate the thickness or size of nanoparticles 
	for a particular application (optical/electrical/magnetic/strength).
'''

# Import necessary libraries
import streamlit as st
import pandas as pd

# Set page configuration, including title and icon
st.set_page_config(
	page_title = "PH 401",
	page_icon="favicon.ico"
)

# Display header and title for the application
st.header("Question 1")
st.title("Nanoparticle Characteristics")

# Define functions to calculate cuboctahedral and spherical nanoparticle characteristics
def calculate_cuboctahedral_total(layer):
	return int((10 * (layer ** 3) + 15 * (layer ** 2) + 11 * layer + 3) / 3)

def calculate_cuboctahedral_surface(layer):
	return int(10 * (layer ** 2) + 2)

def calculate_spherical_total(layer):
    return int((10 * (layer ** 3) - 15 * (layer ** 2) + 11 * layer - 3) / 3)

def calculate_spherical_surface(layer):
   	return int(10 * (layer ** 2) - 20 * layer + 12)

# Radio button to select nanoparticle shape
chosen_shape = st.radio("Select nanoparticle shape:",('Cuboctahedral', 'Spherical'))

# Display success message based on the selected nanoparticle shape
if (chosen_shape == 'Cuboctahedral'):
    st.success("You selected: Cuboctahedral")
else:
    st.success("You selected: Spherical")

# Dropdown to select an application for the nanoparticle
chosen_application = st.selectbox("Select an application:",('Optical', 'Electrical', 'Magnetic', 'Strength', 'None'), 4)

# Display success message based on the selected application
if (chosen_application == 'Optical'):
    st.error("You selected: Optical")
elif (chosen_application == 'Electrical'):
	st.error("You selected: Electrical")
elif (chosen_application == 'Magnetic'):
	st.error("You selected: Magnetic")
elif (chosen_application == 'Strength'):
	st.error("You selected: Strength")
else:
    st.error("You selected: None")

# Set size limits based on the selected application
global max_size, min_size
if chosen_application == 'Optical':
	min_size=40 
	max_size=100
elif chosen_application == 'Electrical':
	min_size=10 
	max_size=20
elif chosen_application == 'Magnetic':
	min_size=1
	max_size=10
elif chosen_application == 'Strength':
	min_size=1
	max_size=50
else:
	min_size=1
	max_size=100

# Slider to specify size limits for the nanoparticle
size_values = st.slider('Specify size limits for nanoparticle: (in nm)', min_size, max_size, (min_size, 50))

# Generate a list of particle sizes based on the slider values
particle_sizes = [i for i in range(size_values[0], size_values[1]+1)]

# Initialize lists to store nanoparticle data
surface_atoms_percentages = []
bulk_atoms_percentages = []
particle_data = []

# Calculate nanoparticle characteristics based on the selected shape
if(chosen_shape=='Cuboctahedral'):
	particle_data = [[i,int(calculate_cuboctahedral_total(i)-calculate_cuboctahedral_surface(i)),calculate_cuboctahedral_surface(i), calculate_cuboctahedral_total(i)] for i in particle_sizes]
	surface_atoms_percentages = [(calculate_cuboctahedral_surface(k)/calculate_cuboctahedral_total(k))*100 for k in particle_sizes]
	bulk_atoms_percentages = [(1-(calculate_cuboctahedral_surface(k)/calculate_cuboctahedral_total(k)))*100 for k in particle_sizes]
elif(chosen_shape=='Spherical'):
	particle_data = [[i,int(calculate_spherical_total(i)-calculate_spherical_surface(i)),calculate_spherical_surface(i), calculate_spherical_total(i)] for i in particle_sizes]
	surface_atoms_percentages = [(calculate_spherical_surface(k)/calculate_spherical_total(k))*100 for k in particle_sizes]
	bulk_atoms_percentages = [(1-(calculate_spherical_surface(k)/calculate_spherical_total(k)))*100 for k in particle_sizes]

# Generate percentage and ratio data for visualization
percentages_data = [[surface_atoms_percentages[i], bulk_atoms_percentages[i]] for i in range(len(particle_sizes))]
ratios_data = [bulk_atoms_percentages[i]/surface_atoms_percentages[i]*100 for i in range(len(particle_sizes))]

# Create a DataFrame for the first five particle sizes and display it as a table
particles_df = pd.DataFrame(particle_data[:5], columns = ['Particle Size','Bulk Atoms', 'Surface Atoms', 'Total Atoms'])
st.table(particles_df)

# Create DataFrames for percentage and ratio data for visualization
chart_data = pd.DataFrame(percentages_data, columns=['Surface Atoms', 'Bulk Atoms'])
ratio_data = pd.DataFrame(ratios_data)

# Button to trigger data visualization
if st.button('Visualize Data'):
	st.write("% of Bulk and Surface Atoms vs. Particle Size")
	st.line_chart(chart_data)
	st.write("Ratio of Bulk/Surface Atoms vs. Particle Size")
	st.line_chart(ratio_data)