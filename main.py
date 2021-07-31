import requests
import json
from time import sleep

chunks = []
output = []

def setup(filename):
    with open(filename) as f:
        chunk = []
        for line in f:
            chunk.append(line.strip())
            
            if len(chunk) >= 10:
                chunks.append(chunk)
                chunk = []
        
        chunks.append(chunk)

def run(print_mode):
    for chunk in chunks:
        try:
            request = requests.post("https://api.mojang.com/profiles/minecraft", json.dumps(chunk))
            
            for profile in request.json():
                if print_mode:
                    print(profile)
                
                try:
                    output.append(profile['id'])
                except Exception as e:
                    # I think error is here if profile doesn't exist
                    print(profile)
                    print(e)
        except Exception as e:
            print(e)
            print("Rate limited, probably; Waiting 10mins.")
            sleep(600)
            break

def save(filename):
    with open(filename, "w+") as f:
        f.write("\n".join(output))

setup("input.txt")
run(True)
save("output.txt")