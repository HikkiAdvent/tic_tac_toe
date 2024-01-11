class FieldIndexError(IndexError):

    def __str__(self):
        return 'Введено значение за границами поля'


class CellOccupiedError(Exception):

    def __str__(self):
        return 'Эта ячейка уже занята'
