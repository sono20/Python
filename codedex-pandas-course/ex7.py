import pandas as pd 
games = pd.DataFrame({
    'title': ['The Witcher 3', 'Cyberpunk 2077', 'Elden Ring', 'Dark Souls 3', 
              'Bloodborne', 'Sekiro', 'Hollow Knight', 'Hades', 'Celeste', 'Stardew Valley'],
    'year': [2015, 2020, 2022, 2016, 2015, 2019, 2017, 2020, 2018, 2016],
    'genre': ['RPG', 'RPG', 'RPG', 'RPG', 'RPG', 'Action', 'Metroidvania', 
              'Roguelike', 'Platformer', 'Simulation'],
    'rating': [9.3, 7.8, 9.5, 9.0, 9.1, 9.4, 9.2, 9.3, 9.4, 9.1],
    'hours_played': [120, 45, 80, 95, 70, 60, 40, 55, 25, 150]
})

games['completed'] = [True, False, True, True, True, True, True, True, True, True]

games = games.sort_values('rating', ascending=False)

recent_top_games = games[(games['year'] >= 2018) & (games['rating'] > 9.0)]