# 📖 Understanding PID Control in LEGO SPIKE Prime

This document explains **PID control theory** and how it applies to **robotics and LEGO SPIKE Prime**.

## **1️⃣ What is PID Control?**

PID (Proportional-Integral-Derivative) is a **control loop system** used in robotics to **adjust movement based on sensor feedback**. It helps robots:

- Stay on **a line accurately**.
- Maintain **smooth, stable movement**.
- Adjust speed dynamically based on **error correction**.

## **2️⃣ Breakdown of PID Components**

| Component            | Function                  | Effect                                         |
| -------------------- | ------------------------- | ---------------------------------------------- |
| **P (Proportional)** | Reacts to current error   | Higher P = Faster correction but can overshoot |
| **I (Integral)**     | Corrects cumulative error | Helps with drift correction                    |
| **D (Derivative)**   | Predicts future errors    | Reduces oscillations                           |

## **3️⃣ How PID is Used in Line Following**

A **color sensor** detects the edge of a black line. The PID controller:

1. **Reads sensor data (reflection value).**
2. **Computes the error** (difference from target reflection).
3. **Adjusts motor speed** to correct the error.

Formula for PID correction:

$$Correction = (P * error) + (I * integral of error) + (D * rate of change of error)$$
