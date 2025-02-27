from utils.constants import ITEMS_DICT

class PromptGenerator:
    @staticmethod
    def create_extraction_prompt(file_name: str, content: str) -> str:
        return f"""
    Analyze this veterinary medical document and extract structured data in JSON format.
    Extract the details with the following categories as keys: {ITEMS_DICT[file_name]}, with the main key being '{file_name}'.
    Follow this exact format:
    ```{{
        "{file_name}": {{
            "category1": "<value>",
            "category2": "<value>",
            ...
        }}
    }}
    ```

    DO NOT CREATE MULTIPLE SUB KEYS. 
    If there are any units, please include them in the extracted values. example: glucose: "100 mg/dL"
    Extract ALL available information from this text:
    {content}

    Return ONLY the JSON with extracted values. Use empty strings for missing information.
    """