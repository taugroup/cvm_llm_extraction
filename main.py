from data_processing.file_processor import FileProcessor
from data_processing.data_generator import DataGenerator

def main():
    processor = FileProcessor()
    generator = DataGenerator(processor)
    df = generator.generate_dataset()
    print("Data processing completed. Result saved to CSV.")

if __name__ == "__main__":
    main()