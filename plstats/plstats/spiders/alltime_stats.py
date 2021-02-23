import scrapy

class alltime_spider(scrapy.Spider):
    name = 'alltime'

    start_urls = [
        'https://www.premierleague.com/clubs/1/Arsenal/stats',
        'https://www.premierleague.com/clubs/2/Aston-Villa/stats',
        'https://www.premierleague.com/clubs/30/Barnsley/stats',
        'https://www.premierleague.com/clubs/35/Birmingham-City/stats',
        'https://www.premierleague.com/clubs/3/Blackburn-Rovers/stats',
        'https://www.premierleague.com/clubs/44/Blackpool/stats',
        'https://www.premierleague.com/clubs/27/Bolton-Wanderers/stats',
        'https://www.premierleague.com/clubs/127/Bournemouth/stats',
        'https://www.premierleague.com/clubs/32/Bradford-City/stats',
        'https://www.premierleague.com/clubs/131/Brighton-and-Hove-Albion/stats',
        'https://www.premierleague.com/clubs/43/Burnley/stats',
        'https://www.premierleague.com/clubs/46/Cardiff-City/stats',
        'https://www.premierleague.com/clubs/31/Charlton-Athletic/stats',
        'https://www.premierleague.com/clubs/4/Chelsea/stats',
        'https://www.premierleague.com/clubs/5/Coventry-City/stats',
        'https://www.premierleague.com/clubs/6/Crystal-Palace/stats',
        'https://www.premierleague.com/clubs/28/Derby-County/stats',
        'https://www.premierleague.com/clubs/7/Everton/stats',
        'https://www.premierleague.com/clubs/34/Fulham/stats',
        'https://www.premierleague.com/clubs/159/Huddersfield-Town/stats',
        'https://www.premierleague.com/clubs/41/Hull-City/stats',
        'https://www.premierleague.com/clubs/8/Ipswich-Town/stats',
        'https://www.premierleague.com/clubs/9/Leeds-United/stats',
        'https://www.premierleague.com/clubs/26/Leicester-City/stats',
        'https://www.premierleague.com/clubs/10/Liverpool/stats',
        'https://www.premierleague.com/clubs/11/Manchester-City/stats',
        'https://www.premierleague.com/clubs/12/Manchester-United/stats',
        'https://www.premierleague.com/clubs/13/Middlesbrough/stats',
        'https://www.premierleague.com/clubs/23/Newcastle-United/stats',
        'https://www.premierleague.com/clubs/14/Norwich-City/stats',
        'https://www.premierleague.com/clubs/15/Nottingham-Forest/stats',
        'https://www.premierleague.com/clubs/16/Oldham-Athletic/stats',
        'https://www.premierleague.com/clubs/37/Portsmouth/stats',
        'https://www.premierleague.com/clubs/17/Queens-Park-Rangers/stats',
        'https://www.premierleague.com/clubs/40/Reading/stats',
        'https://www.premierleague.com/clubs/18/Sheffield-United/stats',
        'https://www.premierleague.com/clubs/19/Sheffield-Wednesday/stats',
        'https://www.premierleague.com/clubs/20/Southampton/stats',
        'https://www.premierleague.com/clubs/42/Stoke-City/stats',
        'https://www.premierleague.com/clubs/29/Sunderland/stats',
        'https://www.premierleague.com/clubs/45/Swansea-City/stats',
        'https://www.premierleague.com/clubs/24/Swindon-Town/stats',
        'https://www.premierleague.com/clubs/21/Tottenham-Hotspur/stats',
        'https://www.premierleague.com/clubs/33/Watford/stats',
        'https://www.premierleague.com/clubs/36/West-Bromwich-Albion/stats',
        'https://www.premierleague.com/clubs/25/West-Ham-United/stats',
        'https://www.premierleague.com/clubs/39/Wigan-Athletic/stats',
        'https://www.premierleague.com/clubs/22/Wimbledon/stats',
        'https://www.premierleague.com/clubs/38/Wolverhampton-Wanderers/stats',
    ]

    def parse(self, response):
        yield {
            'team': response.url.split('/')[-2], # Getting team name
            'names': response.xpath('//span[@class="stat"]/text()').getall(), # Getting stat names
            'values': response.xpath('//span[@class="stat"]/span/text()').getall(), # Getting stat values
        }
            