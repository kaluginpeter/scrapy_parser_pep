import os
import csv
import datetime as dt
from collections import defaultdict

from pep_parse.settings import BASE_DIR, RESULT_DIR


class PepParsePipeline:
    def open_spider(self, spider):
        result_dir = BASE_DIR / RESULT_DIR
        result_dir.mkdir(exist_ok=True)
        self.count_pep_statuses = defaultdict(int)

    def process_item(self, item, spider):
        self.count_pep_statuses[item['status']] += 1
        return item

    def close_spider(self, spider):
        CURRENT_TIME = dt.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        filename = os.path.join(
            BASE_DIR, f'{RESULT_DIR}/status_summary_{CURRENT_TIME}.csv'
        )
        initial_fieldnames = ['Статус', 'Количество']
        self.count_pep_statuses['Total'] = sum(
            self.count_pep_statuses.values()
        )
        with open(filename, mode='w', encoding='utf-8') as csvfile:
            csv.DictWriter(
                csvfile, fieldnames=initial_fieldnames
            ).writerows(self.count_pep_statuses)
