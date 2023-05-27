#!/bin/bash

set -e


if [ ${{github.event_name != "pull_request"}} ]; then
      echo "Tipo de evento invalido para avaliacao de codigo"
fi


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
            gh pr close ${{ github.event.pull_request._links.self.href }} -c "PR fechada pois não atendeu o código não possui Mapper(componentModel = Spring)"
      fi
done