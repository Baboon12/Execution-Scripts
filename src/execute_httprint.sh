#!/bin/bash

# Define target servers
servers=("www.instagram.com" "www.example2.com" "www.example3.com")

# Path to signatures file
signatures_file="/usr/share/httprint/signatures.txt"  # Update this path if needed

# Output directory for reports
output_dir="httprint_reports"
mkdir -p $output_dir

# Loop through each server and run Httprint
for server in "${servers[@]}"
do
    server_clean=$(echo $server | tr -d '[:punct:]')
    echo "Analyzing $server..."

    # Identify web server version and type
    httprint -h $server -s $signatures_file > $output_dir/${server_clean}_basic.txt

    # Generate HTML report
    httprint -h $server -s $signatures_file -o $output_dir/${server_clean}_report.html

    # Generate CSV report
    httprint -h $server -s $signatures_file -oc $output_dir/${server_clean}_report.csv

    # Generate XML report
    httprint -h $server -s $signatures_file -ox $output_dir/${server_clean}_report.xml

    # Detailed server analysis with no automatic SSL detection
    httprint -h $server -s $signatures_file -noautossl > $output_dir/${server_clean}_detailed.txt
done

echo "Httprint analysis completed for all servers."
