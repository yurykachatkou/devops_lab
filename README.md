###### PrStats

###### Version 1.1

###### Description

Simple python app to get information about pull requests

#### Usage


usage: `python prstats.py [-h] -ow OWNER -r REPO [-u USER] [-op OPTION] [-v]`

optional arguments:
  `-h, --help`            show this help message and exit
  
  `-ow OWNER, --owner OWNER` Owner of a repository
  
                        
  `-r REPO, --repo REPO`  Name of a repository
  `-u USER, --user USER`  Info for user who made pull requests. If not
                        specified, info for all users will be outputted
			
  `-op OPTION, --option OPTION`
  
Input options: 
`state` - to get a state of PR,
`title` - to get PR title,
`id` - to get id of PR,
`weeks` - to get a week number, PR was opened,
`title` - to get a title of PR.
If not specified, all option will be outputted
`-v`show program's version number and exit


#### Output Examples

![Image](/images/prstats.png)


