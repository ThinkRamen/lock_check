import json
import subprocess

default_password = 'admin'


def serial_number():
    """
    returns serial number from system command using subprocess.Popen, formats the data from bytes to str, and formats it.
    """
    check_serial = "system_profiler SPHardwareDataType | awk '/Serial/ {print $4}'"
    proc = subprocess.Popen(
        check_serial, shell=True, stdout=subprocess.PIPE)
    output = proc.communicate()[0]
    serial_number = output.decode("UTF-8").strip()
    return serial_number
    ###


def fmm_status():
    """
    checks for find my mac.
    """
    check_fmm = 'nvram -p | awk "/fmm-mobileme-token-FMM-BridgeHasAccount/{print $NF}"'
    proc = subprocess.Popen(check_fmm, shell=True, stdout=subprocess.PIPE)
    output = proc.communicate()[0]
    fmm_status = output.decode("UTF-8").strip()
    if fmm_status == 'BridgeHasAccountValue':
        fmm_status = True
    else:
        fmm_status = False
    return fmm_status
    ###


def icloud_status():  # TODO
    check_icloud = ''
    proc = subprocess.Popen(check_icloud,
                            shell=True, stdout=subprocess.PIPE)
    output = proc.communicate()[0]
    output = output.decode("UTF-8").strip()
    icloud_status = output
    return icloud_status
    ###


def activation_lock_status():
    check_activation_lock = '/usr/sbin/system_profiler SPHardwareDataType | awk "/Activation Lock Status/{print $NF}"'
    proc = subprocess.Popen(check_activation_lock,
                            shell=True, stdout=subprocess.PIPE)
    output = proc.communicate()[0]
    output = output.decode("UTF-8").strip()
    output = output.split(':')
    activation_lock_status = output[1].strip()
    if activation_lock_status == None:
        activation_lock_status = 'Not Supported'
    return activation_lock_status
    ###


def mdm_status():  # TODO
    check_mdm = 'sudo profiles status -type enrollment'
    proc = subprocess.Popen(check_mdm, shell=True, stdout=subprocess.PIPE)
    output = proc.communicate()[0]
    mdm_status = output.decode("UTF-8").strip()
    mdm_status = mdm_status.splitlines()
    return mdm_status
    ###


def dep_status():  # TODO
    check_dep = 'echo "admin" | sudo profiles renew -type enrollment && sudo profiles show -type enrollment'
    proc = subprocess.Popen(check_dep, shell=True,
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = proc.communicate()[0]
    dep_status = output.decode("UTF-8").strip()
    if output == "Error fetching Device Enrollment configuration: Client is not DEP enabled." or output == "(null)":
        dep_status = 'Unlocked'
    else:
        dep_status = 'Locked'
    return dep_status
    ###


def lock_check_json():
    dictionary = {}
    dictionary['Serial'] = serial_number()
    dictionary['FMM Enabled'] = fmm_status()
    dictionary['iCloud Enabled'] = icloud_status()
    dictionary['Activation Lock'] = activation_lock_status()
    dictionary['MDM Status'] = mdm_status()
    dictionary['DEP Status'] = dep_status()
    JSON = json.dumps(dictionary, indent=4)
    return JSON
# for commands that require password use encrypted file user can enter password in.
