#!/usr/bin/python3
description = [
'Bit 0 – Enable AVRCP buttons (see GPIO on pg. 15 for more info)',
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

hex_opts = '2004' #default
#hex_opts = '1CB6' #mine
#hex_opts = '50F6' #someone elses

scale = 16
num_of_bits = 15
bin_opts = (bin(int(hex_opts, scale))[2:].zfill(num_of_bits))
print ('options: ' + hex_opts)
print ('bits: ' + str(len(bin_opts)))
print ('binary: ' + str(bin_opts))

#print('\x1b[6;30;42m' + 'Success!' + '\x1b[0m')

for a, b in zip(reversed(bin_opts),(description)):
    #print (a)
    #print (type (a))
    if a == '1': 
        print (b + ' ' + '\x1b[6;30;42m' +  'Enabled' + '\x1b[0m')
    else:
        print (b + ' ' + '\x1b[0;30;41m' +  'Disabled' + '\x1b[0m') 
    #print(a, b)
