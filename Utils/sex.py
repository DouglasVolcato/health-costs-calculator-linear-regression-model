class Sex:
    @staticmethod
    def encode(sex):
        if sex == 'female':
            return 0
        else:
            return 1

    @staticmethod
    def decode(sex):
        if sex == 0:
            return 'female'
        else:
            return 'male'
