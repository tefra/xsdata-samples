from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass
class GuestReviews:
    """
    Comments and Reviews from hotel guests.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    comments: list[GuestReviews.Comments] = field(
        default_factory=list,
        metadata={
            "name": "Comments",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )

    @dataclass
    class Comments:
        """
        Parameters
        ----------
        value
        comment_id
            Unique comment identifier. For internal Travelport use only.
        date
            date that the comment was entered.
        commenter_language
            Language of the commenter.
        source
            Source code of the comment entry. Example: 'NB' for
            Nightsbridge, ‘RG’, ‘AG’ for Agrialla,‘TO’.
        comment_source_name
            Name of the source for the comment.
        commenter
            Name of the comment's poster.
        """

        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        comment_id: None | str = field(
            default=None,
            metadata={
                "name": "CommentId",
                "type": "Attribute",
            },
        )
        date: None | str = field(
            default=None,
            metadata={
                "name": "Date",
                "type": "Attribute",
                "pattern": r"[^:Z].*",
            },
        )
        commenter_language: None | str = field(
            default=None,
            metadata={
                "name": "CommenterLanguage",
                "type": "Attribute",
                "length": 2,
            },
        )
        source: None | str = field(
            default=None,
            metadata={
                "name": "Source",
                "type": "Attribute",
            },
        )
        comment_source_name: None | str = field(
            default=None,
            metadata={
                "name": "CommentSourceName",
                "type": "Attribute",
            },
        )
        commenter: None | str = field(
            default=None,
            metadata={
                "name": "Commenter",
                "type": "Attribute",
            },
        )
