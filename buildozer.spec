[app]
title = Cars Special
package.name = carsspecial
package.domain = org.example
version = 1.0
source.dir = .        # <- add this, points to your app source folder
requirements = python3,kivy==2.3.0,cython
orientation = portrait
android.permissions = INTERNET

# Replace deprecated field
p4a.bootstrap = sdl2    # <- instead of android.bootstrap

# Android versions
android.api = 33
android.minapi = 21
android.ndk = 25b
