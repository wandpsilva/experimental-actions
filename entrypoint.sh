#!/bin/bash

set -e

if [ cat README.md | wc -l -le 1 ]; then
      echo "Favor criar um readme para o projeto"
fi