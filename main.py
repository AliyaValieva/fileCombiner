# Aliya Valieva
# avalieva

import filesComb as f
while True:
    user_dir_input = input('What is the path name?: ')
    if user_dir_input == 'DONE':
        break
    allFiles = f.combined(user_dir_input)

    errorTeam, errorRank = f.countErrors()
    
    f.summary(allFiles,user_dir_input) # reports txt file
    f.countFiles(user_dir_input)
