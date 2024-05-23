#!/bin/bash

# Define target networks
networks=("192.168.1.0/24" "10.0.0.0/24" "172.16.0.0/24")

# Output directory for reports
output_dir="unicornscan_reports"
mkdir -p $output_dir

# Loop through each network and run Unicornscan
for network in "${networks[@]}"
do
    network_clean=$(echo $network | tr -d '[:punct:]')
    echo "Scanning network $network..."

    # Run Unicornscan with sudo and output results to files
    sudo unicornscan -i eth0 $network > $output_dir/${network_clean}_results.txt
done

echo "Unicornscan analysis completed for all networks."
