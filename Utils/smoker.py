class Smoker:
    @staticmethod
    def encode(smoker):
        if smoker == 'no':
            return 0
        else:
            return 1

    @staticmethod
    def decode(smoker):
        if smoker == 0:
            return 'no'
        else:
            return 'yes'
