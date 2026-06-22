def calculate_score(
resume,
coding,
interview,
portfolio
):

    score = (
        resume*0.4 +
        coding*0.3 +
        interview*0.2 +
        portfolio*0.1
    )

    return score