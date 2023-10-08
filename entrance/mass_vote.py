def MassVote(_number_of_candidates: int, votes: list) -> str:
    total_votes = sum(votes)
    if total_votes < 1:
        return "no winner"

    winner_votes = max(votes)
    winner_percents = round((winner_votes / total_votes), 3)
    winner_position = votes.index(winner_votes) + 1
    number_of_winners = votes.count(winner_votes)

    if number_of_winners > 1:
        return "no winner"
    if winner_percents > 0.5:
        return f"majority winner {winner_position}"
    if winner_percents <= 0.5:
        return f"minority winner {winner_position}"

    return "no winner"
