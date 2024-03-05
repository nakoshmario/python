class FieldIndexError(IndexError):

    def __str__(self):
        return 'введено значение за границами игрового поля'