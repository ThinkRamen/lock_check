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
    return r.status_code, 'Authorized'
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
    check_serial = "system_profiler SPHardwareDataType | awk '/Serial/ {print $4}'"
    serial_number = output_cmd(check_serial)
    return serial_number
    ###


def fmm_status():
    """
    checks for find my mac.
    """
    check_fmm = 'nvram -p | awk "/fmm-mobileme-token-FMM-BridgeHasAccount/"'
    fmm_status = output_cmd(check_fmm)
    fmm_status = fmm_status.split()[1].strip()
    if fmm_status == 'BridgeHasAccountValue':
        fmm_status = True
    else:
        fmm_status == False
    return fmm_status
    ###


def icloud_status():
    check_icloud = 'defaults read MobileMeAccounts Accounts'
    icloud_status = output_cmd(check_icloud)
    if icloud_status != '(\n)':
        icloud_status = True
    if icloud_status == '(\n)':
        icloud_status = False
    return icloud_status
    ###


def activation_lock_status():
    check_activation_lock = 'system_profiler SPHardwareDataType | awk "/Activation Lock Status/"'
    activation_lock_status = output_cmd(check_activation_lock)
    activation_lock_status = activation_lock_status.split(':')[1].strip()
    if activation_lock_status == None:
        activation_lock_status = 'Not Supported'
    return activation_lock_status
    ###


def mdm_status():
    check_mdm_status = 'echo {} | sudo -S profiles status -type enrollment'.format(
        default_password)
    mdm_status = output_cmd(check_mdm_status)
    if mdm_status.splitlines()[1].split(':')[1].strip() == 'No':
        mdm_status = False
    else:
        mdm_status = True
    return mdm_status
    ###


def dep_status():
    check_dep_status = "echo {} | sudo -S profiles renew -type enrollment && sudo -S profiles show -type enrollment".format(
        default_password)
    proc = subprocess.Popen(check_dep_status, shell=True,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    dep_status = proc.communicate()[1].decode().splitlines()
    # if unlocked
    if dep_status == "Error fetching Device Enrollment configuration: Client is not DEP enabled." or dep_status == "(null)":
        dep_status = False
    return dep_status
    ###


def lock_check_json():
    dictionary = {}
    dictionary['Serial'] = serial_number()
    dictionary['FMM Enabled'] = fmm_status()
    dictionary['iCloud Enabled'] = icloud_status()
    dictionary['Activation Lock'] = activation_lock_status()
    dictionary['MDM Enrollment'] = mdm_status()
    dictionary['Enrolled Via DEP'] = dep_status()
    JSON = json.dumps(dictionary, indent=4)
    return JSON


get_auth()
print(lock_check_json())
