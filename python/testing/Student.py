class testStudentDS:
    def __init__(self):
        self.data = []
        self.count = 0
    
    def insert(self,name,marks):
        student = (name,marks)
        self.data.append(student)

    def quickSort(self):
        self._quickSort_(0,len(self.data)-1)
        print(self.data)
    
    def _quickSort_(self,start,end):
        if start<end:
            mid = self._partition_(start,end)
            self._quickSort_(start,mid-1)
            self._quickSort_(mid+1,end)

    
    def get_all(self):
        for i in self.data:
            print(i[1])

    
    def _partition_(self,start,end):
        piv = self.data[start]
        low = start+1
        high = end
        while True:
            if low<=high and piv[1]>self.data[low][1]:
                low+=1
            if low<=high and piv[1]<self.data[high][1]:
                high-=1
            if low<=high:
                self.data[high],self.data[low] = self.data[low],self.data[high]
            else:
                break

        self.data[high],self.data[start] = self.data[start],self.data[high]
        return high
        