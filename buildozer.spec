[app]
title = Atik Avcisi
package.name = atik_avcisi
package.domain = org.atik

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,tflite,txt

version = 1.0

requirements = python3,kivy==2.3.0,numpy,pillow

orientation = portrait
fullscreen = 1

android.permissions = CAMERA,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,INTERNET
android.api = 33
android.minapi = 21
android.ndk = 28c
android.ndk_api = 21
android.archs = arm64-v8a
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
