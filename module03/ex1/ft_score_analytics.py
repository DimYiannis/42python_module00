import sys
print("=== Player Score Analytics ===")

if len(sys.argv) == 1:
    print("No scores provided. Usage: python3 ft_score_analytics.py <score2> <score2> ...")
else:
    scores = []
    for arg in sys.argv[1:]:
        scores = scores + [int(arg)]
    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {sum(scores) / (len(scores))}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")
