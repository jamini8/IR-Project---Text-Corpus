import scrapy
from InformationRetrieval.items import SongItem
from datetime import datetime
import re


class InformationRetrieval(scrapy.Spider):
    name = "my_scraper"

    # First Start Url
    name = "my_scraper"

    # First Start Url
    start_urls = ['https://www.lklyrics.com/songs/amaradewa_w_d/adawan_wu_denethin_galana',
 'https://www.lklyrics.com/songs/amaradewa_w_d/ama_ganga_galala',
 'https://www.lklyrics.com/songs/amaradewa_w_d/aradhana_2',
 'https://www.lklyrics.com/songs/amaradewa_w_d/ase_mathuwana',
 'https://www.lklyrics.com/songs/amaradewa_w_d/bodhiyen_wata',
 'https://www.lklyrics.com/songs/amaradewa_w_d/daru_duka_uhula',
 'https://www.lklyrics.com/songs/amaradewa_w_d/das_kon_saki_sanda',
 'https://www.lklyrics.com/songs/amaradewa_w_d/dathe_elli',
 'https://www.lklyrics.com/songs/amaradewa_w_d/dathe_karagata',
 'https://www.lklyrics.com/songs/amaradewa_w_d/gilem_obe_guna_mude',
 'https://www.lklyrics.com/songs/amaradewa_w_d/guru_gedara',
 'https://www.lklyrics.com/songs/amaradewa_w_d/hanthane_',
 'https://www.lklyrics.com/songs/amaradewa_w_d/handapane_weli_thala',
 'https://www.lklyrics.com/songs/amaradewa_w_d/hanthana_sihine_bala_walapemi',
 'https://www.lklyrics.com/songs/amaradewa_w_d/heena_hathak_mada',
 'https://www.lklyrics.com/songs/amaradewa_w_d/heen_sare_oba_awa_awa',
 'https://www.lklyrics.com/songs/amaradewa_w_d/kale_gahaka_mal',
 'https://www.lklyrics.com/songs/amaradewa_w_d/kale_pipunu_malak_wilasa',
 'https://www.lklyrics.com/songs/amaradewa_w_d/kanda_udin_ena',
 'https://www.lklyrics.com/songs/amaradewa_w_d/kandulu_kathawe',
 'https://www.lklyrics.com/songs/amaradewa_w_d/karadara_podi_banda',
 'https://www.lklyrics.com/songs/amaradewa_w_d/mage_kandulin',
 'https://www.lklyrics.com/songs/amaradewa_w_d/maha_piritha_wi_numba',
 'https://www.lklyrics.com/songs/amaradewa_w_d/mahaweli_mahaweli',
 'https://www.lklyrics.com/songs/amaradewa_w_d/mal_gomu_gomu',
 'https://www.lklyrics.com/songs/amaradewa_w_d/mala_ira_basina_sanda_yaame',
 'https://www.lklyrics.com/songs/amaradewa_w_d/me_guru_pare',
 'https://www.lklyrics.com/songs/amaradewa_w_d/mihipita_angalak_himi_nethi_minisek',
 'https://www.lklyrics.com/songs/amaradewa_w_d/mindada_hee_sara',
 'https://www.lklyrics.com/songs/amaradewa_w_d/muni_siri_pa_simbiminne',
 'https://www.lklyrics.com/songs/amaradewa_w_d/muwarada_bara_pipi_mal_gomu',
 'https://www.lklyrics.com/songs/amaradewa_w_d/nil_maane_mal_pipuna',
 'https://www.lklyrics.com/songs/amaradewa_w_d/nila_kobei_raana_adi',
 'https://www.lklyrics.com/songs/amaradewa_w_d/nim_him_sewwa_ma_sasare',
 'https://www.lklyrics.com/songs/amaradewa_w_d/niwan_purata_maga_penwana',
 'https://www.lklyrics.com/songs/amaradewa_w_d/oba_ma_thurule',
 'https://www.lklyrics.com/songs/amaradewa_w_d/oba_sumudu_neth',
 'https://www.lklyrics.com/songs/amaradewa_w_d/obe_sina_wikasitha_wewa',
 'https://www.lklyrics.com/songs/amaradewa_w_d/paalu_anduru_nil_ahasa_mamai',
 'https://www.lklyrics.com/songs/amaradewa_w_d/paloswaka_sanda_payanu_wenne',
 'https://www.lklyrics.com/songs/amaradewa_w_d/pem_rala_patharin',
 'https://www.lklyrics.com/songs/amaradewa_w_d/premaye_nijabima',
 'https://www.lklyrics.com/songs/amaradewa_w_d/rana_gira_joduwayi',
 'https://www.lklyrics.com/songs/amaradewa_w_d/sandakath_pini_diya',
 'https://www.lklyrics.com/songs/amaradewa_w_d/sansare_eka_mohothak',
 'https://www.lklyrics.com/songs/amaradewa_w_d/sasara_wasana_thuru',
 'https://www.lklyrics.com/songs/amaradewa_w_d/seetha_pini_bindu',
 'https://www.lklyrics.com/songs/amaradewa_w_d/seethala_wathura_galayi',
 'https://www.lklyrics.com/songs/amaradewa_w_d/shantha_me_ra_yame',
 'https://www.lklyrics.com/songs/amaradewa_w_d/sihina_nelum_mala',
 'https://www.lklyrics.com/songs/amaradewa_w_d/sihina_sathak_mada',
 'https://www.lklyrics.com/songs/amaradewa_w_d/siripa_piyume',
 'https://www.lklyrics.com/songs/amaradewa_w_d/sithiwili_opala',
 'https://www.lklyrics.com/songs/amaradewa_w_d/swarna_wimaaneta_eha_lokayen']

                    
    def parse(self, response):
        item = SongItem()

        
        item['Title'] = response.xpath("//h1/descendant::text()").extract()
        item['Singer'] = response.xpath("//table[contains(@class, 'table table-bordered')]//tr[1]/td/a/descendant::text()").extract()
        item['Composer'] = response.xpath("//table[contains(@class, 'table table-bordered')]//tr[2]/td/a/descendant::text()").extract()
        item['Lyricist'] = response.xpath("//table[contains(@class, 'table table-bordered')]//tr[3]/td/a/descendant::text()").extract()
        item['image'] = response.xpath("//div[contains(@class, 'col-md-6')]//img/@src").extract()


        yield item