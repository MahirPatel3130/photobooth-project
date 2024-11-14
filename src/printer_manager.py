import cups

class PrinterManager:
    def __init__(self, printer_name="Canon_SELPHY_CP1500"):
        self.conn = cups.Connection()
        self.printer_name = printer_name
        
        # Check if the specified printer is available
        if not self.is_printer_connected():
            raise ValueError(f"Printer '{self.printer_name}' not found. Please check the connection.")

    def is_printer_connected(self):
        # Get the list of printers
        printers = self.conn.getPrinters()
        # Check if the specified printer is available
        return self.printer_name in printers

    def print_image(self, image_path):
        """
        Prints the specified image on the connected printer.
        """
        if not self.is_printer_connected():
            print("Printer is not connected.")
            return

        # Print the file
        print(f"Printing {image_path} on {self.printer_name}...")
        self.conn.printFile(self.printer_name, image_path, "Photo Print", {})

    def list_printers(self):
        """
        Lists all available printers.
        """
        printers = self.conn.getPrinters()
        for printer in printers:
            print(f"Printer found: {printer}")
        return list(printers.keys())

    def set_printer(self, printer_name):
        """
        Sets a different printer by name.
        """
        self.printer_name = printer_name
        if not self.is_printer_connected():
            raise ValueError(f"Printer '{self.printer_name}' not found.")
        print(f"Printer set to: {self.printer_name}")
