[app]

# (str) Title of your application
title = LeBased

# (str) Package name
package.name = lebased

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,txt,db,otf,ttf

# (list) Source files to exclude (let empty to not exclude anything)
#source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anything)
#source.exclude_dirs = tests, bin, venv

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
requirements = python3,kivy,kivymd,sqlite3,requests

# (str) Custom source folders for requirements
# Sets custom source for any requirements with recipes
# requirements.source.kivy = ../../kivy

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (list) Supported orientations
# Valid options are: landscape, portrait, portrait-reverse or landscape-reverse
orientation = portrait

# (list) List of service to declare
#services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY

#
# OSX Specific
#

#
# author = © Copyright Info

# change the major version of python used by the app
osx.python_version = 3

# Kivy version to use
osx.kivy_version = 1.9.1

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (string) Presplash background color (for android toolchain)
# Supported formats are: #RRGGBB #AARRGGBB or one of the following names:
# red, blue, green, black, white, gray, cyan, magenta, yellow, lightgray,
# darkgray, grey, lightgrey, darkgrey, aqua, fuchsia, lime, maroon, navy,
# olive, purple, silver, teal.
#android.presplash_color = #FFFFFF

# (string) Presplash animation using Lottie format.
# see https://lottiefiles.com/ for examples and https://airbnb.design/lottie/
# for general documentation.
# Lottie files can be created using various tools, like Adobe After Effect or Synfig.
#android.presplash_lottie = "path/to/lottie/file.json"

# (str) Adaptive icon of the application (used if Android API level is 26+ at runtime)
#icon.adaptive_foreground.filename = %(source.dir)s/data/icon_fg.png
#icon.adaptive_background.filename = %(source.dir)s/data/icon_bg.png

# (list) Permissions
# (See https://python-for-android.readthedocs.io/en/latest/buildoptions/#build-options-1 for all the supported syntaxes and properties)
android.permissions = android.permission.INTERNET, (name=android.permission.WRITE_EXTERNAL_STORAGE)

# (list) features (adds uses-feature -tags to manifest)
#android.features = android.hardware.usb.host

# (int) Target Android API, should be as high as possible.
android.api = 31

# (int) Minimum API your APK / AAB will support.
android.minapi = 21

# (int) Android SDK version to use
#android.sdk = 20

# (str) Android NDK version to use
android.ndk = 23b

# (int) Android NDK API to use. This is the minimum API your app will support, it should usually match android.minapi.
android.ndk_api = 21

# (bool) Use --private data storage (True) or --dir public storage (False)
#android.private_storage = True

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
#android.ndk_path =

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
#android.sdk_path =

# (str) ANT directory (if empty, it will be automatically downloaded.)
#android.ant_path =

# (bool) If True, then skip trying to update the Android sdk
# This can be useful to avoid excess Internet downloads or save time
# when an update is due and you just want to test/build your package
# android.skip_update = False

# (bool) If True, then automatically accept SDK license
# agreements. This is intended for automation only. If set to False,
# the default, you will be shown the license when first running
# buildozer.
# android.accept_sdk_license = False

# (str) Android entry point, default is ok for Kivy-based app
#android.entrypoint = org.kivy.android.PythonActivity

# (str) Full name including package path of the Java class that implements Android Activity
# use that parameter together with android.entrypoint to set custom Java class instead of PythonActivity
#android.activity_class_name = org.kivy.android.PythonActivity

# (str) Extra xml to write directly inside the <manifest> element of AndroidManifest.xml
# use that parameter to provide a filename from where to load your custom XML code
#android.extra_manifest_xml = ./src/android/extra_manifest.xml

# (str) Extra xml to write directly inside the <manifest><application> tag of AndroidManifest.xml
# use that parameter to provide a filename from where to load your custom XML arguments:
#android.extra_manifest_application_arguments = ./src/android/extra_manifest_application_arguments.xml

# (str) Full name including package path of the Java class that implements Python Service
# use that parameter to set custom Java class which extends PythonService
#android.service_class_name = org.kivy.android.PythonService

