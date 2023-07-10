# Define the source
src_instance = "https://us-west-2-1.aws.cloud2.influxdata.com"  # Enter your InfluxDB Cloud URL (e.g., https://us-west-2-1.aws.cloud2.influxdata.com).
src_bucket = ""  # Enter the bucket from which you want to download data.
src_org = ""  # Enter your organization.
src_token = ""  # Enter your token. Make sure the token has permission to read the bucket.
src_time = "-2h"  # Define how much data you want to export. It can be -1m, -6h, -2d, -30d, etc.

# Define the destination
dst_instance = ""  # Enter your InfluxDB hosted in Voltmetrix (e.g., https://544657bw2.customers.voltmetrix.io:8086).
dst_bucket = ""  # Enter the destination bucket. It needs to be created previously.
dst_org = ""  # Enter your organization. This can be your org ID or the email address used to register for InfluxDB Cloud.
dst_token = ""  # Enter your destination token. Make sure it has permission to write to the bucket.

