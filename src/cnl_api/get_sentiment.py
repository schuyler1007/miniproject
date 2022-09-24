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
    # """
    # When interacting with Google Cloud Client libraries, the library can auto-detect the
    # credentials to use.

    # // TODO(Developer):
    # //  1. Before running this sample,
    # //  set up ADC as described in https://cloud.google.com/docs/authentication/external/set-up-adc
    # //  2. Replace the project variable.
    # //  3. Make sure that the user account or service account that you are using
    # //  has the required permissions. For this sample, you must have "storage.buckets.list".
    # Args:
    #     project_id: The project id of your Google Cloud project.
    # """

    # This snippet demonstrates how to list buckets.
    # *NOTE*: Replace the client created below with the client required for your application.
    # Note that the credentials are not specified when constructing the client.
    # Hence, the client library will look for credentials using ADC.

    storage_client = storage.Client(project=project_id)
    buckets = storage_client.list_buckets()
    print("Buckets:")
    for bucket in buckets:
        print(bucket.name)
    print("Listed all storage buckets.")


def sample_analyze_sentiment(content):

    client = language_v1.LanguageServiceClient()

    # content = 'Your text to analyze, e.g. Hello, world!'

    if isinstance(content, six.binary_type):
        content = content.decode("utf-8")

    type_ = language_v1.Document.Type.PLAIN_TEXT
    document = {"type_": type_, "content": content}

    response = client.analyze_sentiment(request={"document": document})
    sentiment = response.document_sentiment
    print("Score: {}".format(sentiment.score))
    print("Magnitude: {}".format(sentiment.magnitude))

sample_analyze_sentiment("Hello World")