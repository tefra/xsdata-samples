from dataclasses import dataclass, field

from sdmx_ml.models.metadata_provision_agreement_type import (
    MetadataProvisionAgreementType,
)

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class MetadataProvisionAgreementsType:
    """MetadataProvisionAgreementsType describes the structure of the metadata
    provision agreements container.

    It contains one or more metadata provision agreement, which can be
    explicitly detailed or referenced from an external structure
    document or registry service.

    :ivar metadata_provision_agreement: MetadataProvisionAgreement
        provides the details of a metadata provision agreement, which is
        an agreement for a metadata provider to report reference
        metadata against a flow.
    """

    metadata_provision_agreement: tuple[
        MetadataProvisionAgreementType, ...
    ] = field(
        default_factory=tuple,
        metadata={
            "name": "MetadataProvisionAgreement",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "min_occurs": 1,
        },
    )
