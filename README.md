# Android Lockscreen Payload

A python script that creates ducky script for bad usbs that can be used to unlock android lock screen

## Usage

You can simply copy-paste the ducky script from **payload.txt** file into your bad usb

## Notice !

I've tested the timeouts on android 11 and it works fine till 50 attempts and I had no time to wait for more to see the increased timeouts after those attempts. So I have simply put default delay of 2 minutes for every attempt after 50 tries. If you guys know about the increased timeouts after 50 attempts then make sure to updated it in **ducky_writer.py** file. 

The order of the pins in the script is based on **four-digit-pin-codes-sorted-by-frequency-withcount.csv** by [danielmiessler](https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/four-digit-pin-codes-sorted-by-frequency-withcount.csv)

## License
[GNU General Public License v3.0](https://github.com/amanbytes/Android-Lockscreen-Payload/blob/main/LICENSE)