# (str) Android app theme, default is ok for Kivy-based app
# android.apptheme = "@android:style/Theme.NoTitleBar"

# (list) Pattern to whitelist for the whole project
#android.whitelist =

# (str) Path to a custom whitelist file
#android.whitelist_src =

# (str) Path to a custom blacklist file
#android.blacklist_src =

# (list) List of Java .jar files to add to the libs so that pyjnius can access
# their classes. Don't add jars that you do not need, since extra jars can slow
# down the build process. Allows wildcards matching, for example:
# OUYA-ODK/libs/*.jar
#android.add_jars = foo.jar,bar.jar,path/to/more/*.jar

# (list) List of Java files to add to the android project (can be java or a
# directory containing the files)
#android.add_src =

# (list) Android AAR archives to add
#android.add_aars =

# (list) Put these files or directories in the apk assets directory.
# Either form may be used, and assets need not be in 'source.include_exts'.
# 1) android.add_assets = source_asset_relative_path
# 2) android.add_assets = source_asset_path:destination_asset_relative_path
#android.add_assets =

# (list) Put these files or directories in the apk res directory.
# The option may be used in three ways, the value may contain one or zero ':'
# Some examples:
# 1) A file to add to resources, legal resource names contain ['a-z','0-9','_']
# android.add_resources = my_icons/all-inclusive.png:drawable/all_inclusive.png
# 2) A directory, here  'legal_icons' must contain resources of one kind
# android.add_resources = legal_icons:drawable
# 3) A directory, here 'legal_resources' must contain one or more directories, 
# each of a resource kind:  drawable, xml, etc...
# android.add_resources = legal_resources
#android.add_resources =

# (list) Gradle dependencies to add
#android.gradle_dependencies =

# (bool) Enable AndroidX support. Enable when 'android.gradle_dependencies'
# contains an 'androidx' package, or any package from Kotlin source.
# android.enable_androidx requires android.api >= 28
#android.enable_androidx = True

# (list) add java compile options
# this can for example be necessary when importing certain java libraries using the 'android.gradle_dependencies' option
# see https://developer.android.com/studio/write/java8-support for further information
# android.add_compile_options = "sourceCompatibility = 1.8", "targetCompatibility = 1.8"

# (list) Gradle repositories to add {can be necessary for some android.gradle_dependencies}
# please enclose in double quotes 
# e.g. android.add_gradle_repositories = "maven { url 'https://kotlin.bintray.com/ktor' }"
#android.add_gradle_repositories =

# (list) packaging options to add 
# see https://google.github.io/android-gradle-dsl/current/com.android.build.gradle.internal.dsl.PackagingOptions.html
# can be necessary to solve conflicts in gradle_dependencies
# please enclose in double quotes 
# e.g. android.add_packaging_options = "exclude 'META-INF/proguard/androidx-annotations.pro'"
#android.add_packaging_options =

# (list) Java classes to add as activities to the manifest.
#android.add_activities = com.example.ExampleActivity

# (str) OUYA Console category. Should be one of GAME or APP
# If you leave this blank, OUYA support will not be enabled
#android.ouya.category = APP

# (str) Filename of OUYA Console icon. It must be a 732x412 png image.
#android.ouya.icon.filename = %(source.dir)s/data/ouya_icon.png

# (str) XML file to include as an intent filters in <activity> tag
#android.manifest.intent_filters =

# (str) launchMode to set for the main activity
#android.manifest.launch_mode = standard

# (list) Android additional libraries to copy into libs/armeabi
#android.add_libs_armeabi = libs/android/*.so
#android.add_libs_armeabi_v7a = libs/android-v7/*.so
#android.add_libs_arm64_v8a = libs/android-v8/*.so
#android.add_libs_x86 = libs/android-x86/*.so
#android.add_libs_mips = libs/android-mips/*.so

# (bool) Indicate whether the screen should stay on
# Don't forget to set the appropriate permission (android.permissions = WAKE_LOCK)
#android.wakelock = False

# (list) Android application meta-data to set (key=value format)
#android.meta_data =

