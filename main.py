# imports
import subprocess
import json


def info_to_file():
    """
    create file with the output of the system_profiler and similar commands used to find hardware info.
    """
    file = open('output.txt', 'w')
    process = subprocess.Popen('system_profiler -detailLevel mini', shell=True,
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    process = process.communicate()[0]
    file.write(process)
    return file


info_to_file()

# split info based on ':' to seperate attribute names with info.


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


def to_dict():
    """
    transforms funtions info to a dictionary
    """
    audit_info = {
        'Battery Health': battery_info(),
        'Bluetooth': bluetooth_info(),
        'Card Reader': card_reader_info(),
        'CPU Count': cpu_info(),
        'CPU MFG': cpu_info(),
        'CPU Model': cpu_info(),
        'CPU SKU': cpu_info(),
        'CPU Speed': cpu_info(),
        'CPU Type': cpu_info(),
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
    return audit_info


def serializer():
    json_info = json.dumps(to_dict())
    return json_info


print(serializer())
