# Use a pipeline as a high-level helper
from concurrent.futures import ProcessPoolExecutor
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import multiprocessing

    
def tanglishtextclassifier(text):
    pipe = pipeline("text-classification", model="Hate-speech-CNERG/deoffxlmr-mono-tamil")

    num_workers = min(multiprocessing.cpu_count(), 8) 

    with ProcessPoolExecutor(max_workers=num_workers) as executor:
        tokenizer = AutoTokenizer.from_pretrained("Hate-speech-CNERG/deoffxlmr-mono-tamil")
        model = AutoModelForSequenceClassification.from_pretrained("Hate-speech-CNERG/deoffxlmr-mono-tamil")

        inputtext = text
        print(inputtext, pipe(inputtext))
        
    return pipe(text)
