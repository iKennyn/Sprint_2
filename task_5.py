class Results:
    win_points = 0
    sport_name = ''

    def __init__(self, victories, draws, losses):
        self.victories = victories
        self.draws = draws
        self.losses = losses

    def number_of_wins(self):
        return f'{self.sport_name} побед: {self.victories}'

    def number_of_draws(self):
        return f'{self.sport_name} ничьих: {self.draws}'

    def number_of_losses(self):
        return f'{self.sport_name} поражений: {self.losses}'

    def total_points(self):
        return f'Общее количество очков {self.win_points * self.victories + self.draws}'

class Football(Results):
    win_points = 3
    sport_name = 'Футбольных'

class Hockey(Results):
    win_points = 5
    sport_name = 'Хоккейных'

football_team = Football(4,5, 2)
hockey_team = Hockey(2,2, 2)
for team in [football_team, hockey_team]:
    print((team.number_of_wins()),team.number_of_draws(), team.number_of_losses(), team.total_points())
