distance = 0

def on_forever():
    global distance
    distance = Rover.ultrasonic()
    Rover.set_allrgb(Rover.hsl(Math.constrain(distance, 0, 240), 99, 50))
    if distance >= 15:
        Rover.move(100)
    else:
        Rover.motor_run_dual(-100, 100)
basic.forever(on_forever)
