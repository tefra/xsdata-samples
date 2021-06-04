from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class VehicleLoadingEnumeration(Enum):
    NONE_VALUE = "none"
    LOADING = "loading"
    UNLOADING = "unloading"
    ADDITIONAL_LOADING = "additionalLoading"
    ADDITIONA_UNLOADING = "additionaUnloading"
    UNKNOWN = "unknown"
