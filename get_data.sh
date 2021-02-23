mkdir Data
cd plstats
scrapy crawl alltime -O alltime.json
cd ..
python clean_team_data.py