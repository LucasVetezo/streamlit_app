#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 12:18:24 2025

@author: Lucas Vetezo

"""

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Title of the app
st.title("Research on Linear Hydraulic Fracture Propagation")

# Introduction
st.header("Overview")
st.write("""
This research focuses on understanding the propagation of linear hydraulic fractures in subsurface environments. 
Hydraulic fracturing is a critical process in enhancing the extraction of oil, gas, and geothermal energy. 
The study investigates the factors influencing fracture growth, such as fluid pressure, rock properties, and stress fields.
""")

# Key Findings
st.header("Key Findings")
st.write("""
1. **Fracture Length and Width**: The fracture length increases with higher fluid injection rates, while the width is influenced by the rock's elastic properties.
2. **Pressure Distribution**: The pressure distribution within the fracture is non-uniform, with higher pressures near the injection point.
3. **Stress Anisotropy**: The orientation of the fracture is strongly influenced by the in-situ stress anisotropy.
4. **Fluid Viscosity**: Higher fluid viscosity leads to slower fracture propagation but results in wider fractures.
""")

# Trends and Results
st.header("Trends and Results")
st.write("""
The following trends were observed from the research:
- **Fracture Propagation Rate**: The rate of fracture propagation is proportional to the square root of the injection rate.
- **Rock Brittleness**: Brittle rocks tend to produce longer and narrower fractures compared to ductile rocks.
- **Environmental Impact**: The study highlights the importance of minimizing fluid leakage to reduce environmental risks.
""")

# Visualization of Results
st.header("Visualization of Results")

# Example: Fracture Length vs. Injection Rate
st.subheader("Fracture Length vs. Injection Rate")
injection_rates = np.linspace(1, 10, 100)  # Injection rates in m^3/s
fracture_lengths = 2 * np.sqrt(injection_rates)  # Example relationship

fig, ax = plt.subplots()
ax.plot(injection_rates, fracture_lengths, label="Fracture Length")
ax.set_xlabel("Injection Rate (m³/s)")
ax.set_ylabel("Fracture Length (m)")
ax.set_title("Fracture Length as a Function of Injection Rate")
ax.legend()
st.pyplot(fig)

# Example: Pressure Distribution Along Fracture
st.subheader("Pressure Distribution Along Fracture")
fracture_distance = np.linspace(0, 10, 100)  # Distance along fracture in meters
pressure = 10 * np.exp(-0.2 * fracture_distance)  # Example pressure decay

fig, ax = plt.subplots()
ax.plot(fracture_distance, pressure, label="Pressure")
ax.set_xlabel("Distance Along Fracture (m)")
ax.set_ylabel("Pressure (MPa)")
ax.set_title("Pressure Distribution Along the Fracture")
ax.legend()
st.pyplot(fig)

# Conclusion
st.header("Conclusion")
st.write("""
This research provides valuable insights into the mechanics of linear hydraulic fracture propagation. 
The findings can be applied to optimize hydraulic fracturing operations, improve energy extraction efficiency, and mitigate environmental impacts.
""")

# Contact Information
st.sidebar.header("Contact Information")
st.sidebar.write("For more information, please contact:")
st.sidebar.write("Researcher Name: Lucas Vetezo")
st.sidebar.write("Email: thami94vee@gmail.com")
st.sidebar.write("Institution: Wits University")

