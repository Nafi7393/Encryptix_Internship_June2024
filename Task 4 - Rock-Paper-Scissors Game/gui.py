import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox
from main import get_computer_choice, determine_winner, valid_number_of_games


class RockPaperScissorsGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.user_score = 0
        self.computer_score = 0
        self.total_game_num = 0
        self.games_to_win = 0
        self.current_game = 0

        # Widgets
        self.label_instruction = QLabel('Enter the total number of games to play (must be an odd number):')
        self.input_total_games = QLineEdit()
        self.button_start = QPushButton('Start Game')
        self.button_rock = QPushButton('Rock')
        self.button_paper = QPushButton('Paper')
        self.button_scissors = QPushButton('Scissors')
        self.label_result = QLabel('')
        self.label_final_result = QLabel('')
        self.total_game_played = QLabel('')
        self.empty_label = QWidget()

        self.button_start.setObjectName("startButton")
        self.button_rock.setObjectName("rockButton")
        self.button_paper.setObjectName("paperButton")
        self.button_scissors.setObjectName("scissorsButton")

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Rock Paper Scissors Game')
        self.setGeometry(600, 200, 400, 650)

        # Layouts
        vbox = QVBoxLayout()

        vbox.addWidget(self.label_instruction)
        vbox.addWidget(self.input_total_games)
        vbox.addWidget(self.button_start)
        vbox.addWidget(self.empty_label)
        vbox.addWidget(self.button_rock)
        vbox.addWidget(self.button_paper)
        vbox.addWidget(self.button_scissors)
        vbox.addWidget(self.label_result)
        vbox.addWidget(self.label_final_result)
        vbox.addWidget(self.total_game_played)
        self.setLayout(vbox)

        # Connections
        self.button_start.clicked.connect(self.start_game)
        self.button_rock.clicked.connect(lambda: self.play_game('rock'))
        self.button_paper.clicked.connect(lambda: self.play_game('paper'))
        self.button_scissors.clicked.connect(lambda: self.play_game('scissors'))

        self.disable_buttons()

        self.setStyleSheet("""
            QLabel {
                font-size: 16px;
                color: #333;
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                padding: 10px 20px;
                border-radius: 5px;
                font-size: 16px;
            }
            QPushButton#button_start {
                background-color: #f44336;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:disabled {
                background-color: #d3d3d3;
                color: #a9a9a9;
            }
            QLineEdit {
                font-size: 16px;
                padding: 5px;
            }
        """)

    def start_game(self):
        total_game_num = self.input_total_games.text().strip()

        try:
            self.total_game_num = int(total_game_num)
            if not valid_number_of_games(self.total_game_num):
                self.show_message('Please enter an odd number!')
                return
        except ValueError:
            self.show_message('Please enter a valid number!')
            return
        self.enable_buttons()

        self.games_to_win = (self.total_game_num // 2) + 1
        self.current_game = 0
        self.user_score = 0
        self.computer_score = 0
        self.total_game_played.setText(f"Game {self.current_game}/{self.total_game_num}")
        self.label_final_result.setText('')

    def play_game(self, user_choice):
        if self.current_game >= self.total_game_num:
            self.show_message('All games have been played!')
            return

        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)

        result_text = f"\n--------------------------------\n"
        result_text += f" You chose: {user_choice.upper()}\n"
        result_text += f" Computer chose: {computer_choice.upper()}\n"
        result_text += f"--------------------------------\n"

        if winner == "tie":
            result_text += " It's a tie!\n"
        elif winner == "user":
            result_text += " You win!\n"
            self.user_score += 1
        else:
            result_text += " You lose!\n"
            self.computer_score += 1

        result_text += f"--------------------------------\n\n"
        result_text += f" Score - YOU: {self.user_score} | COMPUTER: {self.computer_score}\n"

        self.label_result.setText(result_text)
        self.current_game += 1
        # Check for winner after every round based on score
        self.total_game_played.setText(f"Game {self.current_game}/{self.total_game_num}")
        self.check_winner()

    def check_winner(self):
        if self.user_score == self.games_to_win:
            self.label_final_result.setText("Congratulations! You are the final winner!")
            self.disable_buttons()

        elif self.computer_score == self.games_to_win:
            self.label_final_result.setText("The computer is the final winner. Better luck next time!")
            self.disable_buttons()

        if self.current_game == self.total_game_num:
            if self.user_score == self.computer_score:
                self.label_final_result.setText("It's a tie! No clear winner.")
            elif self.user_score > self.computer_score:
                self.label_final_result.setText("Congratulations! You are the final winner!")
            else:
                self.label_final_result.setText("The computer is the final winner. Better luck next time!")
            self.disable_buttons()

    def disable_buttons(self):
        # Add logic to disable buttons (rock, paper, scissors) to prevent further plays
        self.button_rock.setEnabled(False)
        self.button_paper.setEnabled(False)
        self.button_scissors.setEnabled(False)

    def enable_buttons(self):
        # Add logic to disable buttons (rock, paper, scissors) to prevent further plays
        self.button_rock.setEnabled(True)
        self.button_paper.setEnabled(True)
        self.button_scissors.setEnabled(True)

    def show_message(self, message):
        msg_box = QMessageBox()
        msg_box.setText(message)
        msg_box.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RockPaperScissorsGUI()
    window.show()
    sys.exit(app.exec_())
