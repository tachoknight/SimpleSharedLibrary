# SimpleSharedLibrary
Just a simple project to show how to create a C-based shared library and call it from a C program.

# Why?
I have the occasional need to have a program that calls a shared library to test something (e.g. RPM packaging). This project saves me the time from having to write a throwaway, nothing program whose functionaly is irrelvant but the components are (i.e. the shared library and the main executable). I've had this project in one form or another for years and decided it was easier to just grab it from GitHub than from somewhere else.

I hope this provides some utility for others as well.

# Usage
Assuming you have a working C compiler and Make installed, just clone this repo and run `make`. You'll also likely need to add `export LD_LIBRARY_PATH=.:$LD_LIBRARY_PATH` before running the program so it can find the shared library (`libadd.so`).
