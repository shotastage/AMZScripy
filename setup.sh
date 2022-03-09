#!/usr/bin/env bash

brew install oath-toolkit >> /dev/null

echo "アカウント追加用のキー: "
read ACKEY

echo $ACKEY >> .amz_otp_config

oathtool --totp --base32 $ACKEY
