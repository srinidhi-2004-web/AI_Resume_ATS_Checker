from ranking import calculate_score
from recommendation import recommend

score = calculate_score(
    90,
    85,
    80,
    75
)

print("Final Score =", score)
print(recommend(score))