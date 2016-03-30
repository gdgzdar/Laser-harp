import serial


def parseBools(last_bools, actual_bools):
    for x in range(len(actual_bools)):
        if actual_bools[x] == True and not actual_bools[x] == last_bools[x]:
            print("Port " + str(x) + ': ' + str(actual_bools[x]))


actual_bools = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
last_bools = []
arduino = serial.Serial('/dev/ttyACM1', 9600)
for x in range(10):
    data = arduino.readline()
    print(data)
while True:
    last_bools = actual_bools
    actual_bools = []
    for x in range(len(data) - 2):
        if data[x] == '0':
            actual_bools.append(False)
        else:
            actual_bools.append(True)
    parseBools(last_bools, actual_bools)
    print(data)

