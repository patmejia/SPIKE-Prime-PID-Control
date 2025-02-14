# Line Following with Adaptive PID  

This script controls a **LEGO SPIKE Prime robot** using an **adaptive PID algorithm** to follow a black line.

## Features  
- Dynamically adjusts **P, I, and D values** for better performance.  
- Uses **real-time sensor feedback** from a color sensor.  
- Can be **fine-tuned based on logged data**.

## How to Use  
1. **Upload this file** to your SPIKE Prime hub.  
2. **Run the script** and watch the robot follow the line.  
3. **Retrieve `pid_log.txt`** for performance analysis.  

## Adjusting PID Values  
Modify the **`P_BASE`, `I_BASE`, and `D_BASE`** values in the script for better results.  

## Why This Works  
- **Proportional (P)** → Controls reaction speed.  
- **Integral (I)** → Fixes small long-term drift.  
- **Derivative (D)** → Prevents overcorrection & stabilizes turns.  
