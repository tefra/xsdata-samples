from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass(kw_only=True)
class ExternalReferencing:
    """
    A location defined by reference to an external/other referencing
    system.

    :ivar external_location_code: A code in the external referencing
        system which defines the location.
    :ivar external_referencing_system: Identification of the
        external/other location referencing system.
    :ivar external_referencing_extension:
    """

    external_location_code: str = field(
        metadata={
            "name": "externalLocationCode",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
            "max_length": 1024,
        }
    )
    external_referencing_system: str = field(
        metadata={
            "name": "externalReferencingSystem",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
            "max_length": 1024,
        }
    )
    external_referencing_extension: None | ExtensionType = field(
        default=None,
        metadata={
            "name": "externalReferencingExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
