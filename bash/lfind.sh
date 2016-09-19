#! /bin/bash
#    find source code in the local tree and below
#
if [ $# -eq 0 ]; then
  echo "Usage: $0 arg1 [arg2 arg3 arg4]"
  echo 'Search for files *args* from your current working directory down'
  exit 1
fi

#for a in $*; do
#    find . -name \*$a\* -print
#done
#exit 0

if [ $# -eq 1 ]; then
  find . -name \*$1\* -print
elif [ $# -eq 2 ]; then
  find . -name \*$1\* -print | grep -i $2
elif [ $# -eq 3 ]; then
  find . -name \*$1\* -print | grep -i $2 | grep -i $3
elif [ $# -eq 4 ]; then
  find . -name \*$1\* -print | grep -i $2 | grep -i $3 | grep -i $4
else
  echo Unsupported number of arguments, max is 4
  exit 1
fi
  
