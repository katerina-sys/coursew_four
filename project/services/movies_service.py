from typing import Optional

from project.dao import MoviesDAO
from project.exceptions import ItemNotFound
from project.models import Movie


class MoviesService:
    def __init__(self, dao: MoviesDAO) -> None:
        self.dao = dao

    def get_item(self, pk: int) -> Movie:
        if genre := self.dao.get_by_id(pk):
            return genre
        raise ItemNotFound(f'Movie with pk={pk} not exists.')

    def get_all(self, page: Optional[int] = None, filter: Optional[str] = None) -> list[Movie]:
        return self.dao.get_all_order_by(page=page, filter=filter)
