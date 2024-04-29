
# OurApi Repository Overview

Welcome to the OurApi repository! This repository contains two main components: `ourapi.py` and `app.py`. Below is an overview of these files and their functionalities.

## ourapi.py

This file is the core of our connection to the Oura API. It includes the `OuraApiClient` class, which facilitates interaction with the Oura API services. To use this class, simply import it and create an instance as shown below:

```python
from ourapi import OuraApiClient
client = OuraApiClient()
client.create_sleep_viz()
```

To operate this client, you will need a personal access token, which can be obtained [here](https://cloud.ouraring.com/personal-access-tokens).

For more comprehensive usage scenarios, refer to the [official API documentation](https://cloud.ouraring.com/docs).


## app.py

This script utilizes Streamlit to create a visual application that leverages data from the OuraApiClient. It provides a user-friendly interface to interact with the insights derived from the Oura API.

![sample_image]('images/sample.png')
