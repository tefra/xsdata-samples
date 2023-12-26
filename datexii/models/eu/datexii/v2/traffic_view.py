from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.linear_traffic_view import LinearTrafficView
from datexii.models.eu.datexii.v2.predefined_non_ordered_location_group_versioned_reference import (
    PredefinedNonOrderedLocationGroupVersionedReference,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class TrafficView:
    """
    An identifiable instance of a traffic view at a single point in time relating
    to a predefined location set, comprising one or more linear traffic views each
    of which comprise one or more traffic view records.

    :ivar traffic_view_time: The time to which the traffic view relates,
        i.e. the instance in time at which the traffic view was taken
        (comparable to taking a photograph).
    :ivar predefined_non_ordered_location_group_reference: A reference
        to a versioned instance of a predefined non ordered location
        group as specified in a PredefinedLocationsPublication.
    :ivar linear_traffic_view:
    :ivar traffic_view_extension:
    :ivar id:
    """

    traffic_view_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "trafficViewTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    predefined_non_ordered_location_group_reference: Optional[
        PredefinedNonOrderedLocationGroupVersionedReference
    ] = field(
        default=None,
        metadata={
            "name": "predefinedNonOrderedLocationGroupReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    linear_traffic_view: List[LinearTrafficView] = field(
        default_factory=list,
        metadata={
            "name": "linearTrafficView",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 1,
        },
    )
    traffic_view_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "trafficViewExtension",
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
