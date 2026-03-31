# 🚇 KO-NECT OpenEnv

**AI Training Environment for Urban Transport Optimization**

---

## 🧠 Overview

KO-NECT OpenEnv is a **real-world simulation environment** designed to train and evaluate AI agents on **urban transport operations management**.

The environment models the coordination of:

* Metro systems
* Water Metro systems
* Driver allocation
* Incident handling
* Demand fluctuations

It introduces **dynamic uncertainty** through events such as festivals, breakdowns, and weather disruptions, requiring agents to make **adaptive, multi-step decisions**.

---

## 🎯 Motivation

Urban transport systems today operate in **siloed and reactive modes**, leading to:

* Inefficient resource utilization
* Delays during peak demand
* Poor incident response

KO-NECT addresses this by providing a **unified decision-making simulation**, enabling AI agents to learn:

* Resource optimization
* Demand-aware scheduling
* Real-time operational recovery

---

## ⚙️ Environment Design

### 🔁 Core API

The environment follows the **OpenEnv-style interface**:

* `reset()` → Initializes environment state
* `step(action)` → Applies action and returns `(observation, reward, done, info)`
* `state()` → Returns current system state

---

### 📊 Observation Space

| Variable           | Description                                        |
| ------------------ | -------------------------------------------------- |
| `time`             | Simulation timestep                                |
| `active_drivers`   | Number of drivers deployed                         |
| `available_trains` | Number of operational trains                       |
| `pending_issues`   | Unresolved incidents                               |
| `demand_level`     | Transport demand (low/medium/high)                 |
| `delays`           | System delays                                      |
| `event`            | External disruption (festival/rain/breakdown/none) |

---

### 🎮 Action Space

| Action           | Description                       |
| ---------------- | --------------------------------- |
| `assign_drivers` | Allocate additional drivers (0–N) |
| `add_trains`     | Increase train capacity           |
| `resolve_issues` | Handle operational issues         |

---

## 🌪️ Dynamic Simulation Features

### ⏱️ Time-Based Evolution

* Demand changes over time
* System evolves every step

### 🎉 Event Engine

Simulates real-world disruptions:

* **Festival** → sudden demand spike
* **Rain** → moderate delays
* **Breakdown** → reduced capacity + high delays

### ⚖️ Resource Constraints

* Limited drivers and trains
* Over-allocation penalties

### 🚨 Failure Conditions

* Excessive delays terminate episode

---

## 🎯 Reward Function

The reward function provides **dense feedback** across the episode:

### Positive Signals

* Delay reduction
* Issue resolution
* Efficient handling of high demand

### Penalties

* Resource overuse
* Unresolved issues
* Poor handling of disruptions

### Output Range

```
Reward ∈ [0.0, 1.0]
```

---

## 🧪 Tasks & Graders

The environment includes **3 progressively challenging tasks**:

### 🟢 Easy — Delay Stabilization

* Objective: Minimize system delays
* Metric: Delay reduction

---

### 🟡 Medium — Demand Management

* Objective: Handle high demand efficiently
* Metric: Resource utilization vs demand

---

### 🔴 Hard — Full System Optimization

* Objective: Manage delays, issues, and disruptions simultaneously
* Metric: Multi-factor performance score

---

### 📏 Grading

Each task returns:

```
Score ∈ [0.0, 1.0]
```

✔ Deterministic
✔ Reproducible
✔ Increasing difficulty

---

## 🤖 Baseline Agent

A rule-based agent is provided in `inference.py`:

* Responds to demand levels
* Allocates resources dynamically
* Attempts issue resolution

This establishes a **reproducible baseline score** for evaluation.

---

## 🧪 Validation

Run:

```
python validate_env.py
```

This verifies:

* API correctness (`reset`, `step`, `state`)
* Reward bounds (0–1)
* State consistency
* Execution without errors

---

## 🐳 Deployment

The environment is containerized and deployed using Docker.

### Build:

```
docker build -t ko-nect .
```

### Run:

```
docker run ko-nect
```

---

## 🌐 HuggingFace Space

The environment is deployed as a live API:

* `/reset` → Initialize environment
* `/step` → Apply action
* `/state` → Get current state

---

## 🚀 Key Strengths

* ✅ Real-world utility (urban transport optimization)
* ✅ Dynamic, event-driven simulation
* ✅ Multi-objective reward design
* ✅ Progressive task difficulty
* ✅ Scalable to smart city applications

---

## 🔮 Future Extensions

* Integration with real-time transport data APIs
* Reinforcement learning agent training
* Predictive demand forecasting using ML models
* Multi-agent coordination (metro + water metro)

---

## 🏁 Conclusion

KO-NECT OpenEnv provides a **high-fidelity simulation environment** for evaluating AI agents in complex, real-world operational scenarios.

It bridges the gap between **theoretical RL environments** and **practical urban system challenges**, making it valuable for both research and real-world deployment.

---
