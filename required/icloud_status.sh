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
echo $CURRENTUSER
echo $APPLEIDEMAIL
echo $APPLEIDEXISTS
echo $APPLEIDNAME
echo $APPLEIDMANAGED