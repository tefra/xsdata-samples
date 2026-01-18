from __future__ import annotations

from dataclasses import dataclass

from .data_source_version_structure import DataSourceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DataSource(DataSourceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
