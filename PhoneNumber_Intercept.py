import re
import subprocess
import time

# Set the phone number to intercept
PHONE_NUMBER = "1234567890"

# Check if the phone number is valid
if not re.match("^[0-9]+$", PHONE_NUMBER):
    print("Invalid phone number")
    exit(1)

# Start tshark to capture all packets from and to the phone number
tshark_command = ["tshark", "-i", "any", "-p", "-f", "(ip.src == {} or ip.dst == {})".format(PHONE_NUMBER, PHONE_NUMBER), "-w", "call_and_sms.pcapng"]
tshark_process = subprocess.Popen(tshark_command)

# Display a message to the user
print("Press Enter to stop capturing")

# Wait for the user to press Enter
time.sleep(1)

# Stop tshark
tshark_process.terminate()

# Check if the call_and_sms.pcapng file exists
if os.path.isfile("call_and_sms.pcapng"):
    # Open the capture file in tcpdump pcap viewx tool
    tcpdump_pcap_viewx_command = ["tcpdump_pcap_viewx", "call_and_sms.pcapng"]
    subprocess.run(tcpdump_pcap_viewx_command)

    # Display a message to the user
    print("Call and SMS messages opened successfully")
else:
    print("Failed to capture call and SMS messages")
