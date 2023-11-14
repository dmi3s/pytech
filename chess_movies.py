# chess coordinates: a1 - h8
# matrix coordinates 0,7 - 7,0


ALPHA2INT = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}


def chess2m(chess: tuple[str, str]) -> tuple[int, int]:
    def decode_alpha(alpha: str) -> int:
        return ALPHA2INT[alpha.lower()]

    def decode_int(number: str) -> int:
        return 8 - int(number)

    a, i = chess
    return decode_int(i), decode_alpha(a)


def is_rook_attack(rook: tuple[int, int], square: tuple[int, int]) -> bool:
    return rook != square and (rook[0] == square[0] or rook[1] == square[1])


def is_bishop_attack(bishop: tuple[int, int], square: tuple[int, int]) -> bool:
    return bishop != square and (abs(bishop[0] - square[0]) == abs(bishop[1] - square[1]))


def is_queen_attack(queen: tuple[int, int], square: tuple[int, int]) -> bool:
    return is_bishop_attack(queen, square) or is_rook_attack(queen, square)


def is_knight_attack(knight: tuple[int, int], square: tuple[int, int]) -> bool:
    return (square[0] - knight[0]) ** 2 + (square[1] - knight[1]) ** 2 == 5


def is_king_attack(king: tuple[int, int], square: tuple[int, int]) -> bool:
    return king != square and (square[0] - king[0]) ** 2 + (square[1] - king[1]) ** 2 <= 2


def gen_chessboard() -> list[list[str]]:
    return [['.'] * 8 for _ in range(8)]


def print_chessboard(board: list[list[str]], end='\n') -> None:
    for num, ln in zip(range(8, 0, -1), board):
        print(f"{num} {''.join(ln)}")
    print("  abcdefgh", end=end)


def main():
    chb = gen_chessboard()
    fig = chess2m(('d', '4'))
    chb[fig[0]][fig[1]] = 'Q'
    for i in range(8):
        for j in range(8):
            if is_queen_attack(fig, (i, j)):
                chb[i][j] = '*'
    print_chessboard(chb)


if __name__ == '__main__':
    main()
