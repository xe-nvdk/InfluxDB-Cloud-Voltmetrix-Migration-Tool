import importer
import stack

print("#######################################################################################################################")
print("########################### Welcome to InfluxDB Cloud Importer by Ignacio Van Droogenbroeck ###########################")
print("#######################################################################################################################\n")

print("I'm going to help you to export your entire stack from InfluxDB Cloud OSS to InfluxDB Cloud\n")
print("What do you want to do?\n\nPress 1 to export Dashboards, Labels, Telegraf configuration, alerts, etc.\nPress 2 to export data.\nPress 99 to do both.\n")

def main():
    
    action = input("Enter your choice: ")

    if action == "1":
        stack.stack()

    elif action == "2":
        importer.data()

    elif action == "99":
        stack.stack()
        importer.data()

    else:
        print("Invalid option")

main()

