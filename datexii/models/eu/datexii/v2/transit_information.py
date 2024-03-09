from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.multilingual_string import MultilingualString
from datexii.models.eu.datexii.v2.non_road_event_information import (
    NonRoadEventInformation,
)
from datexii.models.eu.datexii.v2.transit_service_information_enum import (
    TransitServiceInformationEnum,
)
from datexii.models.eu.datexii.v2.transit_service_type_enum import (
    TransitServiceTypeEnum,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class TransitInformation(NonRoadEventInformation):
    """The availability of transit services and information relating to their
    departures.

    This is limited to those transit services which are of direct
    relevance to road users, e.g. connecting rail or ferry services.

    :ivar journey_destination: Indicates the stated termination point of
        the transit journey.
    :ivar journey_origin: Indicates the stated starting point of the
        transit journey.
    :ivar journey_reference: Indicates a transit service journey number.
    :ivar transit_service_information: Information about transit
        services.
    :ivar transit_service_type: The type of transit service to which the
        information relates.
    :ivar scheduled_departure_time: Indicates the timetabled departure
        time of a transit service for a specified location.
    :ivar transit_information_extension:
    """

    journey_destination: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "journeyDestination",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    journey_origin: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "journeyOrigin",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    journey_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "journeyReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        },
    )
    transit_service_information: Optional[TransitServiceInformationEnum] = (
        field(
            default=None,
            metadata={
                "name": "transitServiceInformation",
                "type": "Element",
                "namespace": "http://datex2.eu/schema/2/2_0",
                "required": True,
            },
        )
    )
    transit_service_type: Optional[TransitServiceTypeEnum] = field(
        default=None,
        metadata={
            "name": "transitServiceType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    scheduled_departure_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "scheduledDepartureTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    transit_information_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "transitInformationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
