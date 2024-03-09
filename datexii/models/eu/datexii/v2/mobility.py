from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.mobility_enum import MobilityEnum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class Mobility:
    """
    An indication of whether the associated instance of a SituationRecord is mobile
    (e.g. a march or parade moving along a road) or stationary.

    :ivar mobility_type: An indication of whether the associated
        instance of a SituationRecord is mobile (e.g. a march or parade
        moving along a road) or stationary.
    :ivar mobility_extension:
    """

    mobility_type: Optional[MobilityEnum] = field(
        default=None,
        metadata={
            "name": "mobilityType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    mobility_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "mobilityExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
