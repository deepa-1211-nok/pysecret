#!/bin/bash

#いちいち実行がめんどいのでまとめる
arg=$1
if [ $arg == test ]
then
    python3 -m unittest test/test.py
fi
