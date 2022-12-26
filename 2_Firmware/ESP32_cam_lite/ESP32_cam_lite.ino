// Copyright 18/12/2022 Meng Lin - https://github.com/MengLinMaker
// Licensed under the Apache License, Version 2.0 (the "License");
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Stripped down 

#include <Arduino.h>
#include <WiFi.h>

#include "esp_camera.h"
#include "camera_pins.h"



// Enter sensitive information or import from an env.h file
#ifndef WIFI_SSID || WIFI_PASSWORD
  #include "env.h"
#endif
const char* ssid = WIFI_SSID;
const char* password = WIFI_PASSWORD;

// Declare if index page is needed
// #define INCLUDE_INDEX_HTML




// Declare function before use
void startCameraServer();

void setup() {
  // Enable serial for debugging
  Serial.begin(1000000);
  Serial.setDebugOutput(true);
  
  // Attempt to connect to WiFi
  WiFi.begin(ssid, password);
  WiFi.setSleep(false);
  Serial.print("Connecting to WiFi");
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }


  
  camera_config_t config;
  // Define camera pin map to esp32
  config.pin_d0 = Y2_GPIO_NUM;
  config.pin_d1 = Y3_GPIO_NUM;
  config.pin_d2 = Y4_GPIO_NUM;
  config.pin_d3 = Y5_GPIO_NUM;
  config.pin_d4 = Y6_GPIO_NUM;
  config.pin_d5 = Y7_GPIO_NUM;
  config.pin_d6 = Y8_GPIO_NUM;
  config.pin_d7 = Y9_GPIO_NUM;
  config.pin_xclk = XCLK_GPIO_NUM;
  config.pin_pclk = PCLK_GPIO_NUM;
  config.pin_vsync = VSYNC_GPIO_NUM;
  config.pin_href = HREF_GPIO_NUM;
  config.pin_sscb_sda = SIOD_GPIO_NUM;
  config.pin_sscb_scl = SIOC_GPIO_NUM;
  config.pin_pwdn = PWDN_GPIO_NUM;
  config.pin_reset = RESET_GPIO_NUM;

  // Default esp32 cam settings
  config.xclk_freq_hz = 10000000;
  config.frame_size = FRAMESIZE_HVGA;
  config.pixel_format = PIXFORMAT_JPEG;
  config.grab_mode = CAMERA_GRAB_WHEN_EMPTY;
  config.fb_location = CAMERA_FB_IN_DRAM;
  config.jpeg_quality = 6;
  config.fb_count = 1;

  // Initialise camera
  esp_err_t err = esp_camera_init(&config);
  if (err != ESP_OK) {
    Serial.printf("Camera init failed with error 0x%x", err);
    return;
  }

  // Start camera
  startCameraServer();
  Serial.print("\nCamera Ready! Use 'http://");
  Serial.print(WiFi.localIP());
  Serial.println("' to connect");

  // Take pictures to adjust auto config
  for (int i = 0; i < 5; i++) {
    esp_camera_fb_get();
  }
}

void loop() {}