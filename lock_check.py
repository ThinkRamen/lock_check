import json
import subprocess
import requests
import sys
import os

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
    serial_number = output_cmd(
        "system_profiler SPHardwareDataType | awk '/Serial/ {print $4}'")
    return serial_number
    ###


def fmm_status():
    """
    checks for find my mac.
    """
    try:
        fmm_status = output_cmd('./scripts/fmm_status.sh')
        if fmm_status == 'Enabled':
            fmm_status = True
        elif fmm_status == 'Disabled':
            fmm_status = False
    except:
        print('error: fmm_status()')
    return fmm_status
    ###


def icloud_status():
    icloud_status = output_cmd('./scripts/icloud_status.sh').splitlines()
    # bash: $?: false = 1, true = 0
    if icloud_status[2] == "0":
        icloud_status = True
    elif icloud_status[2] == "1":
        icloud_status = False
    return icloud_status
    ###


def activation_lock_status():
    activation_lock_status = output_cmd('./scripts/activation_lock_status.sh')
    if activation_lock_status == 'Enabled':
        activation_lock_status = True
    elif activation_lock_status == 'Disabled':
        activation_lock_status = False
    elif activation_lock_status == "Not Supported":
        activation_lock_status = None
    return activation_lock_status
    ###


def mdm_status():
    check_mdm_status = 'echo {} | sudo -S profiles status -type enrollment'.format(
        default_password)
    mdm_status = output_cmd(check_mdm_status)
    mdm_status = mdm_status.splitlines()[1].split(':')[1].strip()
    if mdm_status == 'No':
        mdm_status = False
    elif mdm_status == 'Yes':
        mdm_status = True
    return mdm_status
    ###


def dep_status():
    dep_status = output_cmd('./scripts/dep_status.sh')
    print(dep_status)
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
