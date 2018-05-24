init -100 python:
    class Wordpack(renpy.store.object):
        NOUN_INDEX = 0
        ADJ_INDEX = 1
        VERB_INDEX = 2
        OTHER_INDEX = 3

        nouns = []
        adjectives = []
        verbs = []
        other = []

        def __init__(self):
            nouns = []
            adjectives = []
            verbs = []
            other = []
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

        def add_to_size(self, size_tuple, *args):
            num_nouns = size_tuple[NOUN_INDEX]
            num_adjectives = size_tuple[ADJECTIVE_INDEX]
            num_verbs = size_tuple[VERB_INDEX]
            num_other = size_tuple[OTHER_INDEX]

            self.nouns = self.add_words_to_size(NOUN_INDEX, num_nouns, args)
            self.adjectives = self.add_words_to_size(ADJECTIVE_INDEX, num_adjectives, args)
            self.verbs = self.add_words_to_size(VERB_INDEX, num_verbs, args)
            self.other = self.add_words_to_size(OTHER_INDEX, num_other, args)
            return

        def add_words_to_size(self, dest_index, new_size_tuple, *args):
            # If we already have more nouns than we need, randomly select
            # to size
            new_list = []
            new_size = new_size_tuple[dest_index]
            num_wordpacks = len(args)
            get_function = ""
            if (dest_index == NOUN_INDEX):
                new_list = self.nouns
                get_function = "newwords.get_nouns()"
            elif (dest_index == ADJECTIVE_INDEX):
                new_list = self.adjectives
                get_function = "newwords.get_adjectives()"
            elif (dest_index == VERB_INDEX):
                new_list = self.verbs
                get_function = "newwords.get_verbs()"
            elif (dest_index == OTHER_INDEX):
                new_list = self.other
                get_function = "newwords.get_other()"
            else: # TODO: error checking?
                return "dest_index out of range."

            if (len(new_list) >= new_size):
                new_list = random.sample(new_list, new_size)
            else:
                needed_words = new_size - len(new_list)
                words_added = 0
                words_per_pack = needed_words // num_wordpacks
                for newwords in args:
                    new_list += random.sample(eval(get_function), words_per_pack)
                    needed_words -= words_per_pack
                    num_wordpacks -= 1
                    # this will update the words_per_pack so it will work with uneven division
                    words_per_pack = needed_words // num_wordpacks
            return new_list

        def get_nouns(self):
            return self.nouns

        def get_adjectives(self):
            return self.adjectives

        def get_verbs(self):
            return self.verbs

        def get_other(self):
            return self.other
