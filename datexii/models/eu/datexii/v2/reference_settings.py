from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.predefined_non_ordered_location_group_versioned_reference import (
    PredefinedNonOrderedLocationGroupVersionedReference,
)
from datexii.models.eu.datexii.v2.traffic_status_enum import TrafficStatusEnum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class ReferenceSettings:
    """
    Specification of the default value for traffic status on a group of
    predefined locations on the road network.

    Only when traffic status differs from this value at a location in the
    group need a value be sent.

    :ivar predefined_non_ordered_location_group_reference: A reference
        to a versioned instance of a predefined non ordered location
        group as specified in a PredefinedLocationsPublication.
    :ivar traffic_status_default: The default value of traffic status
        that can be assumed to apply to the locations defined by the
        associated predefined location set.
    :ivar reference_settings_extension:
    """

    predefined_non_ordered_location_group_reference: (
        PredefinedNonOrderedLocationGroupVersionedReference | None
    ) = field(
        default=None,
        metadata={
            "name": "predefinedNonOrderedLocationGroupReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    traffic_status_default: TrafficStatusEnum | None = field(
        default=None,
        metadata={
            "name": "trafficStatusDefault",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    reference_settings_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "referenceSettingsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
