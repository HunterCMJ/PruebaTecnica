import requests

class ApiDownloader:
    # as i get to choose the api, i'll define the url as a class parameter, bc it won't change.
    def __init__(self, url):
        self.url = url
    
    def download_data(self, limit=100):
        response = requests.get(self.url)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
        # 
        if isinstance(data, list):
            # to get always the limit nimber of records.
            return data[:limit]
        else:
            raise TypeError("API response must be a list of records")


if __name__ == "__main__":
    
    ######### Entries #########:

    url = "https://jsonplaceholder.typicode.com/comments"
    limit = 100

    ######### Instances #########

    downloader = ApiDownloader(url)

    ######### Execution #########

    # as the test suggests, ill download only 100 records
    data = downloader.download_data(limit)
   