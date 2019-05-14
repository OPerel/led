class Columns():
    ''' create a 2D array of columns '''
    def __init__(self, lis, slice_len):
        self.lis = lis
        self.slice_len = slice_len

    # slice the list into n sized chuncks
    def s_list(self):
        for i in range(0, len(self.lis), self.slice_len):
            yield self.lis[i:i + self.slice_len]

    # create columns sublists
    def columns(self):
        return list(zip(*self.s_list()))
