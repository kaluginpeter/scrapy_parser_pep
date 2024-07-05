import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        links_on_peps = response.css(
            'section#index-by-category section tr a.pep'
        )[::2]
        for link_on_pep in links_on_peps:
            yield response.follow(link_on_pep, callback=self.parse_pep)

    def parse_pep(self, response):
        title = response.css('section#pep-content h1.page-title::text').get()
        separator_index = title.index('–')
        number = int(title[4:separator_index - 1])
        name = title[separator_index + 2:]
        status_of_pep = response.css(
            'dl.rfc2822 dd.field-even abbr::text'
        ).get()
        pep_item = PepParseItem(
            number=number,
            name=name,
            status=status_of_pep
        )
        yield pep_item
