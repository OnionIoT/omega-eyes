import omegaMotors

class cameraControl:
    def __init__(self, panChannel, tiltChannel, inputRange):
        self.panChannel     = panChannel
        self.tiltChannel    = tiltChannel

        self.inputRange     = inputRange

        # calculate degree change for each input step
        self.step   = float(inputRange)/180.0

        # instantiate a Servo object for both pan and tilt
        self.panServo = omegaMotors.Servo(self.panChannel, omegaMotors.SERVO_MIN_PULSE, omegaMotors.SERVO_MAX_PULSE)
        self.tiltServo = omegaMotors.Servo(self.tiltChannel, omegaMotors.SERVO_MIN_PULSE, omegaMotors.SERVO_MAX_PULSE)

		# center the servos
		self.panServo.setAngle(90)
		self.tiltServo.setAngle(90)

    def move(self, panValue, tiltValue):
        print "Setting pan servo to ", self.calculateAngle(panValue)
        self.panServo.setAngle(self.calculateAngle(panValue))

		# tilt - invert the measurement
		newTiltValue = self.inputRange - tiltValue
        print "Setting tilt servo to ", self.calculateAngle(newTiltValue)
        self.tiltServo.setAngle(self.calculateAngle(newTiltValue))

    def calculateAngle(self, inputValue):
        angle = int(round(float(inputValue)/self.step))
        return angle
