from typing import Optional


class Node:
    """
    Provide necessary documentation
    """
    def __init__(self, data=None, next=None):
        """
        Provide necessary documentation
        """
        self.data = data
        self.next = next


class LinkedList:
    """
    Provide necessary documentation
    """
    def __init__(self):
        """
        Initialize the head
        """
        self.head = None

    def insert_at_end(self, data):
        """
        Insert node at end of the list
        :param data: integer data that will be used to create a node
        """
        # Write code here
        """
        Insert node at end of the list
        :param data: integer data that will be used to create a node
        """
        newNode = Node(data)
        if (self.head):
            current = self.head
            while (current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode        

    def status(self):
        """
        It prints all the elements of list.
        """
        # write code here
        current = self.head
        status_of_linked_list = []
        while (current):
            status_of_linked_list.append(current.data)
            current = current.next
        print(status_of_linked_list)
        

class Solution:
    """
    Provide necessary documentation
    """
    def addTwoNumbers(self, first_list: Optional[LinkedList], second_list: Optional[LinkedList]) -> Optional[LinkedList]:
        """
        :param first_list: Linkedlist with non-negative integers
        :param second_list: Linkedlist with non-negative integers
        :return: returns the sum as a linked list
        """
        # Write code here
        data1 = ''
        data2 = ''
        temp1 = first_list.head
        temp2 = second_list.head
        while temp1.next is not None:
            data1 = str(temp1.data) + data1
            temp1 = temp1.next
        data1 = str(temp1.data) + data1
        while temp2.next is not None:
            data2 = str(temp2.data) + data2
            temp2 = temp2.next
        data2 = str(temp2.data) + data2
        sum = int(data1) + int(data2)
        result = list(map(int, list(str(sum)[::-1])))
        new_list = LinkedList()
        for i in result:
            new_list.insert_at_end(i)
        return new_list        
        

# Do not edit the following code      
# Create an instance for LinkedList
first_list = LinkedList()
# Create an another instance for LinkedList
second_list = LinkedList()
# Read data for first list
data_for_first_list = list(map(int, input().strip().split(" ")))
# Add data at the end of first_list
for data in data_for_first_list:
    first_list.insert_at_end(data)
# Read data for second list
data_for_second_list = list(map(int, input().strip().split(" ")))
# Add data at the end of second_list
for data in data_for_second_list:
    second_list.insert_at_end(data)
# Create an instance for Solution
solution = Solution()
# Pass first_list and second_list to addTwoNumbers, which returns a new linked list
new_list = solution.addTwoNumbers(first_list, second_list)
# Display the status of new_list
new_list.status()
