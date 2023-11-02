# Call_-_SMS_Interception_Attack

README.md
Call and SMS Capture Script

This script captures all packets from and to a specified phone number. It can be used to capture call and SMS messages for later analysis.

Usage:

./call_and_sms_capture.sh
Requirements:

tshark
tcpdump_pcap_viewx
Steps:

Set the phone number to intercept in the PHONE_NUMBER variable.
Run the script.
Press Enter to stop capturing.
If the capture file call_and_sms.pcapng exists, the script will open it in tcpdump pcap viewx tool.
Example:

PHONE_NUMBER="653772744"

./call_and_sms_capture.sh
This will capture all packets from and to the phone number +237653772744. Once the capture is complete, the script will open the capture file in tcpdump pcap viewx tool so that you can analyze the call and SMS messages
