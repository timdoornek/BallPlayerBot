import pybaseball
import shutil
import application_constants

'''---------------------------------------------
    Main method to build files
    --------------------------------------------'''
def generate_name_text_files():
    # get all mlb baseball players
    df = pybaseball.chadwick_register()

    #filter out null names
    df = df[df['name_first'].notnull()]
    df = df[df['name_last'].notnull()]

    #filter out initialisms
    df = df[df.name_first.str.isalpha()]
    df = df[df.name_last.str.isalpha()]

    # filter by year cause older names are funnier
    df = df.loc[df['mlb_played_last'] <= 1980]

    # just first names and last names
    df_first_names = df['name_first']
    df_last_names = df['name_last']

    # remove duplicates
    df_first_names = df_first_names.drop_duplicates()
    df_last_names = df_last_names.drop_duplicates()

    #only grab random 1000 of first names 
    df_first_names = df_first_names.sample(n=1000)

    #save to txt file
    df_first_names.to_csv(application_constants.FIRST_NAME_TXT_NAME, header=None, index=None, sep=' ', mode='w')
    df_last_names.to_csv(application_constants.LAST_NAME_TXT_NAME, header=None, index=None, sep=' ', mode='w')

    #append appropriate wordsets to each
    append_files(application_constants.ENGLISH_WORDS_TXT_NAME, application_constants.FIRST_NAME_TXT_NAME)
    append_files(application_constants.ENGLISH_NOUNS_TXT_NAME, application_constants.LAST_NAME_TXT_NAME)
    
'''---------------------------------------------
    Helper method to append files
    --------------------------------------------'''
def append_files(appending_file_path, appended_to_file_path):
    with open(appending_file_path, mode='r', encoding="utf8") as file1:
        with open(appended_to_file_path, mode='a', encoding="utf8") as file2:
            shutil.copyfileobj(file1, file2)
            