def count_smileys(arr):
    smileys = []
    for word in arr:
        if len(word) == 2 and word[0] in [":", ";"] and word[-1] in [")", "D"]:
            smileys.append(word)
        elif len(word) > 2 and word[0] in [":", ";"] and word[1] in ["-", "~"] and word[-1] in [")", "D"]:
            smileys.append(word)
    return len(smileys)


print(count_smileys([':D',':~)',';~D',':)']))