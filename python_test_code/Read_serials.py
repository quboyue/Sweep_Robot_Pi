import time
import math
import serial 
import socket
ser = serial.Serial(  # 下面这些参数根据情况修改
  port='COM6',# 串口
  baudrate=115200,# 波特率
  parity=serial.PARITY_ODD,
  stopbits=serial.STOPBITS_TWO,
  bytesize=serial.SEVENBITS

)



client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip_port = ('127.0.0.1', 7402)
msg=""
while True:
    data = ser.readline().decode()

    try:

      result=str(data.split(",")[3].split(":")[1])
      print(data.split(",")[3])
      msg=result
    except:
      pass
    client.sendto(msg.encode('utf-8'),ip_port)

 
client.close()
