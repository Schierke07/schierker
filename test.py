import os

def make_commit(days: int):
    if days < 1:
        return os.system('git push')
    else:
        #dates = f'{days} days ago'
        dates = "2021-6-7 10:10:10"

        with open('data.txt', 'a') as file:
            file.write(f'{1}\n')

        os.system('git add data.txt')
        os.system('git commit --amend --date="'+dates+'" -m "First Commit"')

        return days*make_commit(days-1)

make_commit(5)