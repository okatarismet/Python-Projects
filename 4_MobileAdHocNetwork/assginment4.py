#
#
# completed
import sys
import math
command_txt_sys = "commands"
command_text = open(command_txt_sys, "r")
num_command_text = sum(1 for line in open(command_txt_sys))
Packet_size = int(sys.argv[1])
command_list = []
seconds = 0
just_seconds = 0
packet_number = 1
hersey_degistiren_bool = 0
REMAINING_DATA_SIZE = 0
minutes = 0
ROUTES = {}
hours = 0
at = 0
total_cost = 0
cost_partial = 0
cost_list = []
line_number = 0
new = 0
number_of_packets = 0
total_size = 1.0
battery_of_node = {}
initial_node = ""
final_node = ""
range_of_node = []
a,routes  = [],[]
big_routes  = []
route_counter = 0
at,cost,emergency = 0,0,0
nodes_neighbours_string = ""
kapsanan_area = {}
remotable_nodes = []
cordinates = {}
nodes_neighbours = {}
ROUTES = []


def CRNODE(name_of_node, kordinates, range_of_node, battery):
    cordinates.setdefault(name_of_node, kordinates)
    kapsanan_area.setdefault(name_of_node, range_of_node)
    battery_of_node.setdefault(name_of_node, int(battery))
    print("\tCOMMAND *CRNODE*: New node " + name_of_node + " is created")
def MOVE(name_of_node, kordinates):
    del cordinates[name_of_node]
    cordinates.update({name_of_node: kordinates})
    print("\tCOMMAND *MOVE*: The location of " + name_of_node + " is changed")
def CHBTTRY(name_of_node, battery):
    battery_of_node.update({name_of_node: int(battery)})
    print("\tCOMMAND *CHBTTRY*: Battery level of node " + name_of_node + " is changed to " + battery)
def RMNODE(name_of_node):
    del cordinates[name_of_node]
    del kapsanan_area[name_of_node]
    del battery_of_node[name_of_node]
    print("\tCOMMAND *RMNODE*: Node " + name_of_node + " is removed")
def SEND(initial_node_v, final_node_v, total_size1):
    print("\tCOMMAND *SEND*: Data is ready to send from " + initial_node_v + " to " + final_node_v)
    global total_size,initial_node,final_node
    initial_node = initial_node_v
    final_node = final_node_v
    total_size = total_size1
    number_of_packets = float(total_size) / float(Packet_size)
def COST(first_node,last_node):
    global cost_partial
    at = math.sqrt(int(math.fabs(cordinates[first_node][0] - cordinates[last_node][0])) ** 2 + int(math.fabs(cordinates[first_node][1] - cordinates[last_node][1])) ** 2)
    return at/battery_of_node[last_node]
def ROUTE_FINDER(name_of_node):
    global  route_counter
    global total_cost
    if nodes_neighbours[name_of_node] in routes: # herhalde sikinti burada
        nodes_neighbours[name_of_node]
    routes.append(name_of_node)
    if final_node in routes or nodes_neighbours[name_of_node] == None:
        big_routes.append(" -> ".join(routes))
        route_counter +=1
        cost_list.append("%.4f" % total_cost)
        total_cost -= COST(routes[-2], routes[-1])
        del routes[-1]
        return a.append(routes[-1])
    if len(nodes_neighbours[name_of_node]) > 1:
        for i in nodes_neighbours[name_of_node]:
            if i not in routes:
                total_cost += COST(name_of_node,i)
                ROUTE_FINDER(i)
    if len(nodes_neighbours[name_of_node]) == 1:
        if nodes_neighbours[name_of_node] not in routes:
            total_cost += COST(name_of_node, nodes_neighbours[name_of_node][0])
            ROUTE_FINDER(nodes_neighbours[name_of_node][0])
    if len(nodes_neighbours[name_of_node]) == 0:
        total_cost -= COST(routes[-2], routes[-1])
        del routes[-1]
        return a.append(routes[-1])
    else:
        if len(routes)<2:
            return 0
        else:
            total_cost -= COST(routes[-2], routes[-1])
            del routes[-1]
