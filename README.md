# weekly-top-200-songs-by-country
## Overview

This Python script allows you to generate a Spotify playlist containing the top 200 songs of a specific country using the Spotify Charts API. The script scrapes the Spotify Charts website to gather the song data and creates a playlist for the specified country.

## Prerequisites
Python 3.x
pip (Python package manager)

## Installation
1. Clone the repository to your local machine
2. Change into the project directory
3. install the required Python packages

Packages required: spotipy, requests, decouple, os

## Usage
Run the script by providing the username and country as command-line arguments. The username is your Spotify username, and the country is the name of the country you want to generate the playlist for. The supported countries are stated in countrycodes.py. 

The terminal call is written in the following way: 

python main.py &lt;username&gt; &lt;country&gt;

## Example Calls:
United States: python main.py &lt;username&gt; united states

Canada: python main.py &lt;username&gt; canada

## Notes:
- Make sure to set up a Spotify Developer account and obtain API credentials if you haven't already.
- You will need to authenticate the script with your Spotify account the first time you run it.
