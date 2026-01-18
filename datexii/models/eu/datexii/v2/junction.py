from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.junction_classification_enum import (
    JunctionClassificationEnum,
)
from datexii.models.eu.datexii.v2.multilingual_string import MultilingualString
from datexii.models.eu.datexii.v2.road import Road

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class Junction:
    """
    Junction (on a highway), can also be an interchange or if applicable
    also a motorway service station (see junctionClassification).

    :ivar junction_classification: Explicit type of junction.
    :ivar junction_name: Name of the junction.
    :ivar junction_number: Number of the junction, might also include
        letters (example: 23A).
    :ivar motorway: A detailed identification of the motorway the
        junction belongs to.
    :ivar destination_motorway: In case of any type of intersection, the
        destination motorway(s) can be defined.
    :ivar junction_extension:
    """

    junction_classification: JunctionClassificationEnum | None = field(
        default=None,
        metadata={
            "name": "junctionClassification",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    junction_name: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "junctionName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    junction_number: str | None = field(
        default=None,
        metadata={
            "name": "junctionNumber",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        },
    )
    motorway: Road | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    destination_motorway: list[Road] = field(
        default_factory=list,
        metadata={
            "name": "destinationMotorway",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    junction_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "junctionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
