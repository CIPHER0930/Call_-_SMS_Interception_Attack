# Call_-_SMS_Interception_Attack

README.md
Call and SMS Capture Script

This script captures all packets from and to a specified phone number. It can be used to capture call and SMS messages for later analysis.

Usage:
git clone https://github.com/CIPHER0930/Call_-_SMS_Interception_Attack

chmod +x PhoneNumber_intercept.sh
./PhoneNumber_Intercept.sh
OR
bash PhoneNumber_Intercept.sh
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

./PhoneNumber_Intercept.sh

This will capture all packets from and to the phone number +237653772744. Once the capture is complete, the script will open the capture file in tcpdump pcap viewx tool so that you can analyze the call and SMS messages



Author : Shield

MIT License

Copyright (c) 2023 Shield

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
