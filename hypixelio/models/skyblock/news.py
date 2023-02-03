from dataclasses import dataclass


@dataclass
class NewsItem:
    title: str
    text: str
    link: str
    item: dict


class SkyblockNews:
    def __init__(self, data: dict) -> None:
        """
        Parameters
        ----------
        data: dict
            The JSON data to be parsed.
        """
        news = []

        for news_data in data["items"]:
            news.append(
                NewsItem(
                    news_data["title"],
                    news_data["text"],
                    news_data["link"],
                    news_data["item"],
                )
            )

        self.news = news

    def __repr__(self) -> str:
        return f"<{self.__class__.__qualname__} news_amount={len(self.news)}>"

    def __len__(self) -> int:
        return len(self.news)

    def __iter__(self):
        return iter(self.news)
