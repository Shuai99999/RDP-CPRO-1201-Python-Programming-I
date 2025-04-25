rostam_data = {
    "name": "Rostam",
    "nationality": "Turanian",
    "father": "Zal",
    "mother": "Rudaabeh",
    "spouse": "Tahmineh",
    "grandfather": "Sam",
    "delivery": "C-Section",
    "POB": "Zabol",
    "POD": "Kabul",
}

print(rostam_data["mother"], rostam_data["spouse"])
rostam_data["nationality"] = "Iranian"
print(rostam_data)

rostam_data["children"] = ["Sohrab", "Faramarz", "Jahangir", "Siyavash", "Banu-Goshasp"]
print(rostam_data)
