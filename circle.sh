#!/bin/bash
# run the script 100 times
for i in {1..100}
do
    echo "Running iteration $i"
    /home/beijiang/auto_fill/venv/bin/python3.10 /home/beijiang/auto_fill/wjx.py
    sleep 2
done
