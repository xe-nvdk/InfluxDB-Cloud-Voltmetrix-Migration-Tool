# Define the source
src_instance = "" # Enter your InfluxDB URL (Ex: localhost:8086).
src_bucket = "" # Enter the bucket that from you want to download data.
src_org = "" # Enter your organisation.
src_token = "" # Enter your token, make sure that the token has permission to read the bucket.
src_time = "-2h" # Define how much data you want to export. Can be -1m, -6h, -2d, -30d, etc.

# define the destination
dst_instance = "" # Enter your InfluxDB Cloud instace. (Ex: https://us-west-2-1.aws.cloud2.influxdata.com).
dst_bucket = "" # Enter the destination bucket. Needs to be created previuosly.
dst_org = "" # Enter your organisation, this can be your org id or the email address used to register to InfluxDB Cloud.
dst_token = "" # Enter your destination token, make sure that has permission to write in the bucket.