# (str) python-for-android branch to use, defaults to master
p4a.branch = main

# (list) Android library project to add (will be added in the end of build.xml)
#android.library_references =

# (str) Android logcat filters to use
#android.logcat_filters = *:S python:D

# (bool) Copy library instead of making a libpymodules.so
#android.copy_libs = 1

# (list) The Android archs to build for, armeabi, armeabi-v7a, x86, mips
# In past, was `android.arch` as we were not supporting building multiple archs at the same time.
android.archs = arm64-v8a, armeabi-v7a

# (int) overrides automatic versionCode computation (used in build.gradle)
# this is not the same as the version number for the application version,
# it only matters if the application's versionCode number is specific.
# android.override_version_code = 123456

# (str) Custom package that will be passed to the versionCode computation.
# android.version_code = "1"

# (str) The build file to include in the final apk/aab, used to generate the manifest file
# android.build_file = ./build.gradle

# (str) The build file to include in the final apk/aab, used to generate the manifest file
# android.build_template = ./buildozer/build.gradle

# (str) Custom build template, used to build the package
# android.custom_build_template = ./src/buildozer/build.py

# (str) Java Home directory to use to compile the project. This should not be set
# unless you want to override the build tools directory.
# android.java_home =

# (str) A custom AndroidManifest.xml to include in the final apk/aab
# This will be merged into the main AndroidManifest.xml
# android.manifest_template = ./src/android/manifest.template

# (str) Android add resources using custom attributes
# android.add_resources_custom = True

# (list) provide custom font directory. This will be copied to assets/fonts/ 
# android.add_fonts_dir = fonts/

# (bool) Indicate if we want to filter Java bytecode, needed for non-python p4a modules.
# android.filter_java_bytecode = False

# (str) Configuration to build an apk/aab package, or to configure the platform,
# for example android is used by default.
# android.packaging_configuration = ./src/buildozer/config.json

# (str) Default build mode (debug|release)
#android.build_mode = release

# (str) Name of the java file to use as the base activity for our application
# It is recommended to leave this file to the default: org.kivy.android.PythonActivity
# android.java_activity_name = "PythonActivity"

# (list) Additional Java classes to include (to be compiled into classes.dex)
# android.add_class = src/java/org/example/MyClass.java

# (list) Additional .so files to include (to be added in libs/armeabi-v7a/ if an armeabi-v7a build)
# android.add_so_files = src/main/jniLibs/armeabi-v7a/libtesseract.so

# (str) The library files to include, separated by commas, similar to 'android.add_so_files' but for libraries.
# This is used to include native libraries built in C/C++ using jni.
# android.add_library_files = "libmylib.so"

# (list) A list of additional resources to include in the apk/aab.
# These will be placed in the assets/ directory.
# Example: android.add_assets = src/android/res/raw/mydata
# android.add_assets = src/android/res/raw/mydata:res/raw/mydata

# (str) Path to android build scripts directory.
# These will be included in the final apk/aab.
# android.build_scripts = ./src/buildozer/scripts

# (list) A list of additional xml files to include in the apk/aab.
# These will be placed in the res/xml/ directory.
# Example: android.add_resources = src/android/res/xml/myschema.xml
# android.add_resources = src/android/res/xml/myschema.xml:res/xml/myschema.xml

# (str) Path to a directory to store build artifacts.
# android.build_output_directory = ./buildozer_output

# (bool) Indicate whether you want the final apk/aab to be compressed.
# android.compress_final_package = True

# (str) Path to a directory to store temporary files.
# android.tmp_directory = ./buildozer_tmp

# (bool) Indicate whether to use "xgettext" or "msgfmt" commands for translations.
# If true, use xgettext to extract translation strings, otherwise use msgfmt to compile translations.
# android.use_gettext = False

# (bool) Indicate whether to enable ProGuard.
# android.enable_proguard = False

# (bool) Indicate whether to keep intermediate build artifacts.
# android.keep_intermediate_build_artifacts = False

# (str) Path to the buildozer artifacts directory.
# android.artifacts_directory = ./artifacts

