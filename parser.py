def main():
    """ Takes a one line input from STDIN and outputs 'yes' if it is a proper
    propositional statement. No whitespace
    and = '^'
    or = 'v'
    equivalence = '='
    negation = '~'
    implication = '>'
    S = sentence
    P = proposition
    T/F = Truth Symbols
    C = Connective

    Author 1: Evan Srock
    Author 2:
    Author 3:
    """
    the_input = raw_input().strip()
    if sentence(the_input):
        print 'yes'
    else:
        print 'no'


# **************************************************************
def sentence(s):
    """ Checks if s is a valid Sentence. Check for:
    P
    T/F
    ~S
    (S)C(S)  (I don't think parenthesis are included...)
    (I believe that's all...)

    :param s: A string that represents the sentence to check
    :return: boolean
    """
    return False


# **************************************************************
def symbol(p):
    """ Checks if p is a proposition or truth symbol
    Will return False if p is not in the range A,B..Z,a..z or is more than
    one symbol

    :param p: the proposition to be checked
    :return: boolean
    """
    return len(p) == 1 and p.isalpha()


if __name__ == '__main__':
    main()
