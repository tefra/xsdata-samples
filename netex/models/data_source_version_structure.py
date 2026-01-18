from __future__ import annotations

from dataclasses import dataclass, field

from .external_object_ref_structure import ExternalObjectRefStructure
from .type_of_value_version_structure import TypeOfValueVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DataSourceVersionStructure(TypeOfValueVersionStructure):
    class Meta:
        name = "DataSource_VersionStructure"

    email: None | str = field(
        default=None,
        metadata={
            "name": "Email",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    data_licence_code: None | ExternalObjectRefStructure = field(
        default=None,
        metadata={
            "name": "DataLicenceCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    data_licence_url: None | str = field(
        default=None,
        metadata={
            "name": "DataLicenceUrl",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
