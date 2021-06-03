from PIL import Image, ImageFilter

PIZZA = Image.open("assets/PIZZA.jpeg")
FRITAS = Image.open("assets/FRITAS.jpeg")
HAMBUGUER = Image.open("assets/HAMBUGUER.jpeg")
COMBO = Image.open("assets/COMBO.jpeg")

image_blur = PIZZA.filter(ImageFilter.BLUR)
image_blur.save("assets/PIZZAblur.jpeg")

image_contour = FRITAS.filter(ImageFilter.CONTOUR)
image_contour.save("assets/FRITAScontour.jpeg")

image_details = HAMBUGUER.filter(ImageFilter.DETAIL)
image_details.save("assets/HAMBUGUERdetails.jpeg")

image_smooth = COMBO.filter(ImageFilter.SMOOTH)
image_smooth.save("assets/COMBOmooth.jpeg")

image_sharpen = PIZZA.filter(ImageFilter.SHARPEN)
image_sharpen.save("assets/PIZZAsharpen.jpeg")

image_emboss = COMBO.filter(ImageFilter.EMBOSS)
image_emboss.save("assets/COMBOemboss.jpeg")