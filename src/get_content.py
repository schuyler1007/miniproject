from multiprocessing import get_context
from google.cloud import language

def analyze_content(text):
    client = language.LanguageServiceClient()
    document = language.Document(content=text, type_=language.Document.Type.PLAIN_TEXT)

    response = client.classify_text(document=document)

    print(response.categories)

# print(analyze_content("Athena was the goddess of battle strategy, and wisdom. Identified in the Roman mythology as the goddess Minerva. She was always accompanied by her owl and the goddess of victory, Nike. "))