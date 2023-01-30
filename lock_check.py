import json
import subprocess
import requests
import sys
import os
from resources import find_data_file
default_password = 'admin'


def get_auth():
    URL = 'https://lock-check-backend.herokuapp.com/customers/1/?format=json'
    r = requests.get(url=URL)
    data = r.json()
    # if key authorization returns false, halt program
    if data['authorization'] == False:
        fail_message = 'Not Authorized'
        os.system(
            "osascript -e 'Tell application \"System Events\" to display dialog \""+fail_message+"\"'")
        sys.exit(fail_message)
    return print('get_auth_status_code: ' + str(r.status_code))
    ###


def to_txt_file(txt):
    file = open(f'{serial_number()}.txt', 'w')
    file.write(txt)
    file.close()
    return os.path.abspath(file.name)
    ###


def output_cmd(cmd):
    """
    returns terminal command using subprocess.Popen, formats the data from bytes to str, and formats it.
    """
    proc = subprocess.Popen(
        cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = proc.communicate()[0]
    output = output.decode("utf-8").strip()
    return output
    ###


def serial_number():
    return output_cmd(
        "system_profiler SPHardwareDataType | awk '/Serial/ {print $4}'")
    ###


def fmm_status():
    """
    checks for find my mac.
    """
    try:
        fmm_status = output_cmd(find_data_file('fmm_status.sh'))
        if fmm_status == 'Enabled':
            fmm_status = True
        elif fmm_status == 'Disabled':
            fmm_status = False
    except Exception as e:
        print(f'error: {e}')
    return fmm_status
    ###


def icloud_status():
    try:
        icloud_status = output_cmd(
            find_data_file('icloud_status.sh')).splitlines()
        # bash: $?: false = 1, true = 0
        if icloud_status[2] == "0":
            icloud_status = True
        elif icloud_status[2] == "1":
            icloud_status = False
    except Exception as e:
        print(f'error: {e}')
    return icloud_status
    ###


def activation_lock_status():
    try:
        activation_lock_status = output_cmd(
            find_data_file('activation_lock_status.sh'))
        if activation_lock_status == 'Enabled':
            activation_lock_status = True
        elif activation_lock_status == 'Disabled':
            activation_lock_status = False
        elif activation_lock_status == "Not Supported":
            activation_lock_status = None
    except Exception as e:
        print(f'error: {e}')
    return activation_lock_status
    ###


def mdm_status():
    try:
        check_mdm_status = f'echo {default_password} | sudo -S profiles status -type enrollment'
        mdm_status = output_cmd(check_mdm_status)
        mdm_status = mdm_status.splitlines()[1].split(':')[1].strip()
        if mdm_status == 'No':
            mdm_status = False
        elif mdm_status == 'Yes':
            mdm_status = True
    except Exception as e:
        print(f'error: {e}')
    return mdm_status
    ###


def dep_status():
    try:
        dep_status = output_cmd(find_data_file('dep_status.sh'))
        if dep_status == "Error fetching Device Enrollment configuration: Client is not DEP enabled.":
            dep_status = False
        elif dep_status == "Device Enrollment configuration: (null)":
            dep_status = False
        elif dep_status == "Error fetching Device Enrollment configuration - Request too soon.  Try again later.":
            os.system(
                "osascript -e 'Tell application \"System Events\" to display dialog \""+dep_status+"\"'")
            dep_status = None
        else:
            return dep_status
    except Exception as e:
        print(f'error: {e}')
    return dep_status
    ###


def lock_check_json():
    dictionary = {}
    dictionary['Serial'] = serial_number()
    dictionary['FMM Enabled'] = fmm_status()
    dictionary['iCloud Enabled'] = icloud_status()
    dictionary['Activation Lock Enabled'] = activation_lock_status()
    dictionary['MDM Enrollment'] = mdm_status()
    dictionary['Enrolled Via DEP'] = dep_status()
    JSON = json.dumps(dictionary, indent=4)
    # URL = ''
    # POST = requests.post(URL, json=JSON)
    # print(POST.status_code)
    return JSON
