class Columns():
    ''' create a 2D array of columns '''
    def __init__(self, lis, slice_len):
        self.lis = lis
        self.slice_len = slice_len

    def s_list(self):
        ''' slice the list into n sized chuncks '''
        for i in range(0, len(self.lis), self.slice_len):
            yield self.lis[i:i + self.slice_len]

    def columns(self):
        ''' create columns sublists '''
        return list(zip(*self.s_list()))
