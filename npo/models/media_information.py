from __future__ import annotations
from dataclasses import dataclass
from npo.models.media_table_type import MediaTableType

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class MediaInformation(MediaTableType):
    """Base element only used when programs, groups and schedule information need
    to be bundled in one XML.

    E.g. when distributing to cable companies.
    """
    class Meta:
        name = "mediaInformation"
        namespace = "urn:vpro:media:2009"
