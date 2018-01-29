#!/bin/bash

cd ~/Desktop/git-rep/PyQt-audio-record/
source ~/tensorflow_cpu/bin/activate
deepspeech ~/Desktop/models/output_graph.pb test.wav ~/Desktop/models/alphabet.txt
