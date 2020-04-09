#!/usr/bin/env python3

import pytest
import nfldfs.utils as utils


# These are valid parameters and should return no errors
def test_game_parameters_validator_pass():
    assert utils.game_parameters_validator('dk', 2019, 2019, 1, 14) is None
    assert utils.game_parameters_validator('fd', 2014, 2016, 2, 6) is None
    assert utils.game_parameters_validator('yh', 2016, 2017, 1, 1) is None


# Raise an error for invalid dfs site
def test_game_parameters_validator_raise_error_site():
    with pytest.raises(Exception) as info:
        utils.game_parameters_validator('dd', 2019, 2019, 1, 1)

    assert "Invalid dfs site" in str(info.value)


# Raise an error for invalid year
def test_game_parameters_validator_raise_error_year():
    with pytest.raises(Exception) as info:
        utils.game_parameters_validator('dk', '2019', '2019', 1, 1)

    assert "Season From 2019 is out of scope of the valid seasons for this site: [2014, 2015, 2016, 2017, 2018, 2019]" in str(info.value)
