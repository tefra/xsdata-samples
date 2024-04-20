from dataclasses import dataclass, field
from typing import List, Optional

from tpdb.models.author import Author
from tpdb.models.comment import Comment
from tpdb.models.date import Date
from tpdb.models.originalfilename import Originalfilename


@dataclass
class Metainformation:
    class Meta:
        name = "metainformation"

    originalfilename: List[Originalfilename] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    author: Optional[Author] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    date: Optional[Date] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    comment: Optional[Comment] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
