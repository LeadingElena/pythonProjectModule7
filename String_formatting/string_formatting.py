team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
score_1 = 40
score_2 = 42
team_1 = 'Мастера кода'
team_2 = 'Волшебники данных'
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = f'победа команды {team_1}'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = f'победа команды {team_2}'
else:
    challenge_result = 'ничья'

# Использование %
print('В команде Мастера кода участников: %(team1_num)s!' % {'team1_num' : 5})
print('Итого сегодня в командах участников: %(team1_num)s и %(team2_num)s!' % {'team1_num' : 5, 'team2_num' : 6})

# Использование format()
print('Команда Волшебники данных решила задач: {score_2}!'.format(score_2 = 42))
print('Волшебники данных решили задачи за {team1_time} с'.format(team1_time = 1552.512))

# Использование f-строк
print(f'Команды решили {score_1} и {score_2} задач')
print(f'Результат битвы: {challenge_result}!')
print(f'Сегодня было решено {score_1 +score_2} задач, в среднем по '
      f'{round((team1_time + team2_time) / (score_1 + score_2), 1)} секунды на задачу!')

