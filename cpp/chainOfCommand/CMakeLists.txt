cmake_minimum_required(VERSION 3.25)
project(chainOfCommand)

set(CMAKE_CXX_STANDARD 20)

add_executable(chainOfCommand main.cpp StringValidator.h UppercaseValidator.h NumberValidator.h LengthValidator.h)
