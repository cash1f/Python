class tupledict(dict):
    def __contains__(self, key):
        if super(tupledict, self).__contains__(key):
            return True
        return any(key in k for k in self)
    #find_key_value_pair(None, 5, {'this is a': 'bonus case'}))