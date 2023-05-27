#!/bin/bash

set -e


readme=$(cat README.md | wc -l)
if [ $readme -le 3 ]; then
      echo "Favor criar um readme para o projeto"
      exit 1
fi

ls -la
for f in ./*.java
do
      echo $f
      val=$(grep Mapper $f)
      if [ $val != "" ]; then
            echo "existe mapper"
            gh pr close ${INPUT_PRLINK} -c "PR fechada pois não atendeu o código não possui Mapper(componentModel = Spring)"
      fi
done