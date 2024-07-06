from pathlib import Path


RESULT_DIR = 'results'
BASE_DIR = Path(__file__).parent
BOT_NAME = 'pep_parse'
SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULES = SPIDER_MODULES

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
