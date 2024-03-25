from dataclasses import dataclass

from sdmx_ml.models.maintainable_type import MaintainableType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class ProvisionAgreementBaseType(MaintainableType):
    """ProvisionAgreementBaseType defines the base refinement of the
    ProvisionAgreementType.

    Its purpose is to retrict the urn attribute.
    """
