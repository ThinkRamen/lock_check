DEPSTATUS=$(echo "admin" | sudo -S sh -c "profiles renew -type enrollment && profiles show -type enrollment")
echo $DEPSTATUS

