def form_url(main_url: str, url: str, data: dict = None) -> str:
    """
    Form and return the URL for the Hypixel API with GET Params.

    Parameters
    ----------
    main_url: str
        The Main URL With the root domain.
    url: str
        The Route in the Main URL to access the JSON From.
    data: t.Optional[dict]
        The GET Request Key Value pair, Added to end of the Final route specified in the main_url + url.. Defaults
        to None.

    Returns
    -------
    str:
        The Final URL with the GET request parameters, and the URL Route.
    """
    if not data:
        data = {}

    url = main_url + url if url.startswith("/") else url
    url += "?" + "&".join(
        [f"{dict_key}={dict_value}" for dict_key, dict_value in data.items()]
    )

    return url
