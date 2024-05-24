import os

# Define target servers
servers = ["www.instagram.com", "www.example2.com", "www.example3.com"]

# Path to signatures file
signatures_file = "/usr/share/httprint/signatures.txt"  # Update this path if needed

# Output directory for reports
output_dir = "httprint_reports"
os.makedirs(output_dir, exist_ok=True)

# Loop through each server and run Httprint
for server in servers:
    server_clean = server.translate(str.maketrans("", "", '[:punct:]'))
    print(f"Analyzing {server}...")

    # Identify web server version and type
    os.system(f"httprint -h {server} -s {signatures_file} > {output_dir}/{server_clean}_basic.txt")

    # Generate HTML report
    os.system(f"httprint -h {server} -s {signatures_file} -o {output_dir}/{server_clean}_report.html")

    # Generate CSV report
    os.system(f"httprint -h {server} -s {signatures_file} -oc {output_dir}/{server_clean}_report.csv")

    # Generate XML report
    os.system(f"httprint -h {server} -s {signatures_file} -ox {output_dir}/{server_clean}_report.xml")

    # Detailed server analysis with no automatic SSL detection
    os.system(f"httprint -h {server} -s {signatures_file} -noautossl > {output_dir}/{server_clean}_detailed.txt")

print("Httprint analysis completed for all servers.")
