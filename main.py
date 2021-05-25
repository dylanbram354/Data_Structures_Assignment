from sweepstakes import Sweepstakes
from linkedlist import LinkedList
from binary_search_tree import Binary_Search_Tree

if __name__ == '__main__':
    # Question 1

    # 1a (tuple)
    # months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
    #           'November', 'December')
    # print(months[2])

    # 1b (set)
    # birthday_locations = {'Columbus', 'New York', 'Hawaii'}
    # birthday_locations.add('Milwaukee')
    # birthday_locations.add('Boise')
    # birthday_locations.add('Portland')
    # for place in birthday_locations:
    #     print(place)

    # 1c
    # sweepstakes = Sweepstakes()
    # sweepstakes.pick_winner()

    # Question 2

    # def family_member(first, last, relation):
    #     person = {'First name': first, 'Last name': last, 'Relation': relation}
    #     return person
    #
    # my_family = [family_member('Lori', 'Bram', 'Mother'), family_member('Lenny', 'Bram', 'Father'),
    #              family_member('Sara', 'Chapman', 'Sister')]
    # print(my_family)

    # Question 3

    # linkedlist = LinkedList()
    #
    # linkedlist.append_node(60)
    # linkedlist.append_node(55)
    # linkedlist.append_node(65)
    # linkedlist.add_to_beginning(50)
    #
    # print(linkedlist.contains_node(65))

    # Question 4

    tree = Binary_Search_Tree()

    tree.insert_node(10)
    tree.insert_node(15)
    tree.insert_node(5)
    tree.insert_node(11)
    tree.insert_node(45)
    tree.insert_node(4)
    tree.insert_node(8)
    tree.insert_node(9)
    tree.insert_node(7)
    tree.insert_node(2)
    tree.in_order_traversal(tree.root)
    # print(tree.search_for_node(12))

    # Bonus 1










