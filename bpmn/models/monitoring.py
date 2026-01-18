from __future__ import annotations

from dataclasses import dataclass

from .t_monitoring import TMonitoring

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class Monitoring(TMonitoring):
    class Meta:
        name = "monitoring"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
