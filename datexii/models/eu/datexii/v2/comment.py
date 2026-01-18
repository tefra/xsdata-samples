from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

from datexii.models.eu.datexii.v2.comment_type_enum import CommentTypeEnum
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.multilingual_string import MultilingualString

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass(kw_only=True)
class Comment:
    """
    A free text comment with an optional date/time stamp that can be used
    by the operator to convey un-coded observations/information.

    :ivar comment: A free text comment that can be used by the operator
        to convey un-coded observations/information.
    :ivar comment_date_time: The date/time at which the comment was
        made.
    :ivar comment_type: A classification of the the type of comment.
    :ivar comment_extension:
    """

    comment: MultilingualString = field(
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    comment_date_time: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "commentDateTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    comment_type: None | CommentTypeEnum = field(
        default=None,
        metadata={
            "name": "commentType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    comment_extension: None | ExtensionType = field(
        default=None,
        metadata={
            "name": "commentExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
