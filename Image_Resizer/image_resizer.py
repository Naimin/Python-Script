import cv2
import os
import sys

def resize_img(img_path, scale_factor):
    img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
    
    print('Original Dimensions : ',img.shape)

    width = int(img.shape[1] * scale_factor)
    height = int(img.shape[0] * scale_factor)
    dim = (width, height)
    
    # resize image
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    print('Resized Dimensions : ',resized.shape)
    
    return resized
    
def resize_folder(input_folder, output_folder, scale_factor):
    # for each image in the folder
    for file in os.listdir(input_folder):
        resized_img = resize_img(os.path.join(input_folder, file), scale_factor)
        # save the image in the output folder
        cv2.imwrite(os.path.join(output_folder, file), resized_img)
    
def main():
    args = sys.argv[1:]
    
    if len(args) != 3:
        print("Missing arguments!\nUsage: <input folder> <output folder> <scale factor>")
        return
    
    input_folder = args[0]
    output_folder = args[1]
    
    if input_folder == output_folder:
        print("Input folder can't be the same as output folder! Or it will overwrite the original file in the folder")
        return
    
    scale_factor = float(args[2])
    print(args)
    resize_folder(input_folder, output_folder, scale_factor)
    
if __name__== '__main__':
    main()