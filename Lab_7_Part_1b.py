import sympy as sp

# Define symbolic variables
t1, t2, t3, t4 = sp.symbols('t1 t2 t3 t4')

# Define the skew-symmetric matrices
z_hat_bracket = sp.Matrix([[0, -1, 0],
                           [1, 0, 0],
                           [0, 0, 0]])

y_hat_bracket = sp.Matrix([[0, 0, 1],
                           [0, 0, 0],
                           [-1, 0, 0]])

# Calculate e_bracket_z_t1
e_bracket_z_t1 = sp.eye(3) + sp.sin(t1) * z_hat_bracket + (1 - sp.cos(t1)) * z_hat_bracket**2

# Calculate e_bracket_y_t2
e_bracket_y_t2 = sp.eye(3) + sp.sin(t2) * y_hat_bracket + (1 - sp.cos(t2)) * y_hat_bracket**2

# Calculate e_bracket_y_t3
e_bracket_y_t3 = sp.eye(3) + sp.sin(t3) * y_hat_bracket + (1 - sp.cos(t3)) * y_hat_bracket**2

# Calculate e_bracket_y_t4
e_bracket_y_t4 = sp.eye(3) + sp.sin(t4) * y_hat_bracket + (1 - sp.cos(t4)) * y_hat_bracket**2

# Calculate the final result
result = e_bracket_z_t1 @ e_bracket_y_t2 @ e_bracket_y_t3 @ e_bracket_y_t4

# Simplify the result
simplified_result = sp.simplify(result)

# Display the simplified result
simplified_result_display = simplified_result

# Define the desired orientation matrix
R_desired = sp.Matrix([[1, 0, 0],
                       [0, 0, -1],
                       [0, -1, 0]])

# Create equations by equating the elements of R and R_desired
equations = [sp.Eq(simplified_result[i, j], R_desired[i, j]) for i in range(3) for j in range(3)]

# Solve the system of equations for the joint angles
solutions = sp.solve(equations, (t1, t2, t3, t4), dict=True)

# Display the solutions
print(simplified_result_display)
print(solutions)
