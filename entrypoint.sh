#!/bin/bash

set -e


readme=$(cat README.md | wc -l)
if [ $readme -le 3 ]; then
      echo "Favor criar um readme para o projeto com pelo menos 4 linhas"
      exit 1
fi


for f in ./*.java; do 
      if grep -q "Mapper" $f; then
            if ! grep -q "componentModel" $f; then
                  echo "O mapper da classe $f nao possui anotacao componentModel = Spring"
                  gh pr close ${PR} -c "PR fechado devido falhas na validacao de qualidade do codigo!"
            fi
      fi
done