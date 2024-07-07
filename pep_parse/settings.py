from pathlib import Path


RESULT_DIR = 'results'
BASE_DIR = Path(__file__).parent
BOT_NAME = 'pep_parse'
SPIDER_MODULE = 'pep_parse.spiders'
SPIDER_MODULES = [SPIDER_MODULE]
NEWSPIDER_MODULE = SPIDER_MODULE

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
