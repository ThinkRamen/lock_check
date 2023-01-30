echo admin | sudo -S profiles renew -type enrollment
DEPSTATUS=$(echo admin | sudo -S profiles show -type enrollment 2>&1)
echo "$DEPSTATUS"