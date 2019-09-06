from dc_base_scrapers.geojson_scraper import GeoJsonScraper
from dc_base_scrapers.hashonly_scraper import HashOnlyScraper


search_url = "https://opendata.arcgis.com/api/v2/datasets?filter[catalogs]=data-lbhf.opendata.arcgis.com&include=organizations%2Cgroups&page[number]=1&page[size]=10&q=polling&sort=-updatedAt"
stations_url = "https://data-lbhf.opendata.arcgis.com/datasets/c15c9a3aca054d4cb7c6b3f84779d64d_0.geojson"
districts_url = "https://data-lbhf.opendata.arcgis.com/datasets/c15c9a3aca054d4cb7c6b3f84779d64d_11.geojson"
council_id = "E09000013"


search_scraper = HashOnlyScraper(search_url, council_id, 'datasets', 'json')
search_scraper.scrape()
stations_scraper = GeoJsonScraper(stations_url, council_id, 'utf-8', 'stations', key='OBJECTID')
stations_scraper.scrape()
districts_scraper = GeoJsonScraper(districts_url, council_id, 'utf-8', 'districts', key='OBJECTID')
districts_scraper.scrape()
