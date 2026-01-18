from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(kw_only=True)
class DirectPositionListType:
    value: Iterable[float] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
    srs_name: None | str = field(
        default=None,
        metadata={
            "name": "srsName",
            "type": "Attribute",
        },
    )
    srs_dimension: None | int = field(
        default=None,
        metadata={
            "name": "srsDimension",
            "type": "Attribute",
        },
    )
    count: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
