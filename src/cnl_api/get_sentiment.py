from google.cloud import language
from google.oauth2 import service_account

def analyze_sentiment(text):
    client = language.LanguageServiceAsyncClient
    document = language.Document(content=text, type_=language.Document.Type.PLAIN_TEXT)

    response = client.analyze_sentiment(document=document)

    sentiment = response.document_sentiment
    res = dict(text=text, score=f"{sentiment.score:.1%}", magnitude=f"{sentiment.magnitude:.1%}",)

    return res

text = "Guido van Rossum is great!"
analyze_sentiment(text)