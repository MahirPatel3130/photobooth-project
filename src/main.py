from camera_controller import CameraController
from overlay_processor import OverlayProcessor
from printer_manager import PrinterManager 

def main():
    camera = CameraController()
    overlay_processor = OverlayProcessor(background_path="assets/ScottyClause.jpg")
    printer_manager = PrinterManager(printer_name="Canon_SELPHY_CP1500")

    try:
        camera.connect_camera()  # Verify connection
        camera.capture_photo()  # Capture photo
        overlay_processor.apply_overlay("photobooth_images/captured_image.jpg")  # Apply overlay
        printer_manager.print_image("overlayed_photobooth_images/final_image.jpg")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
