#!/usr/bin/env python3

# This is a standalone script that lists all available scenes in the crowd application

scenes = [
    {"key": "the-matrix", "title": "The Matrix (1999)"},
    {"key": "harry-potter-1", "title": "Harry Potter and the Philosopher's Stone (2001)"},
    {"key": "mean-girls", "title": "Mean Girls (2004)"},
    {"key": "lotr-fellowship", "title": "The Lord of the Rings: The Fellowship of the Ring (2001)"},
    {"key": "batman-tdk-power", "title": "The Dark Knight (2008)"},
    {"key": "starwars-ep3-darthplagueis", "title": "Star Wars - Episode III (Revenge of the Sith)"},
]

if __name__ == "__main__":
    print("Available scenes:")
    print("----------------")
    print("Scene Key                        | Title")
    print("----------------------------------|-----------------------------------------------")
    for scene in scenes:
        print(f"{scene['key']:35} | {scene['title']}")
    
    print("\nUsage example:")
    print("python crowd.py --scene the-matrix --channel C123456 --delay 2 --speed 1.0")
