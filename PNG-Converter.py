from PIL import Image

ImgPath = input('Enter Image Path: ')

try:     
    ImgPath = ImgPath.replace('"','') # Remove Quotation Marks

    myImg = Image.open(ImgPath).convert('RGB') # Convert to 24Bit

    myImg.save('24Bit.png')

except:   
    print('Invalid Image (' + str(ImgPath) + ')!')
