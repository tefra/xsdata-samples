from __future__ import annotations

from dataclasses import dataclass

from .t_data_store import TDataStore

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class DataStore(TDataStore):
    class Meta:
        name = "dataStore"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
