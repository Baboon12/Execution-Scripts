#!/bin/bash

# Basic HTTP GET request
echo "Performing basic HTTP GET request..."
curl https://www.instagram.com

# Analyzing robots.txt
echo "Analyzing robots.txt..."
curl https://www.instagram.com/robots.txt

# Retrieving meta tags
echo "Retrieving meta tags..."
curl -i https://www.instagram.com

# Inspecting comments and code metadata
echo "Inspecting comments and code metadata..."
curl -s https://www.instagram.com | grep "<!--"

# Analyzing WAF: Observe response headers and behavior for WAF indications
echo "Analyzing WAF..."
curl -I https://www.instagram.com

# Proxy usage (uncomment and replace <proxy_host> and <proxy_port> with actual values)
# echo "Using proxy..."
# curl -x <proxy_host>:<proxy_port> https://www.instagram.com

# Backend database detection: Manual analysis required
echo "Backend database detection requires manual analysis."

# Creating a local copy of the website
echo "Creating a local copy of the website..."
curl -o instagram.html https://www.instagram.com

# Analyzing HTTP methods
echo "Analyzing HTTP methods..."
curl -X OPTIONS https://www.instagram.com

# Checking security headers
echo "Checking security headers..."
curl -I https://www.instagram.com

echo "Curl commands executed successfully."

