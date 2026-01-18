from dataclasses import dataclass, field
from typing import Optional

from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.code_type import (
    CodeType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.date_type import (
    DateType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.indicator_type import (
    IndicatorType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.base_component_type import (
    BaseComponentType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.gender_code_type import (
    GenderCodeType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.marital_status_code_type import (
    MaritalStatusCodeType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.individual_actor_name_type import (
    IndividualActorNameType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1"
)


@dataclass
class IndividualActorType(BaseComponentType):
    """
    <description xmlns=""/>.

    :ivar name: <description xmlns="">The name of the
        individual.</description>
    :ivar birth_date: <description xmlns="">Date on which the Individual
        was born.</description>
    :ivar death_date: <description xmlns="">Date on which the Individual
        died.</description>
    :ivar death_indicator: <description xmlns="">Flag indicating whether
        the Individual has died</description>
    :ivar nationality_code: <description xmlns="">Nationality of the
        Individual</description>
    :ivar language_code: <description xmlns="">Language of the
        Individual</description>
    :ivar gender_code: <description xmlns="">Gender of the
        Individual</description>
    :ivar marital_status_code: <description xmlns="">Martial status of
        the Individual</description>
    :ivar employee_code:
    """

    name: IndividualActorNameType | None = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    birth_date: DateType | None = field(
        default=None,
        metadata={
            "name": "BirthDate",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    death_date: DateType | None = field(
        default=None,
        metadata={
            "name": "DeathDate",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    death_indicator: IndicatorType | None = field(
        default=None,
        metadata={
            "name": "DeathIndicator",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    nationality_code: CodeType | None = field(
        default=None,
        metadata={
            "name": "NationalityCode",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    language_code: str | None = field(
        default=None,
        metadata={
            "name": "LanguageCode",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    gender_code: GenderCodeType | None = field(
        default=None,
        metadata={
            "name": "GenderCode",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    marital_status_code: MaritalStatusCodeType | None = field(
        default=None,
        metadata={
            "name": "MaritalStatusCode",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    employee_code: CodeType | None = field(
        default=None,
        metadata={
            "name": "EmployeeCode",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
