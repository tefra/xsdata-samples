from dataclasses import dataclass, field
from typing import Optional

from generali.models.com.generali.enterprise_services.core.gbo.common.v1.base_identified_component_type import (
    BaseIdentifiedComponentType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.checks_made_against_type import (
    ChecksMadeAgainstType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.checks_made_by_type import (
    ChecksMadeByType,
)

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


@dataclass
class CheckType(BaseIdentifiedComponentType):
    """
    The schema containing the declarations for the framework check object.

    This is used to support the verification of a business object with a
    authoritative third-party reference, e.g. Dun and Bradstreet or a
    Postal Address lookup.

    :ivar made_against: The object against which the set of checks have
        been made.
    :ivar made_by: The person or organisation that made the checks
        against the business object.
    """

    made_against: Optional[ChecksMadeAgainstType] = field(
        default=None,
        metadata={
            "name": "MadeAgainst",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    made_by: Optional[ChecksMadeByType] = field(
        default=None,
        metadata={
            "name": "MadeBy",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
