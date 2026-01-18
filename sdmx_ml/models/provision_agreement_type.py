from dataclasses import dataclass, field

from sdmx_ml.models.provision_agreement_base_type import (
    ProvisionAgreementBaseType,
)

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class ProvisionAgreementType(ProvisionAgreementBaseType):
    """
    ProvisionAgreementType describes the structure of a provision
    agreement.

    A provision agreement defines an agreement for a data provider to
    report data against a dataflow. Attributes which describe how the
    registry must behave when data or metadata is registered against this
    provision agreement are supplied.

    :ivar dataflow: Dataflow provides a reference to a pre-existing
        dataflow in the registry. The reference is provided via a URN
        and/or a full set of reference fields.
    :ivar data_provider: DataProvider provides a reference to a pre-
        existing data provider in the registry. The reference is
        provided via a URN and/or a full set of reference fields.
    """

    dataflow: str | None = field(
        default=None,
        metadata={
            "name": "Dataflow",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "required": True,
            "pattern": r".+\.datastructure\.Dataflow=.+",
        },
    )
    data_provider: str | None = field(
        default=None,
        metadata={
            "name": "DataProvider",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "required": True,
            "pattern": r".+\.base\.DataProvider=.+:DATA_PROVIDERS\(.+\).+",
        },
    )
