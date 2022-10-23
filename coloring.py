
import sys
"""
    Spracovanie txt suboru. Vrati dictionary, kde key je cislo vrcholu a values su jeho farba a susedia.
    Dalej vrati max_n, co je pocet vrcholov grafu.
    @link - cesta k txt suboru
"""
def process_txt(): 
    with open(sys.argv[1], "r") as f:
        pairs = f.read().splitlines()

    max_n = 0
    for i in range(len(pairs)):
        pairs[i] = [int(num) for num in pairs[i].split(' ')] 
        if(max_n < (max(pairs[i]))):
            max_n = max(pairs[i])
    # pairs = [[1, 2] , [1, 6], [4, 1] ...]

    conections = {}
    for i in range(1, max_n+1):
        conections[i] = ['0'] # default farba
        for j in range(len(pairs)):
            if i in pairs[j]:
                conections[i].append([num for num in pairs[j] if num != i].pop()) #pr [1, 2] => 2 
    # conections = {1 : ['0', 2, 3, 6], 2 : ['0', 1, 5, 6] ...}

    return conections, max_n


"""
    Funkcia vrati False, ak je niektory sused zafarbeny danou farbou, inak vrati True
    @neighbors_list - list obsahujuci susedov daneho vrchola
    @conections - zoznam vrcholov, ich farieb a susedov 
    @color - farba, ktorou chceme vrchol zafarbit
"""
def safe_color(neighbors_list, conections, color):
    for neighbor in neighbors_list[1:]:
        if conections[neighbor][0] == color:
            return False
    return True


"""
    Funkcia vrati uz zafarbeny graf. 
    @conections - zoznam prepojeni
    @max_n - pocet vrcholov
"""
def color_graph(conections, max_n):
    for key, neighbors in conections.items():
        for color in range(1,max_n+1):
            if safe_color(neighbors, conections, str(color)):
                conections[key][0] = str(color)
                break
    return conections


def print_graph(graph):
    for key, value in graph.items():
        print(f"{key} {value[0]}")


def main():
    conections, max_n = process_txt()
    graph = color_graph(conections, max_n)
    print_graph(graph)

if __name__ ==  "__main__":
    main()