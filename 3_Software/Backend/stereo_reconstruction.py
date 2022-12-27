from sanic import Sanic
import requests
import cv2
import numpy as np



app = Sanic("stereo_reconstruction")



def requestImage(imageUrl):
  imageResponse = requests.get(f'{imageUrl}/capture', stream=True).raw
  image = np.asarray(bytearray(imageResponse.read()), dtype="uint8")
  return cv2.imdecode(image, cv2.IMREAD_COLOR)



if __name__ == "__main__":
  rightImageUrl = "http://192.168.20.16"
  leftImageUrl = "http://192.168.20.19"

  rightImage = requestImage(rightImageUrl)
  leftImage = requestImage(leftImageUrl)

  # Show images
  cv2.imshow('Right Image',rightImage)
  cv2.imshow('Left Image',leftImage)
  cv2.waitKey(0)
  cv2.destroyAllWindows()