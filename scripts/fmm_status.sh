# get Find My Mac status
FMMSTATUS=$(nvram -p | awk '/fmm-mobileme-token-FMM-BridgeHasAccount/{print $NF}')
if [ "$FMMSTATUS" = "BridgeHasAccountValue" ]; then
    FMMSTATUS="Enabled"
else
    FMMSTATUS="Disabled"
fi

echo "$FMMSTATUS\c"