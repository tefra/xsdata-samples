from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .description_reference import DescriptionReference
from .identifier import Identifier
from .name import Name

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractGmltype:
    class Meta:
        name = "AbstractGMLType"

    description_reference: DescriptionReference | None = field(
        default=None,
        metadata={
            "name": "descriptionReference",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    identifier: Identifier | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    name: Iterable[Name] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    id: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
