class Product:
    def __init__(self, box_quantity, serial) -> None:
        self.box_quantity = box_quantity
        self.serial = serial

    def show_info(self):
        return "The product contains %s. The serial is: %s " % (self.box_quantity, self.serial)
