# imports
import json
import subprocess
from lock_check import serial_number


def hardware_info(cmds, keyword=None):
    found_keyword = None
    # Run the system_profiler command and get the output as a string
    try:
        hardware_info = subprocess.run(
            cmds, capture_output=True, text=True).stdout
        if keyword != None:
            # Search the output for the keyword line and extract the value
            for line in hardware_info.splitlines():
                if keyword in line:
                    found_keyword = line.strip()
        else:
            return hardware_info
    except Exception as e:
        print('exception:', e)

    return found_keyword
    ###


class Battery:
    def cycle_count():
        return int(hardware_info(['system_profiler', 'SPPowerDataType'], 'Cycle Count').split(":")[1])
        ###

    def designed_capacity():
        return int(hardware_info(
            ['ioreg', '-w0', '-l'], 'DesignCapacity').split('=')[1])
        ###

    def full_charge_capacity():
        return int(hardware_info(
            ['system_profiler', 'SPPowerDataType'], 'Full Charge Capacity').split(":")[1])
        ###

    def percent_of_designed_capacity():
        return round(float(Battery.full_charge_capacity()/Battery.designed_capacity()*100), 2)
        ###
    ###


def bios_info():
    return hardware_info(['system_profiler', 'SPHardwareDataType'], 'System Firmware Version').split(' ')[3]
    ###


class Cpu:
    def full_name():
        return hardware_info(['sysctl', '-n', 'machdep.cpu.brand_string']).strip()
        ###

    def manufacturer():
        return hardware_info(['system_profiler', 'SPHardwareDataType'])
        ###

    def model():
        return None
        ###

    def type():
        return None
        ###

    def speed():
        return hardware_info(
            ['system_profiler', 'SPHardwareDataType'], 'Processor Speed').split(':')[1].strip()
        ###

    def cores():
        return hardware_info(['system_profiler', 'SPHardwareDataType'], 'Total Number of Cores').split(':')[1].strip()
        ###


def gpu_info():
    return hardware_info(['system_profiler', 'SPDisplaysDataType'], 'Chipset Model').split(':')[1].strip()
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
        return hardware_info(['system_profiler', 'SPHardwareDataType'], 'Memory').split(':')[1].strip()

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
            'Bluetooth': None,
            'Card Reader': None,
            'ChassisType': None,
            'CPU': {
                'FullName': Cpu.full_name(),
                'Manufacturer': None,
                'Model': None,
                'Type': None,
                'Speed': Cpu.speed(),
                'Cores': Cpu.cores(),
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
            'Optic Type': None,
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


hardware_info(['systemctl'])
