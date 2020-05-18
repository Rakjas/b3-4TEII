all: libwrap.so.1.0.1 libwrap.so.1

libwrap.so.1.0.1: wrapper.c wrapper.h
	gcc -Wall -c -fPIC -g wrapper.c
	gcc -shared -Wl,-soname,libwrapper.so.1 -o libwrapper.so.1.0.1 wrapper.o

libwrap.so.1: libwrapper.so.1.0.1
	ln -s libwrapper.so.1.0.1 libwrapper.so.1

clean:
	rm -fr libwrapper.so.1.0.1 libwrapper.so.1 wrapper.o *~ 
