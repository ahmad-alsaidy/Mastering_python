from PIL import Image

my_image = Image.open(r"C:\Users\alsai\Documents\programming\Mastering_python\assignments\86_89\elzero-pillow.png")

box1 = (400, 0, 800, 400)

cropped1 = my_image.crop(box1)

grey1 = cropped1.convert("L")

# grey1.save(r"C:\Users\alsai\Documents\programming\Mastering_python\assignments\86_89\image1.png")

# -----------------
# -----------------

box2 = (0, 400, 1200, 800)

cropped2 = my_image.crop(box2)

grey2 = cropped2.convert("L")

grey2.rotate(180)

# grey2.save(r"C:\Users\alsai\Documents\programming\Mastering_python\assignments\86_89\image2.png")
