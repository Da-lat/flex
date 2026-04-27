import pytest

from champs import myresources
from champs.random_champs import constants, filters, random_champ_weighted
from champs.random_champs.filters import DamageTypeFilter, RoleFilter


def _weighted_role_pool(role: str) -> set[str]:
    return {
        row["champion"]
        for row in myresources.CHAMPS_WITH_ROLE_DATA
        if row.get(role, "").strip()
    }


def _filter_of_type(filter_objects, filter_type):
    return next(
        filter_object for filter_object in filter_objects if isinstance(filter_object, filter_type)
    )


def test_role_filter_sanitise_filter_maps_aliases() -> None:
    assert RoleFilter.sanitise_filter("adc") == "BOT"
    assert RoleFilter.sanitise_filter("jgl") == "JUNGLE"
    assert RoleFilter.sanitise_filter("support") == "SUPP"


def test_role_filter_sanitise_filter_rejects_invalid() -> None:
    with pytest.raises(ValueError):
        RoleFilter.sanitise_filter("invalid-role")


@pytest.mark.parametrize("role", constants.ROLES)
def test_role_keyword_pool_matches_weighted_role_source(role: str) -> None:
    filtered = set(random_champ_weighted.get_random_champs_with_filters(999, [role.lower()]))

    assert filtered == _weighted_role_pool(role)


def test_ambiguous_adc_filter_maps_to_role_only() -> None:
    filter_objects = filters.parse_filters(["adc"])

    assert _filter_of_type(filter_objects, RoleFilter).filters == [constants.BOT]
    assert _filter_of_type(filter_objects, DamageTypeFilter).filters == []
    filtered = set(random_champ_weighted.get_random_champs_with_filters(999, ["adc"]))

    assert filtered == _weighted_role_pool(constants.BOT)
