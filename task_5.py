class Results:
    
    def __init__(self, viktories, draws, loses):
        self.viktories = viktories
        self.draws = draws
        self.loses = loses

class Football(Results):
    def __init__(self, viktories, draws, loses):
        super().__init__(viktories, draws, loses)

    def number_of_wins(self):
        return f'Футбольных побед: {self.viktories}'
    
    def number_of_draws(self):
        return f'Футбольных ничьих: {self.draws}'
    
    def number_of_loses(self):
        return f'Футбольных поражений: {self.loses}'
    
    def total_points(self):
        return f'Общее количество очков: {self.viktories * 3 + self.draws}'
    
class Hockey(Results):
    def __init__(self, viktories, draws, loses):
        super().__init__(viktories, draws, loses)

    def number_of_wins(self):
        return f'Хоккейных побед: {self.viktories}'
    
    def number_of_draws(self):
        return f'Хоккейных ничьих: {self.draws}'
    
    def number_of_loses(self):
        return f'Хоккейных поражений: {self.loses}'
    
    def total_points(self):
        return f'Общее количество очков: {self.viktories * 2 + self.draws}'
    
football_team = Football(2, 2, 2)
hockey_team = Hockey(2, 2, 2)

for team in (football_team, hockey_team):
    print(team.number_of_wins(), team.number_of_draws(), team.number_of_loses(), team.total_points(), sep = '\n')