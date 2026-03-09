class restrrictions:

    regax  = r'[1-9]{4}'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return str(value)
