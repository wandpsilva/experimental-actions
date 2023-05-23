#!/bin/bash

set -e

n1=${INPUT_N1}
n2=${INPUT_N2}

if [ $n1 -eq 0] || [ $n2 -eq 0 ]; then
      echo "informe valores maiores que zeros!"
fi

echo "$n1 and $n2"