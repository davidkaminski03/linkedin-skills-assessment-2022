import barcode
from barcode.writer import ImageWriter
  
#Define content of the barcode as a string
text = '09405 5112 9837 0625 3164 03'
# number = "420141509405 5112 9837 0625 3164 03"
number = '81007123452112345678'

#Get the required barcode format
barcode_format = barcode.get_barcode_class('gs1_128')
#Generate barcode and render as image
my_barcode = barcode_format(number, writer=ImageWriter())
  
#Save barcode as PNG
my_barcode.save("generated_barcode")