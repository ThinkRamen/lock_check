#!/bin/sh

# Activation Lock plugin v1.2.0.0
# written by Ella Hansen for Ignition www.ignitionit.com
# get MDM status
MDM=$(profiles status -type enrollment)

Green=$'\e[1;32m'

# check serial number and if mdm profiles are active
echo "Serial Number"
serialnumber=$(system_profiler SPHardwareDataType | awk '/Serial/ {print $4}')
SERIALNUMBER="${serialnumber}"
echo $SERIALNUMBER
echo 'admin17' | sudo -S sh -c '
profiles renew -type enrollment
profiles show -type enrollment
profiles status -type enrollment
profiles validate -type enrollment
'

# get Find My Mac status
FMMSTATUS=$(nvram -p | awk '/fmm-mobileme-token-FMM-BridgeHasAccount/{print $NF}')
if [ "$FMMSTATUS" = "BridgeHasAccountValue" ]; then
	FMMSTATUS="Enabled"
else
	FMMSTATUS="Disabled"
fi

ACTIVATIONLOCKSTATUS=$(/usr/sbin/system_profiler SPHardwareDataType | awk '/Activation Lock Status/{print $NF}')
if [ -z "$ACTIVATIONLOCKSTATUS" ]; then
	ACTIVATIONLOCKSTATUS="Not Supported"
fi


#get Apple ID email, name, and management status
CURRENTUSER=$(/usr/bin/stat -f%Su /dev/console)

APPLEIDEMAIL=$(/usr/libexec/PlistBuddy -c "print :Accounts:0:AccountID" /Users/$CURRENTUSER/Library/Preferences/MobileMeAccounts.plist 2>/dev/null)
APPLEIDEXISTS=$?
APPLEIDNAME=$(/usr/libexec/PlistBuddy -c "print :Accounts:0:DisplayName" /Users/$CURRENTUSER/Library/Preferences/MobileMeAccounts.plist 2>/dev/null)
APPLEIDMANAGED=$(/usr/libexec/PlistBuddy -c "print :Accounts:0:isManagedAppleID" /Users/$CURRENTUSER/Library/Preferences/MobileMeAccounts.plist 2>/dev/null)

if [ "$APPLEIDMANAGED" = "false" ]; then
	APPLEIDMANAGED="False"
elif [ "$APPLEIDMANAGED" = "true" ]; then
	APPLEIDMANAGED="True"
fi

#data to report
REPORT="Find My Mac: $FMMSTATUS\nActivation Lock: $ACTIVATIONLOCKSTATUS\n$MDM\n\nApple ID Information\nDisplay name: $APPLEIDNAME\nEmail: $APPLEIDEMAIL\nManaged: $APPLEIDMANAGED"

# if activation lock is enabled but no Apple ID is detected
if (( $APPLEIDEXISTS != 0 )) && [ "$ACTIVATIONLOCKSTATUS" = "Enabled" ]; then
	echo "Activation Lock is enabled but the current user is not signed into iCloud\n\nFind My Mac: $Red$FMMSTATUS\nActivation Lock: $ACTIVATIONLOCKSTATUS"

# if FMM is enabled but no Apple ID is detected
elif (( $APPLEIDEXISTS != 0 )) && [ "$FMMSTATUS" = "Enabled" ]; then
	echo "Find My Mac is enabled but the current user is not signed into iCloud\n\nFind My Mac: $Red$FMMSTATUS\nActivation Lock: $ACTIVATIONLOCKSTATUS"

# if activation lock is disabled and no Apple ID is detected
elif (( $APPLEIDEXISTS != 0 )) && [ "$FMMSTATUS" = "Disabled" ]; then
	echo "Find My Mac is disabled and the current user is not signed into iCloud\n\nFind My Mac: $Green$FMMSTATUS\nActivation Lock: $ACTIVATIONLOCKSTATUS"

# if Activation Lock is enabled and Apple ID is NOT managed, report alert
elif [ "$ACTIVATIONLOCKSTATUS" = "Enabled" ] && [ "$APPLEIDMANAGED" = "False" ]; then
	echo "Activation Lock is enabled with an unmanaged Apple ID\n\n$REPORT"

# if FMM is enabled and Apple ID is NOT managed, report alert
elif [ "$FMMSTATUS" = "Enabled" ] && [ "$APPLEIDMANAGED" = "False" ]; then
	echo "Find My Mac is enabled with an unmanaged Apple ID\n\n$REPORT"

# if activation lock is enabled and Apple ID is managed, report warning
elif [ "$ACTIVATIONLOCKSTATUS" = "Enabled" ] && [ "$APPLEIDMANAGED" = "True" ]; then
	echo "Activation Lock is enabled with a managed Apple ID\n\n$REPORT"

# if FMM is enabled and Apple ID is managed, report warning
elif [ "$FMMSTATUS" = "Enabled" ] && [ "$APPLEIDMANAGED" = "True" ]; then
	echo "Find My Mac is enabled with a managed Apple ID\n\n$REPORT"

# if activation lock is disabled, report ok
elif [ "$FMMSTATUS" = "Disabled" ] && [ "$ACTIVATIONLOCKSTATUS" = "Disabled" ]; then
	echo "Find My Mac and Activation Lock are disabled\n\n$REPORT"

# if activation lock is disabled, report ok
elif [ "$FMMSTATUS" = "Disabled" ] && [ "$ACTIVATIONLOCKSTATUS" = "Disabled" ]; then
	echo "Find My Mac is disabled\n\n$REPORT"

else
	exit 0
fi