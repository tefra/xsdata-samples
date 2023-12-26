from dataclasses import dataclass, field
from typing import List, Optional
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.predefined_location_versioned_reference import (
    PredefinedLocationVersionedReference,
)
from datexii.models.eu.datexii.v2.traffic_view_record import TrafficViewRecord

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class LinearTrafficView:
    """
    An identifiable instance of a linear traffic view at a single point in time
    relating to a linear section of road, comprising one or more traffic view
    records.

    :ivar linear_predefined_location_reference: A reference to a
        versioned predefined location which is of type linear.
    :ivar traffic_view_record:
    :ivar linear_traffic_view_extension:
    :ivar id:
    """

    linear_predefined_location_reference: Optional[
        PredefinedLocationVersionedReference
    ] = field(
        default=None,
        metadata={
            "name": "linearPredefinedLocationReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    traffic_view_record: List[TrafficViewRecord] = field(
        default_factory=list,
        metadata={
            "name": "trafficViewRecord",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 1,
        },
    )
    linear_traffic_view_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "linearTrafficViewExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
