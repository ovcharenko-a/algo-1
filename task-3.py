"""
Модуль построения национальной команды слиянием рейтинга
"""

def merge_teams(team_1, team_2, len_team):
    """
    Слить две команды в команду заданного размера
    """
    i_1 = 0
    i_2 = 0
    i_t = 0
    new_team = [0] * len_team
    while i_t < len_team and (i_1 < len(team_1) or i_2 < len(team_2)):
        if i_1 == len(team_1):
            new_team[i_t] = team_2[i_2]
            i_2 += 1
        elif i_2 == len(team_2):
            new_team[i_1] += 1
        elif team_1[i_1] >= team_2[i_2]:
            new_team[i_t] = team_1[i_1]
            i_1 += 1
        else:
            new_team[i_t] = team_2[i_2]
            i_2 += 1
        i_t += 1
    return new_team


def get_national_team(regional_teams, size):
    """
    Создать национальную сборную из массивов команд
    """
    team = regional_teams.pop(0)
    for reg_team in regional_teams:
        team = merge_teams(team, reg_team, size)
    return team


if __name__ == "__main__":
    print("run!")
    commandos = [[45, 31, 24, 22, 20, 17, 14, 13, 12, 10],
                 [31, 18, 15, 12, 10, 8, 6, 4, 2, 1],
                 [51, 30, 10, 9, 8, 7, 6, 5, 2, 1]]
    national_team = get_national_team(commandos, 10)
    print(national_team)
