# This script helps to get aws instance metadata

import json

import requests


def get_metadata(url):
    """ This function returns aws instance metadata in json format"""
    metadata = {}
    r = requests.get(url)
    sections = r.text.split('\n')
    for section in sections:
        new_url = url + section
        if new_url.endswith('/'):
            get_metadata(new_url)
        else:
            r1 = requests.get(new_url)
            try:
                metadata[section] = json.loads(r1.text)
            except ValueError:
                metadata[section] = r1.text
    return metadata


# main function
if __name__ == "__main__":
    url = 'http://169.254.169.254/latest/meta-data/'
    metadata = get_metadata(url)
    print(metadata)
