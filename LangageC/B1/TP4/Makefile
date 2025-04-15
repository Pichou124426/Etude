.PHONY: all clean

PROGS= calc
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
