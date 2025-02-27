import os

class Settings:
    LLM_MODEL = "deepseek-r1:14b"
    DATA_DIR = "data"
    OUTPUT_DIR = "output"
    OUTPUT_CSV = os.path.join(OUTPUT_DIR, "extracted_data.csv")
    
    @property
    def file_paths(self):
        if not os.path.exists(self.DATA_DIR):
            os.makedirs(self.DATA_DIR)
        
        if not os.path.exists(self.OUTPUT_DIR):
            os.makedirs(self.OUTPUT_DIR)
        return {
            'signalment_physical': os.path.join(self.DATA_DIR, 'signalment_physical.pdf'),
            'cbc': os.path.join(self.DATA_DIR, 'cbc.pdf'),
            'chem': os.path.join(self.DATA_DIR, 'chem.pdf'),
            'cpli': os.path.join(self.DATA_DIR, 'cpli.pdf'),
            'aus': os.path.join(self.DATA_DIR, 'aus.pdf')
        }

settings = Settings()