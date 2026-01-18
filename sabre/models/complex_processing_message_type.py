from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

from sabre.models.processing_message_type import ProcessingMessageType

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass(kw_only=True)
class ComplexProcessingMessageType(ProcessingMessageType):
    """
    Attributes:
        leg: Optional list of departure dates for each leg
    """

    leg: list[ComplexProcessingMessageType.Leg] = field(
        default_factory=list,
        metadata={
            "name": "Leg",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "max_occurs": 10,
        },
    )

    @dataclass(kw_only=True)
    class Leg:
        """
        Attributes:
            departure_date: Departure date
        """

        departure_date: XmlDate = field(
            metadata={
                "name": "DepartureDate",
                "type": "Attribute",
                "required": True,
            }
        )
