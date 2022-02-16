class ArrayList:
    def __init__(self) -> None:
        self.size = 0
        self.total = 10
        self.l = [None] * self.total

    def __check_grow_arr(self, new_size):
        if new_size <= self.total:
            return

        self.total *= 2
        new_l = [None] * self.total

        for i in range(len(self.l)):
            new_l[i] = self.l[i]

        self.l = new_l

    def __check_shrink_arr(self, new_size):
        if new_size > self.total * 0.25:
            return

        self.total //= 2
        new_l = [None] * self.total

        for i in range(self.size):
            new_l[i] = self.l[i]

        self.l = new_l

    def append(self, new_el) -> None:
        self.add(new_el, self.size)

    def add(self, new_el, new_i) -> None:
        if new_i > self.size:
            print("Error: Can't add at index {}, size is {}".format(
                new_i, self.size))
            return

        self.__check_grow_arr(self.size + 1)

        for i in range(self.size, new_i - 1, -1):
            if i == new_i:
                self.l[i] = new_el
            else:
                self.l[i] = self.l[i-1]

        self.size += 1

    def set(self, value, i):
        if i >= self.size:
            print("Error: Can't set index {}, size is {}".format(i, self.size))
            return
        self.l[i] = value

    def remove(self, i):
        if i < 0 or i >= self.size:
            print("Error: Can't remove index {}, out of bounds (0, {})".format(
                i, self.size - 1))
            return

        self.__check_shrink_arr(self.size - 1)

        for i in range(i, self.size):
            if i == self.size - 1:
                self.l[i] = None
            else:
                self.l[i] = self.l[i + 1]

        self.size -= 1

    def to_string(self):
        out = "[ "

        for el in self.l:
            if el is None:
                out += "None "
            else:
                out += str(el) + " "

        out += "]"

        return out


if __name__ == "__main__":
    test = ArrayList()

    for i in range(20):
        test.append(i)
        print(test.to_string())

    test.add("woah", 10)
    print(test.to_string())

    test.set("hehe", 13)
    test.set("wrong", 100)
    print(test.to_string())

    for i in range(15):
        test.remove(0)
        print(test.to_string())
