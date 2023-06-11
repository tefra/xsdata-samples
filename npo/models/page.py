from __future__ import annotations
from dataclasses import dataclass
from npo.models.page_type import PageType

__NAMESPACE__ = "urn:vpro:pages:2013"


@dataclass
class Page(PageType):
    class Meta:
        name = "page"
        namespace = "urn:vpro:pages:2013"
