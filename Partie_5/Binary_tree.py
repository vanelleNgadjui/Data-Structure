#  Arbre binaire de recherche
# fonction qui construit un arbre binaire de recherche à partir de cette liste, et qui retourne la valeur minimale trouvée dans l'arbre. 

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def construct_bst(arr):
    if not arr:
        return None
    
    root = Node(arr[0])
    
    for i in range(1, len(arr)):
        curr = root
        while True:
            if arr[i] < curr.val:
                if curr.left is None:
                    curr.left = Node(arr[i])
                    break
                else:
                    curr = curr.left
            else:
                if curr.right is None:
                    curr.right = Node(arr[i])
                    break
                else:
                    curr = curr.right
                    
    return find_min_value(root)

def find_min_value(root):
    curr = root
    while curr.left:
        curr = curr.left
    return curr.val

# Exemple d'utilisation de la fonction
arr = [5, 3, 7, 2, 4, 6, 8, 1, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
min_val = construct_bst(arr)
print(min_val)
