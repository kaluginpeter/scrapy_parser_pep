import os
import csv
from collections import defaultdict

BASE_DIR = BASE_DIR = os.path.dirname(os.path.dirname(__file__))


class PepParsePipeline:
    def open_spider(self, spider):
        self.filename = os.path.join(
            BASE_DIR, 'results/status_summary_%(time)s.csv'
        )
        self.count_pep_statuses = defaultdict(int)
        self.count_peps = 0

    def process_item(self, item, spider):
        self.count_peps += 1
        self.count_pep_statuses[item['status']] += 1
        return item

    def close_spider(self, spider):
        initial_fieldnames = ['Статус', 'Количество']
        final_row = ['Total', self.count_peps]
        with open(self.filename, mode='w', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=initial_fieldnames)
            writer.writeheader()
            for status, count in self.count_pep_statuses.items():
                writer.writerow(
                    {
                        initial_fieldnames[0]: status,
                        initial_fieldnames[1]: count
                    }
                )
            writer.writerow(
                {
                    initial_fieldnames[0]: final_row[0],
                    initial_fieldnames[1]: final_row[1]
                }
            )
