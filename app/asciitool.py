from PIL import Image
import numpy as np

gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

def map_matrix_gscale(normalised_array):
    height, width = normalised_array.shape
    string_array = np.empty((height, width)).astype('str')
    for i in range(height):
        for j in range(width):
            string_array[i][j] = gscale1[normalised_array[i][j]]
    return string_array


def scale_matrix(image_array):
    return (image_array*(len(gscale1)-1)).astype('int')

def average_image(image: Image, width: int, height: int):
    average_array = np.empty((height, width))
    image_array = np.array(image)
    for i in range(height):
        for j in range(width):
            average_array[i][j] = np.mean(image_array[i][j])/255
    return average_array

def writeStringToFile(string_matrix, outputFilePath):
    file = open(outputFilePath, "w")
    for row in string_matrix:
        file.write(''.join(row)+'\n')

def writeString(string_matrix):
    ans = ""
    for row in string_matrix:
        ans += (''.join(row)+'\n')
    return ans
def imageToAscii(file):
    print(type(file))
    im = Image.open(file)
    rgb_im = im.convert('RGB')
    width, height = rgb_im.size
    average_im = average_image(rgb_im, int(width), int(height))
    normalized_matrix = scale_matrix(average_im)
    string_matrix = map_matrix_gscale(normalized_matrix)

    ascii_art = writeString(string_matrix)

    return ascii_art

