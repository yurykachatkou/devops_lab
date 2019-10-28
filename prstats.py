import requests
import datetime
import getpass
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-ow', '--owner', required=True,
                    help='Owner of a repository')
parser.add_argument('-r', '--repo', required=True,
                    help='Name of a repository')
parser.add_argument('-u', '--user', required=False,
                    help='Info for user who made pull requests. '
                    'If not specified, info for all users will be outputted')
parser.add_argument('-op', '--option', required=False,
                    help='Input options: '
                    '"state" - to get a state of PR, '
                    '"title" - to get PR title, '
                    '"id" - to get id of PR, '
                    '"day" - to get a day of the week PR was opened, '
                    '"weeks" - to get a number of week PR was opened, '
                    '"title" - to get a title of PR. '
                    'If not specified, all option will be outputted')
parser.add_argument('-v', action="version", version="version 1.1")

args = parser.parse_args()

repo = args.repo
owner = args.owner
user = args.user
option = args.option

username = input("Input your github login: ")
password = getpass.getpass(prompt='Password:')

url = 'https://api.github.com/repos/{}/{}/pulls' \
      '?per_page=100&state=all'.format(owner, repo)
print(url)
r = requests.get(url, auth=(username, password))
# current date
curdate = datetime.datetime.now()
data = r.json()

for i, v in enumerate(data):
    if data[i]['user']['login'] == user or not user:
        # get date of pull creation
        crday = datetime.datetime.\
            strptime(data[i]['created_at'][0:10], '%Y-%m-%d')
        # difference between current date and date of pull creation
        daydiff = str((crday - curdate).days)[1:]
        # dayofweek
        weeknum = crday.strftime('%A')
        # print day
        if option == 'day':
            print('Pull #{}. User:{}. Number of days: {}'.
                  format(str(i + 1), data[i]['user']['login'], daydiff))
        # print week
        elif option == 'weeks':
            print('Pull #{}. User:{}. Day of the week opened: {}'.
                  format(str(i + 1), data[i]['user']['login'], weeknum))
        # print every option
        elif not option:
            print('Pull #{}. User: {}. Number of days: {}. '
                  'Day of the week opened: {}. '
                  'State: {}. Id: {}.'.
                  format(str(i + 1),
                         data[i]['user']['login'],
                         daydiff, weeknum, data[i]['state'], data[i]['id']))
        # print other options
        elif option == "state" or option == "id" or option == "title":
            print('Pull #{}. User: {}. {}: {}.'.
                  format(str(i + 1),
                         data[i]['user']['login'], option, data[i][option]))
        else:
            print('Wrong arguments. '
                  '"Type python prstats -h" To see help info.')
            break
