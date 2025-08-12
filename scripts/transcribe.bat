@echo off

set YEAR=%DATE:~0,4%
set MONTH=%DATE:~5,2%
set DAY=%DATE:~8,2%

set HOUR=%TIME:~0,2%
set MINUTE=%TIME:~3,2%
set SECOND=%TIME:~6,2%

python .\whisper_streaming\whisper_online.py .\results\dummy\output.mp3 --min-chunk-size 1 --model small.en --model_cache_dir .\models\whisper --lan auto --task transcribe --backend faster-whisper --vac --vac-chunk-size 1 -l DEBUG > ".\results\%YEAR%-%MONTH%-%DAY%_%HOUR%-%MINUTE%-%SECOND%.txt"