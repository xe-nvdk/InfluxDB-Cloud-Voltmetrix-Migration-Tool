from influxdb_client import InfluxDBClient
from values import src_bucket, src_instance, src_org, src_time, src_token, dst_instance, dst_bucket, dst_org, dst_token
import csv
import os
import re

def data():

    client = InfluxDBClient(url=src_instance, token=src_token, org=src_org)
    bucket = src_bucket
    query_api = client.query_api()
    csv_result = query_api.query_csv(f'from(bucket:"{bucket}") |> range(start: {src_time}) |> drop(columns: ["_start", "_stop"])')

    writer = csv.writer(open("exported.csv", 'w'))
    print("Downloading bucket", bucket,"to exported.csv")
    for csv_line in csv_result:
        if not len(csv_line) == 0:
            writer.writerow(csv_line)

    size_bucket = os.path.getsize('exported.csv')
    tomb = (size_bucket / 1048576)
    print("The size of the file is:", tomb, "MB")

    upload = input(str("Do you want to continue: y/n: "))
    if upload == "y" and "Y":
        print(f"Uploading the data, this can take some time depending of the size of your file: {tomb:.2f} MB")
        os.system(f"influx write --host {dst_instance} --org {dst_org} --token {dst_token} --bucket {dst_bucket} --format csv --file exported.csv")
        print(f"It's done, go to your instance {dst_instance}, log in, and explore the bucket, you should the see the information there.")
    else:
        print("\nOk, Bye Bye")