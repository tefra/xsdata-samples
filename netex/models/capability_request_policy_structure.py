from dataclasses import dataclass, field
from typing import List, Optional, Union
from .empty_type_1 import EmptyType1

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class CapabilityRequestPolicyStructure:
    national_language: List[str] = field(
        default_factory=list,
        metadata={
            "name": "NationalLanguage",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        },
    )
    translations: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Translations",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    gml_coordinate_format_or_wgs_decimal_degrees: Optional[
        Union[str, EmptyType1]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "GmlCoordinateFormat",
                    "type": str,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "WgsDecimalDegrees",
                    "type": EmptyType1,
                    "namespace": "http://www.siri.org.uk/siri",
                },
            ),
        },
    )
