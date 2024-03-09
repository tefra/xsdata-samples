from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.generic_publication_extension_type import (
    GenericPublicationExtensionType,
)
from datexii.models.eu.datexii.v2.payload_publication import PayloadPublication

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class GenericPublication(PayloadPublication):
    """
    A publication used to make level B extensions at the publication level.

    :ivar generic_publication_name: The name of the generic publication.
    :ivar generic_publication_extension:
    """

    generic_publication_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "genericPublicationName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
            "max_length": 1024,
        },
    )
    generic_publication_extension: Optional[
        GenericPublicationExtensionType
    ] = field(
        default=None,
        metadata={
            "name": "genericPublicationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
