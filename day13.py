import re
import numpy as np


def ocr_pixelchars(arr, width, height, image_path='ocr.png'):
    try:
        from PIL import Image
        import cv2
        import matplotlib.pyplot as plt
        from scipy.ndimage.filters import gaussian_filter
        import pytesseract
    except ImportError:
        print("Missing dependencies for OCR (PIL, cv2, matplotlib, scipy, pytesseract)")
        return npa_tostring(arr)
    upscaled_image = np.asarray(Image.fromarray(arr).resize([width*5, height*5], resample=Image.NEAREST))
    smoothed_image = gaussian_filter(upscaled_image, 1.7)
    plt.imsave(image_path, smoothed_image)
    pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"
    tessdata_dir_config = '--tessdata-dir "C:/Program Files/Tesseract-OCR/tessdata" --psm 10'
    data = pytesseract.image_to_string(cv2.imread(image_path), config=tessdata_dir_config)
    return data


def npa_tostring(arr):
    res = ""
    arr.transpose()
    for row in arr:
        rowres = ""
        for val in row:
            if val != 0:
                rowres += "#"
            else:
                rowres += " "
        if "#" in rowres:
            res += rowres + "\n"
    return res


def points_to_npa(points, value=1, margin=100):
    height = max(points,key=lambda item:item[1])[1]+margin+1
    width = max(points,key=lambda item:item[0])[0]+margin+1
    a = np.zeros((height, width))
    for point in points:
        a[point[1]+margin//2, point[0]+margin//2] = value
    return a, width, height


def main():
    points = set()
    folds = []
    with open('day13.txt', 'r') as f:
        for line in f.read().splitlines():
            numbers = re.findall("\d+", line)
            if len(numbers) == 2:
                points.add((int(numbers[0]), int(numbers[1])))
            elif len(numbers) == 1:
                folds.append((line.split()[-1][0], int(numbers[0])))

    firstfold = True
    for fold in folds:
        index = 0
        if fold[0] == "y":
            index = 1
        for point in list(points):
            if point[index] > fold[1]:
                new_point = list(point)
                new_point[index] = point[index]-(point[index] - fold[1])*2
                points.add(tuple(new_point))
                points.remove(point)
        if firstfold:
            print(f'part1: {len(points)}')
            firstfold = False

    npa, width, height = points_to_npa(points)
    print(f'part2: {ocr_pixelchars(npa, width, height, "day13.png")}')


if __name__ == "__main__":
    main()
