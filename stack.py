from values import src_instance, src_org, src_token, dst_instance, dst_token, dst_org
import os

print("###############################################################################")
print("#################### Let's export some resources ##############################")
print("###############################################################################\n")

def stack():
    print("I'm exporting your resources...")
    os.system(f"influx export all --host {src_instance} --org {src_org} --token {src_token} --file exported.yml")
    print("It's done\n")

    print("Now, I'm importing this to your InfluxDB Cloud instance. You need to confirm...")
    os.system(f"influx apply --host {dst_instance} --org {dst_org} --token {dst_token} --file exported.yml")
    print("\nYou're ready to roll")