import os
import time

class CameraController:
	def __init__(self, countdown_time=10, default_save_path="photobooth_images/captured_image.jpg"):
		self.countdown_time = countdown_time
		self.default_save_path = default_save_path

	def connect_camera(self):
		#Check if the camera is detected
		print("Checking camera connection...")
		response = os.popen("gphoto2 --auto-detect").read()
		if "Nikon DSC D3400" in response:
			print("Camera Connected.")
		else:
			print("Camera not detected. Please check the connection.")
			raise Exception("Camera connection failed")
			
	def capture_photo(self, user_name=None):
		# Set the sav path based on the user name, default to "captured_image.jpg" if no name is given
		save_path = f"~/photobooth_images/{user_name}.jpg" if user_name else self.default_save_path 
		print(f"Capturing photo for {user_name or'guest'} in {self.countdown_time} seconds")

		# Wait for the countdown
		time.sleep(self.countdown_time)
		
		# Capture the photo and save it to the path
		os.system(f"gphoto2 --capture-image-and-download --filename {save_path}")
		print(f"Photo captured and saved as {save_path}")
