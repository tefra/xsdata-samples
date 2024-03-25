from dataclasses import dataclass, field
from typing import Tuple

from sdmx_ml.models.provision_agreement_type import ProvisionAgreementType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class ProvisionAgreementsType:
    """ProvisionAgreementsType describes the structure of the provision agreements
    container.

    It contains one or more provision agreement, which can be explicitly
    detailed or referenced from an external structure document or
    registry service.

    :ivar provision_agreement: ProvisionAgreement provides the details
        of a provision agreement, which is an agreement for a data
        provider to report data against a flow.
    """

    provision_agreement: Tuple[ProvisionAgreementType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ProvisionAgreement",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "min_occurs": 1,
        },
    )
