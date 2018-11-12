import math
def run(inputlist, reg):
    running = True
    outputlist = []
    try:
        reg
    except NameError:
        reg = [0 for x in range(100)]


    acc = 0
    pc  = 0

    mar = 0
    mdr = 0
    
        
    while running:
        inputlist,outputlist,running,reg,acc,pc,mar,mdr = fde(inputlist,outputlist,running,reg,acc,pc,mar,mdr)

    return outputlist
    

def fde(inputlist, outputlist, running, reg, acc, pc, mar, mdr):
    #fetch
    mar = pc
    mdr = reg[pc]
    pc = pc + 1
    if pc == 100:
        running = False
    #decode
    opcode = math.floor(mdr / 100)
    operand = mdr % 100
    #execute
    if opcode == 0:
        running = False
    elif opcode == 1:
        acc = acc + reg[operand]
    elif opcode == 2:
        acc = acc - reg[operand]
    elif opcode == 3:
        reg[operand] = acc
    elif opcode == 4:
        pass
    elif opcode == 5:
        acc = reg[operand]
    elif opcode == 6:
        pc = operand
    elif opcode == 7:
        if acc == 0:
            pc = operand
        else:
            pass
    elif opcode == 8:
        if acc >= 0:
            pc = operand
        else:
            pass
    elif opcode == 9:
        if operand == 1:
            acc = inputlist.pop(0)
        elif operand == 2:
            outputlist.append(acc)

    return inputlist, outputlist, running, reg, acc, pc, mar, mdr
            

regin = [0 for x in range(100)]
regin[0] = 901
regin[1] = 390
regin[2] = 901
regin[3] = 190
regin[4] = 902
print(run([15, 20], reg=regin))


