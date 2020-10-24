#!/bin/bash

help() {
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


create() {
  reponame=$1
  if [ "$reponame" = "" ]; then echo No repository name provided. Please use 'repo.cmd help' to see usage && read -n1 -r -p "Press any key to exit" key && exit
  fi
  echo # $1 > README.md
  python3 main.py --create $1
  git init
  git add README.md
  git commit -m "Repository Initialised"
  git branch -M main
  git remote add origin https://github.com/$username/$$1.git
  git push -u origin main
}

delete() {
  reponame=$1
  if [ "$reponame" = "" ]; then echo No repository name provided. Please use 'repo.cmd help' to see usage && exit
  fi
  python3 main.py --delete $1
}


main() {
  if [ "$1" = "" ]; then echo No argument supplied. Please use 'help' to see usage && exit; fi;
  if [ "$1" = "help" ]; then help; fi;
  if [ "$1" = "c" ]; then create $2; fi;
  if [ "$1" = "create" ]; then create $2; fi;
  if [ "$1" = "d" ]; then delete $2; fi;
  if [ "$1" = "delete" ]; then delete $2; fi;
}

main $1 $2

exit
