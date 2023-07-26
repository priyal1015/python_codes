#importing googletrans library to the language translations
import googletrans

#lets see what's inside googletrans
#print(dir(googletrans))

#lets do the translation now
language_translator = googletrans.Translator()


#lets create a function to extract the list of languages
def get_languages():

    #lets see what all languages can our translator work with
    language_info = googletrans.LANGUAGES

    #empty language list
    language_list = []

    #iterating over the dictionary
    for language in language_info.items():

        #extracting the languages and adding it to the language list 
        language_list.append(language[1])

    #lets return the list
    return language_list

# print(get_languages())


#lets create a function to get the list of abbreviations
def get_abbreviations():

    #lets see what all languages can our translator work with
    language_info = googletrans.LANGUAGES

    #empty language list
    abbreviation_list = []

    #iterating over the dictionary
    for language in language_info.items():

        #extracting the languages and adding it to the language list 
        abbreviation_list.append(language[0])

    #lets return the list
    return abbreviation_list

#lets define a function to do translations
def do_translation(text_to_be_translated, source_language, target_language):

    #to use anything global from inside of a function, use the keyword global
    global language_translator

    #lets call the translate function
    output = language_translator.translate(text = text_to_be_translated, dest = target_language , src = source_language)
    
    #extracting the text from output
    translated_text =  output.text

    #return it
    return translated_text

#lets call this function
result = do_translation('What is your name' , 'en' , 'hi')
print(result)