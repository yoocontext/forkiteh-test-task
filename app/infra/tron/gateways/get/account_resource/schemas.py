from dataclasses import dataclass


@dataclass
class GetAccountResourceResponseSchema:
    free_net_limit: int
    asset_net_used: list["KeyValue"]
    asset_net_limit: list["KeyValue"]
    total_net_limit: int
    total_net_weight: int
    total_energy_limit: int
    total_energy_weight: int


@dataclass
class KeyValue:
    key: str
    value: int