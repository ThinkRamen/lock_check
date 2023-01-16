ACTIVATIONLOCKSTATUS=$(/usr/sbin/system_profiler SPHardwareDataType | awk '/Activation Lock Status/{print $NF}')
if [ -z "$ACTIVATIONLOCKSTATUS" ]; then
    ACTIVATIONLOCKSTATUS="Not Supported"
fi

echo $ACTIVATIONLOCKSTATUS