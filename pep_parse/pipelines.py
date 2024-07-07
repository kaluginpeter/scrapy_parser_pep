import csv
from collections import defaultdict
import datetime as dt

from pep_parse.settings import BASE_DIR, RESULT_DIR


class PepParsePipeline:
    def __init__(self):
        self.result_dir = BASE_DIR / RESULT_DIR
        self.result_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.count_pep_statuses = defaultdict(int)

    def process_item(self, item, spider):
        self.count_pep_statuses[item['status']] += 1
        return item

    def close_spider(self, spider):
        current_time = dt.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        filename = self.result_dir / f'status_summary_{current_time}.csv'
        with open(filename, mode='w', encoding='utf-8') as csvfile:
            csv.DictWriter(csvfile).writerows([
                ('Статус', 'Количество'),
                *self.count_pep_statuses.items(),
                ('Total', sum(
                    self.count_pep_statuses.values()
                ))
            ])
