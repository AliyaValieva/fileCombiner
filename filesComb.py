# Aliya Valieva
# avalieva

import csv
import directories as d


def combined(user_dir_input):

    validSports = ['NFL', 'NBA', 'NHL', 'MLB']
    validRanks = [1, 2, 3]
    global errorTeam
    global errorRank
    errorTeam = errorRank = 0
    files = d.make_dir(user_dir_input)

    combined = '/Reports/combined_out.csv'
    with open(user_dir_input + combined, 'w+') as f:
        writer = csv.writer(f)
        writer.writerow(['City','Team Name', 'Sport', 'Rank'])

        for file in files:

            with open(file, 'r') as foo:
                reader = csv.reader(foo)
                next(foo)

                for row in reader:
                    try:
                        if row[2] not in validSports:
                            errorTeam += 1
                            raise TypeError
                        elif int(row[3]) not in validRanks:
                            errorRank += 1
                            raise ValueError
                        writer.writerow(row)
                    except ValueError:
                        pass
                    except TypeError:
                        pass

    return combined

def countErrors():
    return errorTeam, errorRank


def summary(combined, user_dir_input):
    results = '/Reports/summary_report.txt'

    with open(user_dir_input + results, 'w+') as fin:
        with open(user_dir_input + combined, 'r') as bar:
            top1_nfl = []
            top2_nfl = []
            top3_nfl = []

            nfl_team_1 = {}
            nfl_team_2 = {}
            nfl_team_3 = {}
            nfl_eval = {}

            top1_nba = []
            top2_nba = []
            top3_nba = []
            nba_team_1 = {}
            nba_team_2 = {}
            nba_team_3 = {}
            nba_eval = {}


            top1_nhl = []
            top2_nhl = []
            top3_nhl = []
            nhl_team_1 = {}
            nhl_team_2 = {}
            nhl_team_3 = {}
            nhl_eval = {}

            top1_mlb = []
            top2_mlb = []
            top3_mlb = []
            mlb_team_1 = {}
            mlb_team_2 = {}
            mlb_team_3 = {}
            mlb_eval = {}

            reader = csv.DictReader(bar)
            for row in reader:
                if row['Sport'] == 'NFL' and row['Rank'] == '1':
                    if row['Team Name'] not in nfl_team_1:
                        nfl_team_1[row['Team Name']] = 1
                    else:
                        nfl_team_1[row['Team Name']] += 1

                elif row['Sport'] == 'NFL' and row['Rank'] == '2':
                    if row['Team Name'] not in nfl_team_2:
                        nfl_team_2[row['Team Name']] = 1
                    else:
                        nfl_team_2[row['Team Name']] += 1
                elif row['Sport'] == 'NFL' and row['Rank'] == '3':
                    if row['Team Name'] not in nfl_team_3:
                        nfl_team_3[row['Team Name']] = 1
                    else:
                        nfl_team_3[row['Team Name']] += 1
                elif row['Sport'] == 'NBA' and row['Rank'] == '1':
                    if row['Team Name'] not in nba_team_1:
                        nba_team_1[row['Team Name']] = 1
                    else:
                        nba_team_1[row['Team Name']] += 1
                elif row['Sport'] == 'NBA' and row['Rank'] == '2':
                    if row['Team Name'] not in nba_team_2:
                        nba_team_2[row['Team Name']] = 1
                    else:
                        nba_team_2[row['Team Name']] += 1
                elif row['Sport'] == 'NBA' and row['Rank'] == '3':
                    if row['Team Name'] not in nba_team_3:
                        nba_team_3[row['Team Name']] = 1
                    else:
                        nba_team_3[row['Team Name']] += 1
                elif row['Sport'] == 'NHL' and row['Rank'] == '1':
                    if row['Team Name'] not in nhl_team_1:
                        nhl_team_1[row['Team Name']] = 1
                    else:
                        nhl_team_1[row['Team Name']] += 1
                elif row['Sport'] == 'NHL' and row['Rank'] == '2':
                    if row['Team Name'] not in nhl_team_2:
                        nhl_team_2[row['Team Name']] = 1
                    else:
                        nhl_team_2[row['Team Name']] += 1
                elif row['Sport'] == 'NHL' and row['Rank'] == '3':
                    if row['Team Name'] not in nhl_team_3:
                        nhl_team_3[row['Team Name']] = 1
                    else:
                        nhl_team_3[row['Team Name']] += 1
                elif row['Sport'] == 'MLB' and row['Rank'] == '1':
                    if row['Team Name'] not in mlb_team_1:
                        mlb_team_1[row['Team Name']] = 1
                    else:
                        mlb_team_1[row['Team Name']] += 1
                elif row['Sport'] == 'MLB' and row['Rank'] == '2':
                    if row['Team Name'] not in mlb_team_2:
                        mlb_team_2[row['Team Name']] = 1
                    else:
                        mlb_team_2[row['Team Name']] += 1
                elif row['Sport'] == 'MLB' and row['Rank'] == '3':
                    if row['Team Name'] not in mlb_team_3:
                        mlb_team_3[row['Team Name']] = 1
                    else:
                        mlb_team_3[row['Team Name']] += 1

                if row['Sport'] == 'NFL' and row['Rank'] in '1,2,3':
                    if row['Team Name'] not in nfl_eval:
                        nfl_eval[row['Team Name']] = 1
                    else:
                        nfl_eval[row['Team Name']] += 1
                elif row['Sport'] == 'NBA' and row['Rank'] in '1,2,3':
                    if row['Team Name'] not in nba_eval:
                        nba_eval[row['Team Name']] = 1
                    else:
                        nba_eval[row['Team Name']] += 1
                elif row['Sport'] == 'NHL' and row['Rank'] in '1,2,3':
                    if row['Team Name'] not in nhl_eval:
                        nhl_eval[row['Team Name']] = 1
                    else:
                        nhl_eval[row['Team Name']] += 1
                elif row['Sport'] == 'MLB' and row['Rank'] in '1,2,3':
                    if row['Team Name'] not in mlb_eval:
                        mlb_eval[row['Team Name']] = 1
                    else:
                        mlb_eval[row['Team Name']] += 1

            with open(user_dir_input + '/Reports/summary_report.csv', 'w+') as bar:

                bar.write('Team Name, Sport, Number of times picked')
                for key in nfl_eval:
                    bar.write('\n' + key + ',NFL,'+str(nfl_eval[key]))
                for key in nhl_eval:
                    bar.write('\n' + key + ',NHL,' + str(nhl_eval[key]))
                for key in nba_eval:
                    bar.write('\n' + key + ',NBA,' + str(nba_eval[key]))
                for key in mlb_eval:
                    bar.write('\n' + key + ',MLB,' + str(mlb_eval[key]))

            maxValueNFL = max(nfl_eval.values())

            for key in nfl_eval:
                if maxValueNFL == nfl_eval[key]:
                    top1_nfl.append(key)
                    nfl_eval[key] = -1

            maxValueNFL = max(nfl_eval.values())

            for key in nfl_eval:
                if maxValueNFL == nfl_eval[key] and nfl_eval[key] != -1:
                    top2_nfl.append(key)
                    nfl_eval[key] = -1

            maxValueNFL = max(nfl_eval.values())

            for key in nfl_eval:
                if maxValueNFL == nfl_eval[key] and nfl_eval[key] != -1:
                    top3_nfl.append(key)
                    nfl_eval[key] = -1

            maxValueNBA = max(nba_eval.values())
            for key in nba_eval:
                if maxValueNBA == nba_eval[key]:
                    top1_nba.append(key)
                    nba_eval[key] = -1

            maxValueNBA = max(nba_eval.values())
            for key in nba_eval:
                if maxValueNBA == nba_eval[key] and nba_eval[key] != -1:
                    top2_nba.append(key)
                    nba_eval[key] = -1

            maxValueNBA = max(nba_eval.values())
            for key in nba_eval:
                if maxValueNBA == nba_eval[key] and nba_eval[key] != -1:
                    top3_nba.append(key)
                    nba_eval[key] = -1

            maxValueNHL = max(nhl_eval.values())
            for key in nhl_eval:
                if maxValueNHL == nhl_eval[key]:
                    top1_nhl.append(key)
                    nhl_eval[key] = -1

            maxValueNHL = max(nhl_eval.values())
            for key in nhl_eval:
                if maxValueNHL == nhl_eval[key] and nhl_eval[key] != -1:
                    top2_nhl.append(key)
                    nhl_eval[key] = -1

            maxValueNHL = max(nhl_eval.values())
            for key in nhl_eval:
                if maxValueNHL == nhl_eval[key] and nhl_eval[key] != -1:
                    top3_nhl.append(key)
                    nhl_eval[key] = -1

            maxValueMLB = max(mlb_eval.values())
            for key in mlb_eval:
                if maxValueMLB == mlb_eval[key]:
                    top1_mlb.append(key)
                    mlb_eval[key] = -1
            maxValueMLB = max(mlb_eval.values())
            for key in mlb_eval:
                if maxValueMLB == mlb_eval[key] and mlb_eval[key] != -1:
                    top2_mlb.append(key)
                    mlb_eval[key] = -1
            maxValueMLB = max(mlb_eval.values())
            for key in mlb_eval:
                if maxValueMLB == mlb_eval[key] and mlb_eval[key] != -1:
                    top3_mlb.append(key)
                    mlb_eval[key] = -1

        fin.write('--- RANKS EVALUATIONS ---')
        fin.write('\n\nRank One for NFL\n\n')
        for key in nfl_team_1:
            fin.write("This team: " + key + " appeared " + str(nfl_team_1[key]) + " times.\n")

        fin.write('\nRank Two for NFL\n\n')
        for key in nfl_team_2:
            fin.write('This team: '+ key + ' appeared ' + str(nfl_team_2[key]) + ' times.\n')
        fin.write('\nRank Three for NFL\n\n')
        for key in nfl_team_3:
            fin.write('This team: ' + key + ' appeared ' + str(nfl_team_3[key]) + ' times.\n')
        fin.write('\n\nRank One for NBA\n\n')
        for key in nba_team_1:
            fin.write('This team: ' + key + ' appeared ' + str(nba_team_1[key]) + ' times.\n')
        fin.write('\nRank Two for NBA\n\n')
        for key in nba_team_2:
            fin.write('This team: ' + key + ' appeared ' + str(nba_team_2[key]) + ' times.\n')
        fin.write('\nRank Three for NBA\n\n')
        for key in nba_team_3:
            fin.write('This team: ' + key + ' appeared ' + str(nba_team_3[key]) + ' times.\n')
        fin.write('\n\nRank One for NHL\n\n')
        for key in nhl_team_1:
            fin.write('This team: ' + key + ' appeared ' + str(nhl_team_1[key]) + ' times.\n')
        fin.write('\nRank Two for NHL\n\n')
        for key in nhl_team_2:
            fin.write('This team: ' + key + ' appeared ' + str(nhl_team_2[key]) + ' times.\n')
        fin.write('\nRank Three for NHL\n\n')
        for key in nhl_team_3:
            fin.write('This team: ' + key + ' appeared ' + str(nhl_team_3[key]) + ' times.\n')
        fin.write('\n\nRank One for MLB\n\n')
        for key in mlb_team_1:
            fin.write('This team: ' + key + ' appeared ' + str(mlb_team_1[key]) + ' times.\n')
        fin.write('\nRank Two for MLB\n\n')
        for key in mlb_team_2:
            fin.write('This team: ' + key + ' appeared ' + str(mlb_team_2[key]) + ' times.\n')
        fin.write('\nRank Three for MLB\n\n')
        for key in mlb_team_3:
            fin.write('This team: ' + key + ' appeared ' + str(mlb_team_3[key]) + ' times.\n')

        fin.write('--- COUNT OF ERRORS HANDLED ---')
        fin.write('\n\nNumber of invalid sport teams: '+ str(errorTeam))
        fin.write('\nNumber of invalid rank: ' + str(errorRank))

        sorted(nfl_eval,reverse=True)
        fin.write('\n\n--- TOP TEAMS EVALUATIONS ---')
        fin.write('\n\nTop 1 NFL Teams: ' + str(top1_nfl))
        fin.write('\n\nTop 2 NFL Teams: ' + str(top2_nfl))
        fin.write('\n\nTop 3 NFL Teams: ' + str(top3_nfl))
        fin.write('\n\nTop 1 NBA Teams: ' + str(top1_nba))
        fin.write('\n\nTop 2 NBA Teams: ' + str(top2_nba))
        fin.write('\n\nTop 3 NBA Teams: ' + str(top3_nba))
        fin.write('\n\nTop 1 NHL Teams: ' + str(top1_nhl))
        fin.write('\n\nTop 2 NHL Teams: ' + str(top2_nhl))
        fin.write('\n\nTop 3 NHL Teams: ' + str(top3_nhl))
        fin.write('\n\nTop 1 MLB Teams: ' + str(top1_mlb))
        fin.write('\n\nTop 2 MLB Teams: ' + str(top2_mlb))
        fin.write('\n\nTop 3 MLB Teams: ' + str(top3_mlb))


def countFiles(user_dir_input):

    pathName = user_dir_input
    files = d.make_dir(pathName)
    foo1 = []
    with open(user_dir_input + '/Reports/summary_report.txt','a') as foobar:
        foobar.write('\n\n--- INFORMATION ABOUT FILES AND DIRECTORY ---')
        foobar.write('\n\nThe csv files evaluated: \n\n')
        for foo in files:
            foobar.write(str(foo)+'\n\n')
            foo1.append(foo)
        foobar.write('The Number of files in main directory: ' + str(len(foo1)))
        foobar.write('\n\nThe Name of your main directory: ' + str(pathName))
