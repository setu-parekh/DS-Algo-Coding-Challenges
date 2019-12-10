class Node:
    def __init__(self, val):
        # Value associated to every node.
        # Imagine this as creating a Car object with default color, which you want to set when you create the Car object.
        self.val = val

        # Pointer to point to next node. By default it is None
        self.next = None


if __name__ == '__main__':
    # Similar to car1 = Car('Pink') if we have a Car class. Remember, we had discussed it recently.
    node1 = Node(10)

    # Note: at this point, when we create a Node object (named node1), it's next is set to None
    print(node1.next) # This should be None

    # Similarly we create two more nodes
    node2 = Node(20)
    node3 = Node(30)


    # As of now, all the three nodes above are just separate nodes. Not linked with each other.
    # Now, we will set their link

    node1.next = node2
    node2.next = node3

    # So, now, the three nodes are set as this: node1 ---> node2 ----> node3
    # node3's next still points to None
    # node1 ---> node2 ---> node3 ---> None

    print(node1.next) # This will print the object of node2
    print(node1.next.val) # This will print the value of node2 (because, node1.next == node2). And then, we do node2.val (which is 20)

    print(node2.next) # This will print the object of node3
    print(node2.next.val) # This will print the value of node3 (because, node2.next == node3). And then, we do node3.val (which is 30)

    # The above linking has essentially created a LL. Where first node is 'node1' with value 10, second node is 'node2' with value 20 and last node is 'node3' with value 30

    # Now we can also use a for loop to print all three values.
    # Note: the head of the LL is basically the first node of the list. This 'head' is nothing but a variable and we assign 'node1' to it.
    #       this way, head will point to node1 (start of the LL). Sometimes we also use variable name 'current' in place of 'head'

    # After that, we iterate through the LL using next pointer, just like how we iterate normal list.
    # But until how long can we keep iterating? Until the 'head' or 'current' is pointing to a node.

    # This way, we will start iterating from first node
    current = node1

    # This way, the while loop will only run until current has some value and is not None.
    # Note: current will always have a Node object as its value.
    # Just like on line 49 above, current is initialized with node1 (which is an object of Node class).
    while current:
        # Here, the value of 'current' will be node1 in first iteration.
        # If you directly try to print 'current', that will print something like <__main__.Node object at 0x100955ed0>
        # If you want to see the 'val' property, you can print current.val (which in first iteration will be 10)

        print('Iteration - Value of node object in iteration-1 is: {}'.format(current.val))

        # Currently, this is the situation
        #     current
        #        |
        #        |
        #     node1 (10) -----> node2 (20) -----> node3 (30) ------> None

        # Now, before going to the next iteration of while loop, we need to move the current pointer forward.
        # How can we do that? Remember that node1's next pointer can be reached via 'node1.next' - 'next' is basically a property of Node class.
        # For object node1, we have assigned node1.next = node2

        current = current.next

        # In the line above, current was referring to node1, so current.next will be node2, and we will simply assign that back to variable 'current' itself
        # Something like i = i + 1

        # Currently, this is the situation
        #                       current
        #                         |
        #                         |
        #     node1 (10) -----> node2 (20) -----> node3 (30) ------> None

        # So, now, the while loop will execute again because node2 is not None.
        # Similar process will happen and current = current.next this time will be equal to current = node2.next which is nothing but current = node3


        # Currently, this is the situation
        #                                        current
        #                                          |
        #                                          |
        #     node1 (10) -----> node2 (20) -----> node3 (30) ------> None
        # Again, while loop will execute because current is not None

        # However, during the iteration when current = node3, and line 71 executes, what will happen?
        # Note that node3.next = None (because it is the last node of LL)

        # Hence during execution of line 71 for current = node3:
        #     current = current.next ==> current = node3.next ==> current = None

        # Currently, this is the situation
        #                                                           current
        #                                                             |
        #                                                             |
        #     node1 (10) -----> node2 (20) -----> node3 (30) ------> None

        # So, now when while loop will come again, the value of current will be None.
        # Hence condition while current: will be false
        # So it will no longer go into the while loop, and it will end.
