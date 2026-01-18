from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
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

    external_location_code: str | None = field(
        default=None,
        metadata={
            "name": "externalLocationCode",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
            "max_length": 1024,
        },
    )
    external_referencing_system: str | None = field(
        default=None,
        metadata={
            "name": "externalReferencingSystem",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
            "max_length": 1024,
        },
    )
    external_referencing_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "externalReferencingExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
