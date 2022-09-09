# This code parses date/times, so please
#
#     pip install python-dateutil
#
# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = response_data_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Any, List, TypeVar, Type, cast, Callable
from enum import Enum
from datetime import datetime
import dateutil.parser


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


@dataclass
class ClanStatistics:
    pass

    @staticmethod
    def from_dict(obj: Any) -> 'ClanStatistics':
        assert isinstance(obj, dict)
        return ClanStatistics()

    def to_dict(self) -> dict:
        result: dict = {}
        return result


class LocalizedName(Enum):
    모병장교 = "모병 장교"
    부사관 = "부사관"
    부사령관 = "부사령관"
    사령관 = "사령관"
    신병 = "신병"
    작전장교 = "작전 장교"


class Name(Enum):
    COMBAT_OFFICER = "combat_officer"
    COMMANDER = "commander"
    EXECUTIVE_OFFICER = "executive_officer"
    JUNIOR_OFFICER = "junior_officer"
    RECRUIT = "recruit"
    RECRUITMENT_OFFICER = "recruitment_officer"


@dataclass
class Role:
    localized_name: LocalizedName
    name: Name
    rank: int
    order: int

    @staticmethod
    def from_dict(obj: Any) -> 'Role':
        assert isinstance(obj, dict)
        localized_name = LocalizedName(obj.get("localized_name"))
        name = Name(obj.get("name"))
        rank = from_int(obj.get("rank"))
        order = from_int(obj.get("order"))
        return Role(localized_name, name, rank, order)

    def to_dict(self) -> dict:
        result: dict = {}
        result["localized_name"] = to_enum(LocalizedName, self.localized_name)
        result["name"] = to_enum(Name, self.name)
        result["rank"] = from_int(self.rank)
        result["order"] = from_int(self.order)
        return result


@dataclass
class Item:
    days_in_clan: int
    last_battle_time: int
    battles_per_day: float
    personal_rating: int
    exp_per_battle: float
    damage_per_battle: float
    online_status: bool
    frags_per_battle: float
    is_press: bool
    wins_percentage: float
    role: Role
    abnormal_results: bool
    battles_count: int
    id: int
    profile_link: str
    name: str

    @staticmethod
    def from_dict(obj: Any) -> 'Item':
        assert isinstance(obj, dict)
        days_in_clan = from_int(obj.get("days_in_clan"))
        last_battle_time = from_int(obj.get("last_battle_time"))
        battles_per_day = from_float(obj.get("battles_per_day"))
        personal_rating = from_int(obj.get("personal_rating"))
        exp_per_battle = from_float(obj.get("exp_per_battle"))
        damage_per_battle = from_float(obj.get("damage_per_battle"))
        online_status = from_bool(obj.get("online_status"))
        frags_per_battle = from_float(obj.get("frags_per_battle"))
        is_press = from_bool(obj.get("is_press"))
        wins_percentage = from_float(obj.get("wins_percentage"))
        role = Role.from_dict(obj.get("role"))
        abnormal_results = from_bool(obj.get("abnormal_results"))
        battles_count = from_int(obj.get("battles_count"))
        id = from_int(obj.get("id"))
        profile_link = from_str(obj.get("profile_link"))
        name = from_str(obj.get("name"))
        return Item(days_in_clan, last_battle_time, battles_per_day, personal_rating, exp_per_battle, damage_per_battle, online_status, frags_per_battle, is_press, wins_percentage, role, abnormal_results, battles_count, id, profile_link, name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["days_in_clan"] = from_int(self.days_in_clan)
        result["last_battle_time"] = from_int(self.last_battle_time)
        result["battles_per_day"] = to_float(self.battles_per_day)
        result["personal_rating"] = from_int(self.personal_rating)
        result["exp_per_battle"] = to_float(self.exp_per_battle)
        result["damage_per_battle"] = to_float(self.damage_per_battle)
        result["online_status"] = from_bool(self.online_status)
        result["frags_per_battle"] = to_float(self.frags_per_battle)
        result["is_press"] = from_bool(self.is_press)
        result["wins_percentage"] = to_float(self.wins_percentage)
        result["role"] = to_class(Role, self.role)
        result["abnormal_results"] = from_bool(self.abnormal_results)
        result["battles_count"] = from_int(self.battles_count)
        result["id"] = from_int(self.id)
        result["profile_link"] = from_str(self.profile_link)
        result["name"] = from_str(self.name)
        return result


@dataclass
class ResponseData:
    status: str
    items: List[Item]
    is_hidden_statistics: bool
    clan_statistics: ClanStatistics
    last_updated_at: datetime

    @staticmethod
    def from_dict(obj: Any) -> 'ResponseData':
        assert isinstance(obj, dict)
        status = from_str(obj.get("status"))
        items = from_list(Item.from_dict, obj.get("items"))
        is_hidden_statistics = from_bool(obj.get("is_hidden_statistics"))
        clan_statistics = ClanStatistics.from_dict(obj.get("clan_statistics"))
        last_updated_at = from_datetime(obj.get("last_updated_at"))
        return ResponseData(status, items, is_hidden_statistics, clan_statistics, last_updated_at)

    def to_dict(self) -> dict:
        result: dict = {}
        result["status"] = from_str(self.status)
        result["items"] = from_list(lambda x: to_class(Item, x), self.items)
        result["is_hidden_statistics"] = from_bool(self.is_hidden_statistics)
        result["clan_statistics"] = to_class(ClanStatistics, self.clan_statistics)
        result["last_updated_at"] = self.last_updated_at.isoformat()
        return result


def response_data_from_dict(s: Any) -> ResponseData:
    return ResponseData.from_dict(s)


def response_data_to_dict(x: ResponseData) -> Any:
    return to_class(ResponseData, x)
