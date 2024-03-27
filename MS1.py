def czyt(s): 
    gd = {}
    node = {}
    element = []
    BC=[]
    flag = 0
    with open(s) as f:
        for line in f:
            if(flag == 0):
                if line[0] == "*": 
                    flag = flag + 1
                    continue
                (key, val) = line.split()
                gd[str(key)] = int(val)
            elif(flag == 1):
                if line[0] == "*": 
                    flag = flag + 1
                    continue
                line = line.lstrip()
                line = line.replace(",", "")
                (key, a, b) = line.split()
                node[str(key)] = (float(a),float(b))
            elif(flag == 2):
                if line[0] == "*": 
                    flag = flag + 1
                    continue
                line = line.lstrip()
                line = line.replace(",", "")
                line = line.split()
                temp_list = [int(number) for number in line]
                element.append(temp_list)
            elif(flag == 3):
                if line[0] == "*": 
                    flag = flag + 1
                    continue
                line = line.lstrip()
                line = line.replace(",", "")
                line = line.split()
                BC = [int(number) for number in line]
                #BC.append(temp_list)
    return gd, node, element, BC

# gd, node, element, BC = czyt('D:\MS\Test2_4_4_MixGrid.txt')
# print(gd)
# print('\n')
# print(node)
# print('\n')
# print(element)
# print('\n')
# print(BC)
# print('\n')