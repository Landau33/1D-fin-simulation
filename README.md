# 1D Fin Steady-State Heat Conduction Simulation

This project simulates the **steady-state temperature distribution on a 1D circular fin** with convection at its surface.  
The fin has temperature-dependent thermal conductivity \(k(T)\), using **two-point linear interpolation**.

This is a simple and clear numerical model suitable for thermal engineering coursework, numerical methods practice, and fin performance analysis.

---

## ✅ Features

- Steady-state 1D heat conduction along a rod/fin  
- Convection at all control volumes  
- Temperature-dependent thermal conductivity using 2 points:  
- Iterative "energy residual balancing" solver  
- Node-by-node temperature update  
- Configurable:
- Number of nodes
- Geometry
- Boundary conditions
- Numerical tolerances
- Matplotlib visualization

---

## ✅ Mathematical Model

The fin is modeled by the energy balance at each control volume:

\[
Q_\text{left} + Q_\text{right} + Q_\text{conv} = 0
\]

where:

- Conduction:
\[
Q_\text{left} = k \cdot \frac{A}{dx} (T_{i-1}-T_i)
\]
\[
Q_\text{right} = k \cdot \frac{A}{dx} (T_{i+1}-T_i)
\]

- Convection:
\[
Q_\text{conv} = h P dx (T_a - T_i)
\]

Thermal conductivity is interpolated from two user-specified points:

\[
k(T) = k_1 + (k_2-k_1)\frac{T - T_1}{T_2-T_1}
\]

---

## ✅ Project Structure
---

## ✅ Installation

Make sure Python 3.8+ is installed.  
Then install dependencies:

```bash
pip install -r requirements.txt
