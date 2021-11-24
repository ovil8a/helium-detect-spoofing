import requests
import json
import pandas as pd


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
url="https://api.helium.io/v1/cities"
def main():
    ciudades=requests.get(url,headers =headers)
    json_data = json.loads(ciudades.text)
    df = pd.DataFrame(json_data)
    print(df)

def obtenapi():
    pass




if __name__=="__main__":
    main()

