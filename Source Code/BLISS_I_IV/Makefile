BIN	= bliss
OBJS	= ntt32.o distribution.o notrandom.o sha3.o main.o \
	bliss.o bliss_param.o pubpriv.o
DIST	= hilabliss

CC	= gcc
CFLAGS	= -Wall -Ofast 
LIBS	= -lm
LDFLAGS	=
INCS	=

$(BIN): $(OBJS)
	$(CC) $(LDFLAGS) -o $(BIN) $(OBJS) $(LIBS)

.c.o:
	$(CC) $(CFLAGS) $(INCS) -c $< -o $@

clean:
	rm -rf $(DIST)-*.txz $(OBJS) $(BIN) *~

dist:	clean
	cd ..; \
	tar cfvJ $(DIST)/$(DIST)-`date -u "+%Y%m%d%H%M00"`.txz $(DIST)/*
