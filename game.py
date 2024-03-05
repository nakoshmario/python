from gameparts import Board
from gameparts.exceptions import FieldIndexError
# крестики нолики




def main():
    game = Board()
    game.display()
    row = int(input('введите номер строки: '))

    if row < 0 or row >= game.field_size:
        raise FieldIndexError
    column = int(input('введите номер столбика: '))
    if  column < 0 or column >= game.field_size:
        raise FieldIndexError
    game.make_move(row,column,'X')
    print('ход сделан!')
    game.display()

    while True:
            try:
                row = int(input('введите номер строки: '))
                if row < 0 or row >= game.field_size                        
                 raise FieldIndexError
                column = int(input('введите номер столбика: '))
                if  column < 0 or column >= game.field_size:
                    raise FieldIndexError
     
            except FieldIndexError:
                print("неверный формат ввода")
                print('буквы вводить нельзя')
                print('введите заново')
                continue
            except Exception as e:
                print('ошибка',type(e).__name__)



            

if __name__ == '__main__':
    main()


    