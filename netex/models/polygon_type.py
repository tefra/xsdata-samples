from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .abstract_surface_type import AbstractSurfaceType
from .exterior import Exterior
from .interior import Interior

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(kw_only=True)
class PolygonType(AbstractSurfaceType):
    exterior: None | Exterior = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    interior: Sequence[Interior] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
