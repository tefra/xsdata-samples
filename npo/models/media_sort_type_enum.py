from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "urn:vpro:api:2013"


class MediaSortTypeEnum(Enum):
    TITLE = "title"
    SORT_DATE = "sortDate"
    PUBLISH_DATE = "publishDate"
    EPISODE = "episode"
    EPISODE_ADDED = "episodeAdded"
    MEMBER_ADDED = "memberAdded"
    MEMBER = "member"
    CREATION_DATE = "creationDate"
    LAST_MODIFIED = "lastModified"
