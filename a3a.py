# This class demonstrate the working of Minheap using list
# It also implements the down top and top down heapify operations

class MinHeap:
    def __init__(self, arr=[]):
        self.minheap = arr

    def insert(self, element):
        """
        This method insert the element in the minheap using down-top heapify operation
        :param element: item to be inserted in min heap

        """
        self.minheap.append(element)  # add element at the end of the min heap
        curpos = len(self.minheap) - 1  # count the total elements in the min heap
        while curpos > 0:  # continue up the newly inserted element until it reaches to top or appropriate position
            parentnode = (curpos - 1) // 2  # get the parent location
            if self.minheap[parentnode] < element:  # if parent already satisfies the min heap property
                break

            if self.minheap[parentnode] >= self.minheap[curpos]:  # if parent has greater value than it child
                # make child as parent by moving to up and parent as child by moving down
                temp = self.minheap[parentnode]
                self.minheap[parentnode] = self.minheap[curpos]
                self.minheap[curpos] = temp
                curpos = parentnode

    def get_min(self):
        return self.minheap[0]

    def extract_min(self):
        """
        This method delete the top most value in the min heap which has the minimum value
        and then adjust the heap using top to down heapify operation
        :return: Minimum value in the heap
        """
        if not self.is_empty():
            # if heap is not empty then delete the min value and
            # move the last value to the top
            lastindex = len(self.minheap) - 1
            minval = self.minheap[0]
            temp = self.minheap.pop(lastindex)
            if self.is_empty():
                return minval
            else:
                self.minheap[0] = temp
            parent = 0
            end = len(self.minheap) - 1
            # top to down heapify process until top value reaches to it appropriate position
            while parent <= (end - 1) // 2:
                leftchild = parent * 2 + 1  # calculate the left child position
                rightchild = parent * 2 + 2  # calculate the right child position
                # if parent value is more than both of its child
                # then find the child with min value and swap that child and parent
                if leftchild <= end and rightchild <= end and self.minheap[parent] > self.minheap[leftchild] and \
                        self.minheap[parent] > self.minheap[rightchild]:
                    if self.minheap[leftchild] < self.minheap[rightchild]:
                        min = self.minheap[leftchild]
                        index = leftchild
                    else:
                        min = self.minheap[rightchild]
                        index = rightchild
                    self.minheap[index] = self.minheap[parent]
                    self.minheap[parent] = min
                    parent = index
                # if left child has min value than it parent then swap parent and left child
                elif leftchild <= end and self.minheap[parent] > self.minheap[leftchild]:
                    element = self.minheap[parent]
                    self.minheap[parent] = self.minheap[leftchild]
                    self.minheap[leftchild] = element
                    parent = leftchild
                # if right child has min value than it parent then swap parent and right child
                elif rightchild <= end and self.minheap[parent] > self.minheap[rightchild]:
                    element = self.minheap[parent]
                    self.minheap[parent] = self.minheap[rightchild]
                    self.minheap[rightchild] = element
                    parent = rightchild
                else:
                    break

            return minval

        else:
            return None

    def is_empty(self):
        if len(self) == 0:
            return True
        return False

    def __len__(self):
        if len(self.minheap) == 0:
            tnode = 0
        else:
            tnode = len(self.minheap)
        return tnode

    # Following code checks the working of min heap and not the part of Part A solution

    def disp(self):
        print(self.minheap)


'''
minheap = MinHeap()
print(minheap.is_empty())
minheap.insert(10)
minheap.insert(8)
minheap.insert(20)
minheap.insert(5)
minheap.insert(6)
minheap.insert(17)
minheap.insert(13)
minheap.insert(2)
minheap.disp()
print(minheap.get_min())
print(len(minheap))
print("Removal")
print(minheap.extract_min())
minheap.disp()
print(minheap.get_min())
print(len(minheap))

while not minheap.is_empty():
    minheap.extract_min()

print(len(minheap))
'''
