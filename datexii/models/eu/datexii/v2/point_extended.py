from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.junction import Junction
from datexii.models.eu.datexii.v2.multilingual_string import MultilingualString

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class PointExtended:
    """
    Extension point for 'Point' to support the description of junctions
    (and other alternative point descriptions).

    :ivar description: Textual description for a point location
    :ivar junction:
    """

    description: None | MultilingualString = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    junction: None | Junction = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
