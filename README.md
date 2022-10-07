# SwitchBot_Thermometer
Collect data from [SwitchBot MeterTH S1](https://switch-bot.com/products/switchbot-meter) with Windows Powershell (Python, Bleak, BT 4.0 BLE)\
*SwitchBot Thermometer and Hygrometer (FCC ID : 2AKXB-METERTH1)*

## Requirements (Windows)
- Bluetooth Adaptater 4.0 BLE or USB BT Dongle 4.0 (BLE : Bluetooth Low Energy)
- [Pyhton 3](https://www.python.org/downloads/release/python-3107)
- [Bleak](https://github.com/hbldh/bleak)


## Installation (Powershell)
```powershell
# Pyhton 3
wget "https://www.python.org/ftp/python/3.10.7/python-3.10.7-amd64.exe" -OutFile ".\python-3.10.7-amd64.exe"
.\python-3.10.7-amd64.exe

# Bleak
pip install bleak

# SwitchBot_Thermometer
cd "$env:LOCALAPPDATA\Programs\Python\Python310\Lib\site-packages\bleak\"
wget "https://raw.githubusercontent.com/cesar93600/SwitchBot_Thermometer/main/SwitchBot.py" -OutFile ".\SwitchBot.py"

# Activate your Bluetooth before execution Script
py -3 ".\SwitchBot.py"
```


## Usage (Powershell)
```powershell

$SwitchBot = $(py -3 ".\SwitchBot.py")
# JSON Output : {'Meter': 'SwitchBot MeterTH S1', 'Mac': 'EA:73:76:7F:55:2C', 'Temperature': 20.1, 'Humidity': 55, 'Battery': 100}

# Convert to Object
$SwitchBot = ConvertFrom-Json($SwitchBot)

# Get Object Properties
$SwitchBot.Meter
# Output : SwitchBot MeterTH S1
```

## Sources
- [Linux / Raspberry Pi - Version](https://linuxtut.com/en/749678e1fe0e73cf18e6) (Code used for adaptation)
- [BleakScanner](https://bleak.readthedocs.io/en/latest/api/scanner.html?highlight=scan#starting-and-stopping) (Bleak documentation)
