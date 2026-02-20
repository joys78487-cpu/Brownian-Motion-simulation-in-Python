# 🔬 Brownian Motion Simulation in Python

A computational simulation of Brownian Motion demonstrating temperature-dependent molecular dynamics using NumPy, Matplotlib, and Seaborn.

This project visualizes how microscopic particle motion emerges from probabilistic velocity distributions and how temperature influences kinetic energy.

---

## 📌 Overview

This simulation models 200 gas particles moving randomly inside a 2D square container.

The system demonstrates:

- Random particle motion (Brownian motion)
- Temperature-controlled velocity scaling
- Elastic wall collisions
- Real-time animation
- Energy-based color visualization

The project connects kinetic theory of gases with computational modeling and scientific visualization.

---

## 🧠 Scientific Background

Brownian Motion describes the random movement of particles suspended in a medium due to molecular collisions.

From kinetic theory:

Average Kinetic Energy ∝ Temperature  
KE = ½mv²  

As temperature increases:
- Velocity magnitude increases
- Average kinetic energy increases
- Particles move faster

In this simulation, velocity is initialized using a Gaussian distribution scaled by √T to reflect this proportionality.

---

## ⚙️ How the Simulation Works

### 1️⃣ Initialization
- Generate random particle positions inside a 2D box.
- Assign random velocities using NumPy’s normal distribution.
- Scale velocity magnitude according to temperature.

### 2️⃣ Motion Update

Position = Position + Velocity × dt

### 3️⃣ Boundary Collision
If a particle hits a wall:
- The corresponding velocity component reverses.
- This simulates elastic reflection.

### 4️⃣ Speed & Energy Visualization
- Speed is calculated using Euclidean norm:

  speed = √(vx² + vy²)

- Speeds are normalized.
- Seaborn’s `coolwarm` colormap is applied:
  - 🔵 Blue → Low kinetic energy  
  - 🔴 Red → High kinetic energy  

### 5️⃣ Animation
Matplotlib’s `FuncAnimation` continuously updates particle positions and saves the output as a GIF.

---

## 🛠 Technologies Used

- Python  
- NumPy — numerical computation & vector operations  
- Matplotlib — plotting & animation  
- Seaborn — energy-based color mapping  

---

## 🚀 Installation & Usage

### Clone the repository

git clone https://github.com/your-username/brownian-motion-simulation.git  
cd brownian-motion-simulation  

### Install dependencies

pip install numpy matplotlib seaborn  

### Run the simulation

python Code.py  

The animation will display and a `simulation.gif` file will be generated.

---

## 📊 Adjustable Parameters

Inside the script, you can modify:

- `N` → number of particles  
- `temperature` → controls velocity magnitude  
- `box_size` → container dimensions  
- `dt` → time step  

Increasing temperature results in faster particle motion and stronger red coloration.

---

## 📈 Learning Outcomes

- Applied physics concepts through computational modeling  
- Built real-time animation systems  
- Implemented vector-based motion updates  
- Connected probabilistic modeling with visual analytics  
- Strengthened scientific programming skills  

---

## ⚠️ Limitations

- 2D model (real systems are 3D)
- No inter-particle collisions
- Assumes ideal gas behavior
- Simplified elastic boundary reflection

---

## 🔮 Future Improvements

- Add inter-particle collision detection
- Extend to 3D simulation
- Add pressure calculation
- Plot temperature vs average kinetic energy graph
- Introduce Maxwell–Boltzmann velocity distribution visualization
- Add GUI controls for live parameter adjustment

---

## 🎯 Conclusion

This project demonstrates how theoretical physics concepts can be translated into interactive computational models.

It highlights the power of Python’s scientific ecosystem in simulating real-world physical phenomena and visualizing stochastic systems.
