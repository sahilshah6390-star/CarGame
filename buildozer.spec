[app]
# (str) Title of your application
title = Cars Special

# (str) Package name
package.name = carsspecial

# (str) Package domain
package.domain = org.example

# (str) Source code directory
source.dir = .

# (list) Application requirements
requirements = python3,kivy

# (str) Icon of your app (optional)
icon.filename = %(source.dir)s/icon.png

# (str) Supported orientation (portrait, landscape, all)
orientation = portrait

# (bool) Fullscreen
fullscreen = 0

# (str) Version of your app
version = 1.0.0

# (str) Entry point of your app
# (default is main.py)
# entrypoint = main.py

[buildozer]
# (str) Buildozer working directory
buildozer_dir = .

# (str) Log level (0=error,1=warning,2=info,3=debug,4=trace)
log_level = 2

[android]
# (bool) Use private data storage
private_storage = True

# (int) Android API to use
android.api = 33

# (int) Minimum API your app will support
android.minapi = 21

# (int) Android SDK version
android.sdk = 33

# (str) Android NDK version
android.ndk = 25b

# (bool) Do not use android SDK/NDK auto install
# android.sdk_path = /path/to/sdk
# android.ndk_path = /path/to/ndk

# (str) Presplash image (optional)
# presplash.filename = %(source.dir)s/presplash.png

# (bool) Sign APK (optional)
# android.keystore = %(source.dir)s/my.keystore
