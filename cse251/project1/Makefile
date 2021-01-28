CC := gcc
LIBS := -lm
CFLAGS := -Wall -Werror

TARGET=proj1
SRC=proj1.c

$(TARGET): $(SRC)
	$(CC) -o $(TARGET) $(CFLAGS) $(LIBS) $(SRC)

.PHONY: clean
clean:
	rm -rf $(TARGET)
