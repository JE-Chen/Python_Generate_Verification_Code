import random
import os
import base64

from io import BytesIO
from PIL import Image,ImageDraw,ImageFont

class Generate():

    def Generate_Color(self,R=255,G=255,B=255):
        """
        :param R: Color R
        :param G: Color G
        :param B: Color B
        :return: R,G,B
        """
        return random.randint(0,R),random.randint(0,G),random.randint(0,B)

    def Generate_Picture(self,Width=175,Height=55):
        """
        :param Width: Image Width
        :param Height: Image Height
        :return: Picture with color
        """
        return Image.new('RGB',(Width,Height),self.Generate_Color())

    def Generate_String(self):
        Num = str(random.randint(0,9))
        Low_Aplha = chr(random.randint(97,122))
        return random.choice([Num,Low_Aplha])

    def Generate_Code(self,Count,Image,Font_Size):
        """
        :param Count: Code Count
        :param Image: Draw Code Image
        :param Font_Size: Font's size
        :return: Code picture
        """
        Draw = ImageDraw.Draw(Image)
        Font_File = os.path.join('../Font/arial.ttf')
        Font=ImageFont.truetype(Font_File,size=Font_Size)
        Temp=[]
        for i in range(Count):
            Chars=self.Generate_String()
            Draw.text((10+i*30,-2),Chars,self.Generate_Color(),Font)
            Temp.append(Chars)
        Vaild="".join(Temp)
        return Vaild,Image

    def Generate_Noise(self,Image,Width=175,Height=55,Line_Count=3,Point_Count=15):
        """
        :param Image: Noise Image
        :param Width: Image Width
        :param Height: Image Hieght
        :param Line_Count: Line's count
        :param Point_Count: Point's count
        :return: After Noise Image
        """

        Draw = ImageDraw.Draw(Image)

        #Draw Line
        for i in range(Line_Count):
            x1 = random.randint(0, Width)
            x2 = random.randint(0, Width)
            y1 = random.randint(0, Height)
            y2 = random.randint(0, Height)
            Draw.line((x1, y1, x2, y2), fill=self.Generate_Color())

            #Draw Point
            for i in range(Point_Count):
                Draw.point([random.randint(0, Width), random.randint(0, Height)], fill=self.Generate_Color())
                x = random.randint(0, Width)
                y = random.randint(0, Height)
                Draw.arc((x, y, x + 4, y + 4), 0, 90, fill=self.Generate_Color())

        return Image

    def Generate_Base64_Image(self,Save=False):

        Code_Image = self.Generate_Picture()
        Vaild,Code_Image = self.Generate_Code(5,Code_Image,40)
        Code_Image = self.Generate_Noise(Code_Image)

        if Save:
            Code_Image.save('Code_Image.png')

        Bytes = BytesIO()
        Code_Image.save(Bytes,'png')
        Data = Bytes.getvalue()
        Bytes.close()

        Encode64 = base64.b64encode(Data)
        Data = str(Encode64,encoding='utf-8')
        Image_Data = "data:image/jpeg;base64,{data}".format(data=Data)
        return Vaild,Image_Data

if __name__ == "__main__":
    g = Generate()
    print(g.Generate_Base64_Image(True))
