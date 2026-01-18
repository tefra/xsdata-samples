from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass(kw_only=True)
class OpenlrAreaLocationReference:
    """
    a two-dimensional part of the surface of the earth which is bounded by
    a closed curve.

    An area location may cover parts of the road network but does not
    necessarily need to. It is represente according to the OpenLR standard
    for Area Locations.
    """

    openlr_area_location_reference_extension: None | ExtensionType = field(
        default=None,
        metadata={
            "name": "openlrAreaLocationReferenceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
