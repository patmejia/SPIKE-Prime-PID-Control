# PID Data Visualization  

This script reads `pid_log.txt` and **plots the PID values over time** to help analyze the robot’s performance.  

## Features  
- Displays **error, P, I, D values, and corrections** over time.  
- Helps **fine-tune PID settings** by identifying instability.  

## How to Use  
1. Run the **line following script** to generate `pid_log.txt`.  
2. Copy `pid_log.txt` to your computer.  
3. Run:  
   ```sh
   python plot_pid.py
   ```
4. Adjust PID settings based on the graphs.

## Example Output  
- A **smooth error graph** means **good tuning**.  
- If **P is too high**, the graph will show **oscillations**.  
- If **I is too high**, corrections will **keep increasing** over time.  
