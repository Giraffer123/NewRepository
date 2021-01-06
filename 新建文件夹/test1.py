from graphics import *
from tkinter.filedialog import askopenfilename


def main():
    filename = askopenfilename()
    image1 = Image(Point(100, 100), filename)
    print(image1.getWidth())
    print(image1.getHeight())
    for i in range(image1.getWidth()):
        for j in range(image1.getHeight()):
            r, g, b = image1.getPixel(i, j)
            bright = int(round(0.299 * r + 0.587 * g + 0.114 * b))
            image1.setPixel(i, j, color_rgb(bright, bright, bright))

    image1.save("test.ppm")


main()