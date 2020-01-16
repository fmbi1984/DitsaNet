
'''

import crcmod

msg_data = b'1VALUE: I0.07,V1.96,T32.49,P3C,t426.26,Tt436.26,TT1706,R'
#packet_data = b'\x026ACTION: PASS\x036;\x04'
#msg_data = packet_data[1:len(packet_data)-4]
#msg_data= packet_data[1:len(packet_data)]
print(msg_data)
xmodem_crc_func = crcmod.mkCrcFun(0x11021, rev=False, initCrc=0x0000, xorOut=0x0000)
crc16 = xmodem_crc_func(bytes(msg_data[0:len(msg_data)]))
print(crc16)

x = crc16 >> 8
y = crc16 & 0x00FF
print(x)
print(y)

x = [False, '', '', '', '', '', '0.0', '0.0', 'I', True, 1]

y = float(x[7])

print(y)

'''


x = "lblPage "+str(14)

print(x)