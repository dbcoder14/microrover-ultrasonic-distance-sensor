let distance = 0
basic.forever(function () {
    distance = Rover.Ultrasonic()
    Rover.setALLRGB(Rover.hsl(Math.constrain(distance, 0, 240), 99, 50))
    if (distance >= 15) {
        Rover.Move(100)
    } else {
        Rover.MotorRunDual(-100, 100)
    }
})
