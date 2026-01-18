from __future__ import annotations

from dataclasses import dataclass, field

from tpdb.models.author import Author
from tpdb.models.comment import Comment
from tpdb.models.date import Date
from tpdb.models.originalfilename import Originalfilename


@dataclass
class Metainformation:
    class Meta:
        name = "metainformation"

    originalfilename: list[Originalfilename] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    author: Author | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    date: Date | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    comment: Comment | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
