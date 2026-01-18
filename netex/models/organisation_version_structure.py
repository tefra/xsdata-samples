from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Any

from .alternative_names_rel_structure import AlternativeNamesRelStructure
from .contact_structure import ContactStructure
from .entity_in_version_structure import (
    DataManagedObjectStructure,
    ValidBetweenVersionStructure,
)
from .external_object_ref_structure import ExternalObjectRefStructure
from .locale import Locale
from .multilingual_string import MultilingualString
from .organisation_parts_rel_structure import OrganisationPartsRelStructure
from .organisation_refs_rel_structure import OrganisationRefsRelStructure
from .organisation_type_enumeration import OrganisationTypeEnumeration
from .private_code import PrivateCode
from .private_code_structure import PrivateCodeStructure
from .related_organisations_rel_structure import (
    RelatedOrganisationsRelStructure,
)
from .responsibility_sets_rel_structure import ResponsibilitySetsRelStructure
from .type_of_organisation_refs_rel_structure import (
    TypeOfOrganisationRefsRelStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class OrganisationVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "Organisation_VersionStructure"

    public_code: None | PrivateCodeStructure = field(
        default=None,
        metadata={
            "name": "PublicCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    private_code: None | PrivateCode = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    company_number: None | str = field(
        default=None,
        metadata={
            "name": "CompanyNumber",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    vatnumber: None | str = field(
        default=None,
        metadata={
            "name": "VATNumber",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    external_operator_ref: None | ExternalObjectRefStructure = field(
        default=None,
        metadata={
            "name": "ExternalOperatorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    name: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    short_name: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    legal_name: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "LegalName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    trading_name: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "TradingName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    alternative_names: None | AlternativeNamesRelStructure = field(
        default=None,
        metadata={
            "name": "alternativeNames",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    description: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    remarks: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    locale: None | Locale = field(
        default=None,
        metadata={
            "name": "Locale",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    contact_details: None | ContactStructure = field(
        default=None,
        metadata={
            "name": "ContactDetails",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    private_contact_details: None | ContactStructure = field(
        default=None,
        metadata={
            "name": "PrivateContactDetails",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    organisation_type: Iterable[OrganisationTypeEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "OrganisationType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    types_of_organisation: None | TypeOfOrganisationRefsRelStructure = field(
        default=None,
        metadata={
            "name": "typesOfOrganisation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    status: None | bool = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    validity_period: None | OrganisationVersionStructure.ValidityPeriod = (
        field(
            default=None,
            metadata={
                "name": "ValidityPeriod",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    parts: None | OrganisationPartsRelStructure = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    own_responsibility_sets: None | ResponsibilitySetsRelStructure = field(
        default=None,
        metadata={
            "name": "ownResponsibilitySets",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    delegated_responsibility_sets: None | ResponsibilitySetsRelStructure = (
        field(
            default=None,
            metadata={
                "name": "delegatedResponsibilitySets",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    delegated_from: None | OrganisationRefsRelStructure = field(
        default=None,
        metadata={
            "name": "delegatedFrom",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    related_organisations: None | RelatedOrganisationsRelStructure = field(
        default=None,
        metadata={
            "name": "relatedOrganisations",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )

    @dataclass
    class ValidityPeriod(ValidBetweenVersionStructure):
        name: Any = field(
            init=False,
            default=None,
            metadata={
                "type": "Ignore",
            },
        )
        description: Any = field(
            init=False,
            default=None,
            metadata={
                "type": "Ignore",
            },
        )
        conditioned_object_ref: Any = field(
            init=False,
            default=None,
            metadata={
                "type": "Ignore",
            },
        )
        with_condition_ref: Any = field(
            init=False,
            default=None,
            metadata={
                "type": "Ignore",
            },
        )
        key_list: Any = field(
            init=False,
            default=None,
            metadata={
                "type": "Ignore",
            },
        )
        extensions: Any = field(
            init=False,
            default=None,
            metadata={
                "type": "Ignore",
            },
        )
        branding_ref: Any = field(
            init=False,
            default=None,
            metadata={
                "type": "Ignore",
            },
        )
        validity_conditions_or_valid_between: Any = field(
            init=False,
            default=None,
            metadata={
                "type": "Ignore",
            },
        )
        alternative_texts: Any = field(
            init=False,
            default=None,
            metadata={
                "type": "Ignore",
            },
        )
