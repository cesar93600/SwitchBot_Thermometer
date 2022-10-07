# -*- coding: utf-8 -*-
import asyncio
import struct
from bleak import BleakScanner
mac = 'EA:73:76:7F:55:2C'
uuid = '00000d00-0000-1000-8000-00805f9b34fb'
result = None
async def main():
    stop_event = asyncio.Event()
    def callback(device, advertising_data):
        if mac == device.address:
            if advertising_data.service_data:
                valueBinary = advertising_data.service_data[uuid]
                batt = valueBinary[2] & 0b01111111
                isTemperatureAboveFreezing = valueBinary[4] & 0b10000000
                temp = ( valueBinary[3] & 0b00001111 ) / 10 + ( valueBinary[4] & 0b01111111 )
                if not isTemperatureAboveFreezing:
                    temp = -temp
                humid = valueBinary[5] & 0b01111111
                result = {
                    'Meter': 'SwitchBot MeterTH S1',
                    'Mac': mac,
                    'Temperature': temp,
                    'Humidity': humid,
                    'Battery': batt
                }
                print(result)
                stop_event.set()
        pass
    async with BleakScanner(callback) as scanner:
        ...
        await stop_event.wait()
    ...
asyncio.run(main())
