# SPIKE Prime Adaptive PID Control

This repository contains an **adaptive PID controller** for **LEGO SPIKE Prime robots**, used in **FIRST LEGO League (FLL)**.

## 📂 Project Structure

| File                                | Description                                    |
| ----------------------------------- | ---------------------------------------------- |
| `line_following_pid.py`             | **Main PID script** for line following         |
| `auto_tuning_line_following_PID.py` | **Auto-tuning version** for better corrections |
| `plot_pid.py`                       | **Graphs PID values** to analyze performance   |
| `pid_log.txt`                       | Stores **real-time PID data** from the robot   |
| `diagrams/`                         | Flowcharts and explanations of PID behavior    |
| `README.md`                         | Project documentation                          |
| `LICENSE`                           | Open-source license                            |

## 🚀 Learn More

- **[Glossary](docs/GLOSSARY.md)**: Learn about key terms like **encoders, feedback loops, and auto-tuning**.
- **[PID Theory](docs/PID_THEORY.md)**: Understand **how PID control works** and how to tune it.

## 🚀 Getting Started

1. **Upload `line_following_pid.py`** to your SPIKE Prime hub.
2. **Run the script** and let the robot follow the line.
3. **Retrieve `pid_log.txt`** and analyze it with `plot_pid.py`.

## 📊 PID Data Analysis

Run:

```sh
python plot_pid.py
```

This will generate **graphs** of **error, correction, and PID values** over time.

## 🔧 Adjusting PID Settings

Edit these values in `line_following_pid.py`:

```python
P_BASE = 0.5  # Proportional gain (higher = faster response)
I_BASE = 0.001  # Integral gain (higher = fixes long-term drift)
D_BASE = 0.3  # Derivative gain (higher = smooths movement)
```

Tune them based on **logged performance data**.

## 📜 License

This project is licensed under the **MIT License**.
