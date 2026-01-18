from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass(kw_only=True)
class AxleSpacing:
    """
    The spacing details between the axle sets of an individual vehicle
    numbered from the front to the back of the vehicle.

    :ivar axle_spacing: The spacing interval, indicated by the
        axleSpacingSequenceIdentifier, between the axles of an
        individual vehicle from front to back of the vehicle.
    :ivar axle_spacing_sequence_identifier: Indicates the sequence of
        the interval between the axles of the individual vehicle from
        front to back (e.g. 1, 2, 3...). This cannot exceed
        (numberOfAxles -1) if the numberOfAxles is also given as part of
        the VehicleCharacteristics.
    :ivar axle_spacing_extension:
    """

    axle_spacing: float = field(
        metadata={
            "name": "axleSpacing",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    axle_spacing_sequence_identifier: int = field(
        metadata={
            "name": "axleSpacingSequenceIdentifier",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    axle_spacing_extension: None | ExtensionType = field(
        default=None,
        metadata={
            "name": "axleSpacingExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
