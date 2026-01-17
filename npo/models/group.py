from __future__ import annotations

from dataclasses import dataclass

from npo.models.group_type import GroupType

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class Group(GroupType):
    """
    A groups collects a number of programs and/or other groups.

    Examples: season, series, playlist and album.
    """

    class Meta:
        name = "group"
        namespace = "urn:vpro:media:2009"
