
class MinhLista(list):
    def append(self, *args) -> None:
        return self.extend(args)


l = MinhLista()
l.append(1)
print(l)
l.append(2, 3, 4, 5, 6, 7)
print(l)