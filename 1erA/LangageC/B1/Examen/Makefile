.PHONY: all clean 

PROGS= multtab multtab2 ndigits  histogram courses intlist
CC=gcc
CFLAGS=
LDFLAGS=-lm

all: $(PROGS)

%: %.c
	$(CC) $(CFLAGS) -o $@ $< $(LDFLAGS)

%.s: %.c
	$(CC) -S $< 

clean:
	rm -f $(PROGS) *.s
