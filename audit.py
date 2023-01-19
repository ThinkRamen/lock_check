# imports
import json
import subprocess
import re
from lock_check import serial_number


def hardware_info(cmds, keyword=None):
    found_keyword = None
    # Run the system_profiler command and get the output as a string
    hardware_info = subprocess.run(cmds, capture_output=True, text=True).stdout
    if keyword != None:
        # Search the output for the keyword line and extract the value
        for line in hardware_info.splitlines():
            if keyword in line:
                found_keyword = line.strip()
    else:
        return hardware_info
    return found_keyword
    ###


class Battery:
    def cycle_count():
        return int(hardware_info(['system_profiler', 'SPPowerDataType'], 'Cycle Count').split(":")[1])

    def designed_capacity():
        return int(hardware_info(
            ['ioreg', '-w0', '-l'], 'DesignCapacity').split('=')[1])
        ###

    def full_charge_capacity():
        return int(hardware_info(
            ['system_profiler', 'SPPowerDataType'], 'Full Charge Capacity').split(":")[1])
        ###

    def percent_of_designed_capacity():
        return int(Battery.full_charge_capacity()/Battery.designed_capacity()*100)
        ###


def bios_info():
    # return hardware_info(['system_profiler', 'SPSoftwareDataType'])
    return None


def bluetooth_info():
    return None
    ###


def card_reader_info():
    return None
    ###


class Cpu:
    def count():
        return None
        ###

    def manufacturer():
        return None
        ###

    def sku():
        return None
        ###

    def speed():
        return None
        ###

    def type():
        return None
        ###


def gpu_info():
    return None
    ###


class Hdd:
    def model():
        return None

    def serial():
        return None

    def size():
        return None

    def type():
        return None
        ###

    def manufacturer():
        return None


def manufacturer_info():
    return hardware_info(['system_profiler', 'SPHardwareDataType'], 'Manufacturer')


def model_info():
    return hardware_info(['sysctl', '-n', 'hw.model']).strip()


class Ram():
    def count():
        return None
        ###

    def size():
        return None
        ###

    def total_size():
        ram_info = hardware_info(['system_profiler', 'SPMemoryDataType'])

    def type():
        return None
        ###


class Peripherals():
    def screen_size():
        return None

    def webcam():
        return None

    def wifi():
        return None


def audit_json():
    """
    transforms funtions info to a dictionary
    """
    audit_info = {
        'Serial': serial_number(),
        'Hardware': {
            'Battery': {
                'CycleCount': Battery.cycle_count(),
                'DesignedCapacity': Battery.designed_capacity(),
                'FullChargeCapacity': Battery.full_charge_capacity(),
                'PercentOfDesignedCapacity': Battery.percent_of_designed_capacity(),
            },
            "Bios": bios_info(),
            'Bluetooth': bluetooth_info(),
            'Card Reader': card_reader_info(),
            'ChassisType': '',
            'CPU': {
                'id': '',
                'FullName': '',
                'Manufacturer': '',
                'Model': '',
                'Type': '',
                'Speed': '',
                'Cores': '',

            },
            'GraphicsCard': gpu_info(),
            'HardDrive': {
                'Manufacturer': Hdd.manufacturer(),
                'Model': Hdd.model(),
                'Serial': Hdd.serial(),
                'Type': Hdd.type(),
            },
            'Manufacturer': manufacturer_info(),
            'Model': model_info(),
            # MOTHERBOARD
            'Optic Type': '',
            'Ram Count': Ram.count(),
            'Ram Size': Ram.size(),
            'Ram Total Size': Ram.total_size(),
            'Ram Type': Ram.type(),
            'Screen Size': Peripherals.screen_size(),
            'Webcam': Peripherals.webcam(),
            'Wifi': Peripherals.wifi(),
        }
    }
    json_info = json.dumps(audit_info, indent=4)
    return json_info


print(audit_json())
