from PIL import Image
from pytesser import image_to_string
import pyscreenshot as ImageGrab
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys

url = 'https://www.bustabit.com/play'

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)



#Navigate to URL

# part of the screen
if __name__ == "__main__":
	driver.get(url)
	time.sleep(5)
	
	t_end = time.time() + 60 * 2
	counter = 1
	
	while time.time() < t_end:
		im=ImageGrab.grab(bbox=(80,170,400,400))
		im.show()
		ImageGrab.grab_to_file("im" + str(counter) + ".png")
		counter = counter + 1

	counter = counter + 1
	for num in range(counter):
		im = Image.open("C:\Users\Tomonari\workspace\python\Bustabit" + "\im" + str(counter) + ".png")
		text = image_to_string(im.convert('RGB'))
		
		busted = text.strip()
		busted = busted[8: -1]
		print busted.strip()







