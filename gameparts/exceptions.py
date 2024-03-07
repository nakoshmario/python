class FieldIndexError(IndexError):

    def __str__(self):
        return 'введено значение за границами игрового поля'
class CelloccupiedError(Exception):
    def __str__(self):
        return 'попытка изменить занятую строчку'