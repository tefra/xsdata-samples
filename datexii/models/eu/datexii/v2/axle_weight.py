from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class AxleWeight:
    """
    The weight details of a specific axle on the vehicle.

    :ivar axle_position_identifier: Indicates the position of the axle
        on the vehicle numbered from front to back (i.e. 1, 2, 3...).
        This cannot exceed the numberOfAxles if provided as part of
        VehicleCharacteristics.
    :ivar axle_weight: The weight of the specific axle, indicated by the
        axleSequenceIdentifier, on the vehicle numbered from front to
        back of the vehicle.
    :ivar maximum_permitted_axle_weight: The maximum permitted weight of
        this specific axle on the vehicle.
    :ivar axle_weight_extension:
    """

    axle_position_identifier: int | None = field(
        default=None,
        metadata={
            "name": "axlePositionIdentifier",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    axle_weight: float | None = field(
        default=None,
        metadata={
            "name": "axleWeight",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    maximum_permitted_axle_weight: float | None = field(
        default=None,
        metadata={
            "name": "maximumPermittedAxleWeight",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    axle_weight_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "axleWeightExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
