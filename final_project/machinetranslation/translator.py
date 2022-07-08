from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator(
    'J32pntVKQ20Nw9epzY7jsUvnhwzuYMQbdMDh0UxsT-NF')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(
    'https://api.us-south.language-translator.watson.cloud.ibm.com/instances/d17ee213-c2b5-480d-8b3f-2da36103a0a6')
languages = language_translator.list_languages().get_result()
# print(json.dumps(languages, indent=2))


def englishToFrench(englishText):
    frenchText = language_translator.translate(
        text=englishText,
        model_id='en-fr').get_result()
    # x = json.dumps(frenchText, indent=2, ensure_ascii=False)
    # print(json.dumps(frenchText, indent=2, ensure_ascii=False))
    destructured_Text = frenchText["translations"][0]["translation"]
    print(destructured_Text)
    return destructured_Text


def frenchToEnglish(frenchText):
    englishText = language_translator.translate(
        text=frenchText,
        model_id='fr-en').get_result()
    # print(json.dumps(englishText, indent=2, ensure_ascii=False))
    destructured_Text = englishText["translations"][0]["translation"]
    return destructured_Text


# englishToFrench("")