# (str) Path to the buildozer logs directory.
# android.logs_directory = ./logs

# (str) Path to the buildozer packages directory.
# android.packages_directory = ./packages

# (bool) Enable the support for OpenCL.
# android.enable_opencl = False

# (str) Path to the directory containing assets to include in the apk/aab.
# android.assets_directory = ./assets

# (str) Path to the directory containing resources to include in the apk/aab.
# android.resources_directory = ./resources

# (str) Path to the directory containing libraries to include in the apk/aab.
# android.libraries_directory = ./libraries

# (str) Path to the directory containing Java files to include in the apk/aab.
# android.java_directory = ./java

# (str) Path to the directory containing build scripts to include in the apk/aab.
# android.build_scripts_directory = ./build_scripts

# (str) Path to the directory containing additional assets to include in the apk/aab.
# android.additional_assets_directory = ./additional_assets

# (str) Path to the directory containing additional resources to include in the apk/aab.
# android.additional_resources_directory = ./additional_resources

# (str) Path to the directory containing additional libraries to include in the apk/aab.
# android.additional_libraries_directory = ./additional_libraries

# (str) Path to the directory containing additional Java files to include in the apk/aab.
# android.additional_java_directory = ./additional_java

# (str) Path to the directory containing additional build scripts to include in the apk/aab.
# android.additional_build_scripts_directory = ./additional_build_scripts

# (bool) Indicate whether to enable debugging for Python code.
# android.enable_python_debugging = False

# (str) The build mode (debug|release) to use.
# android.build_mode = debug

# (list) A list of custom arguments to pass to the buildozer command.
# Example: android.buildozer_custom_args = "--profile=release"
# android.buildozer_custom_args = "--profile=release"

# (list) A list of custom arguments to pass to the build command.
# Example: android.build_custom_args = "--no-scripts"
# android.build_custom_args = "--no-scripts"

# (str) The package format (apk|aab) to build.
# android.package_format = apk

# (list) A list of custom arguments to pass to the build tool.
# Example: android.build_tool_custom_args = "--no-scripts"
# android.build_tool_custom_args = "--no-scripts"

# (bool) Indicate whether to enable debugging for Java code.
# android.enable_java_debugging = False

# (str) The build directory.
# android.build_directory = ./build

# (str) The output directory.
# android.output_directory = ./output

# (str) The temporary directory.
# android.tmp_directory = ./tmp

# (str) The assets directory.
# android.assets_directory = ./assets

# (str) The resources directory.
# android.resources_directory = ./resources

# (str) The libraries directory.
# android.libraries_directory = ./libraries

# (str) The Java directory.
# android.java_directory = ./java

# (str) The build scripts directory.
# android.build_scripts_directory = ./build_scripts

# (str) The additional assets directory.
# android.additional_assets_directory = ./additional_assets

# (str) The additional resources directory.
# android.additional_resources_directory = ./additional_resources

# (str) The additional libraries directory.
# android.additional_libraries_directory = ./additional_libraries

# (str) The additional Java directory.
# android.additional_java_directory = ./additional_java

# (str) The additional build scripts directory.
# android.additional_build_scripts_directory = ./additional_build_scripts

# (bool) Indicate whether to enable debugging for Python code.
# android.enable_python_debugging = False

# (bool) Indicate whether to enable debugging for Java code.
# android.enable_java_debugging = False

# (list) A list of custom arguments to pass to the build tool.
# Example: android.build_tool_custom_args = "--no-scripts"
# android.build_tool_custom_args = "--no-scripts"

# (str) The package format (apk|aab) to build.
# android.package_format = apk

# (bool) Indicate whether to enable the Android Bundle tool.
# android.enable_bundle_tool = False

# (bool) Indicate whether to use a custom build template.
# android.use_custom_build_template = False

# (str) The custom build template file to use.
# android.custom_build_template = buildozer/build.gradle.template

# (list) A list of custom arguments to pass to the build tool.
# Example: android.build_tool_custom_args = "--no-scripts"
# android.build_tool_custom_args = "--no-scripts"

