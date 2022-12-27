import requests
import cv2
import numpy as np



async def requestImage(camUrl):
  imageResponse = requests.get(f'{camUrl}/capture', stream=True).raw
  image = np.asarray(bytearray(imageResponse.read()), dtype="uint8")
  return cv2.imdecode(image, cv2.IMREAD_COLOR)



if __name__ == "__main__":
  rightCamUrl = "http://192.168.20.16"
  leftCamUrl = "http://192.168.20.19"

  for i in range(10):
    rightImage = requestImage(rightCamUrl)
    leftImage = requestImage(leftCamUrl)

  # Show images
  cv2.imshow('Right Image',rightImage)
  cv2.imshow('Left Image',leftImage)
  cv2.waitKey(0)
  cv2.destroyAllWindows()