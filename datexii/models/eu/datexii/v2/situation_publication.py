from dataclasses import dataclass, field
from typing import List, Optional
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.payload_publication import PayloadPublication
from datexii.models.eu.datexii.v2.situation import Situation

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class SituationPublication(PayloadPublication):
    """
    A publication containing zero or more traffic/travel situations.
    """

    situation: List[Situation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    situation_publication_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "situationPublicationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
