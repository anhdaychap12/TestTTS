def groupAnagrams(strs):
    anagramGroups = {}
    
    for string in strs:
        sortedStr = "".join(sorted(string))
        
        if sortedStr not in anagramGroups:
            anagramGroups[sortedStr] = []
        
        anagramGroups[sortedStr].append(string)
    
    return list(anagramGroups.values())

print(groupAnagrams( ["a"]))