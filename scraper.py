from dc_base_scrapers.geojson_scraper import GeoJsonScraper
from dc_base_scrapers.hashonly_scraper import HashOnlyScraper


search_url = "https://opendata.arcgis.com/api/v3/search?q=polling&sort=-modified&agg%5Bfields%5D=downloadable%2ChasApi%2Csource%2Ctags%2Ctype%2Caccess&catalog%5BgroupIds%5D=any(6ecd0e3c9f47481bbccdd7e419ccf212)"
stations_url = "https://data-lbhf.opendata.arcgis.com/datasets/c15c9a3aca054d4cb7c6b3f84779d64d_0.geojson"
districts_url = "https://data-lbhf.opendata.arcgis.com/datasets/c15c9a3aca054d4cb7c6b3f84779d64d_11.geojson"
council_id = "E09000013"


search_scraper = HashOnlyScraper(search_url, council_id, 'datasets', 'json')
search_scraper.scrape()
stations_scraper = GeoJsonScraper(stations_url, council_id, 'utf-8', 'stations', key='OBJECTID')
stations_scraper.scrape()
districts_scraper = GeoJsonScraper(districts_url, council_id, 'utf-8', 'districts', key='OBJECTID')
districts_scraper.scrape()
