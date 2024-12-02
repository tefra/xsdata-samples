from dataclasses import dataclass, field

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1"


@dataclass
class ExtendedRecordTypeCompanyLevels:
    class Meta:
        global_type = False

    company_level: list[str] = field(
        default_factory=list,
        metadata={
            "name": "CompanyLevel",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        },
    )
