# imports
import json
from lock_check import serial_number
from lock_check import output_cmd

hardware_info = output_cmd()


class Battery:
    def designed_capacity():
        output = output_cmd('')
        return
        ###

    def full_charge_capacity():
        return
        ###

    def percent_of_designed_capacity():
        return
        ###


def bluetooth_info():
    return


def card_reader_info():
    return


class Cpu:
    def count():
        return
        ###

    def manufacturer():
        return
        ###

    def sku():
        return
        ###

    def speed():
        return
        ###

    def type():
        return
        ###


def gpu_info():
    return


class Hdd:
    def model():
        return

    def serial():
        return

    def size():
        return

    def type():
        return


class Ram:
    def count():
        return

    def size():
        return

    def type():
        return


def Peripherals():
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
