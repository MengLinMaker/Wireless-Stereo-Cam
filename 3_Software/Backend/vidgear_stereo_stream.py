import cv2
import requests
import time
from vidgear.gears import CamGear



def setControl(url:str, var:str, val:str):
  try:
    requests.get(f"{url}/control?var={var}&val={val}")
    print(f"Successfully set - {var}: {val}")
  except:
    print(f"Cannot set - {var}': '{val}")



def requestStream(camUrl):
  videoStream = CamGear(source = f"{camUrl}:81/stream").start()
  return videoStream



if __name__ == '__main__':
  rightCamUrl = "http://192.168.20.16"
  leftCamUrl = "http://192.168.20.19"

  rightCamResponse = requestStream(rightCamUrl)
  leftCamResponse = requestStream(leftCamUrl)
  #rightCamResponse = CamGear(0).start()


  frameSize = 1
  setControl(rightCamUrl, "framesize", f"{frameSize}")
  setControl(leftCamUrl, "framesize", f"{frameSize}")

  xclk = 20
  setControl(rightCamUrl, "xclk", f"{xclk}")
  setControl(leftCamUrl, "xclk", f"{xclk}")

  while True:
    rightFrame = rightCamResponse.read()
    cv2.imshow("Right Camera", rightFrame)

    leftFrame = leftCamResponse.read()
    cv2.imshow("Left Camera", leftFrame)

    if cv2.waitKey(1) == 27:
      break

  cv2.destroyAllWindows()

  rightCamResponse.stop()
  leftCamResponse.stop()
