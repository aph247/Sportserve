#!/usr/bin/env python3

import pytest
from assets.helpers.utils import epoch_request


@pytest.mark.parametrize('test_id, epoch, date_time_string', [
        pytest.param("Epoch 0", 0, '"1970-01-01 12:00:00"'),
        pytest.param("Epoch 1", 1, '"1970-01-01 12:00:01"'),
        pytest.param("Max Epoch", 9999999999, '"2286-11-20 05:46:39"')
    ])
def test_valid_epoch(test_id, epoch, date_time_string):
    """
    In this test we are testing the limits for epoch value from 0 to 9999999999
    The max value is assuming Milliseconds are not supported
    """
    epoch_request(epoch, date_time_string)


@pytest.mark.parametrize('test_id, epoch, date_time_string', [
        pytest.param("Year 1999", 915148800, '"1999-01-01 12:00:00"'),
        pytest.param("Year 2000", 946684800, '"2000-01-01 12:00:00"'),
        pytest.param("Year 2001", 978307200, '"2001-01-01 12:00:00"'),
        pytest.param("Month Jan", 980942400, '"2001-01-31 12:00:00"'),
        pytest.param("Month Dec", 1009756800, '"2001-12-31 12:00:00"'),
        pytest.param("Day 1st of year", 1672570800, '"2023-01-01 11:00:00"'),
        pytest.param("Day Last of year", 1704067199, '"2023-12-31 11:59:59"'),
        pytest.param("Time Min of day", 1703984461, '"2023-12-31 01:01:01"'),
        pytest.param("Time Max of day", 1698796799, '"2023-10-31 23:59:59"'),
        pytest.param("Time Midnight", 1703980800, '"2023-12-31 00:00:00"'),
        pytest.param("Time AM", 1703998800, '"2023-12-31 05:00:00"'),
        pytest.param("Time PM", 1704011600, '"2023-12-31 17:00:00"'),
        pytest.param("Negative Epoch", -1, '"1969-12-31 11:59:59"'),
        pytest.param("Leap Year", 1709204400, '"2024-02-29 11:00:00"')

    ])
def test_valid_timestamp_format(test_id, epoch, date_time_string):
    """
    In this test we are testing epoch values that will trigger maximum and minimum
    values for components of the returned datetime string such as days, months hours, etc
    """
    epoch_request(epoch, date_time_string)


@pytest.mark.parametrize('test_id, epoch, date_time_string', [
        pytest.param("Alphameric", "Abc", 'false'),
        pytest.param("Alphanumeric", "100a", 'false'),
        pytest.param("Symbols", "@#$", 'false')
    ])
def test_invalid_epoch_values(test_id, epoch, date_time_string):
    """
    In this test we are testing the response to invalid Epoch values
    """
    epoch_request(epoch, date_time_string)


@pytest.mark.parametrize('test_id, epoch, date_time_string', [
        pytest.param("SQL injection", "999 OR 1=1", 'false')
    ])
def test_sql_injection(test_id, epoch, date_time_string):
    """
    In this test we are testing the response to SQL injection
    """
    epoch_request(epoch, date_time_string)