from values import src_instance, src_org, src_token, dst_instance, dst_token, dst_org
import os

def stack():
    print("I'm exporting your resources...")
    os.system(f"influx export all --host {src_instance} --org {src_org} --token {src_token} --file exported.yml")
    print("Export completed.\n")

    print("Now, I'm importing this to your InfluxDB hosted by Voltmetrix instance. Please confirm...")
    os.system(f"influx apply --host {dst_instance} --org {dst_org} --token {dst_token} --file exported.yml")
    print("\nYou're ready to go.")
