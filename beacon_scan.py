from bluetooth.ble import BeaconService
import time
import backend

class Beacon(object):
    
    def __init__(self, data, address):
        self._uuid = data[0]
        self._major = data[1]
        self._minor = data[2]
        self._power = data[3]
        self._rssi = data[4]
        self._address = address
        
    def __str__(self):
        ret = "Beacon: address:{ADDR} uuid:{UUID} major:{MAJOR}"\
                " minor:{MINOR} txpower:{POWER} rssi:{RSSI}"\
                .format(ADDR=self._address, UUID=self._uuid, MAJOR=self._major,
                        MINOR=self._minor, POWER=self._power, RSSI=self._rssi)
        return ret

apiKey = ""
authDomain = ""
databaseURL = ""
storageBucket = ""


service = BeaconService()
backend.startFireBase(apiKey, authDomain, databaseURL, storageBucket)

while True:
    devices = service.scan(1)
    beaconCount = 0
    for address, data in list(devices.items()):
        b = Beacon(data, address)
        if b._uuid[:8] == "11111111":
            print("Beacon {} Beer Temp: {}C Humidity: {}%".format(b._uuid, b._major, b._minor))
            backend.sendData({"uuid":b._uuid, "temp":b._major, "humidity":b._minori})
            beaconCount += 1

    print("Packages Found: {}".format(beaconCount))
    time.sleep(1)
