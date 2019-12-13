from vendor.Qt import QtCore, QtGui, QtWidgets
import sys

import nuke
import math

print("test")

def custom_contactsheet():
    # Result: #Scans all readnodes
    readnodes = nuke.allNodes('Read')

    # Create a empty list
    ctnlist = []
    my_ctn_dict = {}

    # create var f and get the filenames-value of the readnodes 
    # and split the filepath on every /
    # create var chunks with splitted strings 
    for i in readnodes:
        f = i.knob("file").value()
        chunks = f.split("/")   
        # get the 3th chunk from the right of the string
        ctnlist.append(chunks[-3])

        if chunks[-3] not in my_ctn_dict:
            my_ctn_dict[chunks[-3]] = []
        my_ctn_dict[chunks[-3]].append(i)


    # create a NoOp with the list of all the ctn's
    st = '\n'.join(map(str, sorted(set(ctnlist))))
    try:
        nuke.toNode("list").knob("label").setValue(st)
    except:
        nuke.nodes.NoOp(label=st, name="list")           

    #dropdown menu---------------------------------------------------------------------------------------------------------
    p = nuke.Panel('SelectCTN')
    p.addEnumerationPulldown('choose',st)
    p.show()

    #print p.value('choose')

    sel = p.value('choose') #put the ctn name from the dropdown menu in the sel variable

    # count the same ctn readnodes    
    total = (ctnlist.count(sel))
    contAspx = math.ceil(math.sqrt(total)) # square root of tot select nodes to drive the aspect of contactsheet
    if math.sqrt(total) % 1.0 > 0:
        contAspy = round(math.sqrt(total)) # square root of tot select nodes to drive the aspect of contactsheet
    else:
        contAspy = contAspx

    #deselect nodes
    s = nuke.allNodes()
    for i in s:
        i['selected'].setValue(False)

    # select all the readnodes with the same ctn
    for i in readnodes:
        f = i.knob("file").value()
        chunks = f.split("/") 
        if chunks[-3] == sel:
            i.setSelected(True)

    # get readnode resolution
    current_format = nuke.toNode('Read1').knob('format').actualValue()
    resolution = (current_format.width(), current_format.height()) # combine multiple values in one line with ,
    print resolution

    def set_values_of_node(node, values):
        for key, value in values.items():
            node.knob(key).setValue(value)

    # make a contactsheet------------------------------------------------------

    new_nodes = []
    for i in range(1):
        new_nodes.append(nuke.createNode('ContactSheet'))

    for sheet in new_nodes:
        set_values_of_node(sheet, {
            "rows": contAspy,
            "columns": contAspx,
            "width": resolution[0],
            "height": (contAspy / contAspx) * resolution[1]
        })


    # get position of first readnode
    node = nuke.toNode('Read1')
    xPos = node.xpos()
    yPos = node.ypos()
    print xPos
    print yPos

    # Reposition ContactSheet
    ContactSheets = nuke.allNodes('ContactSheet')

    Readnode = nuke.toNode('Read1')
    ReadxPos = Readnode.xpos()
    ReadyPos = Readnode.ypos(
)
    y_pos = ReadyPos + 150
    y_offset = 50

    for ContactSheet in sorted(ContactSheets, key=lambda x: x.name()):
        ContactSheet.setXpos(ReadxPos)
        ContactSheet.setYpos(y_pos)
        y_pos += y_offset

    #-----------------------------------------------------------------------