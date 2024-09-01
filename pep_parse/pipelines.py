import csv
from datetime import datetime as dt
from pathlib import Path


BASE_DIR = Path(__file__).parent.parent


class PepParsePipeline:

    def open_spider(self, spider):
        self.pep_statuses_count = {}

    def process_item(self, item, spider):
        self.pep_statuses_count[item['status']] = self.pep_statuses_count.get(
            item['status'], 0) + 1
        return item

    def close_spider(self, spider):
        self.pep_statuses_count['Total'] = sum(
            self.pep_statuses_count.values())
        total_statuses = list(
            ({'Статус': 'Количество'} | self.pep_statuses_count).items())
        now = dt.now()
        now_formatted = now.strftime('%Y-%m-%d_%H-%M-%S')
        file_name = f'results/status_summary_{now_formatted}.csv'
        file_path = BASE_DIR / file_name
        with open(file_path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f, dialect='unix')
            writer.writerows(total_statuses)
