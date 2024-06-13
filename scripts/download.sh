#!/bin/bash

set -ex
# pip install video2dataset

#python save_video_txt.py
rm -rf ./videos ./tmp
mkdir ./tmp
video2dataset --url_list="videos.txt" --output_folder="videos" --input_format "txt" --output_format "files" --tmp_dir "./tmp"