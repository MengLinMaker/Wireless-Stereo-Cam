import cv2
import requests
import time



def setControl(url:str, var:str, val:str):
  try:
    requests.get(f"{url}/control?var={var}&val={val}")
    print(f"Successfully set - {var}: {val}")
  except:
    print(f"Cannot set - {var}': '{val}")



def requestStream(camUrl):
  videoStream = cv2.VideoCapture(camUrl + ":81/stream")
  videoStream.set(cv2.CAP_PROP_BUFFERSIZE, 0)
  #videoStream.set(cv2.CAP_PROP_FPS, 10)
  return videoStream



if __name__ == '__main__':
  rightCamUrl = "http://192.168.20.16"
  leftCamUrl = "http://192.168.20.19"

  rightCamResponse = requestStream(rightCamUrl)
  leftCamResponse = requestStream(leftCamUrl)

  frameSize = 1
  setControl(rightCamUrl, "framesize", f"{frameSize}")
  setControl(leftCamUrl, "framesize", f"{frameSize}")

  xclk = 20
  setControl(rightCamUrl, "xclk", f"{xclk}")
  setControl(leftCamUrl, "xclk", f"{xclk}")

  while True:
    time.sleep(0.1)
    if rightCamResponse.isOpened():
      dummy, rightFrame = rightCamResponse.read()
      cv2.imshow("Right Camera", rightFrame)

    if leftCamResponse.isOpened():
      dummy, leftFrame = leftCamResponse.read()
      cv2.imshow("Left Camera", leftFrame)

    if cv2.waitKey(1) == 27:
      break

  cv2.destroyAllWindows()

  rightCamResponse.release()
  leftCamResponse.release()