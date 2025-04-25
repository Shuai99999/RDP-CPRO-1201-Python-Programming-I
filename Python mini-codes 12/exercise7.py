kings = {
    "Deioces": -700,
    "Cyrus": -559,
    "Alexander ": -336,
    "Seleucus": -311,
    "Antiochus VII": -139,
    "Darayan I": -132,
    "Arsaces I": -247,
    "Musa": -2,
    "Ardavan IV": 213,
    "Ardashir I": 224,
    "Shapur I": 240,
    "Hormizd I": 270,
    "Bahram I": 271,
}

sasanid_empire = [name for name, year in kings.items() if year > 223]
print(sasanid_empire)
