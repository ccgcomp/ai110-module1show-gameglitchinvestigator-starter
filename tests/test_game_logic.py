from logic_utils import check_guess, parse_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, outcome should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, outcome should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"

def test_hint_direction_matches_outcome():
    # Regression test for bug #1: the hint text was swapped, telling the
    # player to go HIGHER when their guess was already too high (and vice versa).
    _, message_high = check_guess(60, 50)
    assert "LOWER" in message_high

    _, message_low = check_guess(40, 50)
    assert "HIGHER" in message_low

def test_guess_below_range_is_rejected():
    # Regression test for bug #2: guesses outside the allowed range were
    # silently accepted instead of being rejected.
    ok, value, err = parse_guess("0", 1, 100)
    assert ok is False
    assert value is None
    assert err is not None

def test_guess_above_range_is_rejected():
    ok, value, err = parse_guess("101", 1, 100)
    assert ok is False
    assert value is None
    assert err is not None

def test_guess_within_range_is_accepted():
    ok, value, err = parse_guess("50", 1, 100)
    assert ok is True
    assert value == 50
    assert err is None

def test_guess_at_range_boundaries_is_accepted():
    ok_low, value_low, _ = parse_guess("1", 1, 100)
    ok_high, value_high, _ = parse_guess("100", 1, 100)
    assert ok_low is True and value_low == 1
    assert ok_high is True and value_high == 100
