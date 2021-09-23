# Cyclic-Redundancy-Check-Using-tkinter
This repo contains GUI implementation of Cyclic Redundancy Check (Error Detection Technique).

# What is CRC?
A CRC is derived using a more complex algorithm which involves MODULO ARITHMETIC (hence the 'cyclic' name). The remainder is known as CRC which contains one bit less than the divisor.
Message Sent = Data + CRC

# Error detection at receiver's side
If the remainder after performing division on message bits recieved with actual divisor is zero then there is no error in the data unit & receiver accepts it but if the remainder is not zero then  it indicats the data unit bits has been changed or damaged, and the message is rejected.

# GUI 
![image](https://user-images.githubusercontent.com/71524518/134492473-29c8abec-b287-4835-a2a9-fdf759882cdc.png)

# User Inputs in GUI
Actual bits is the original data bits of the message that is to be sent.
CRC polynomial is the polynomial that is to be used to calculate remainder bits in order to protect actual message from errors.
