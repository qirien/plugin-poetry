# This file contains possible wordpacks that Plugin Poetry can use.

init python:
    # Basic words that you probably want on every board.
    basic_nouns = ["word", "you", "she", "joy", "I", "we",  "scent", "sound", "me", "pain", "wonder", "dream", "moon", "sun", "us"]
    basic_adjectives = ["beautiful", "blue", "gray", "red", "soft", "feathery",  "pink", "your", "my", "our", "orange", "this", "brown", "dry", "her"]
    basic_verbs = ["jump", "know", "smile", "dance", "sing", "kick", "glow", "is", "are", "eat", "trust", "am"]
    basic_other = ["in", "on", "after", "before", "for", "of", "and", "the", "-ing", "-ly", "!", "?", "-s", "every", "from", "around", "between", "-y", "a", "no", "where", "when", "to", "-ness"]
    basic_words = Wordpack()
    basic_words.add_words(basic_nouns, basic_adjectives, basic_verbs, basic_other)

    # Family-related words
    family_nouns = ["hair", "family", "face", "father", "mother", "soul", "eye", "daughter", "son", "girl"]
    family_adjectives = ["young", "gentle", "old", "rosy", "happy", "personal", "bright", "clever", "jealous", "sweet"]
    family_verbs = ["touch", "feel", "grow", "build", "adore", "love", "nurture", "thank", "help", "frown", "sleep", "pout"]
    family_other = ["forever", "together"]
    family_words = Wordpack()
    family_words.add_words(family_nouns, family_adjectives, family_verbs, family_other)

    # Baby-related words
    baby_nouns = ["blanket", "nose", "toe", "milk", "baby", "hand", "fist", "mouth", "belly button", "blood", "diaper", "scent", "smile", "toy", "cheek"]
    baby_adjectives = ["tiny", "cute", "tender", "tight", "precious", "chubby", "stinky", "fragile"]
    baby_verbs = ["cry", "hold", "babble", "cuddle", "yawn", "nap", "crawl", "whisper", "wail"]
    baby_other = ["oh"]
    baby_words = Wordpack()
    baby_words.add_words(baby_nouns, baby_adjectives, baby_verbs, baby_other)

    # Romance related words
    romance_nouns = ["body", "lips", "soul", "eyes", "legs", "hair", "scent", "baby", "honey", "marriage", "you", "skin", "chocolate", "wine", "sunset", "two", "smile", "heart", "lover", "friend"]
    romance_adjectives = ["smooth", "graceful", "sexy", "sweaty", "hot", "tender", "sparkly", "romantic", "my", "sweet", "crimson", "lonely", "awesome", "fabulous", "gorgeous", "beautiful", "best", "one"]
    romance_verbs = ["sigh", "nibble", "caress", "kiss", "embrace", "taste", "soar", "dance", "entangle", "devour", "drink", "flutter", "hold", "murmur", "whisper"]
    romance_other = ["oh", "together", "with", "alone", "just", "always", "yes"]
    romance_words = Wordpack()
    romance_words.add_words(romance_nouns, romance_adjectives, romance_verbs, romance_other)

    # Farm-related words
    farm_nouns = ["breakfast", "sunrise", "plant", "flower", "seed", "fire", "light", "water", "earth", "air", "planet", "space", "fruit", "harvest", "grass", "dirt", "sky", "sunset", "moon", "weed", "pest", "goat", "soil"]
    farm_adjectives = ["simple", "slow", "green", "sharp", "alive", "dead", "brittle"]
    farm_verbs = ["soar", "grow", "build", "help", "cut", "wrench", "dig", "glisten"]
    farm_other = ["yum", "ugh"]
    farm_words = Wordpack()
    farm_words.add_words(farm_nouns, farm_adjectives, farm_verbs, farm_other)

    # Separation/death related words
    separation_nouns = ["distance", "gulf", "chasm", "ocean", "river", "fence", "wall", "mist", "haze", "vision", "death", "loss", "soul", "heaven", "void", "life"]
    separation_adjectives = ["dark", "alone", "far", "lonely", "empty", "sad", "melancholy", "hollow", "lost", "found", "vast", "unknown", "strange"]
    separation_verbs = ["miss", "exist", "travel", "depress", "find", "search", "lose", "shrink", "seek", "die", "live"]
    separation_other = ["oh", "without", "however", "but", "still", "with", "together"]
    separation_words = Wordpack()
    separation_words.add_words(separation_nouns, separation_adjectives, separation_verbs, separation_other)

    # Space-related words
    space_nouns = ["star", "flare", "rock", "planet", "crabird", "wolf slug", "turtle snail", "colony", "liaison", "geyser", "jellystar", "jellysquid", "lightspeed", "nebula", "cave", "accident", "tentacle", "space"]
    space_adjectives = ["hot", "binary", "trinary", "alien", "solar", "terrestrial", "celestial", "distant", "rainy", "wet", "jiggly", "purple"]
    space_verbs = ["revolve", "blaze", "steam", "radiate", "work", "mine", "explode", "dig", "murder", "glow", "tingle"]
    space_other = ["huh", "but", "together"]
    space_words = Wordpack()
    space_words.add_words(space_nouns, space_adjectives, space_verbs, space_other)

    # Activism words
    activism_nouns = ["color", "speech", "law", "police", "government", "job", "silence", "humanity", "we", "voice", "speech", "hero", "martyr", "effect", "reform", "justice", "mercy", "culture", "liberty", "yourself", "you", "me", "I", "tax", "amendment", "neighbor", "duty", "now", "experience", "dream", "protest", "city"]
    activism_adjectives = ["black", "brown", "white", "free", "equal", "strong", "different", "same", "one", "dead", "alive", "collective", "social", "right", "moral", "civil", "perfect", "my", "your", "our", "patriotic", "blind", "done", "ready", "able", "separate", "broken", "new", "strong"]
    activism_verbs = ["matter", "live", "imagine", "speak", "shout", "work", "pray", "see", "hear", "understand", "unite", "divide", "champion", "change", "advocate", "march", "educate", "love", "is", "are", "enforce", "promote", "must", "need", "want", "stop", "demonstrate"]
    activism_other=["to", "-s", "of", "together", "-d", "never", "always", "as", "and", "?", "!", "but", "in", "when", "-ing", "with"]
    activism_words = Wordpack()
    activism_words.add_words(activism_nouns, activism_adjectives, activism_verbs, activism_other)

