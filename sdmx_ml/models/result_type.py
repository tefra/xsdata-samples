from dataclasses import dataclass, field
from typing import Optional, Tuple

from sdmx_ml.models.registration_type import RegistrationType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry"


@dataclass(frozen=True)
class ResultType:
    """ResultType contains the details about a data or metadata source, through the
    complete registration information.

    In addition, a reference to the content constraints for the data
    source may be provided, if the query requested this information.

    :ivar registration: Registration provides the details of a matching
        registration. In addition to the data source and provision
        agreement information, the id of the registration must also be
        provided.
    :ivar constraint: Constraint provides a reference to a data or
        metadata constraint in the registry for the resulting data
        source (or possibly constraints base on the registration
        provision agreement, data provider, structure usage, or
        structure). The reference is provided for by a URN and/or a
        complete set of reference fields.
    """

    registration: Optional[RegistrationType] = field(
        default=None,
        metadata={
            "name": "Registration",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
            "required": True,
        },
    )
    constraint: Tuple[str, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Constraint",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
            "pattern": r".+\.registry\.DataConstraint=.+|.+\.registry\.MetadataConstraint=.+",
        },
    )
