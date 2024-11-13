# Makefile
CC = gcc
CFLAGS = -Wall -Wextra -Werror -fPIC
LDFLAGS = -shared
TARGET_LIB = libadd.so

all: main

$(TARGET_LIB): add.o
	$(CC) $(LDFLAGS) -o $(TARGET_LIB) add.o

add.o: add.c add.h
	$(CC) $(CFLAGS) -c add.c

main: main.o $(TARGET_LIB)
	$(CC) $(CFLAGS) -o main main.o -L. -ladd

main.o: main.c add.h
	$(CC) $(CFLAGS) -c main.c

clean:
	rm -f *.o *.so main

.PHONY: all clean
