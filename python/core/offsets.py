from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class SunPatch:
    addr: int
    hack: bytes
    reset: bytes


@dataclass(frozen=True)
class VersionOffsets:
    name: str
    timestamp: int
    lawn: int
    board: int
    slot: int
    slot_count: int
    slot_seed_type: int
    slot_seed_type_im: int
    game_ui: int
    game_mode: int
    scene: int
    free_planting: int
    sun: int
    user_data: int
    money: int
    unlock_sun_limit: SunPatch


OFFSETS_1051_EN = VersionOffsets(
    name="1.0.0.1051 (en)",
    timestamp=0x49ECF563,
    lawn=0x6A9EC0,
    board=0x768,
    slot=0x144,
    slot_count=0x24,
    slot_seed_type=0x5C,
    slot_seed_type_im=0x60,
    game_ui=0x7FC,
    game_mode=0x7F8,
    scene=0x554C,
    free_planting=0x814,
    sun=0x5560,
    user_data=0x82C,
    money=0x28,
    unlock_sun_limit=SunPatch(addr=0x00430A23, hack=b"\xEB", reset=b"\x7E"),
)

OFFSETS_1065_EN = VersionOffsets(
    name="1.2.0.1065 (en)",
    timestamp=0x4A37D6AF,
    lawn=0x6A9EC0,
    board=0x768,
    slot=0x144,
    slot_count=0x24,
    slot_seed_type=0x5C,
    slot_seed_type_im=0x60,
    game_ui=0x7FC,
    game_mode=0x7F8,
    scene=0x554C,
    free_planting=0x814,
    sun=0x5560,
    user_data=0x82C,
    money=0x28,
    unlock_sun_limit=SunPatch(addr=0x00430A83, hack=b"\xEB", reset=b"\x7E"),
)

OFFSETS_1073_EN = VersionOffsets(
    name="GOTY 1.2.0.1073 (en)",
    timestamp=0x4C2E3453,
    lawn=0x729670,
    board=0x868,
    slot=0x15C,
    slot_count=0x24,
    slot_seed_type=0x5C,
    slot_seed_type_im=0x60,
    game_ui=0x91C,
    game_mode=0x918,
    scene=0x5564,
    free_planting=0x934,
    sun=0x5578,
    user_data=0x94C,
    money=0x50,
    unlock_sun_limit=SunPatch(addr=0x0041E6F5, hack=b"\xEB", reset=b"\x7E"),
)

OFFSETS_1096_EN = VersionOffsets(
    name="GOTY 1.2.0.1096 (en)",
    timestamp=0x4D02B058,
    lawn=0x731C50,
    board=0x868,
    slot=0x15C,
    slot_count=0x24,
    slot_seed_type=0x5C,
    slot_seed_type_im=0x60,
    game_ui=0x91C,
    game_mode=0x918,
    scene=0x5564,
    free_planting=0x934,
    sun=0x5578,
    user_data=0x94C,
    money=0x54,
    unlock_sun_limit=SunPatch(addr=0x0041F4E5, hack=b"\xEB", reset=b"\x7E"),
)

VERSIONS_BY_TIMESTAMP = {
    OFFSETS_1051_EN.timestamp: OFFSETS_1051_EN,
    OFFSETS_1065_EN.timestamp: OFFSETS_1065_EN,
    OFFSETS_1073_EN.timestamp: OFFSETS_1073_EN,
    OFFSETS_1096_EN.timestamp: OFFSETS_1096_EN,
}

KNOWN_VERSION_NAMES = {
    0x49ECF563: "1.0.0.1051 (en)",
    0x4A37D6AF: "1.2.0.1065 (en)",
    0x4A5B7963: "1.0.4.7924 (es)",
    0x4C237519: "1.0.7.3556 (es)",
    0x4CE4C3D6: "1.0.7.3467 (ru)",
    0x4C2E3453: "GOTY 1.2.0.1073 (en)",
    0x4D02B058: "GOTY 1.2.0.1096 (en)",
    0x4CA31BAA: "GOTY 1.2.0.1093 (de/es/fr/it)",
    0x4C563DE1: "GOTY 1.1.0.1056 (zh)",
    0x4CC8E5F8: "GOTY 1.1.0.1056 (ja)",
    0x4FCD7BE2: "GOTY 1.1.0.1056 (zh 2012-06)",
    0x5003D437: "GOTY 1.1.0.1056 (zh 2012-07)",
    0x49359C21: "BETA 0.1.1.1014 (en)",
    0x499A6204: "BETA 0.9.9.1029 (en)",
}

FORCE_ENGLISH_PROFILES = {
    "1051-en": OFFSETS_1051_EN,
    "1065-en": OFFSETS_1065_EN,
    "1073-en": OFFSETS_1073_EN,
    "1096-en": OFFSETS_1096_EN,
}

WINDOW_TITLES = [
    "Plants vs. Zombies",
    "Plants vs. Zombies 1.2.0.1073",
    "Plants vs. Zombies 1.2.0.1073 RELEASE",
    "Plants vs. Zombies GOTY",
    "Pflanzen gegen Zombies 1.2.0.1093",
    "Plantas contra Zombis 1.2.0.1093",
    "Plantes contre Zombies 1.2.0.1093",
    "Piante contro zombi 1.2.0.1093",
    "Bloom & Doom BETA 0.1.1.1014",
    "Plants vs. Zombies BETA 0.9.9.1029",
]

PROCESS_EXE_NAMES = {
    "plantsvszombies.exe",
    "popcapgame1.exe",
    "pvz.exe",
}
