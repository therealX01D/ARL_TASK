import pandas as pd
import numpy as np 
from PIL import Image
inputd = pd.read_csv("driving_log.csv")
outputd = pd.DataFrame()
def image_to_array(path):
    img = Image.open(path).convert('L')
    img_array = np.asarray(img)
    #
    #img_array = np.asarray(img_array.flatten())
    #print(img_array.shape)

    #reshape((320,160,3))
    return img_array

outputd["centerimg"] =inputd["centerimg"].apply(image_to_array).to_numpy()
outputd["leftimg"] = inputd["leftimg"].apply(image_to_array).to_numpy()
outputd["rightimg"] = inputd["rightimg"].apply(image_to_array).to_numpy()
outputd["steering"] = inputd["steering"]
outputd["throttle"] = inputd["throttle"]
outputd["reverse"] = inputd["reverse"]
outputd["speed"] = inputd["speed"]
outputd.to_pickle("file.pkl")  
print(outputd.head())
