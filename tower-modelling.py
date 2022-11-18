import cv2
import ndjson
import numpy
from matplotlib import pyplot as plt

class TowerModelling: 
    def __init__(self, path): 
        self.path = path 

    def read(self): 
        with open(self.path, 'r') as f:
            __data = ndjson.load(f)[:200] 

            for __i in __data:
                __image = __i['drawing'] 

                __img = numpy.zeros((256, 256, 3), numpy.uint8) #
                __img.fill(255) 

                for __j in __image: 
                    for __k in range(len(__j[0])-1): 
                        cv2.line(__img, (__j[0][__k], __j[1][__k]), (__j[0][__k+1], __j[1][__k+1]), (0, 0, 0), 1)

                plt.imshow(__img) 
                plt.savefig('./images2/' + __i['key_id'] + '.png') 
            
            return __data 
    
    def show_information(self, data): 
        print("Number of images: ", len(data)) 
        print("Number of labels: ", len(data[0]['word']))
        print("Labels: ", data[0]['word']) 
        print("Image: ", data[0]['drawing']) 
    

if __name__ == '__main__': 
    path = './Tower.ndjson' 
    tower = TowerModelling(path)
    data = tower.read() 
    tower.show_information(data) 


    
        
