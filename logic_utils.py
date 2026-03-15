#FIX: Refactored logic into logic_utils.py using Copilot Agent modeel. 
# Updated app.py to use new logic functions.

def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    # FIX: Flip the comparison to match the correct logic. If guess is greater than
    # secret, it's "Too High". Otherwise, it's "Too Low".
    try:
        if guess > secret:
            return "Too High", "📉 Go LOWER!"
        else:
            return "Too Low", "📈 Go HIGHER!"
    except TypeError:
        g = str(guess)

        if g == secret:
            return "Win", "🎉 Correct!"
        
        # FIX: Try numeric comparison for string representations of numbers
        # Since lexicographical comparison of strings can be misleading 
        # (e.g. "10" < "2"), we attempt to convert both to integers for a 
        # more intuitive comparison. If conversion fails, we fall back to string 
        # comparison.
        try:
            guess_int = int(g)
            secret_int = int(secret)
            if guess_int > secret_int:
                return "Too High", "📉 Go LOWER!"
            else:
                return "Too Low", "📈 Go HIGHER!"
        except ValueError:
            # Fallback to string comparison for non-numeric strings
            if g > secret:
                return "Too High", "📉 Go LOWER!"
            return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points
    
    # Penalize for wrong guesses
    if outcome in ["Too High", "Too Low"]:
        return current_score - 5
    
    return current_score
