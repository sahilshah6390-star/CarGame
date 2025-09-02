[app]
title = Cars Special
package.name = carsspecial
package.domain = org.example
version = 1.0
source.dir = .               # <- points to your app source folder
requirements = python3,kivy==2.3.0,cython
orientation = portrait
android.permissions = INTERNET
p4a.bootstrap = sdl2         # <- replaces deprecated android.bootstrap
android.api = 33
android.minapi = 21
android.ndk = 25b
