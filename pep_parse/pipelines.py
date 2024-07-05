import os
import csv
from collections import defaultdict

from pep_parse.constants import BASE_DIR, RESULT_DIR


class PepParsePipeline:
    def open_spider(self, spider):
        self.count_pep_statuses = defaultdict(int)

    def process_item(self, item, spider):
        self.count_pep_statuses[item['status']] += 1
        return item

    def close_spider(self, spider):
        filename = os.path.join(
            BASE_DIR, f'{RESULT_DIR}/status_summary_%(time)s.csv'
        )
        initial_fieldnames = ['Статус', 'Количество']
        self.count_pep_statuses['Total'] = sum(
            self.count_pep_statuses.values()
        )
        with open(filename, mode='w', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=initial_fieldnames)
            writer.writerows(self.count_pep_statuses)


if __name__ == '__main__':
    result_dir = BASE_DIR / RESULT_DIR
    result_dir.mkdir(exist_ok=True)
