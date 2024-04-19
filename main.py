import requests
import json
import pandas as pd
import os
from dotenv import load_dotenv
from FDA_Recall import FDA_Recall

load_dotenv()

FDA_KEY = os.getenv("FDA_API_KEY")

fda_key_string = 'api_key=' + FDA_KEY

fda_url = 'https://api.fda.gov/food/enforcement.json?' + fda_key_string


def main():
    state = input('What state would you like to search for? ')
    state = '+'.join(state.split(' '))

    city = input('What city would you like to search for? ')
    city = '+'.join(city.split(' '))
    
    search = f'search=state:{state}+AND+city:{city}&limit=5'
    
    try: 
        res = requests.get(fda_url+'&'+search).json()
        
        recalls = [FDA_Recall(x) for x in res['results']]


        for recall in recalls:
            print('Recall Number:', recall.get_city() + ' ' + recall.get_state())
            print('Recall Description:', recall.get_product_description())
            print('Recall Reason:', recall.get_reason_for_recall())
            print('Recall Date:', recall.get_recall_initiation_date())
            print('Recall Classification:', recall.get_classification())
            print('Was the recall voluntary or mandated:', recall.get_voluntary_mandated())

            print('\n\n')


    except:
        print('No results found')


if __name__ == "__main__":  
    main()
