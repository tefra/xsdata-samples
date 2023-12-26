from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class Document:
    """
    APIS Document Details.

    Parameters
    ----------
    sequence
        Sequence number for the document.
    type_value
        Type of the Document. Visa, Passport, DriverLicense etc.
    level
        Applicability level of the Document. Required, Supported,
        API_Supported or Unknown.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    sequence: None | int = field(
        default=None,
        metadata={
            "name": "Sequence",
            "type": "Attribute",
        },
    )
    type_value: None | str = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        },
    )
    level: None | str = field(
        default=None,
        metadata={
            "name": "Level",
            "type": "Attribute",
        },
    )
