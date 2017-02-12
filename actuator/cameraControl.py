import omegaMotors

class cameraControl:
    def __init__(self, panChannel, tiltChannel, inputRange):
        self.panChannel     = panChannel
        self.tiltChannel    = tiltChannel

        self.inputRange     = inputRange

        # calculate degree change for each input step
        self.step   = float(inputRange)/180.0

        # instantiate a Servo object for both pan and tilt
        # TODO: panServo = omegaMotors.servo(self.panChannel, omegaMotors.SERVO_MIN_PULSE, omegaMotors.SERVO_MAX_PULSE)
        # TODO: tiltServo = omegaMotors.servo(self.tiltChannel, omegaMotors.SERVO_MIN_PULSE, omegaMotors.SERVO_MAX_PULSE)

    def move(self, panValue, tiltValue):
        print "Setting pan servo to ", self.calculateAngle(panValue)
        # TODO: set panServo.setAngle(self.calculateAngle(panValue))
        print "Setting tilt servo to ", self.calculateAngle(tiltValue)
        # TODO: set tiltServo.setAngle(self.calculateAngle(tiltValue))

    def calculateAngle(self, inputValue):
        angle = int(round(float(inputValue)/self.step))
        return angle
