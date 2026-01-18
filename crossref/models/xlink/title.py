from __future__ import annotations

from dataclasses import dataclass

from crossref.models.xlink.title_elt_type import TitleEltType

__NAMESPACE__ = "http://www.w3.org/1999/xlink"


@dataclass(kw_only=True)
class Title(TitleEltType):
    class Meta:
        name = "title"
        namespace = "http://www.w3.org/1999/xlink"