# (list) A list of custom arguments to pass to the packaging tool.
# Example: android.packaging_tool_custom_args = "--no-sign"
# android.packaging_tool_custom_args = "--no-sign"

# (str) The name of the application to use in the final APK.
# android.app_name = MyKivyApp

# (str) The package name to use in the final APK.
# android.package_name = org.kivy.myapp

# (str) The version code to use in the final APK.
# android.version_code = 1

# (str) The version name to use in the final APK.
# android.version_name = 1.0

# (str) The minimum SDK version to use in the final APK.
# android.min_sdk_version = 21

# (str) The target SDK version to use in the final APK.
# android.target_sdk_version = 30

# (bool) Indicate whether to enable debugging for Python code.
# android.enable_python_debugging = False

# (bool) Indicate whether to enable debugging for Java code.
# android.enable_java_debugging = False

# (list) A list of custom arguments to pass to the buildozer command.
# Example: android.buildozer_custom_args = "--profile=release"
# android.buildozer_custom_args = "--profile=release"

# (list) A list of custom arguments to pass to the build command.
# Example: android.build_custom_args = "--no-scripts"
# android.build_custom_args = "--no-scripts

# (str) Path to the keystore file to use for signing the APK.
# android.keystore = ./my-release-key.keystore

# (str) The alias of the key to use for signing the APK.
# android.keystore_alias = my-key-alias

# (str) The password for the key to use for signing the APK.
# android.keystore_password = password

# (str) The password for the keystore to use for signing the APK.
# android.keystore_storepass = password

# (str) The signing key file to use for signing the APK.
# android.signing_key = ./my-release-key.jks

# (str) The alias of the key to use for signing the APK.
# android.signing_key_alias = my-key-alias

# (str) The password for the key to use for signing the APK.
# android.signing_key_password = password

# (str) The password for the signing key file to use for signing the APK.
# android.signing_key_storepass = password

# (str) Path to the directory containing buildozer artifacts.
# android.artifacts_directory = ./artifacts

# (str) Path to the directory containing buildozer logs.
# android.logs_directory = ./logs

# (str) Path to the directory containing buildozer packages.
# android.packages_directory = ./packages

# (bool) Indicate whether to enable debugging for Python code.
# android.enable_python_debugging = False

# (bool) Indicate whether to enable debugging for Java code.
# android.enable_java_debugging = False

# (list) A list of custom arguments to pass to the buildozer command.
# Example: android.buildozer_custom_args = "--profile=release"
# android.buildozer_custom_args = "--profile=release"

# (list) A list of custom arguments to pass to the build command.
# Example: android.build_custom_args = "--no-scripts"
# android.build_custom_args = "--no-scripts"

# (bool) Indicate whether to enable the Android Bundle tool.
# android.enable_bundle_tool = False

# (bool) Indicate whether to use a custom build template.
# android.use_custom_build_template = False

# (str) The custom build template file to use.
# android.custom_build_template = buildozer/build.gradle.template

# (list) A list of custom arguments to pass to the build tool.
# Example: android.build_tool_custom_args = "--no-scripts"
# android.build_tool_custom_args = "--no-scripts"

# (list) A list of custom arguments to pass to the packaging tool.
# Example: android.packaging_tool_custom_args = "--no-sign"
# android.packaging_tool_custom_args = "--no-sign"

# (str) The name of the application to use in the final APK.
# android.app_name = MyKivyApp

# (str) The package name to use in the final APK.
# android.package_name = org.kivy.myapp

# (str) The version code to use in the final APK.
# android.version_code = 1

# (str) The version name to use in the final APK.
# android.version_name = 1.0

# (str) The minimum SDK version to use in the final APK.
# android.min_sdk_version = 21

# (str) The target SDK version to use in the final APK.
# android.target_sdk_version = 30

# (bool) Indicate whether to enable debugging for Python code.
# android.enable_python_debugging = False

# (bool) Indicate whether to enable debugging for Java code.
# android.enable_java_debugging = False
