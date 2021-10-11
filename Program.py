from usb import *
from time import *
from gpio import *


def main():
  # program pada USB saat akan distart
	# start USB
	usb = USB(0, 57600) 
  # pin mode sesuai dengan nomor pin pada USB
	pinMode(0, IN)
	pinMode(1, IN)
	pinMode(2, IN)
	pinMode(3, IN)
  # kondisi saat bernilai trus
	while True:
    #jika digitalRead pada pinMode nomor 0 bernilai HIGH/ditekan
		if digitalRead(0) == HIGH:
			usb.write("left"); #maka akan mengarahkan mobil ke kiri 
		elif digitalRead(1) == HIGH: # jika digitalRead pada pinMode nomor 1 bernilai HIGH/ditekan
			usb.write("right"); # maka akan mengarahkan mobil ke kanan 
		elif digitalRead(2) == HIGH:  # jika digitalRead pada pinMode nomor 2 bernilai HIGH/ditekan
			usb.write("up"); # maka akan mengarahkan mobil ke atas 
		elif digitalRead(3) == HIGH: #  jika digitalRead pada pinMode nomor 3 bernilai HIGH/ditekan
			usb.write("down"); # maka akan mengarahkan mobil ke bawah 
		else: # jika kondisi lainnya maka akan berhenti/tidak bergerakk
			usb.write("stop");
		
    # dengan delay 500s
		delay(500)

if __name__ == "__main__":
	main()
