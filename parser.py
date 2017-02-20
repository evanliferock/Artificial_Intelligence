def main():
    """ Takes a one line input from STDIN and outputs 'yes' if it is a proper
    propositional statement, no otherwise. NO WHITESPACE
    and = '&'
    or = '|'
    equivalence = '='
    negation = '~'
    implication = '>'
    S = sentence
    P = proposition
    T/F = Truth Symbols
    C = Connective

    Author 1: Evan Srock (esrock)
    Author 2: Patrick Chadbourne
    Author 3: Katie Phillips
    """
    if sentence(Parser()):
        print 'yes'
    else:
        print 'no'


# **************************************************************
def sentence(p):
    """ Checks if s is a valid Sentence. Check for:
    P
    T/F
    ~S

    :param s: A string that represents the sentence to check
    :return: boolean
    """
    return False


# **************************************************************
def negation_sentence(p):
    """
        checks for it to be a valid
    :param p: parser class instance
    :return: boolean
    """
    return False


# **************************************************************
def connective_sentence(p):
    """
        checks fot it to be a valid connective sentence
    :param p: parser class instance
    :return: boolean
    """
    return False


# **************************************************************
def is_symbol(p):
    """ Checks if p is a proposition or truth symbol
    Will return False if p is not in the range A,B..Z,a..z or is more than
    one symbol

    :param p: the proposition to be checked
    :return: boolean
    """
    return len(p) == 1 and p.isalpha()


# **************************************************************
class Parser:
    """
        A class to handle matching tokens and holding the input
        Initializer gets input
        match matches a passed in token with the recorded input
        get_next gets the next token in the input
    """
    index = 0

    def __init__(self):
        """
            sets up the parser by getting the input
             removes whitespace from the input
        """
        self.the_input = raw_input().strip().replace(' ', '')

    def match(self, token):
        """
            Matches the token to the current part of the input. Increments
            index if successful
        :param token: a string of length 1 that is to be matched
        :return: boolean if match successful
        """
        try:
            if self.the_input[self.index] == token:
                self.index += 1
                return True
        except IndexError:
            print 'Error on checking \'' + token + \
                  '\': the input has been parsed'
            return False
        return False

    def get_next(self):
        """
            fetches the next token in the input
        :return: string of length 1 that is to be matched
        """
        return self.the_input[self.index]


if __name__ == '__main__':
    main()
