class SortMethords:
    def __init__(self,data):
        self.data = data
        self.length = len(self.data)
    
    def swap(self,i,j):
        self.data[i],self.data[j] = self.data[j],self.data[i]

    def BubleSort(self):
        for i in range(self.length):
            for j in range(self.length-i-1):
                if self.data[j]>self.data[j+1]:
                    self.swap(j,j+1)
        print(self.data)
    
    def SelectionSort(self):
        for i in range(self.length):
            pos = i
            for j in range(i+1,self.length):
                if self.data[pos]>self.data[j]:
                    pos = j
            self.swap(pos,i)
        print(self.data)

    def insertionSort(self):
        for i in range(1,self.length):
            key = self.data[i]
            j = i-1
            while j>=0 and key<self.data[j]:
                self.data[j+1] = self.data[j]
                j-=1
            self.data[j+1]=key
        print(self.data)

    def QuickSort(self):
        self._quicksort_(0, self.length - 1)
        print(self.data)

    def _quicksort_(self, start, end):
        if start < end:
            mid = self._partition_(start, end)
            self._quicksort_(start, mid - 1)
            self._quicksort_(mid + 1, end)

    def _partition_(self, start, end):
        pivot = self.data[start]
        low = start + 1
        high = end

        while True:
            while low <= high and self.data[low] <= pivot:
                low += 1

            while low <= high and self.data[high] > pivot:
                high -= 1

            if low <= high:
                self.data[low], self.data[high] = self.data[high], self.data[low]
            else:
                break

        self.data[start], self.data[high] = self.data[high], self.data[start]

        return high
 
    def merge_sort(self,arr):

        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])

        return self.merge(left, right)

    def merge(self, left, right):
        
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def heapify(self, n, i):
        largest = i
        left = 2*i + 1
        right = 2*i + 2
        
        if left < n and self.data[left] > self.data[largest]:
            largest = left
        
        if right < n and self.data[right] > self.data[largest]:
            largest = right
        
        if largest != i:
            self.data[i], self.data[largest] = self.data[largest], self.data[i]
            self.heapify(self.data, n, largest)

    def heap_sort(self):
        n = len(self.data)
            
        for i in range(n//2 - 1, -1, -1):
            self.heapify(self.data, n, i)
            
        for i in range(n-1, 0, -1):
            self.data[i], self.data[0] = self.data[0], self.data[i]  
            self.heapify(self.data, i, 0)