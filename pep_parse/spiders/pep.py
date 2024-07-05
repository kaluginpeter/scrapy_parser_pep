import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = [f'https://{link}/' for link in allowed_domains]

    def parse(self, response):
        for link_on_pep in response.css(
            'section#index-by-category section tr a.pep'
        )[::2]:
            yield response.follow(link_on_pep, callback=self.parse_pep)

    def parse_pep(self, response):
        title = response.css('section#pep-content h1.page-title::text').get()
        separator_index = title.index('–')
        yield PepParseItem(
            number=title[4:separator_index - 1],
            name=title[separator_index + 2:],
            status=response.css(
                'dl.rfc2822 dd.field-even abbr::text'
            ).get()
        )
