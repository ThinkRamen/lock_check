import json
import subprocess

class file_to_json():

    def serial_number():
        check_serial = "system_profiler SPHardwareDataType | awk '/Serial/ {print $4}'"
        proc = subprocess.Popen(check_serial, shell=True, stdout=subprocess.PIPE)
        output = proc.communicate()[0]
        serial_number = output.decode("UTF-8").strip()
        return serial_number
        ###
        
    def fmm_status():
        return

    def icloud_status():
        return

    def mdm_status():
        return

    def dep_status():
        return

    dictionary = dict({
        'Serial Number': '',
        'FMM Status': '',
        'iCloud Status': '',
        'MDM Status': '',
        'DEP Status': '',
    })
    JSON = json.dumps(dictionary, indent=4)
    print(JSON)
    ###
