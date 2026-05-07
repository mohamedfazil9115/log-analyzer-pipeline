info_count = 0
error_count = 0
warning_count = 0

# Read log file
with open("logs.txt", "r") as file:
    logs = file.readlines()

# Count log types
for line in logs:
    if "INFO" in line:
        info_count += 1
    elif "ERROR" in line:
        error_count += 1
    elif "WARNING" in line:
        warning_count += 1

# Generate report
with open("report.txt", "w") as report:
    report.write("Log Summary Report\n")
    report.write("-------------------\n")
    report.write(f"INFO: {info_count}\n")
    report.write(f"ERROR: {error_count}\n")
    report.write(f"WARNING: {warning_count}\n")

print("Report generated successfully!")