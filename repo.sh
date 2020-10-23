#!/bin/sh
TODO -- Convert cmd script into sh script
@echo off
goto main


help {
echo ====================================================
echo USAGE
echo =====
echo repo.cmd [command] [options]
echo ====================================================
echo Commands 
echo --help - This help text
echo --create [repository-name] - Create a new repository 
echo --delete [repository-name] - Delete a repository
echo ====================================================
echo Repository names cannot contain spaces or special 
echo characters
echo ====================================================
}


create {
reponame=$2
if [$reponame]==[] echo No repository name provided. Please use 'repo.cmd help' to see usage && pause && exit
echo # $reponame > README.md
python main.py --create $2
git init
git add README.md
git commit -m "Repository Initialised"
git branch -M main
git remote add origin https://github.com/$username/$reponame.git
git push -u origin main
exit
}

delete {
set reponame=$2
if [$reponame]==[] echo No repository name provided. Please use 'repo.cmd help' to see usage && exit
python main.py --delete $2
}


main {
if [$1]==[] echo No argument supplied. Please use 'help' to see usage && exit
if "$1"=="help" goto :help
if [$1]==[c] goto :create
if [$1]==[create] goto :create
if [$1]==[d] goto :delete
if [$1]==[delete] goto :delete
exit
}

exit
