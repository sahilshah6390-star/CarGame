[app]
# (str) Title of your application
title = Cars Special

# (str) Package name
package.name = carsspecial

# (str) Package domain (change your domain)
package.domain = org.example

# (str) Source code directory
source.dir = .

# (list) Application requirements
requirements = python3,kivy

# (str) Icon of your app
icon.filename = %(source.dir)s/icon.png

# (str) Supported orientation (portrait, landscape, all)
orientation = portrait

# (bool) Fullscreen
fullscreen = 0

[buildozer]
# (str) Path to buildozer
buildozer_dir = .

# (str) Android target
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b

[android]
# (bool) Use --private data storage
private_storage = True

# (str) Path to keystore (optional)
# android.keystore = %(source.dir)s/my.keystore
