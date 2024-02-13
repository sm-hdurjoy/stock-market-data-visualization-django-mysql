# populate_db.py
import json
from yourapp.models import Trade  # Import your model
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        with open('your_json_file.json', 'r') as file:
            data = json.load(file)
            for item in data:
                Trade.objects.create(
                    date=item['date'],
                    trade_code=item['trade_code'],
                    high=item['high'],
                    low=item['low'],
                    open=item['open'],
                    close=item['close'],
                    volume=item['volume']
                )
        self.stdout.write(self.style.SUCCESS('Database populated successfully'))
