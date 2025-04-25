persian_poets = "saadi", "frough", "hafez", "parvin", "saeb"
persian_poets_wo_hafez = tuple(x for x in persian_poets if x != "hafez")
print(persian_poets_wo_hafez)
