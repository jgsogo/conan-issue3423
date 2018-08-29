from conans import ConanFile, CMake, tools

class HelloConan(ConanFile):
     name = "issue3423-consumer"
     version = "0.0"

     requires = "issue3423/0.0@issue/test"

