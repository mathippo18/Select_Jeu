from .board import new_board, render, get_cell_distribution, get_legal_cell_changes, is_full
from .board import apply_cell_change, can_type_apply_cell_change, get_leading_player_type
from .cell import TYPE_WHITE, TYPE_BLACK, extract_positions
from .color import colorize, BOLD


def start():
    print("\n######### le jeu démarre ############\n")

    try:
        board = new_board(8, 8)
        # Black always start at reversi
        current_type = TYPE_BLACK

        print(render(board))

        while not is_full(board):

            print_score(get_cell_distribution(board))
            print_ask_board(board, current_type)

            while not apply_cell_change_from_ask_position(board, current_type):
                print("Position incorrecte, essaie a nouveau")

            if not is_full(board):
                reverse_player_type = get_reverse_player_type(current_type)
                if can_type_apply_cell_change(board, reverse_player_type):
                    current_type = reverse_player_type
                elif not can_type_apply_cell_change(board, current_type):
                    print("\nDésolé, il n'y a pas plus de possibilités...\n")
                    break
                else:
                    print("\nL'adversaire ne peut pas jouer, encore a toi!\n")

        print(render(board))
        winner_name = get_leading_player_type(board)
        print("\n#### Joueur {0} gagne !! ####\n".format(colorize(winner_name.upper(), BOLD)))

    except KeyboardInterrupt:
        print("\n\nAu revoir et a la prochaine !\n\n")

    except Exception as e:
        print("WFT, il y a une erreur imprevue, désolé \nMessage: {0}\n".format(str(e)))


def apply_cell_change_from_ask_position(board, cType):
    """ Ask for position and attempt to apply cell change """

    try:
        position = int(input("Joueur ({0}), Quel position ? ".format(colorize(cType.upper(), BOLD))))
        legal_changes = get_legal_cell_changes(board)
        return apply_cell_change(board, legal_changes[cType][position])
    except ValueError:
        return False
    except IndexError:
        return False


def get_reverse_player_type(cType):
    """ Get type from reverse player from type """

    if cType == TYPE_WHITE:
        return TYPE_BLACK

    return TYPE_WHITE


def print_ask_board(board, cType):
    """ Print board with cell change possibilities from type """

    legal_changes = get_legal_cell_changes(board)
    print(render(board, extract_positions(legal_changes[cType])))


def print_score(cell_distribution):
    """ Show score from cell_distribution as string """

    print("\n#### SCORE (WHITE: {0}, BLACK: {1}) ####\n".format(
        cell_distribution[TYPE_WHITE],
        cell_distribution[TYPE_BLACK]
    ))
