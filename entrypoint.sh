#!/bin/bash

set -e
readme=$(cat README.md | wc -l)

if [ $readme -le 1 ]; then
      echo "Favor criar um readme para o projeto"
fi