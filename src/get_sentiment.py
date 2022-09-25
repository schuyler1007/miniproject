# from google.cloud import language
# from google.oauth2 import service_account

# def analyze_sentiment(text):
#     client = language.LanguageServiceAsyncClient
#     document = language.Document(content=text, type_=language.Document.Type.PLAIN_TEXT)

#     response = client.analyze_sentiment(document=document)

#     sentiment = response.document_sentiment
#     res = dict(text=text, score=f"{sentiment.score:.1%}", magnitude=f"{sentiment.magnitude:.1%}",)

#     return res

# text = "Guido van Rossum is great!"
# analyze_sentiment(text)

from google.cloud import language_v1
import six


def authenticate_implicit_with_adc(project_id="miniproject-kk-nm"):
    storage_client = storage.Client(project=project_id)
    buckets = storage_client.list_buckets()
    print("Buckets:")
    for bucket in buckets:
        print(bucket.name)
    print("Listed all storage buckets.")


def sample_analyze_sentiment(content):

    client = language_v1.LanguageServiceClient()

    if isinstance(content, six.binary_type):
        content = content.decode("utf-8")

    type_ = language_v1.Document.Type.PLAIN_TEXT
    document = {"type_": type_, "content": content}

    response = client.analyze_sentiment(request={"document": document})
    sentiment = response.document_sentiment
    print("Score: {}".format(sentiment.score))
    print("Magnitude: {}".format(sentiment.magnitude))

# sample_analyze_sentiment("Athena was the goddess of battle strategy, and wisdom. Identified in the Roman mythology as the goddess Minerva. She was always accompanied by her owl and the goddess of victory, Nike. ")