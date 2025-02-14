import motor_pair
import color_sensor
import runloop
from hub import port

P_GAIN = 0.5
I_GAIN = 0.001
D_GAIN = 0.3
integral = 0
last_error = 0


async def pid_line_follow():
    global integral, last_error
    motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)

    while True:
        error = 50 - color_sensor.reflection(port.E)
        integral += error
        derivative = error - last_error
        correction = (P_GAIN * error) + (I_GAIN * integral) + \
            (D_GAIN * derivative)
        motor_pair.move(motor_pair.PAIR_1, int(correction), velocity=300)
        last_error = error
        await runloop.sleep_ms(10)


async def main():
    await pid_line_follow()

runloop.run(main())
