from __future__ import annotations

from dataclasses import dataclass, field

from .codespace_ref_structure import CodespaceRefStructure
from .data_source_ref_structure import DataSourceRefStructure
from .locale_structure import LocaleStructure
from .responsibility_set_ref_structure import ResponsibilitySetRefStructure
from .system_of_units import SystemOfUnits

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VersionFrameDefaultsStructure:
    default_codespace_ref: None | CodespaceRefStructure = field(
        default=None,
        metadata={
            "name": "DefaultCodespaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    default_data_source_ref: None | DataSourceRefStructure = field(
        default=None,
        metadata={
            "name": "DefaultDataSourceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    default_responsibility_set_ref: None | ResponsibilitySetRefStructure = (
        field(
            default=None,
            metadata={
                "name": "DefaultResponsibilitySetRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    default_locale: None | LocaleStructure = field(
        default=None,
        metadata={
            "name": "DefaultLocale",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    default_location_system: None | str = field(
        default=None,
        metadata={
            "name": "DefaultLocationSystem",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    default_system_of_units: None | SystemOfUnits = field(
        default=None,
        metadata={
            "name": "DefaultSystemOfUnits",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    default_currency: None | str = field(
        default=None,
        metadata={
            "name": "DefaultCurrency",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_length": 3,
            "max_length": 3,
            "pattern": r"[A-Z][A-Z][A-Z]",
        },
    )
