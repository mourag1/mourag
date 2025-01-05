class Board:
    def __init__(self):
        # إنشاء لوحة 3x3 فارغة
        self.board = [" " for _ in range(9)]

    def display(self):
        # عرض اللوحة بشكل منظم
        for row in range(3):
            print(" | ".join(self.board[row * 3: (row + 1) * 3]))
            if row < 2:
                print("---------")

    def update(self, position, symbol):
        # تحديث الخانة برمز اللاعب إذا كانت الخانة فارغة
        if self.board[position] == " ":
            self.board[position] = symbol
            return True
        return False

    def check_winner(self, symbol):
        # جميع التركيبات الفائزة
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # الصفوف
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # الأعمدة
            [0, 4, 8], [2, 4, 6]              # الأقطار
        ]
        # التحقق من وجود تركيبة فائزة
        for condition in win_conditions:
            if all(self.board[i] == symbol for i in condition):
                return True
        return False

    def is_full(self):
        # التحقق مما إذا كانت جميع الخانات ممتلئة
        return " " not in self.board


class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def make_move(self, board, position):
        # محاولة تحديث الخانة برمز اللاعب
        return board.update(position, self.symbol)


class Game:
    def __init__(self):
        # إعداد اللاعبين واللوحة
        self.board = Board()
        self.players = [Player("X"), Player("O")]
        self.current_player_index = 0

    def switch_player(self):
        # تبديل الأدوار بين اللاعبين
        self.current_player_index = 1 - self.current_player_index

    def play(self):
        print("Welcome to Tic Tac Toe!")
        self.board.display()
        
        # استمرار اللعبة حتى الفوز أو التعادل
        while True:
            current_player = self.players[self.current_player_index]
            print(f"\nPlayer {current_player.symbol}'s turn.")

            # التحقق من صحة المدخلات
            try:
                position = int(input("Choose a position (1-9): ")) - 1
                if position < 0 or position > 8:
                    raise ValueError
            except ValueError:
                print("Invalid input! Please enter a number between 1 and 9.")
                continue

            # محاولة اللعب والتحقق من صحة الحركة
            if current_player.make_move(self.board, position):
                self.board.display()

                # التحقق من الفوز أو التعادل
                if self.board.check_winner(current_player.symbol):
                    print(f"\nPlayer {current_player.symbol} wins!")
                    break
                elif self.board.is_full():
                    print("\nIt's a draw!")
                    break

                # تبديل الدور إلى اللاعب الآخر
                self.switch_player()
            else:
                print("Position already taken, try again.")

# تشغيل اللعبة
if __name__ == "__main__":
    game = Game()
    game.play()
