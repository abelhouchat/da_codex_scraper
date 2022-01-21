#!/bin/sh

echo "Getting DA:O codices..."
python3 get_da1_codices.py
echo "Got DA:O codices!"
echo "Getting DA2 codices..."
python3 get_da2_codices.py
echo "Got DA2 codices!"
echo "Getting DA:I codices..."
python3 get_da3_codices.py
echo "Got DA:I codices!"
echo "Got codices for all games!"

echo "Getting DA2 letters..."
python3 get_da2_letters.py
echo "Got DA2 letters!"
echo "Getting DA2 short stories..."
python3 get_da2_short_stories.py
echo "Got DA2 short stories!"

echo "Getting DA:I notes..."
python3 get_da3_notes.py
echo "Got DA:I notes!"
echo "Getting DA:I short stories..."
python3 get_da3_short_stories.py
echo "Got DA:I short stories!"

echo "Getting DA4 short stories..."
python3 get_da4_short_stories.py
echo "Get DA4 short stories!"
