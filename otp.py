import subprocess
import os
import re


def get_otp():

    acs_key = _read_acs_key()
    two_step_authentication = ['oathtool', '--totp', '--base32', acs_key]
    otp_pass = re.findall(r'\d+', subprocess.check_output(two_step_authentication).decode('utf-8'))

    return otp_pass[0]



def _read_acs_key():

    line = ""

    with open(".amz_otp_config", "r") as f:
        line = f.readline().rstrip('\n')

    return line
