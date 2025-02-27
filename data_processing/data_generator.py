import pandas as pd
from config.settings import settings

class DataGenerator:
    def __init__(self, processor):
        self.processor = processor

    def generate_dataset(self) -> pd.DataFrame:
        data = []
        for file_name, path in settings.file_paths.items():
            file_data = self.processor.process_file(path)
            if file_data and file_name in file_data:
                self._extract_items(data, file_name, file_data[file_name])
        return self._create_dataframe(data)

    def _extract_items(self, data: list, file_name: str, items: dict):
        for item_name, value in items.items():
            data.append({
                'filename': file_name,
                'items': item_name,
                'results': value,
                'details': ''
            })

    def _create_dataframe(self, data: list) -> pd.DataFrame:
        df = pd.DataFrame(data)
        if not df.empty:
            df = df[['filename', 'items', 'results', 'details']]
            df.to_csv(settings.OUTPUT_CSV, index=False)
        return df