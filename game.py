import random

class Game:
    def __init__(self) -> None:
        self.draw_matrix()
        win_lose = self.winning(number_games = 100, probability_playerA = 0.5, probability_playerB = 0.25)
        average = self.average_win(number_games = 100, win_lose = win_lose)
        self.math_expectation(probability_playerA = 0.5, probability_playerB = 0.5)
        self.output(self.choices , win_lose, average)


    def player_сhoice(self, probability) -> int:
        return int(random.uniform(0, 1) > probability)

    def draw_matrix(self) -> None:
        print("-------------")
        print("|  3  | -2  |")
        print("-------------")
        print("| -4  |  3  |")
        print("-------------")

    def choice_torage(self, choices: list, probability_playerA: int, probability_playerB: int) -> list:
        choice = [0, 0]
        choice[0] = self.player_сhoice(probability_playerA)
        choice[1] = self.player_сhoice(probability_playerB)
        choices.append(choice)
        return choices
    
    def winning(self, number_games: int, probability_playerA: int, probability_playerB: int) -> list:
        win_lose = [0, 0]
        choice = []
        arr = [[3, -2], [-4, 3]]
        for i in range(number_games):
            self.choices = self.choice_torage(choice, probability_playerA, probability_playerB)
            if arr[self.choices[i][0]][self.choices[i][1]] > 0:
                win_lose[0] += arr[self.choices[i][0]][self.choices[i][1]]
                win_lose[1] -= arr[self.choices[i][0]][self.choices[i][1]]
            else:
                win_lose[0] -= abs(arr[self.choices[i][0]][self.choices[i][1]])
                win_lose[1] += abs(arr[self.choices[i][0]][self.choices[i][1]])
        return win_lose

    def average_win(self, number_games: int, win_lose: list) -> list:
        average = []
        average.append(win_lose[0]/number_games)
        average.append(win_lose[1]/number_games)
        return average

    def math_expectation(self, probability_playerA: int, probability_playerB: int) -> int:
        arr = [[3, -2], [-4, 3]]
        x = arr[0][0] * probability_playerA * probability_playerB + arr[1][1] * (1 - probability_playerA) * (1 - probability_playerB) + arr[0][1] * probability_playerA * (1 - probability_playerB) + arr[1][0] * (1 - probability_playerA) * probability_playerB
        return x

    def output(self, choices: list, win_lose: list, average: list) -> None:
        print("Игрок А")
        if win_lose[0] > 0:
            print("Игрок выйграл:", win_lose[0], "Руб")
        elif win_lose[0] < 0:
            print("Игрок проиграл:", win_lose[0], "Руб")
        else:
            print("Игрок ничего не проиграл, не и не выйграл")

        print("Средняя прибыль игрока в 1 раунде:", average[0], "Руб")
        print("------------------------------------------------------------------------------------------")
        print("Игрок B")
        if win_lose[1] > 0:
            print("Игрок выйграл:", win_lose[1], "Руб")
        elif win_lose[1] < 0:
            print("Игрок проиграл:", win_lose[1], "Руб")
        else:
            print("Игрок ничего не проиграл, не и не выйграл")

        print("Средняя прибыль игрока в 1 раунде:", average[1], "Руб")
        
        print("Мат ожидание:", self.math_expectation(0.5, 0.5))
        print("вектор из 100 пар бинарных чисел, соответствующих результатам случайного выбора строк/столбцов")
        print(choices)

        



