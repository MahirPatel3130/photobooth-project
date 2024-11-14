from PIL import Image
from numpy import array, all

class OverlayProcessor:
	def __init__(self, background_path):
		self.background_path = background_path
		
	def apply_overlay(self, image_path, output_path="overlayed_photobooth_images/final_image.jpg"):
		background_image = Image.open(self.background_path).convert("RGBA")
		overlay = Image.open(image_path).convert("RGBA")
		
		fg_data = array(overlay)

		green_min = array([0, 100, 0, 255])   # Minimum shade of green
		green_max = array([150, 255, 150, 255])  # Maximum shade of green

		mask = all((fg_data[:, :, :3] >= green_min[:3]) & (fg_data[:, :, :3] <= green_max[:3]), axis=-1)
		fg_data[mask] = [0, 0, 0, 0]

		transparent_foreground = Image.fromarray(fg_data)
		background_image = background_image.resize(transparent_foreground.size)
		result = Image.alpha_composite(background_image, transparent_foreground).convert("RGB")

		result.save(output_path)
		print(f"Overlay applied and saved as {output_path}")

