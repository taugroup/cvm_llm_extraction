import os
import json
import re
from docling.document_converter import DocumentConverter
from llm.llm_client import llm_client
from utils.prompts import PromptGenerator

class FileProcessor:
    def __init__(self):
        self.converter = DocumentConverter()
        self.prompt_generator = PromptGenerator()

    def process_file(self, file_path: str) -> dict:
        try:
            file_name = os.path.basename(file_path).split('.')[0]
            print(f"Processing {file_name}...")
            content = self._convert_to_markdown(file_path)
            prompt = self.prompt_generator.create_extraction_prompt(file_name, content)
            response = llm_client.query(prompt)
            return self._parse_response(response)
        except Exception as e:
            print(f"Error processing {file_path}: {str(e)}")
            return {}

    def _convert_to_markdown(self, file_path: str) -> str:
        result = self.converter.convert(file_path)
        return result.document.export_to_markdown()

    def _parse_response(self, response: str) -> dict:
        json_pattern = re.compile(r'```json(.*?)```', re.DOTALL)
        match = json_pattern.search(response)
        if not match:
            raise ValueError("No JSON found in response")
        return json.loads(match.group(1).strip())