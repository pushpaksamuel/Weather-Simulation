# 🌦️ Weather Simulation Using Markov Chains

This project implements a **weather simulation model** using a **Markov chain with holding times**.  
It was developed as part of the Python programming course at **Blekinge Institute of Technology (BTH)**.

The simulation models transitions between four weather states:

- ☀️ **sunny**
- ☁️ **cloudy**
- 🌧️ **rainy**
- ❄️ **snowy**

Each state has:
- A **transition probability distribution** for moving to the next state.
- A **holding time**, defining how long the state persists before transitioning.

---

## 🚀 Features

### ✔️ Markov Chain Weather Model  
The `WeatherSimulation` class:
- Validates probability distributions (each row must sum to 1.0).
- Tracks the current state and remaining holding time.
- Performs probabilistic state transitions.
- Supports generator-style iteration through states.

### ✔️ Simulation Engine  
Simulate any number of days and obtain:
- Total hours spent in each weather state.
- Percentage distribution of weather conditions.

### ✔️ Built-In Testing Functions  
The test script includes:
- Probability validation  
- Holding-time correctness checks  
- Long-run distribution testing  
- Error-handling verification  
- A final result: `1` (pass) or `0` (fail)

---

## 📁 Project Structure
weather-simulation/
│
├── assignment.py       # Main simulation file (WeatherSimulation class)
├── test.py              # Test runner that validates transitions, holding times, and simulation accuracy
└── README.md            # Documentation for the project

