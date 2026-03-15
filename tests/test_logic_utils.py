import pytest

from logic_utils import (
    check_guess,
    get_range_for_difficulty,
    parse_guess,
    update_score,
)


def test_get_range_for_difficulty():
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 100)
    assert get_range_for_difficulty("Hard") == (1, 50)
    # fallback for unknown difficulties
    assert get_range_for_difficulty("Impossible") == (1, 100)


def test_parse_guess_valid_numbers():
    ok, value, err = parse_guess("10")
    assert ok
    assert value == 10
    assert err is None

    ok, value, err = parse_guess("10.0")
    assert ok
    assert value == 10
    assert err is None

    ok, value, err = parse_guess("10.9")
    assert ok
    assert value == 10
    assert err is None


def test_parse_guess_invalid_inputs():
    ok, value, err = parse_guess(None)
    assert not ok
    assert value is None
    assert err is not None
    assert "Enter a guess" in err

    ok, value, err = parse_guess("")
    assert not ok
    assert value is None
    assert err is not None
    assert "Enter a guess" in err

    ok, value, err = parse_guess("not a number")
    assert not ok
    assert value is None
    assert err is not None
    assert "not a number" in err


def test_check_guess_numeric_and_string_secret():
    # Numeric comparison when secret is int
    assert check_guess(50, 50) == ("Win", "🎉 Correct!")
    assert check_guess(60, 50) == ("Too High", "📉 Go LOWER!")
    assert check_guess(40, 50) == ("Too Low", "📈 Go HIGHER!")

    # When secret is a string (e.g., due to app bug/quirk), we still compare numerically
    assert check_guess(50, "50") == ("Win", "🎉 Correct!")
    assert check_guess(9, "10") == ("Too Low", "📈 Go HIGHER!")
    assert check_guess(11, "10") == ("Too High", "📉 Go LOWER!")


def test_update_score_win_and_floor():
    # Winning on early attempts gives more points
    score = update_score(0, "Win", attempt_number=1)
    assert score == 80  # 100 - 10*(1+1)

    # Minimum points floor should be 10
    score = update_score(0, "Win", attempt_number=10)
    assert score == 10


def test_update_score_penalty_for_wrong_guesses():
    assert update_score(10, "Too High", attempt_number=1) == 5
    assert update_score(10, "Too Low", attempt_number=1) == 5
    assert update_score(10, "Other", attempt_number=1) == 10
