class ComplexNumber:
    def __init__(self, real_part, imag_part):
        self.real_part = real_part
        self.imag_part = imag_part
    def display_complex(self):
        print(str(self.real_part) + "+" + str(self.imag_part) + "i")

        