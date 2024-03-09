from dataclasses import dataclass, field
from typing import List, Optional, Union

from .nil_reason_enumeration_value import NilReasonEnumerationValue

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class MeasureOrNilReasonListType:
    value: List[Union[str, NilReasonEnumerationValue]] = field(
        default_factory=list,
        metadata={
            "pattern": r"other:\w{2,}",
            "tokens": True,
        },
    )
    uom: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[^: \n\r\t]+",
        },
    )
