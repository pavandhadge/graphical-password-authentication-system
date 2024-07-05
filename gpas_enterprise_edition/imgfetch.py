import json
import os
import requests
import tqdm
import random
from pexels_api import API

def image_fetch():
    try :
        PAGE_LIMIT = 15
        RESULTS_PER_PAGE = 10

        PEXELS_API_KEY ="uoZcyJJBMLXCkJuulvASvkSg73Iu14lXNENGZyhoc6xIC6pgdLGt8jd2"
        api = API(PEXELS_API_KEY)
        # search query
        queryarray = ["nature","cars","water","books","tree","india","space","love","movies","animals","birds","bikes","trending","holi","cricket","sports","music","bollywood","earth","technology","robots","ladakh","kashmir","jets","f1","yoga"]
        query = random.choice(queryarray)
        print(query)
        photos_dict = {}
        page = 1
        counter = 0

        # Step 1: Getting urls and meta information
        while page <= PAGE_LIMIT:
            api.search(query, page=page, results_per_page=RESULTS_PER_PAGE)
            photos = api.get_entries()
            for photo in tqdm.tqdm(photos):
                photos_dict[photo.id] = vars(photo)['_Photo__photo']
                counter += 1
                if not api.has_next_page:
                    break
                page += 1

        print(f"Finishing at page: {page}")
        print(f"Images were processed: {counter}")
        print(photos_dict)

        PATH = './temp/'
        RESOLUTION = 'original'

        if photos_dict:
            os.makedirs(PATH, exist_ok=True)
            
            # Saving dict
            with open(os.path.join(PATH, f'{query}.json'), 'w') as fout:
                json.dump(photos_dict, fout)

            # Get 5 random keys (image IDs) from the dictionary
            random_keys = random.sample(list(photos_dict.keys()), 5)

            numi = 1
            for key in random_keys:
                val = photos_dict[key]
                url = val['src'][RESOLUTION]
                fname = f"image{numi}.jpg"
                numi += 1
                image_path = os.path.join(PATH, fname)
                if not os.path.isfile(image_path):
                    response = requests.get(url, stream=True)
                    with open(image_path, 'wb') as outfile:
                        outfile.write(response.content)
                else:
                    # Ignore if already downloaded
                    print(f"File {image_path} exists")
        
    
    except Exception as e:
        print("The error is: ",e)
        return -1

# image_fetch()

def deleteimg():
    try :
        for i in range(1,6):
            delimgname = "./temp/image"+str(i)+".jpg"
            fileExists = os.path.isfile(delimgname)

            if fileExists:
                os.remove(delimgname)
        if fileExists:
                os.remove(".json")
        return 0
    
    except Exception as e:
        print("The error is: ",e)
        return -1
    
def del_json():
    try:
        file_list = os.listdir("./temp")
        print(file_list)
        json_files = [f for f in file_list if f.lower().endswith('.json')]
        print(json_files)

        for ijson in range(0,len(json_files)):
            os.remove("./temp/"+json_files[ijson])

    except Exception as e:
        print(f"Error deleting file: {e}")