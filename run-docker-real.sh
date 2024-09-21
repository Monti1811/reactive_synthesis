#!/bin/sh

cat $1 | docker run -i -a stderr -a stdin -a stdout reactive-synthesis-lecture-2024 /synthesize -r

