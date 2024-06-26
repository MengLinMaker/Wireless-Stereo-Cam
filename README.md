# Wireless-Stereo-Cam
THIS PROJECT IS TEMPORARILY ON HOLD. THE ESP32 CAMS OVERHEATED AND THE CAMERAS ARE NO LONGER RESPONDING.

A stero cam for 3D reconstruction using two wireless ESP32 OV2640 cam modules. These modules were chosen due to the much lower price compared to dual camera modules.



## URI
These APIs use HTTP GET requests at `http://<IP_ADDRESS>/`.

#### Port 80
* `/` - Controller html page (disabled by default)
* `/capture` - Get JPG snapshot
* `/status` - Get setting values in JSON format
  * Example return data:
 `{"lamp":0,"autolamp":0,"min_frame_time":0,"framesize":9,"quality":10,"xclk":8,"brightness":0,"contrast":0,"saturation":0,"sharpness":0,"special_effect":0,"wb_mode":0,"awb":1,"awb_gain":1,"aec":1,"aec2":0,"ae_level":0,"aec_value":204,"agc":1,"agc_gain":0,"gainceiling":0,"bpc":0,"wpc":1,"raw_gma":1,"lenc":1,"vflip":1,"hmirror":1,"dcw":1,"colorbar":0,"cam_name":"ESP32 test camera","code_ver":"Mar 10 2022 @ 14:00:45","rotate":"0","stream_url":"http://10.0.0.181:81/"}`
* `/control?var=<SETTING_NAME>&val=<NEW_VALUE>` - Set `SETTING_NAME` to `NEW_VALUE`. Refer to `/status`

#### Port 81
* `/stream` - Streaming video

#### Settings
```
framesize       - See below
quality         - 10 to 63
contrast        - -2 to 2
brightness      - -2 to 2
saturation      - -2 to 2
special_effect  - 0=No Effect, 1=Negative, 2=Grayscale, 3=Red Tint, 4=Green Tint, 5=Blue Tint, 6=Sepia
awb             - 0 = disable, 1 = enable
awb_gain        - 0 = disable, 1 = enable
wb_mode         - if awb enabled: 0=Auto, 1=Sunny, 2=Cloudy, 3=Office, 4=Home
aec             - 0 = disable, 1 = enable
aec_value       - 0 to 1200
aec2            - 0 = disable, 1 = enable
ae_level        - -2 to 2
agc             - 0 = disable, 1 = enable
agc_gain        - 0 to 30
gainceiling     - 0 to 6
bpc             - 0 = disable, 1 = enable
wpc             - 0 = disable, 1 = enable
raw_gma         - 0 = disable, 1 = enable
lenc            - 0 = disable, 1 = enable
hmirror         - 0 = disable, 1 = enable
vflip           - 0 = disable, 1 = enable
dcw             - 0 = disable, 1 = enable
colorbar        - Overlays a color test pattern on the stream; integer, 1 = enabled
face_detect     - Face Detection; 1 = enabled, Only settable if framesize <= 4 (CIF)
face_recognize  - Face recognition; 1 = enabled, only settable if Face detection is already enabled
```


### Frame size
```
 0 - THUMB (96x96)
 1 - QQVGA (160x120)
 3 - HQVGA (240x176)
 5 - QVGA (320x240)
 6 - CIF (400x296)
 7 - HVGA (480x320)
 8 - VGA (640x480)
 9 - SVGA (800x600)
10 - XGA (1024x768)
11 - HD (1280x720)
12 - SXGA (1280x1024)
13 - UXGA (1600x1200)
```



## Credits
This project could not be completed without the help of these sources:
* [easytarget/esp32-cam-webserver](https://github.com/easytarget/esp32-cam-webserver/blob/master/API.md) - URI documentation help
