from dataclasses import dataclass, field
from typing import Optional, Tuple

from sdmx_ml.models.metadata_provision_agreement_base_type import (
    MetadataProvisionAgreementBaseType,
)

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class MetadataProvisionAgreementType(MetadataProvisionAgreementBaseType):
    """ProvisionAgreementType describes the structure of a provision agreement.

    A provision agreement defines an agreement for a data provider to
    report data or reference metadata against a flow. Attributes which
    describe how the registry must behave when data or metadata is
    registered against this provision agreement are supplied.

    :ivar metadataflow: Metadataflow provides a reference to a pre-
        existing metadataflow in the registry. The reference is provided
        via a URN and/or a full set of reference fields.
    :ivar metadata_provider: MetadataProvider provides a reference to a
        pre-existing metadata provider in the registry. The reference is
        provided via a URN and/or a full set of reference fields.
    :ivar target: References identifiable structures to which the
        refernece metadata described by the metadata structure used by
        the metadaflow should be restricted to. These references may
        include wildcards for parts of the reference.
    """

    metadataflow: Optional[str] = field(
        default=None,
        metadata={
            "name": "Metadataflow",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "required": True,
            "pattern": r".+\.metadatastructure\.Metadataflow=.+",
        },
    )
    metadata_provider: Optional[str] = field(
        default=None,
        metadata={
            "name": "MetadataProvider",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "required": True,
            "pattern": r".+\.base\.MetadataProvider=.+:METADATA_PROVIDERS\(.+\).+",
        },
    )
    target: Tuple[str, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Target",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "pattern": r".+\)(\.[A-Za-z0-9_@$\-]+(\.[A-Za-z0-9_@$\-]+)*)?|.+\)(\.\*(\.\*)*)?",
        },
    )
