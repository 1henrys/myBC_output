from constants import *
from dotenv import load_dotenv
import os
import subprocess
import json

mnemonic = os.getenv('BCS_MNEMONIC')
#command = './derive -g --mnemonic="INSERT HERE" --cols=path,address,privkey,pubkey --format=json'
command = f'php derive -g --mnemonic={mnemonic} --coin=eth --cols=path,address,privkey,pubkey --format=json'

p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
output, err = p.communicate()
p_status = p.wait()

keys = json.loads(output)
print(keys)
