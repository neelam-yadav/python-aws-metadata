# python-aws-metadata

## Overview
This repo contains a script which will help in fetching the aws instance metadata. Output will be in json format.

## Run Script
Follow below steps to run the script:

- Create ec2-instance on AWS
  
- SSH to instance

`ssh -i file.pem username@ip-address`

- Clone the repo:

`git clone https://github.com/neelam-yadav/python-aws-metadata.git`

- Run the script on console:

`python metadata.py`


## Usage
To use the script in other modules, use below snippet :

```
from metadata import get_metadata

url = 'http://169.254.169.254/latest/meta-data/'
metadata = get_metadata(url)
```
