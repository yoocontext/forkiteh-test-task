from dataclasses import dataclass


@dataclass
class AccountResponseSchema:
    account_name: str
    type: str
    address: str
    balance: int
    net_window_size: int
    net_window_optimized: bool
    account_resource: "AccountResource"
    frozen_v2: list["FrozenItem"]
    asset_v2: list["AssetItem"]
    free_asset_net_usage_v2: list["FreeAssetNetUsageItem"]
    asset_optimized: bool


@dataclass
class AccountResource:
    energy_window_size: int
    energy_window_optimized: bool


@dataclass
class FrozenItem:
    type: str | None = None


@dataclass
class AssetItem:
    key: str
    value: int


@dataclass
class FreeAssetNetUsageItem:
    key: str
    value: int
