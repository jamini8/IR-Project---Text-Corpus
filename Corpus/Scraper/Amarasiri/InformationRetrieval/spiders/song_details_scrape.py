import scrapy
from InformationRetrieval.items import SongItem
from datetime import datetime
import re


class InformationRetrieval(scrapy.Spider):
    name = "my_scraper"

    # First Start Url
    name = "my_scraper"

    # First Start Url
    start_urls = ['https://www.lklyrics.com/songs/amarasiri_peiris/aa_maga_waradi_sandagalathanna',
 'https://www.lklyrics.com/songs/amarasiri_peiris/hima_diyawi_himalaye',
 'https://www.lklyrics.com/songs/amarasiri_peiris/digasiye_digu_neela_nayana',
'https://www.lklyrics.com/songs/amarasiri_peiris/me_ekama_sandak_yata_dehadak_hamu_wi','https://www.lklyrics.com/songs/amarasiri_peiris/me_kirula_bara_wadi_devi',
'https://www.lklyrics.com/songs/amarasiri_peiris/niyangayata_pasu','https://www.lklyrics.com/songs/amarasiri_peiris/rathriya_sira_geyak','https://www.lklyrics.com/songs/amarasiri_peiris/sakman_sada_ikman_kara','https://www.lklyrics.com/songs/amarasiri_peiris/mage_punchi_rosa_male','https://www.lklyrics.com/songs/amarasiri_peiris/charu_dehe_nura','https://www.lklyrics.com/songs/amarasiri_peiris/dara_duka_sathuta','https://www.lklyrics.com/songs/amarasiri_peiris/dawala_wala_thira','https://www.lklyrics.com/songs/amarasiri_peiris/dhawala_wala_thira_wiwara_karana_saki','https://www.lklyrics.com/songs/amarasiri_peiris/epa_miwitha','https://www.lklyrics.com/songs/amarasiri_peiris/ganga_gala_yaden']

                    
    def parse(self, response):
        item = SongItem()

        
        item['Title'] = response.xpath("//h1/descendant::text()").extract()
        item['Singer'] = response.xpath("//table[contains(@class, 'table table-bordered')]//tr[1]/td/a/descendant::text()").extract()
        item['Composer'] = response.xpath("//table[contains(@class, 'table table-bordered')]//tr[2]/td/a/descendant::text()").extract()
        item['Lyricist'] = response.xpath("//table[contains(@class, 'table table-bordered')]//tr[3]/td/a/descendant::text()").extract()
        item['image'] = response.xpath("//div[contains(@class, 'col-md-6')]//img/@src").extract()


        yield item