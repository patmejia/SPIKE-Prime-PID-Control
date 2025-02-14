import motor_pair
import color_sensor
import runloop
from hub import port

# Base PID values (Auto-adjusted)
P_BASE = 0.5
I_BASE = 0.001
D_BASE = 0.3

# Dynamic PID Adjustment Ranges
MAX_P = 1.2   # Max P for sharp turns
MAX_I = 0.02   # Max I for long steady corrections
MAX_D = 0.5    # Max D to prevent oscillation at high speeds
ERROR_THRESHOLD = 30  # When to increase P

# PID Tracking Variables
integral = 0
last_error = 0


async def pid_line_follow():
    global integral, last_error

    motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)

    while True:
        # Read color sensor reflection
        # Target = 50 (edge of black/white)
        error = 50 - color_sensor.reflection(port.E)

        # Auto-Tuning P-Gain
        if abs(error) > ERROR_THRESHOLD:
            # Increase P for sharp turns
            P = min(MAX_P, P_BASE + 0.02 * abs(error))
        else:
            P = P_BASE  # Use base P for small errors

        # Auto-Tuning I-Gain
        if abs(error) < ERROR_THRESHOLD:  # Use I only when error is small
            integral += error
            I = min(MAX_I, I_BASE + 0.001 * integral)
        else:
            I = 0  # Disable I for large corrections

        # Auto-Tuning D-Gain
        # Increase D at high speeds
        D = min(MAX_D, D_BASE + 0.002 * abs(error))

        # Compute Derivative
        derivative = error - last_error

        # Compute Correction
        correction = (P * error) + (I * integral) + (D * derivative)

        # Apply correction as steering
        motor_pair.move(motor_pair.PAIR_1, int(correction), velocity=300)

        # Store last error for next loop
        last_error = error

        await runloop.sleep_ms(10)  # Update every 10ms


async def main():
    await pid_line_follow()

runloop.run(main())
