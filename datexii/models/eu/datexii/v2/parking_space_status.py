from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from datexii.models.eu.datexii.v2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class ParkingSpaceStatus:
    """
    Status (occupied or closed) for a single parking space which was
    defined in the static part of the model.

    :ivar parking_space_occupied: True: Parking space is occupied;
        False: Parking space is free.
    :ivar parking_space_closed: True: The parking space is closed / not
        accessible. False or omitted: The parking space is accessible.
        This is no statement about its occupation.
    :ivar parking_space_declaration_valid_now: Override validity of
        'ParkingSpace': True = Parking space declaration is valid now;
        False = Parking space declaration is invalid now; Omitted =
        Static validity information is significant (if static validity
        is omitted too, declaration is valid).
    :ivar measurement_or_calculation_time: Point in time at which this
        specific value or set of values has been measured or calculated.
        It may also be a future time at which a data value is predicted.
    :ivar last_calibration: Date of last calibration of the detection
        system in question.
    :ivar parking_space_status_extension:
    """

    parking_space_occupied: bool | None = field(
        default=None,
        metadata={
            "name": "parkingSpaceOccupied",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    parking_space_closed: bool | None = field(
        default=None,
        metadata={
            "name": "parkingSpaceClosed",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    parking_space_declaration_valid_now: bool | None = field(
        default=None,
        metadata={
            "name": "parkingSpaceDeclarationValidNow",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    measurement_or_calculation_time: XmlDateTime | None = field(
        default=None,
        metadata={
            "name": "measurementOrCalculationTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    last_calibration: XmlDateTime | None = field(
        default=None,
        metadata={
            "name": "lastCalibration",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    parking_space_status_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "parkingSpaceStatusExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
