#!/usr/local/bin/bash

filename="input.txt"
readarray -t numbers <${filename}

count=0
for ((idx = 0; idx < ${#numbers[@]}; ++idx)); do
	y=$((idx + 1))
	n1="${numbers[idx]}"
	n2="${numbers[y]}"
	if [[ n2 -gt n1 ]]; then
		((count += 1))
	fi
done
echo "${count}"
