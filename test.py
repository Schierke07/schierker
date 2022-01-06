import os

def make_commit(days: int):
    if days < 1:
        return os.system('git push')
    else:
        #dates = f'{days} days ago'
        dates = "2020-6-7 10:10:10"

        with open('data.txt', 'a') as file:
            file.write(f'{dates}\n')

        os.system('git add data.txt')
        os.system('git commit --date="'+dates+'" -m "First Commit"')

        return days*make_commit(days-1)

make_commit(100)