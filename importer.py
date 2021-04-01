from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS
from values import *
import csv
import os
import re

print("###################################################################################################")
print("############################# Welcome to InfluxDB Cloud importer tool #############################")
print("###################################################################################################\n")

print("I'm going to help you to migrate your current data from a InfluxDB 2.x instance to InfluxDB Cloud\n")

def data():

    client = InfluxDBClient(url=src_instance, token=src_token, org=src_org)

    bucket = src_bucket

    query_api = client.query_api()

    csv_result = query_api.query_csv(f'from(bucket:"{bucket}") |> range(start: {src_time})')

    writer = csv.writer(open("exported.csv", 'w'))
    print("Downloading bucket", bucket,"to exported.csv")
    for csv_line in csv_result:
        if not len(csv_line) == 0:
            writer.writerow(csv_line)

    size_bucket = os.path.getsize('exported.csv')
    tomb = (size_bucket / 1048576)
    cost = (tomb * 0.002)
    print("If you're a PAYG user this write is going to cost you $",cost)

    upload = input(str("Do you want to continue: y/n: "))

    if upload == "y":
        print("Uploading the data, this can take some time depending of the size of your file",tomb,"MB")
        os.system(f"influx write --host {dst_instance} --org {dst_org} --token {dst_token} --bucket {dst_bucket} --file exported.csv")
        print("It's done, go to your instance in Cloud, log in, and explore the bucket, you should the see the information there.")

    else:
        print("\nOk, Bye Bye")