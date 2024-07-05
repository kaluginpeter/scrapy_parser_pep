from pep_parse.constants import RESULT_DIR

BOT_NAME = 'pep_parse'
SPIDER_MODULES = ['pep_parse.spiders']

FEEDS = {
    f'{RESULT_DIR}/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True,
    }
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300
}
