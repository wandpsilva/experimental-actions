#!/bin/bash

set -e
readme=$(cat README.md | wc -l)

if [ $readme -le 3 ]; then
      echo "Favor criar um readme para o projeto"
      exit 1
fi

mapper="false"
for f in ./*.java
do
      echo $f
      val=$(grep Mapper $f)
      if [ $val != "" ]; then
            echo "existe mapper"
      fi
done


#gh pr close ${{ github.pulls_url }} -c "PR fechada pois não atendeu o código não possui Mapper(componentModel = Spring)"