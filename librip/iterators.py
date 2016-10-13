# Итератор для удаления дубликатов
from types import *
class Unique(object):
    def __init__(self, items, **kwargs):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковые строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ разные строки
        #           ignore_case = False, Aбв и АБВ одинаковые строки, одна из них удалится
        # По-умолчанию ignore_case = False
        if type(items)==GeneratorType:
            items=list(items)
        self.lst = items
        self.size = len(items)-1
        self.index = 0
        self.prev=list()
        self.ignore_case = False
        for k,v in kwargs.items():
            if k=='ignore_case' and v==True:
                self.ignore_case=True


    def __next__(self):
        # Нужно реализовать __next__
        while (True):
            if self.index > self.size:
                raise StopIteration
            if self.ignore_case:
                if not str(self.lst[self.index]).upper() in self.prev:
                    self.prev.append(str(self.lst[self.index]).upper())
                    return self.lst[self.index]
            else:
                if not self.lst[self.index] in self.prev:
                    self.prev.append(self.lst[self.index])
                    return self.lst[self.index]
            self.index += 1



    def __iter__(self):
        return self
