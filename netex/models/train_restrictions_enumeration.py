from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class TrainRestrictionsEnumeration(Enum):
    ANY_TRAIN = "anyTrain"
    RESTRICTED = "restricted"
    SPECIFIED_TRAIN_ONLY = "specifiedTrainOnly"
    SPECIFIED_TRAINS_ONLY = "specifiedTrainsOnly"
    SPECIFIED_TRAIN_AND_CONNECTIONS = "specifiedTrainAndConnections"
