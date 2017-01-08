##### Win32 variables #####

WIN32_HMAP_EXE=hmap2.exe
WIN32_LDFLAGS=-Wl,--large-address-aware -Wl,--stack,16777216 -lwinmm

##### Unix variables #####

UNIX_HMAP_EXE=hmap2
UNIX_LDFLAGS=-lpthread -lm

##### Common variables #####

HMAPOBJECTS= cmdlib.o mathlib.o bspfile.o mem.o winding.o scriptlib.o \
    brush.o csg4.o faces.o map.o outside.o portals.o \
    qbsp.o solidbsp.o tjunc.o tree.o writebsp.o \
    wad.o bsp2prt.o bspinfo.o vis.o vis_flow.o vis_sound.o light.o \
    light_face.o light_trace.o threads.o

CC=gcc
CFLAGS=-MD -Wall -O2
#CFLAGS=-MD -Wall -g -ggdb

##### Commands #####

.PHONY: all mingw clean

all:
ifdef windir
	$(MAKE) HMAP_EXE=$(WIN32_HMAP_EXE) LDFLAGS="$(WIN32_LDFLAGS)" $(WIN32_HMAP_EXE)
else
	$(MAKE) HMAP_EXE=$(UNIX_HMAP_EXE) LDFLAGS="$(UNIX_LDFLAGS)" $(UNIX_HMAP_EXE)
endif

mingw:
	$(MAKE) HMAP_EXE=$(WIN32_HMAP_EXE) LDFLAGS="$(WIN32_LDFLAGS)" $(WIN32_HMAP_EXE)

.c.o:
	$(CC) $(CFLAGS) -c $*.c -o $*.o

$(HMAP_EXE): $(HMAPOBJECTS)
	$(CC) -o $@ $^ $(LDFLAGS)

clean:
ifdef windir
	del $(WIN32_HMAP_EXE)
	del *.o
	del *.d
else
	rm -f $(WIN32_HMAP_EXE) $(UNIX_HMAP_EXE) *.[od]
endif

.PHONY: clean

-include *.d
