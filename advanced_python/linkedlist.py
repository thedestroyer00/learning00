# Creating a linklist and UPdating and updating it
class Node:
    def __init__(self, element = None):
        self.element = element
        self.nextelement = None
        
class Linklist:
    def __init(self, headelement):
        self.headelement = headelement
        
    def printlist(self):
        printelement = self.headelement
        while printelement is not None:
            print(printelement.element)
            printelement = printelement.nextelement
            
    def delete_element(self, ele):
        del_element = self.headelement.nextelement
        pre_element = self.headelement
        check = 0
        if self.headelement.element == ele:
            self.headelement = self.headelement.nextelement
            print(f"Now your new head element is {self.headelement.element} ")
            check = 1
            return
        else:
            while del_element is not None:
                if del_element.element == ele:
                    pre_element.nextelement = del_element.nextelement
                    check = 1
                    return
                else: 
                    del_element = del_element.nextelement
                    pre_element = pre_element.nextelement
                    
        if check == 0:
            print("The entered element doesn't exists in the linked list...")
                   
    def insert_element(self,position, new_element):
        self.position = position
        last_element = self.headelement
        if self.position == 'h':
            self.headelement = new_element
            self.headelement.nextelement = last_element
        if position == 'l':
            while(last_element.nextelement):
                last_element = last_element.nextelement
            last_element.nextelement = new_element
                          
linklist = Linklist()
linklist.headelement = Node(5)

e2 = Node(10)
e3 = Node(15)
e4 = Node(20)
e5 = Node(25)
e6 = Node(30)
e7 = Node(35)
e8 = Node(40)

linklist.headelement.nextelement = e2
e2.nextelement = e3
e3.nextelement = e4
e4.nextelement = e5
e5.nextelement = e6
e6.nextelement = e7
e7.nextelement = e8

linklist.printlist()
linklist.insert_element('l',Node(45))
print()
linklist.printlist()
