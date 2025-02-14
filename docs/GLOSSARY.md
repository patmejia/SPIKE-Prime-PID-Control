# **SPIKE Prime Robotics & PID Glossary**

This glossary defines key terms related to PID control, robotics, and their technical principles.

---

## **General Robotics Terms**

- **Encoder:** Measures motor rotation in degrees or ticks. Used for precise movement tracking.
- **Gyroscope:** Measures angular velocity and orientation. Used for balancing and heading correction.
- **Actuator:** A motor or mechanism that converts electrical signals into movement.
- **Feedback Loop:** A system where sensor data continuously adjusts motor commands to reach a target state.

---

## **PID Control Terms**

- **PID Control (Proportional-Integral-Derivative):** A method to adjust motor power based on error correction.
- **Error:** The difference between the desired and actual values (e.g., distance from a line).
- **P (Proportional Gain):** Adjusts power proportionally to the error. Higher values react faster but can overshoot.  
  \[
  P\_\text{output} = K_p \times \text{error}
  \]
- **I (Integral Gain):** Corrects cumulative error by summing past deviations. Helps reduce drift but can cause instability.  
  \[
  I\_\text{output} = K_i \times \sum \text{error}
  \]
- **D (Derivative Gain):** Predicts future error by analyzing the rate of change. Reduces overshoot and smooths corrections.  
  \[
  D\_\text{output} = K_d \times \frac{d(\text{error})}{dt}
  \]
- **PID Formula (Combined):**  
  \[
  \text{Correction} = K_p \times \text{error} + K_i \times \sum \text{error} + K_d \times \frac{d(\text{error})}{dt}
  \]

---

## **Adaptive Control Concepts**

- **Auto-Tuning PID:** Adjusts \(K_p, K_i, K_d\) dynamically based on system behavior instead of fixed values.
- **Oscillation:** Repetitive overcorrection due to excessive gain values, causing instability.
- **Deadband:** A predefined error range where no correction is applied to prevent unnecessary minor adjustments.

---

## **FIRST LEGO League (FLL) Terms**

- **Line Following:** A control method where a color sensor detects a boundary (black/white) and uses PID to stay on the edge.
- **Motor Synchronization:** Adjusting power to ensure multiple motors move at the same speed despite mechanical differences.
- **Yaw Correction:** Adjusting motor power based on gyroscope or encoder readings to maintain a straight path.
