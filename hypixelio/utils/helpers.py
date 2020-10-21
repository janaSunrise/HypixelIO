def form_url(self, main_url: str, url: str, data: dict = {}) -> str:
    url = main_url + url if url.startswith('/') else url
    url += "?" + "&".join(
        [
            f"{dict_key}={dict_value}" for dict_key, dict_value in data.items()
        ]
    )

    return url
