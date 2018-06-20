init -100 python:
    class Wordpack(renpy.store.object):
        NOUN_INDEX = 0
        ADJECTIVE_INDEX = 1
        VERB_INDEX = 2
        OTHER_INDEX = 3

        nouns = []
        adjectives = []
        verbs = []
        other = []

        def __init__(self, wordpack = None):
            if (wordpack == None):
                nouns = []
                adjectives = []
                verbs = []
                other = []
            else:
                nouns = list(wordpack.get_nouns())
                adjectives = list(wordpack.get_adjectives())
                verbs = list(wordpack.get_verbs())
                other = list(wordpack.get_other())
            return

        def add_words(self, nouns, adjectives, verbs, other):
            self.nouns = list(nouns)
            self.adjectives = list(adjectives)
            self.verbs = list(verbs)
            self.other = list(other)
            return

        # Add all the words from all the wordpacks in args to this wordpack
        def add_wordpacks(self, *args):
            for newwords in args:
                self.nouns       += newwords.get_nouns()
                self.adjectives  += newwords.get_adjectives()
                self.verbs       += newwords.get_verbs()
                self.other       += newwords.get_other()
            return

        def trim_to_size(self, size_tuple):
            import random
            self.nouns = random.sample(self.nouns, size_tuple[Wordpack.NOUN_INDEX])
            self.adjectives = random.sample(self.adjectives, size_tuple[Wordpack.ADJECTIVE_INDEX])
            self.verbs = random.sample(self.verbs, size_tuple[Wordpack.VERB_INDEX])
            self.other = random.sample(self.other, size_tuple[Wordpack.OTHER_INDEX])

            self.nouns.sort()
            self.adjectives.sort()
            self.verbs.sort()
            self.other.sort()

            return

        # def add_to_size(self, size_tuple, *args):
        #     import random
        #     num_nouns = size_tuple[Wordpack.NOUN_INDEX]
        #     num_adjectives = size_tuple[Wordpack.ADJECTIVE_INDEX]
        #     num_verbs = size_tuple[Wordpack.VERB_INDEX]
        #     num_other = size_tuple[Wordpack.OTHER_INDEX]
        #
        #     new_list = []
        #     newwords = []
        #     num_wordpacks = len(args)
        #
        #     self.nouns = add_words_to_size(self.nouns, num_nouns, args.nouns) # can't actually do args.nouns
        #     self.adjectives = self.add_words_to_size(Wordpack.ADJECTIVE_INDEX, num_adjectives, args)
        #     self.verbs = self.add_words_to_size(Wordpack.VERB_INDEX, num_verbs, args)
        #     self.other = self.add_words_to_size(Wordpack.OTHER_INDEX, num_other, args)
        #
        #
        #
        #
        # # Given a list of words, add evenly selected words from the word lists in args until it gets to a certain size.
        # def add_words_to_size(new_list, new_size, *args):
        #     # If we already have more words than we need, randomly select
        #     # to size and return
        #     if (len(new_list) >= new_size):
        #         return random.sample(new_list, new_size)
        #     # Otherwise, add from each wordlist given until we don't need any more words.
        #     else:
        #         needed_words = new_size - len(new_list)
        #         words_added = 0
        #         words_per_pack = needed_words // num_wordpacks
        #         for newwords in args:
        #             new_list += random.sample(newwords, words_per_pack)
        #             needed_words -= words_per_pack
        #             num_wordpacks -= 1
        #             # this will update the words_per_pack so it will work with uneven division
        #             words_per_pack = needed_words // num_wordpacks
        #     return new_list

        def get_nouns(self):
            return self.nouns

        def get_adjectives(self):
            return self.adjectives

        def get_verbs(self):
            return self.verbs

        def get_other(self):
            return self.other