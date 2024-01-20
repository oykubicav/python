
def construct_forest(defs):
    func_dict = {}


    # inner recursive function -- can access func_dict
    def construct_tree(term):
        if term not in func_dict:  #  avoid code repetition
            return [term]
        func_dict[term][-1] += 1  # adjust reference counter
        term1, operator, term2, _ = func_dict[term]


        return [term, operator, construct_tree(term1), construct_tree(term2)]


    for defn in defs:

        defn = defn.replace(" ", "")




        func, terms = defn.replace("(x)", "").split("=")
        if "+" in terms:
            terms= terms.replace("+"," + ")
        elif "-" in terms:
            terms = terms.replace("-", " - ")
        elif "*" in terms:
            terms = terms.replace("*", " * ")
        elif "^" in terms:
            terms = terms.replace("^", " ^ ")
        elif "/" in terms:
            terms = terms.replace("/", " / ")




        func_dict[func] = [*terms.split(), 0]  # append a reference counter

    # Pass func key to construct_tree so to avoid code repetition
    forest = list(map(construct_tree, func_dict))
    # Only return trees that were referenced once (i.e. roots)
    return [tree for tree in forest if func_dict[tree[0]][-1] == 1]

    




