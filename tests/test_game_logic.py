from logic_utils import get_range_for_difficulty, check_guess, update_score

def test_hard_difficulty_range():
    # Tests that the Hard difficulty returns the correct 1 to 100 range
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 100

def test_check_guess_too_high():
    # Tests that guessing higher than the secret returns "Too High" and tells the user to go "LOWER!"
    outcome, message = check_guess(guess=75, secret=50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_check_guess_too_low():
    # Tests that guessing lower than the secret returns "Too Low" and tells the user to go "HIGHER!"
    outcome, message = check_guess(guess=25, secret=50)
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_update_score_win():
    # Tests that winning on the first attempt gives the correct score without the +1 bug
    # 100 - 10 * 1 = 90 points
    new_score = update_score(current_score=0, outcome="Win", attempt_number=1)
    assert new_score == 90