def NODES_NEIGHBOURS(name_of_node):
    global range_of_node
    global remotable_nodes
    range_of_node.append(cordinates[name_of_node][0] + kapsanan_area[name_of_node][0])
    range_of_node.append(cordinates[name_of_node][0] - kapsanan_area[name_of_node][1])
    range_of_node.append(cordinates[name_of_node][1] + kapsanan_area[name_of_node][2])
    range_of_node.append(cordinates[name_of_node][1] - kapsanan_area[name_of_node][3])
    for i in cordinates.keys():
        if cordinates[i][0] <= range_of_node[0] and cordinates[i][0] >= range_of_node[1] and cordinates[i][1] <= range_of_node[2] and cordinates[i][1] >= range_of_node[3]:
            if i != name_of_node:
                remotable_nodes.append(i)

    nodes_neighbours.setdefault(name_of_node, remotable_nodes)
    range_of_node = []
    remotable_nodes = []
def DECIMAL_INTEGER(original):
    number = str(original)
    if original < 10:
        number = "0" + number
    return number
    number = ""
def main():
    global command_list
    global nodes_neighbours_string
    global hersey_degistiren_bool
    global line_number
    global new
    hersey_degistiren_bool = 0
    for i in range(num_command_text):
        command_list = command_text.readline().strip("\n").split("\t")
        if "CRNODE" in command_list or "SEND" in command_list or "MOVE" in command_list or "CHBTTRY" in command_list or "RMNODE" in command_list :
            line_number += 1
            if command_list[0] == str(just_seconds):
                new = 1

                if "CRNODE" in command_list:
                    command_list[3] = [int(x) for x in command_list[3].split(";")]
                    command_list[4] = [int(x) for x in command_list[4].split(";")]
                    CRNODE(command_list[2], command_list[3], command_list[4], command_list[5])
                elif "SEND" in command_list:
                    SEND(command_list[2], command_list[3], float(command_list[4]))
                elif "MOVE" in command_list:
                    command_list[3] = [int(x) for x in command_list[3].split(";")]
                    MOVE(command_list[2], command_list[3])
                    del cordinates[command_list[2]]
                    cordinates[command_list[2]] = command_list[3]
                elif "CHBTTRY" in command_list:
                    CHBTTRY(command_list[2], command_list[3])
                elif "RMNODE" in command_list:
                    RMNODE(command_list[2])
print("********************************")
print("AD-HOC NETWORK SIMULATOR - BEGIN")
print("********************************")
while total_size != 0:
    print("SIMULATION TIME: ", DECIMAL_INTEGER(hours) + ":" + DECIMAL_INTEGER(minutes) + ":" + DECIMAL_INTEGER(seconds))
    command_text = open(command_txt_sys, "r")
    main()
    command_text.close()
    if total_size <= Packet_size:
        total_size = 0
    else:
        total_size = total_size - Packet_size
    if new ==1:
        for i in cordinates.keys():
            NODES_NEIGHBOURS(i)
            nodes_neighbours_string = nodes_neighbours_string + "" + i + " -> " + ", ".join(nodes_neighbours[i]) + " | "
        print("\tNODES & THEIR NEIGHBORS:", nodes_neighbours_string)
        nodes_neighbours_string = ""
        ROUTE_FINDER(initial_node)
        nodes_neighbours = {}
        if route_counter >0:
            print("\t"+str(route_counter)+" ROUTE(S)FOUND:")
        else:
            print("\tNO ROUTE FROM ",initial_node," TO ",final_node," FOUND.")
        routes_num = 1
        for i in range(len(big_routes)):
            print("\tROUTE ",routes_num,":", big_routes[i],"COST:",cost_list[i])
            routes_num +=1
        if len(cost_list)>0:
            print("\tSELECTED ROUTE (ROUTE ",str(cost_list.index(min(cost_list))+1),"):",big_routes[cost_list.index(min(cost_list))])
        a = []
        cost_list = []
        big_routes = []
        routes = []
        route_counter = 0
    new = 0
    print("\tPACKET " + str(packet_number) + " HAS BEEN SENT")
    print("\tREMAINING DATA SIZE: " + str(total_size) + " BYTE")
    packet_number += 1
    seconds += 1
    just_seconds += 1
    if seconds >= 60:
        seconds -= 60
        minutes += 1
    if minutes >= 60:
        minutes -= 60
        hours += 1
print('******************************')
print('AD-HOC NETWORK SIMULATOR - END')
print('******************************')
