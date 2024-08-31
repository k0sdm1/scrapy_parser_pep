import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse_pep(self, response):
        pep_data = response.meta['pep_data']
        pep_status = response.css(
            'dt:contains("Status") + dd abbr::text').get()
        pep_data['status'] = pep_status
        yield PepParseItem(pep_data)

    def parse(self, response):
        all_pep_rows = response.css('table.pep-zero-table tbody tr')
        for pep in all_pep_rows:
            pep_number_query, pep_name_query = pep.css('td a')
            pep_data = {
                'number': pep_number_query.css('a::text').get(),
                'name': pep_name_query.css('a::text').get(),
            }
            yield response.follow(
                pep_number_query,
                callback=self.parse_pep,
                meta={'pep_data': pep_data}
            )
