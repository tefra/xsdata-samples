from dataclasses import dataclass
from npo.models.genre_type_2 import GenreType2

__NAMESPACE__ = "urn:vpro:pages:2013"


@dataclass
class Genre(GenreType2):
    class Meta:
        name = "genre"
        namespace = "urn:vpro:pages:2013"
