#!/bin/sh

echo "Getting DA:O codices..."
python3 get_dao_codices.py
echo "Got DA:O codices!"
echo "Getting DA2 codices..."
python3 get_da2_codices.py
echo "Got DA2 codices!"
echo "Getting DA:I codices..."
python3 get_dai_codices.py
echo "Got DA:I codices!"
echo "Got codices for all games!"