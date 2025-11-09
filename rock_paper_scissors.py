import random

class Player:
    def __init__(self, name):
        self.name = name

    def get_move(self):
        pass


class HumanPlayer(Player):
    def get_move(self):
        move = input("Enter Rock, Paper, or Scissors: ").lower()
        while move not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Try again.")
            move = input("Enter Rock, Paper, or Scissors: ").lower()
        return move


class ComputerPlayer(Player):
    def get_move(self):
        return random.choice(["rock", "paper", "scissors"])


class Game:
    def __init__(self, human, computer):
        self.human = human
        self.computer = computer

    def determine_winner(self, human_move, computer_move):
        if human_move == computer_move:
            return "It's a draw!"

        wins = {
            "rock": "scissors",
            "paper": "rock",
            "scissors": "paper"
        }

        if wins[human_move] == computer_move:
            return f"{self.human.name} wins!"
        else:
            return f"{self.computer.name} wins!"

    def play(self):
        print("==== Rock • Paper • Scissors ====")
        human_move = self.human.get_move()
        computer_move = self.computer.get_move()

        print(f"\n{self.human.name} chose: {human_move.capitalize()}")
        print(f"{self.computer.name} chose: {computer_move.capitalize()}")

        result = self.determine_winner(human_move, computer_move)
        print(f"\nResult: {result}")


if __name__ == "__main__":
    player = HumanPlayer("You")
    computer = ComputerPlayer("Computer")
    game = Game(player, computer)
    game.play()
