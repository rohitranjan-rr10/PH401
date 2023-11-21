import streamlit as st
import pandas as pd

st.set_page_config(
	page_title = "PH 401",
	page_icon="favicon.ico"
)

st.header("Question 1")

st.title("Nanoparticle Characteristics")

def calculate_cuboctahedral_total(layer):
	return int((10 * (layer ** 3) + 15 * (layer ** 2) + 11 * layer + 3) / 3)

def calculate_cuboctahedral_surface(layer):
	return int(10 * (layer ** 2) + 2)

def calculate_spherical_total(layer):
    return int((10 * (layer ** 3) - 15 * (layer ** 2) + 11 * layer - 3) / 3)

def calculate_spherical_surface(layer):
   	return int(10 * (layer ** 2) - 20 * layer + 12)

chosen_shape = st.radio("Select nanoparticle shape:",('Cuboctahedral', 'Spherical'))

if (chosen_shape == 'Cuboctahedral'):
    st.success("Cuboctahedral")
else:
    st.success("Spherical")

chosen_application = st.selectbox("Select an application:",('Optical', 'Electrical', 'Magnetic', 'Strength', 'None'), 4)

if (chosen_application == 'Optical'):
    st.error("Optical")
elif (chosen_application == 'Electrical'):
	st.error("Electrical")
elif (chosen_application == 'Magnetic'):
	st.error("Magnetic")
elif (chosen_application == 'Strength'):
	st.error("Strength")
else:
    st.error("None")

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

size_values = st.slider('Specify size limits for nanoparticle: (in nm)', min_size, max_size, (min_size, 50))

particle_sizes = [i for i in range(size_values[0], size_values[1]+1)]

surface_atoms_percentages = []
bulk_atoms_percentages = []
particle_data = []

if(chosen_shape=='Cuboctahedral'):
	particle_data = [[i,int(calculate_cuboctahedral_total(i)-calculate_cuboctahedral_surface(i)),calculate_cuboctahedral_surface(i), calculate_cuboctahedral_total(i)] for i in particle_sizes]
	surface_atoms_percentages = [(calculate_cuboctahedral_surface(k)/calculate_cuboctahedral_total(k))*100 for k in particle_sizes]
	bulk_atoms_percentages = [(1-(calculate_cuboctahedral_surface(k)/calculate_cuboctahedral_total(k)))*100 for k in particle_sizes]
elif(chosen_shape=='Spherical'):
	particle_data = [[i,int(calculate_spherical_total(i)-calculate_spherical_surface(i)),calculate_spherical_surface(i), calculate_spherical_total(i)] for i in particle_sizes]
	surface_atoms_percentages = [(calculate_spherical_surface(k)/calculate_spherical_total(k))*100 for k in particle_sizes]
	bulk_atoms_percentages = [(1-(calculate_spherical_surface(k)/calculate_spherical_total(k)))*100 for k in particle_sizes]

percentages_data = [[surface_atoms_percentages[i], bulk_atoms_percentages[i]] for i in range(len(particle_sizes))]
ratios_data = [bulk_atoms_percentages[i]/surface_atoms_percentages[i]*100 for i in range(len(particle_sizes))]

particles_df = pd.DataFrame(particle_data[:5], columns = ['Particle Size','Bulk Atoms', 'Surface Atoms', 'Total Atoms'])
st.table(particles_df)

chart_data = pd.DataFrame(percentages_data, columns=['Surface Atoms', 'Bulk Atoms'])
ratio_data = pd.DataFrame(ratios_data)

if st.button('Visualize Data'):
	st.write("% of Bulk and Surface Atoms vs. Particle Size")
	st.line_chart(chart_data)
	st.write("Ratio of Bulk/Surface Atoms vs. Particle Size")
	st.line_chart(ratio_data)