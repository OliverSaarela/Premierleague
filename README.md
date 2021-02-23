# Scraping all Premier League stats

Scrapes alltime data from every team that has played in the Premier League into a .csv file.

## Getting started

To get a local copy up and running follow these simple steps.

### Prerequisites

* [python 3.7.9](https://www.python.org/)

### Installation

1. Clone the repo 

```sh
git clone https://github.com/OliverSaarela/Premierleague.git
```

2. Install python packages

Create and activate a virtual environment. Then install the packages from requirements.txt

```sh
pip install -r requirements.txt
```

3. Run .sh file

```sh
bash get_data.sh
```

.csv file is now saved in Data folder. File name format is `YYYY-MM-DD_team_data.csv`