from __future__ import annotations

from dataclasses import dataclass

from .reference_type import ReferenceType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(kw_only=True)
class DescriptionReference(ReferenceType):
    class Meta:
        name = "descriptionReference"
        namespace = "http://www.opengis.net/gml/3.2"
