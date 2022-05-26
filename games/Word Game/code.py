import random
import typing


GAMEWORD_LIST_FNAME = "gamewords.txt"
GUESSWORD_LIST_FNAME = "guesswords.txt"


def filter_word(word: str, length: int) -> str:
    """Filter a word to add it to the wordlist."""
    if len(word.strip()) == length:
        # make sure all the words in our wordlist
        # are stripped of whitespace, and all upper case,
        # for consistency in checking
        return word.strip().upper()
    return None


def create_wordlist(fname: str, length: int) -> typing.List[str]:
    """Load and create a wordlist from a filename."""
    with open(fname, "r") as f:
        lines = f.readlines()
    return list(map(lambda word: filter_word(word, length), lines))


def validate(guess: str, wordlen: int,
             wordlist: typing.Set[str]) -> typing.Tuple[str, str]:
    """
    Validate a guess from a user.

    Return tuple of [None if no error or a string containing
    the error message, the guess].
    """
    # make sure the guess is all upper case
    guess_upper = guess.upper()
    # guesses must be the same as the input word
    if len(guess_upper) != wordlen:
        return f"Guess must be of length {wordlen}", guess_upper

    # guesses must also be words from the word list
    if guess_upper not in wordlist:
        return "Guess must be a valid word", guess_upper
    return None, guess_upper


def get_user_guess(wordlen: int, wordlist: typing.Set[str]) -> str:
    """Get a user guess input, validate, and return the guess."""
    # continue looping until you get a valid guess
    while True:
        guess = input("Guess: ")
        # here we overwrite guess with
        # the filtered guess
        error, guess = validate(guess=guess, wordlen=wordlen,
                                wordlist=wordlist)
        if error is None:
            break

        # show the input error to the user, as appropriate
        print(error)
    return guess


def find_all_char_positions(word: str, char: str) -> typing.List[int]:
    """Given a word and a character, find all the indices of that character."""
    positions = []
    pos = word.find(char)
    while pos != -1:
        positions.append(pos)
        pos = word.find(char, pos + 1)
    return positions


# test cases for find_all_char_positions
# find_all_char_positions("steer", "e") => [2, 3]
# find_all_char_positions("steer", "t") => [1]
# find_all_char_positions("steer", "q") => []


def compare(expected: str, guess: str) -> typing.List[str]:
    """Compare the guess with the expected word and return the output parse."""
    # the output is assumed to be incorrect to start,
    # and as we progress through the checking, update
    # each position in our output list
    output = ["_"] * len(expected)
    counted_pos = set()

    # first we check for correct words in the correct positions
    # and update the output accordingly
    for index, (expected_char, guess_char) in enumerate(zip(expected, guess)):
        if expected_char == guess_char:
            # a correct character in the correct position
            output[index] = "*"
            counted_pos.add(index)

    # now we check for the remaining letters that are in incorrect
    # positions. in this case, we need to make sure that if the
    # character that this is correct for was already
    # counted as a correct character, we do NOT display
    # this in the double case. e.g. if the correct word
    # is "steer" but we guess "stirs", the second "S"
    # should display "_" and not "-", since the "S" where
    # it belongs was already displayed correctly
    # likewise, if the guess word has two letters in incorrect
    # places, only the first letter is displayed as a "-".
    # e.g. if the guess is "floss" but the game word is "steer"
    # then the output should be "_ _ _ - _"; the second "s" in "floss"
    # is not displayed.
    for index, guess_char in enumerate(guess):
        # if the guessed character is in the correct word,
        # we need to check the other conditions. the easiest
        # one is that if we have not already guessed that
        # letter in the correct place. if we have, don't
        # double-count
        if guess_char in expected and \
                output[index] != "*":
            # first, what are all the positions the guessed
            # character is present in
            positions = find_all_char_positions(word=expected, char=guess_char)
            # have we accounted for all the positions
            for pos in positions:
                # if we have not accounted for the correct
                # position of this letter yet
                if pos not in counted_pos:
                    output[index] = "-"
                    counted_pos.add(pos)
                    # we only count the "correct letter" once,
                    # so we break out of the "for pos in positions" loop
                    break
    # return the list of parses
    return output


# test cases for comparing
# compare("steer", "stirs") -> "* * _ - _"
# compare("steer", "floss") -> "_ _ _ - _"
# compare("pains", "stirs") -> "_ _ * _ *"
# compare("creep", "enter") -> "- _ _ * -"
# compare("crape", "enter") -> "- _ _ _ -"
# compare("ennui", "enter") -> "* * _ _ _"


if __name__ == '__main__':
    # the game word is 5 letters
    WORDLEN = 5
    # load the wordlist that we will select words from
    # for the wordle game
    GAMEWORD_WORDLIST = create_wordlist(
        GAMEWORD_LIST_FNAME, length=WORDLEN)

    # load the wordlist for the guesses
    # this needs to be a set, since we pass this into the get_user_guess()
    # function which expects a set
    GUESSWORD_WORDLIST = set(create_wordlist(
        GUESSWORD_LIST_FNAME, length=WORDLEN))

    # select a random word to start with
    WORD = random.choice(GAMEWORD_WORDLIST)
    GAME_WORD_LENGTH = len(WORD)

    # keep track of some game state
    NUM_GUESSES = 0

    # print the game instructions to the user
    print("""
Guess words one at a time to guess the game word.

A * character means a letter was guessed correctly
in the correct position.
A - character means a letter was guessed correctly,
but in the incorrect position.

To quit, press CTRL-C.
""")

    # start of the user name interaction
    print("_ " * GAME_WORD_LENGTH)

    # we use a continuous loop, since there could be a number
    # of different exit conditions from the game if we want
    # to spruce it up.
    try:
        while True:
            # get the user to guess something
            GUESS = get_user_guess(
                wordlen=GAME_WORD_LENGTH, wordlist=GUESSWORD_WORDLIST)
            NUM_GUESSES += 1

            # display the guess when compared against the game word
            result = compare(expected=WORD, guess=GUESS)
            print(" ".join(result))

            if WORD == GUESS:
                print(f"You won! It took you {NUM_GUESSES} guesses.")
                break
    except KeyboardInterrupt:
        print(f"""
You quit - the correct answer was {WORD.upper()}
and you took {NUM_GUESSES} guesses
""")
