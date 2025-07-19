"""
Допзадание 2.
Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.

За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.

Формат ввода следующий:
В первой строке указано целое число n — количество завершенных игр.
После этого идет n строк, в которых записаны результаты игры в следующем формате:
Перваякоманда; Забитопервойкомандой; Втораякоманда; Забитовторойкомандой

Вывод программы необходимо оформить следующим образом:
Команда: Всегоигр Побед Ничьих Поражений Всегоочков

Конкретный пример ввода-вывода приведён ниже.

Порядок вывода команд произвольный.

Sample Input:

3
Спартак;9;Зенит;10
Локомотив;12;Зенит;3
Спартак;8;Локомотив;15

Sample Output:

Спартак:2 0 0 2 0
Зенит:2 1 0 1 3
Локомотив:2 2 0 0 6
"""

n = int(input())

matches = [input().strip() for _ in range(n)]

# Словарь команд
stats = {}

for line in matches:
    team1, score1_str, team2, score2_str = line.split(';')
    score1, score2 = int(score1_str), int(score2_str)

    if team1 not in stats:
        stats[team1] = {'games':0, 'wins':0, 'draws':0, 'losses':0, 'points':0}
    if team2 not in stats:
        stats[team2] = {'games':0, 'wins':0, 'draws':0, 'losses':0, 'points':0}

    # Обновление статистики
    stats[team1]['games'] += 1
    stats[team2]['games'] += 1

    if score1 > score2:
        stats[team1]['wins'] += 1
        stats[team1]['points'] += 3
        stats[team2]['losses'] += 1
    elif score1 < score2:
        stats[team2]['wins'] += 1
        stats[team2]['points'] += 3
        stats[team1]['losses'] += 1
    else:
        # ничья
        stats[team1]['draws'] += 1
        stats[team2]['draws'] += 1
        stats[team1]['points'] += 1
        stats[team2]['points'] += 1

for team in stats:
    data = stats[team]
    print(f"{team}:{data['games']} {data['wins']} {data['draws']} {data['losses']} {data['points']}")