import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np

def saddify(img):
    height, width, colors = img.shape
    power_of_change = 0.5
    reminder = 1 - power_of_change
    for i in range(0, height):
        for j in range(0, width):
            avg = (img[i, j, 0] + img[i, j, 1] + img[i, j, 2]) / 3
            img[i, j, 0] = img[i, j, 0] * reminder + avg * power_of_change
            img[i, j, 1] = img[i, j, 1] * reminder + avg * power_of_change
            img[i, j, 2] = img[i, j, 2] * reminder + avg * power_of_change

def happify(img):
    height, width, colors = img.shape
    power_of_change = 0.5
    reminder = 1 - power_of_change
    grayishness = 0.999
    for i in range(0, height):
        for j in range(0, width):
            if color_happiness(img, i, j)[0] > grayishness:
                if i != 0:
                   dominating_color = color_happiness(img, i - 1, j)
                else:
                    dominating_color = color_happiness(img, i, j)
                if i != height - 1 and dominating_color[0] < color_happiness(img, i + 1, j)[0]:
                    dominating_color[0] = color_happiness(img, i + 1, j)[0]                
                if j != 0 and dominating_color[0] < color_happiness(img, i, j - 1)[0]:
                    dominating_color[0] = color_happiness(img, i, j - 1)[0]
                if j != width - 1 and dominating_color[0] < color_happiness(img, i, j + 1)[0]:
                    dominating_color[0] = color_happiness(img, i, j + 1)[0]
                img[i, j, dominating_color[1]] = dominating_color[0] * power_of_change + img[i, j, dominating_color[1]] * reminder
                

def color_happiness(img, i, j):
    red   = 0 + (1 - img[i, j, 0]) - (1 - img[i, j, 1]) - (1 - img[i, j, 2])
    green = 0 - (1 - img[i, j, 0]) + (1 - img[i, j, 1]) - (1 - img[i, j, 2])
    blue  = 0 - (1 - img[i, j, 0]) - (1 - img[i, j, 1]) + (1 - img[i, j, 2])
    if (red >= green and red >= blue):
        return [1 - red, 0]
    if (green >= red and green >= blue):
        return [1 - green, 1]
    if (blue >= green and red <= blue):
        return [1 - blue, 2]

def show(original, altered):
    f, axarr = plt.subplots(1, 2)
    axarr[0].imshow(original)
    axarr[1].imshow(altered)
    plt.show()


original = mpimg.imread("obrazek.png")
altered = mpimg.imread("obrazek.png")
#saddify(altered)
happify(altered)
show(original, altered)
