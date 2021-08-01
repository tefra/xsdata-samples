from dataclasses import dataclass, field
from typing import List, Optional
from datexii.models.eu.datexii.v2.affected_carriageway_and_lanes import AffectedCarriagewayAndLanes
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.location_descriptor_enum import LocationDescriptorEnum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class SupplementaryPositionalDescription:
    """
    A collection of supplementary positional information which improves the
    precision of the location.

    :ivar location_descriptor: Specifies a descriptor which helps to
        identify the specific location.
    :ivar sequential_ramp_number: The sequential number of an
        exit/entrance ramp from a given location in a given direction
        (normally used to indicate a specific exit/entrance in a complex
        junction/intersection).
    :ivar affected_carriageway_and_lanes:
    :ivar supplementary_positional_description_extension:
    :ivar location_precision: Indicates that the location is given with
        a precision which is better than the stated value in metres.
    """
    location_descriptor: List[LocationDescriptorEnum] = field(
        default_factory=list,
        metadata={
            "name": "locationDescriptor",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    sequential_ramp_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "sequentialRampNumber",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    affected_carriageway_and_lanes: List[AffectedCarriagewayAndLanes] = field(
        default_factory=list,
        metadata={
            "name": "affectedCarriagewayAndLanes",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    supplementary_positional_description_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "supplementaryPositionalDescriptionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    location_precision: Optional[int] = field(
        default=None,
        metadata={
            "name": "locationPrecision",
            "type": "Attribute",
        }
    )
