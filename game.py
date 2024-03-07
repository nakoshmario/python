from gameparts import Board
from gameparts.exceptions import FieldIndexError, CelloccupiedError

# крестики нолики




def main():
    game = Board()
    current_player = 'X'
    running = True
    game.display()

    while running:



        print(f'ход делает  {current_player}')
        while True:
            try:
                row = int(input('введите номер строки: '))
                if row < 0 or row >= game.field_size:                    
                 raise FieldIndexError
                column = int(input('введите номер столбика: '))
                if  column < 0 or column >= game.field_size:
                    raise FieldIndexError
                if game.board[row][column] != ' ':
                    raise CelloccupiedError
            except FieldIndexError:
                print("Неверный ввод, попробуйте еще раз.")     
            except ValueError:
                print("неверный формат ввода")
                print('буквы вводить нельзя')
                print('введите заново')
                continue
            except CelloccupiedError:
                print('ячейка занята, выберите другую')
            except Exception as e:
                print('ошибка',type(e).__name__)
            else:
                break



        game.make_move(row,column,current_player)
        game.display()

        if game.check_win(current_player):
            print(f'победили  {current_player}!')
            running = False
        elif game.is_board_full():
            print('ничья!')
            running=False
        current_player = 'O' if current_player == 'X' else 'X'
   

if __name__ == '__main__':
    main()


    