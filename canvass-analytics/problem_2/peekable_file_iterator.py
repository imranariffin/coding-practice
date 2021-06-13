class PeekableFileIterator:
    def __init__(self, file):
        self.file = file

    def is_empty(self) -> bool:
        return self.peek() == ""

    def pop(self) -> str:
        line = self.file.readline()
        next_pos = self.file.tell()
        self.file.seek(next_pos)
        return line
    
    def next(self) -> None:
        self.file.readline()
        next_pos = self.file.tell()
        self.file.seek(next_pos)

    def peek(self) -> str:
        last_pos = self.file.tell()
        line = self.file.readline()
        self.file.seek(last_pos)
        return line
    
    def close(self) -> None:
        self.file.close()


if __name__ == "__main__":
    with open("./test.csv", "w") as f:
        f.writelines(
            "Line 1\n"
            "Line 2\n"
            "Line 3\n"
        )
    with open("./test.csv", "r") as f:
        file_iter = PeekableFileIterator(file=f)
        while not file_iter.is_empty():
            cmd = int(input("1 to Peek or 2 to Pop: "))
            if cmd == 1:
                print(file_iter.peek())
            else:
                print(file_iter.pop())
        file_iter.close()
    import os
    os.remove("./test.csv")
