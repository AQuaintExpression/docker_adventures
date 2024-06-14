from kaggle.api.kaggle_api_extended import KaggleApi
import zipfile

api = KaggleApi()
api.authenticate()

api.dataset_download_file('mohamedhamad21/spotify-tracks-dataset',
                          file_name='dataset.csv')

with zipfile.ZipFile('dataset.csv.zip', 'r') as zf: 
    zf.extractall()