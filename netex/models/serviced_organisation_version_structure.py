from dataclasses import dataclass, field

from .other_organisation_version_structure import (
    OtherOrganisationVersionStructure,
)
from .service_calendar_ref import ServiceCalendarRef
from .serviced_organisation_type_enumeration import (
    ServicedOrganisationTypeEnumeration,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ServicedOrganisationVersionStructure(OtherOrganisationVersionStructure):
    class Meta:
        name = "ServicedOrganisation_VersionStructure"

    service_calendar_ref: ServiceCalendarRef | None = field(
        default=None,
        metadata={
            "name": "ServiceCalendarRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    serviced_organisation_type: ServicedOrganisationTypeEnumeration | None = (
        field(
            default=None,
            metadata={
                "name": "ServicedOrganisationType",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
