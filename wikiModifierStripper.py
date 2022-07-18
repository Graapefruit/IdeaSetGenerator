import regex as re
if __name__ == "__main__":
    matchingRegex = re.compile("<tr>\s*<td>\s*([a-z_]*?)\s*<\/td>\s*<td>\s*<code>([a-z_ = -.0-9]*?)<\/code>\s*<\/td>\s*<td>([A-Za-z0-9\s*.,‘`'’()-<>=_:\"%#]*?)\s*<\/td>\s*<td>\s*(Additive|Multiplicative|Constant)\s*<\/td>\s*<td>\s*([0-9. ()a-zA-Z]*?)\s*<\/td>\s*<\/tr>", re.IGNORECASE)
    wikiFile = open("OnlyModifiers.txt", 'r')
    outputFile = open("modifiers.txt", "w")
    matches = re.findall(matchingRegex, wikiFile.read())
    wikiFile.close
    for match in matches:
        modifierName = match[0].strip()
        baseValue = match[1].split("=")[1].strip()
        description = match[2].strip().replace("\n", " ")
        effectType = match[3].strip()
        versionAdded = match[4].strip()
        outputFile.write("{};{};{};{};{}\n".format(modifierName, baseValue, description, effectType, versionAdded))
    outputFile.write("adm_cost_modifier;-0.1;Modifies the Cost of Administrative Technologies;Multiplicative;1.1\n")
    outputFile.write("dip_cost_modifier;-0.1;Modifies the Cost of Diplomatic Technologies;Multiplicative;1.1\n")
    outputFile.write("mil_cost_modifier;-0.1;Modifies the Cost of Military Technologies;Multiplicative;1.1\n")
    outputFile.close()
    # TODO: Faction Influence
    # TODO: Estate Loyalty
    # TODO: Estate Influence