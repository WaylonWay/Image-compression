import os
import time 
from PIL import Image

import json

def options():#debugged
    start = input ("1.)Compress\n2.)decompressing\n")


    if "1" in start:
        input_filepath = input ("What is the flie path of the image you wish to compress?\n")
        compress(input_filepath)
        return 0 #output_file

    if "2" in start:
        input_filepath = input ("What is the flie path of the image you wish to decompress?\n")
        decompress(input_filepath)
        return 0# output_file

def compress(filepath):#debugging
    img = Image.open(filepath)
    px = img.load()  
    ImageX , ImageY  = img.size
    test = "the image is {}px by {}px"
    print(test.format(ImageX,ImageY)) 
    compressed_image = [[ImageX,ImageY]]
    X_Y_Value = ImageX * ImageY
    X = 0
    Y = 0 
    amount = 1
    #set values -1 because points start on 0
    ImageX = ImageX - 1
    ImageY = ImageY - 1
    #set current px color
    current_color = px[0,0]
    #set multiplyed value -1 because loop starts on 0
    for Z in range(X_Y_Value-1):
        #if it is on the last pixel 
        if X == ImageX:
            #set variables
            current_color = px[X,Y]
            previous_color = px[X-1,Y]
            #compare colors
            if current_color == previous_color:
                #if colors are the same add 1 to the amount of colors
                amount = amount + 1
                #change X value
                X = X + 1
            else:
                #if the colors are diffrent put the color and amount in the list
                compressed_image.append([amount,px[previous_color]])
                #reset the amount
                amount = 1
                #change X value
                X = X + 1
        #check if on last width pixel
        if X == ImageX:
            #reset the width 
            X = 0
            #change the Y claue to go down a row
            Y = Y - 1
        #check if its safe to use next color var
        if X < ImageX:
            #set variables
            current_color = px[X,Y]
            next_color = px[X+1,Y]
            if current_color == next_color:
                #if colors are the same add 1 to the amount of colors
                amount = amount + 1
                #change X value
                X = X + 1
            else:
                #check if X is on first pixel
                if X == 0:
                    #if the colors are diffrent put the color and amount in the list
                    compressed_image.append([amount,px[ImageX,Y-1]])
                    #reset the amount
                    amount = 1
                    #change X value
                    X = X + 1
                #if it is not on first pixel i can use the prv. color var rather than custom like above
                else:
                    #if the colors are diffrent put the color and amount in the list
                    compressed_image.append([amount,px[previous_color]])
                    #reset the amount
                    amount = 1
                    #change X value
                    X = X + 1
        

        
        
        




            
           
           
    
    with open('img.txt','w') as filehandle:
        json.dump(compressed_image, filehandle)

def decompress(filename):#debuged
    with open(filename,'r') as filehandler:
        
        decompression = json.load(filehandler)

        Height = decompression[0][1]
        Width = decompression[0][0]
        decompression.pop(0)
        Image.new(mode = 'RGB',size = (Width,Height)).save('new.png')
        img = Image.open('new.png', 'r') 
        Y = 0
        X = 0
        #for y in range(Height):

        for f in decompression:
                    
            if X >= Width:
                Y = Y + 1
                X = X - Width
            
            img.save('new.png')
            if f[0] > 1:
                print(f[0])
                while f[0] > 0:
                    r,g,b = f[1]
                    img.putpixel((X,Y),(r,g,b))
                    X = X + 1
                    f[0] = f[0] - 1
                    print(X,Y,r,g,b)
                    if X >= Width:
                        Y = Y + 1
                        X = X - Width
            else:
                r,g,b = f[1]
                img.putpixel((X,Y),(r,g,b))
                print(X,Y,r,g,b)
                X = X + 1
    return img.show()               

options()