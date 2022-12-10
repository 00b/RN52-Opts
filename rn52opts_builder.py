#!/usr/bin/python3

description = [
'Bit 0 – Enable AVRCP buttons',
'Bit 1 – Enable reconnect on power-on',
'Bit 2 – Bluetooth Discoverable on start up',
'Bit 3 – Codec indicators PIO7 (AAC) and PIO6 (aptX)',
'Bit 4 – Reboot after disconnect (otherwise must power cycle)',
'Bit 5 – Mute volume up/down tones',
'Bit 6 – Enable voice command button on PIO4',
'Bit 7 – Disable system tones',
'Bit 8 – Power off after pairing timeout',
'Bit 9 – Reset after power off',
'Bit 10 – Enable list reconnect after panic',
'Bit 11 – Enable latch event indicator PIO2',
'Bit 12 – Enable track change event',
'Bit 13 – Enable tones playback at fixed volume',
'Bit 14 – Enable auto-accept passkey in Keyboard I/O Authentication']

for b in description:
    val = input (b + '? Y/N ')
    if val.lower() == 'y':
        opts_string = opts_string + '1'
    else:
        opts_string = opts_string + '0'

#print(opts_string)
#now put bit 0 on the right/reverse the string.  
opts_string = opts_string[::-1]
#print(len(opts_string))
print('binary ' + opts_string)
opts_hex = f'{int(opts_string, 2):X}'
print('hex: ' + opts_hex)

