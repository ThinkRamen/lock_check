import json
import subprocess

password = 'admin17'


def serial_number():
    check_serial = "system_profiler SPHardwareDataType | awk '/Serial/ {print $4}'"
    proc = subprocess.Popen(
        check_serial, shell=True, stdout=subprocess.PIPE)
    output = proc.communicate()[0]
    serial_number = output.decode("UTF-8").strip()
    return serial_number
    ###


def fmm_status():
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
# TODO


def icloud_status():
    return ''
    ###


def activation_lock_status():
    check_activation_lock = '/usr/sbin/system_profiler SPHardwareDataType | awk "/Activation Lock Status/{print $NF}"'
    proc = subprocess.Popen(check_activation_lock,
                            shell=True, stdout=subprocess.PIPE)
    output = proc.communicate()[0]
    output = output.decode("UTF-8").strip()
    output = output.split(':')
    output = output[1].strip()
    if output == None:
        activation_lock_status = 'Not Supported'
    activation_lock_status = output
    return activation_lock_status
    ###

# TODO


def mdm_status():
    check_mdm = 'sudo profiles status -type enrollment'
    proc = subprocess.Popen(check_mdm, shell=True, stdout=subprocess.PIPE)
    output = proc.communicate()[0]
    mdm_status = output.decode("UTF-8").strip()
    mdm_status = mdm_status.splitlines()
    mdm_status = [i.split(':')[1].strip() for i in mdm_status]
    return mdm_status
    # append by finding mdm status location then +1 for keypair Managed By: "Customer Name"
    ###

# TODO


def dep_status():
    check_dep = 'sudo profiles renew -type enrollment && sudo profiles show -type enrollment'
    proc = subprocess.Popen(check_dep, shell=True, stdout=subprocess.PIPE)
    output = proc.communicate()[0]
    dep_status = output.decode("UTF-8").strip()
    return dep_status
    ###


# if icloud present: add keypairs for icloud account info
dictionary = dict(lock_check={
    'Serial Number': serial_number(),
    'FMM Enabled': fmm_status(),
    'iCloud Enabled': icloud_status(),
    'Activation Lock': activation_lock_status(),
    'MDM Status': mdm_status(),
    'DEP Status': dep_status(),
})

JSON = json.dumps(dictionary, indent=4)

print(JSON)

# for commands that require password use encrypted file user can enter password in.
