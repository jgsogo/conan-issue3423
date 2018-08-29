from conans import ConanFile, CMake, tools

class HelloConan(ConanFile):
     name = "issue3423"
     version = "0.0"
     scm = {
        "type": "git",
        "subfolder": "hello/to/you",
        "url": "auto",
        "revision": "auto"
     }

