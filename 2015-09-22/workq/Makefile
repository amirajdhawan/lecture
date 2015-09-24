.PHONY: test

test: workq
	./workq 4

workq: workq.o 
	$(CC) -o $@ $^ -lpthread -lm -std=c11 

%.o: %.c
	$(CC) -c -O3 $< -std=c11 

clean:
	rm -f *.o workq
