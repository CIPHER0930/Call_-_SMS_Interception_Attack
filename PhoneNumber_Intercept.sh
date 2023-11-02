#!/bin/bash

# Set the phone number to intercept
PHONE_NUMBER="1234567890"

# Check if the phone number is valid
if [[ ! "$PHONE_NUMBER" =~ ^[0-9]+$ ]]; then
  echo "Invalid phone number"
  exit 1
fi

# Start tshark to capture all packets from and to the phone number
tshark -i any -p -f "(ip.src == $PHONE_NUMBER or ip.dst == $PHONE_NUMBER)" -w call_and_sms.pcapng

# Display a message to the user
echo "Press Enter to stop capturing"

# Wait for the user to press Enter
read

# Stop tshark
pkill tshark

# Check if the call_and_sms.pcapng file exists
if [[ -f call_and_sms.pcapng ]]; then
  # Open the capture file in tcpdump pcap viewx tool
  tcpdump_pcap_viewx call_and_sms.pcapng

  # Display a message to the user
  echo "Call and SMS messages opened successfully"
else
  echo "Failed to capture call and SMS messages"
fi
