from dataclasses import dataclass, field
from typing import Optional
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.overall_period import OverallPeriod

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class Contact:
    """
    Address and contact information about some person, service or the parking site,
    provided in detail or via reference.

    :ivar contact_unknown: When true, the contact for the selected role
        and/or timeframe is unknown. Don't use the specialisations in
        this case.
    :ivar contact_not_defined: When true, there is currently no contact
        defined for the selected role and/or timeframe. Don't use the
        specialisations in this case.
    :ivar validity_of_contact:
    :ivar contact_extension:
    """
    contact_unknown: Optional[bool] = field(
        default=None,
        metadata={
            "name": "contactUnknown",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    contact_not_defined: Optional[bool] = field(
        default=None,
        metadata={
            "name": "contactNotDefined",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    validity_of_contact: Optional[OverallPeriod] = field(
        default=None,
        metadata={
            "name": "validityOfContact",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    contact_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "contactExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
