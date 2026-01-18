from __future__ import annotations

from dataclasses import dataclass

from .reference_type import ReferenceType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(kw_only=True)
class AbstractReference(ReferenceType):
    class Meta:
        name = "abstractReference"
        namespace = "http://www.opengis.net/gml/3.2"
