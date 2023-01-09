# imports
import subprocess
import json
from lock_check import serial_number


def battery_info():
    return


def bluetooth_info():
    return


def card_reader_info():
    return


def cpu_info():
    # cpu count

    # cpu manafacturer

    # cpu sku

    # cpu speed

    # cpu type
    return


def gpu_info():
    return
# hdd manafacturer


def hdd_info():
    # hdd model
    return
# hdd serial
    return
# hdd size
    return
# hdd type


def ram_info():
    # ram count

    # ram size

    # ram type
    return


def peripherals_info():
    # screen size

    # webcam

    # wifi
    return


def audit_json():
    """
    transforms funtions info to a dictionary
    """
    audit_info = {
        'Serial': serial_number(),
        'Hardware': {
            'Battery': {
                'DesignedCapacity': '',
            },
            "Bios": '',
            'Bluetooth': bluetooth_info(),
            'Card Reader': card_reader_info(),
            'ChassisType': 'Notebook',
            'CPU': {
                'id': '',
                'FullName': '',
                'Manafacturer': '',
                'Model': '',
                'Type': '',
                'Speed': '',
                'Cores': '',

            },
            'GPU': gpu_info(),
            'HDD MFG': hdd_info(),
            'HDD Model': hdd_info(),
            'HDD Serial': hdd_info(),
            'HDD Type': hdd_info(),
            'Optic Type': '',
            'Ram Count': ram_info(),
            'Ram Size': ram_info(),
            'Ram Total Size': ram_info(),
            'Ram Type': ram_info(),
            'Screen Size': peripherals_info(),
            'Webcam': peripherals_info(),
            'Wifi': peripherals_info(),
        }
    }
    json_info = json.dumps(audit_info, indent=4)

    return json_info
