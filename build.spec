[app]

# (str) Title of your application
title = Soma Learning Game

# (str) Package name
package.name = soma_learning_game

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py live
source.dir = .

# (str) Application versioning (method 1)
version = 1.0

# (int) Minimum source code compatibility
osx.python_version = 3

# (str) Custom source folders for requirements (Separate folders with a comma)
source.include_exts = py,png,jpg,kv,atlas,json,mp3

# (str) Application author's name
author = Your Name

# (str) Application author's email
author.email = your@email.com

# (str) URL of your application homepage (optional)
homepage = https://www.example.com

# (str) Application license
license = MIT

# (str) Description
description = Educational game for kids.

# (list) Application requirements
requirements = kivy==2.0.0, pygame

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) List of service to declare
services = Name, Name2

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (str) Presplash of the application
presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
icon.filename = %(source.dir)s/data/icon.png

# (str) Supported arches of bin (x86, x86_64, armeabi-v7a, arm64-v8a)
arch = armeabi-v7a

# (str) Permissions
android.permissions = INTERNET

# (list) Application meta-data to include/exclude
android.meta_data = key1=value1,key2=value2

# (list) Android assets directories
# android.assets = /path/to/your/assets

# (bool) If True the application will load without a connection to the internet
require.network = True

# (str) Change the Android logcat verbosity (error, warning, info, debug, verbose)
logcat_filter = *:S

# (str) Android logcat logs redirection
logcat = ~/logs.txt

# (list) Pattern to whitelist for the blacklist/whitelist support (deprecated)
# whitelist =

# (str) Domain of the signing key (alternative keystore provider)
# keystore.domain = %(app.package_domain)s

# (str) Keystore type (alternative keystore provider)
# keystore.type = %(app.package_domain)s

# (str) Keystore alias (alternative keystore provider)
# keystore.alias = %(app.package)

# (str) URL for the signing key (alternative keystore provider)
# keystore.url = https://example.com/keys/%(app.package).keystore
