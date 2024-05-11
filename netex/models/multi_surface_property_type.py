from dataclasses import dataclass, field
from typing import Optional, Union

from .multi_surface import MultiSurface
from .nil_reason_enumeration_value import NilReasonEnumerationValue

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class MultiSurfacePropertyType:
    multi_surface: Optional[MultiSurface] = field(
        default=None,
        metadata={
            "name": "MultiSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:\w{2,}",
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
