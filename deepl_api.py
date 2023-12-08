from dotenv import load_dotenv
import deepl
import os

load_dotenv()

deepl_api_key = os.getenv('DEEPL_API_KEY')

if deepl_api_key is None:
    raise ValueError("La clé API DeepL n'a pas été trouvée dans le fichier .env")

translator = deepl.Translator(deepl_api_key)

translate = translator.translate_document_from_filepath(
    "input.txt",
    "output.txt",
    source_lang="FR",
    target_lang="EN-GB",
)

print(translate)