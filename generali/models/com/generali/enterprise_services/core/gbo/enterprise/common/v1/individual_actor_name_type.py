from dataclasses import dataclass, field
from typing import Optional
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.code_type import (
    CodeType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.text_type import (
    TextType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.base_component_type import (
    BaseComponentType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1"
)


@dataclass
class IndividualActorNameType(BaseComponentType):
    """
    <description xmlns=""/>

    :ivar title_code: <description xmlns="">Is the title of the person.
        e.g. Mr., Dr. Ms. </description>
    :ivar first_name_text: <description xmlns="">The primary chosen
        name. Also known as given name.</description>
    :ivar middle_name_text: <description xmlns="">The person middle
        name</description>
    :ivar middle_initial_text: <description xmlns="">The person middle
        initial name</description>
    :ivar family_name_text: <description xmlns="">The person family
        name</description>
    :ivar prefix_code: <description xmlns="">Prefix to the last name
        that is not considered part of the last name, such as German von
        or French dela, etc.</description>
    :ivar suffix_code: <description xmlns="">Suffix to the last name,
        such as Senior, III, the Third etc. </description>
    :ivar salutation_text: <description xmlns="">Way the person is
        addressed e.g. Honorable etc</description>
    :ivar formatted_name_text: <description xmlns="">Formatted
        name</description>
    :ivar aristocratic_title_code: <description xmlns="">Aristocratic
        Title e.g. Duke, Knight</description>
    :ivar legal_name_text: <description xmlns="">Legal Name by which the
        person is addressed</description>
    :ivar preferred_given_name_text: <description xmlns="">Name by which
        the person prefers to be addressed</description>
    """

    title_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "TitleCode",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    first_name_text: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "FirstNameText",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    middle_name_text: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "MiddleNameText",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    middle_initial_text: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "MiddleInitialText",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    family_name_text: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "FamilyNameText",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    prefix_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "PrefixCode",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    suffix_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "SuffixCode",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    salutation_text: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "SalutationText",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    formatted_name_text: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "FormattedNameText",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    aristocratic_title_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "AristocraticTitleCode",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    legal_name_text: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "LegalNameText",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
    preferred_given_name_text: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "PreferredGivenNameText",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
