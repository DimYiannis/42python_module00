
players = ["alice", "bob", "charlie", "diana"]
scores = [2300, 1800, 2150, 2050]
achievements = {"alice": ["first_kill", "level_10", "quest_complete", "treasure_hunter"],
                "bob": ["speed_run", "level_5", "quest_complete"], 
                "charlie": ["level_5", "boss_slayer", "quest_complete", 
                "treasure_hunter", "arena_champion", "speed_run"],
                "diana": ["treasure_hunter","arena_champion", "quest_complete"]}
active = {"alice": True, "bob": True, "charlie": True,
        "diana": False}
regions = ["north", "east", "central", "north"]

if __name__ == "__main__":
    print("=== Game Analytics Dashboard ===")

    print("\n=== List Comprehension Examples ===")

    high_scorers = [players[i]
                    for i in range(len(scores))
                    if scores[i] > 2000]
    print(f"High scorers (>2000): {high_scorers}")

    scores_doubled = [score * 2 for score in scores]
    print(f"Scores doubled: {scores_doubled}")

    active_players = [player for player in players if active[player]]
    print(f"Active players: {active_players}")

    print("\n=== Dict Comprehension Examples ===")

    player_scores = {players[i]: scores[i] 
        for i in range(len(players))
        if active[players[i]]
    }
    print(f"player scores : {player_scores}")

    score_categories = {
        'high': len([s for s in scores if s > 2000]),
        'medium': len([s for s in scores if 1900 <= s <= 2000]),
        'low': len([s for s in scores if s < 1900])
    }
    print(f"Score categories: {score_categories}")

    achievements_counts = {
        player: len(achievements[player]) 
        for player in achievements
        if active[player]
    }
    print(f"Achievement counts: {achievements_counts}")


    print("\n=== Set Comprehension Examples ===")

    unique_players = {player for player in players}
    print(f"Unique players: {unique_players}")

    counts = {}

    for player in players:
        a_list = achievements[player]
        for a in a_list:
            if a in counts:
                counts[a] += 1
            else:
                counts[a] = 1

    unique_achievements = {a for a in counts if counts[a] == 1}
    print(f"Unique achievements: {unique_achievements}")

    active_regions = {region for region in regions}
    print(f"Active regions: {active_regions}")

    print("\n=== Combined Analysis ===")

    total_players = len(players)
    print(f"Total players: {total_players}")

    total_unique = len(unique_achievements)
    print(f"Total unique achievements: {total_unique}")

    avg_score = sum(scores) / len(scores)
    print(f"Average score: {avg_score}")

    max_score = max(scores)
    max_score_index = [i for i in range(len(scores)) if scores[i] == max_score][0]
    top_player = players[max_score_index]
    top_achievements = len(achievements[top_player])
    print(f"Top performer: {top_player} ({max_score} points, {top_achievements} achievements)")
 
