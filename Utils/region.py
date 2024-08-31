class Region:
    @staticmethod
    def encode(region):
        if region == 'southwest':
            return 0
        elif region == 'southeast':
            return 1
        elif region == 'northwest':
            return 2
        elif region == 'northeast':
            return 3
        
    @staticmethod
    def decode(region):
        if region == 0:
            return 'southwest'
        elif region == 1:
            return 'southeast'
        elif region == 2:
            return 'northwest'
        elif region == 3:
            return 'northeast'