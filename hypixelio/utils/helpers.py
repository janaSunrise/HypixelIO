"""
This module is dedicated to the storage of the Helper functions,
Which is imported in the main file: `Client.py` to include in the functions
to Reduce the lines of code, and simplify it.
"""


def form_url(main_url: str, url: str, data: dict = None) -> str:
    """
    Form and return the URL for the Hypixel API with GET Params.

    Parameters:
        main_url (str): The Main URL With the root domain.
        url (str): The Route in the Main URL to acess the JSON From.
        data (dict):
            The GET Request Key Value pair, Added to end of the Final route specified in the main_url + url.

    Returns:
        url (str): The Final URL with the Get request parameters, and the URL Route.
    """
    if not data:
        data = {}

    url = main_url + url if url.startswith('/') else url
    url += "?" + "&".join(
        [
            f"{dict_key}={dict_value}" for dict_key, dict_value in data.items()
        ]
    )

    return url
