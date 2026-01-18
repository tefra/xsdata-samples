from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDuration

from .entity_in_version_structure import DataManagedObjectStructure
from .multilingual_string import MultilingualString

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AccountableElementStructure(DataManagedObjectStructure):
    description: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    accounting_time: None | XmlDuration = field(
        default=None,
        metadata={
            "name": "AccountingTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    accounting_factor: None | XmlDuration = field(
        default=None,
        metadata={
            "name": "AccountingFactor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    preparation_duration: None | XmlDuration = field(
        default=None,
        metadata={
            "name": "PreparationDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    finishing_duration: None | XmlDuration = field(
        default=None,
        metadata={
            "name": "FinishingDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
