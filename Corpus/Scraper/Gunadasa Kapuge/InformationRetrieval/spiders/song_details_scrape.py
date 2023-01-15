import scrapy
from InformationRetrieval.items import SongItem
from datetime import datetime
import re


class InformationRetrieval(scrapy.Spider):
    name = "my_scraper"

    # First Start Url
    name = "my_scraper"

    # First Start Url
    start_urls = ['https://www.lklyrics.com/songs/gunadasa_kapuge/bimbarak_senaga',
 'https://www.lklyrics.com/songs/gunadasa_kapuge/bindu_bindu_tharaka',
 'https://www.lklyrics.com/songs/gunadasa_kapuge/bindunu_pem_hada',
 'https://www.lklyrics.com/songs/gunadasa_kapuge/daasa_nilupul_thema',
 'https://www.lklyrics.com/songs/gunadasa_kapuge/dawasak_pela_nethi_hene',
 'https://www.lklyrics.com/songs/gunadasa_kapuge/dethola_nokee_dey_muhune_liyawenawa',
 'https://www.lklyrics.com/songs/gunadasa_kapuge/domba_mal_kalawe',
 'https://www.lklyrics.com/songs/gunadasa_kapuge/gangawe_geethe',
 'https://www.lklyrics.com/songs/gunadasa_kapuge/ira_batu_tharuwa_2',
 'https://www.lklyrics.com/songs/gunadasa_kapuge/kalladi_palama',
 'https://www.lklyrics.com/songs/gunadasa_kapuge/leli_thalana_nube_athata',
 'https://www.lklyrics.com/songs/gunadasa_kapuge/mage_hada_madala',
 'https://www.lklyrics.com/songs/gunadasa_kapuge/man_mulaavee',
 'https://www.lklyrics.com/songs/gunadasa_kapuge/mariyawe',
 'https://www.lklyrics.com/songs/gunadasa_kapuge/na_kola_andam',
 'https://www.lklyrics.com/songs/gunadasa_kapuge/naabara_goyamata',
 'https://www.lklyrics.com/songs/gunadasa_kapuge/oba_pem_karana',
 'https://www.lklyrics.com/songs/gunadasa_kapuge/obata_yanna_onaa_nam',
 'https://www.lklyrics.com/songs/gunadasa_kapuge/palanchiye_weda_indagena',
 'https://www.lklyrics.com/songs/gunadasa_kapuge/pasak_kota_athy',
 'https://www.lklyrics.com/songs/gunadasa_kapuge/piya_satahan_makii_nomatha_thawa',
 'https://www.lklyrics.com/songs/gunadasa_kapuge/ruwak_adenawa',
 'https://www.lklyrics.com/songs/gunadasa_kapuge/sabanda_api_kandu_nowemu',
 'https://www.lklyrics.com/songs/gunadasa_kapuge/seda_sihina_sudu',
 'https://www.lklyrics.com/songs/gunadasa_kapuge/senehe_sithin',
 'https://www.lklyrics.com/songs/gunadasa_kapuge/sinhala_sindu_kiyana',
 'https://www.lklyrics.com/songs/gunadasa_kapuge/sonduru_numba_lihiniyaka',
 'https://www.lklyrics.com/songs/gunadasa_kapuge/sudu_nanda_ai',
 'https://www.lklyrics.com/songs/gunadasa_kapuge/tharu_rana_ridi_pata_pata',
 'https://www.lklyrics.com/songs/gunadasa_kapuge/unmaada_sithuwam',
 'https://www.lklyrics.com/songs/gunadasa_kapuge/viduli_mini_pahan']

                    
    def parse(self, response):
        item = SongItem()

        
        item['Title'] = response.xpath("//h1/descendant::text()").extract()
        item['Singer'] = response.xpath("//table[contains(@class, 'table table-bordered')]//tr[1]/td/a/descendant::text()").extract()
        item['Composer'] = response.xpath("//table[contains(@class, 'table table-bordered')]//tr[2]/td/a/descendant::text()").extract()
        item['Lyricist'] = response.xpath("//table[contains(@class, 'table table-bordered')]//tr[3]/td/a/descendant::text()").extract()
        item['image'] = response.xpath("//div[contains(@class, 'col-md-6')]//img/@src").extract()


        yield item