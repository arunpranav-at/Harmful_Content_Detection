from concurrent.futures import ProcessPoolExecutor
import multiprocessing

def englishtextclassifier(text):

    num_workers = min(multiprocessing.cpu_count(), 8) 
    with ProcessPoolExecutor(max_workers=num_workers) as executor:
        from transformers import AutoModelForSequenceClassification, AutoTokenizer, TextClassificationPipeline

        model_path = "MAINFOLDER\\toxic-comment-model"
        tokenizer = AutoTokenizer.from_pretrained(model_path)
        model = AutoModelForSequenceClassification.from_pretrained(model_path)

        pipeline =  TextClassificationPipeline(model=model, tokenizer=tokenizer)
        inputtext = text
        print(inputtext, pipeline(inputtext))
        
    return pipeline(text)
