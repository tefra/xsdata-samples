from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.charge_band_versioned_reference import (
    ChargeBandVersionedReference,
)
from datexii.models.eu.datexii.v2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass(kw_only=True)
class ChargeBandByReference:
    """
    Using (a) prior defined charge band(s), identified by its reference.

    :ivar charge_band_reference: A reference to a charge band.
    :ivar charge_band_by_reference_extension:
    """

    charge_band_reference: ChargeBandVersionedReference = field(
        metadata={
            "name": "chargeBandReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    charge_band_by_reference_extension: None | ExtensionType = field(
        default=None,
        metadata={
            "name": "chargeBandByReferenceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
