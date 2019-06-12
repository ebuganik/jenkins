
app: hello_world.o printer.o
	gcc -o app.exe $^

hello_world.o: hello_world.c hello_world.h
	gcc -c -o hello_world.o $<

printer.o: printer.c printer.h
	gcc -c -o printer.o $<

