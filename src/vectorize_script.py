import os
from dotenv import load_dotenv

from src.vectorize_book import CLASS_SUBJECT_NAME
from vectorize_book import vectorize_book_and_store_in_db, vectorize_chapters

load_dotenv()

CLASS_SUBJECT_NAME= os.getenv("CLASS_SUBJECT_NAME")

vectorize_book_and_store_in_db(CLASS_SUBJECT_NAME,"vector_db")
vectorize_chapters(CLASS_SUBJECT_NAME)