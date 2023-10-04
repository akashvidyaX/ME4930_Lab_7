# Importing the necessary library
import numpy as np

# Set the print options to suppress scientific notation
np.set_printoptions(suppress=True)

# Given angles in degrees, converting them to radians
theta_1 = np.deg2rad(90)
theta_2 = np.deg2rad(-45)
theta_3 = np.deg2rad(0)
theta_4 = np.deg2rad(45)

# Define the skew-symmetric matrix function
def skew_symmetric(v):
    return np.array([
        [0, -v[2], v[1]],
        [v[2], 0, -v[0]],
        [-v[1], v[0], 0]
    ])

# Unit vectors for y and z
y_unit_vector = np.array([0, 1, 0])
z_unit_vector = np.array([0, 0, 1])

# Calculate the skew-symmetric matrices for y and z
y_hat_bracket = skew_symmetric(y_unit_vector)
z_hat_bracket = skew_symmetric(z_unit_vector)

# Rodrigues' formula to compute the rotation matrices
def rodrigues_formula(theta, hat_bracket):
    I = np.identity(3)
    return I + np.sin(theta) * hat_bracket + (1 - np.cos(theta)) * np.dot(hat_bracket, hat_bracket)

# Using Rodrigue's formula to find each exponential function
e_z_hat_bracket_theta_1 = rodrigues_formula(theta_1, z_hat_bracket)
e_y_hat_bracket_theta_2 = rodrigues_formula(theta_2, y_hat_bracket)
e_y_hat_bracket_theta_3 = rodrigues_formula(theta_3, y_hat_bracket)
e_y_hat_bracket_theta_4 = rodrigues_formula(theta_4, y_hat_bracket)

# Calculate the final rotation matrix product of exponentials 
R = e_z_hat_bracket_theta_1 @ e_y_hat_bracket_theta_2 @ e_y_hat_bracket_theta_3 @ e_y_hat_bracket_theta_4

# Print the final rotation matrix
print(R)
