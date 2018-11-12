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
            

#regin = [0 for x in range(100)]
#print(run([15, 20], reg=regin))



def compile(filename):
    f= open(filename, "r")
    program = [line for line in f]
    f.close()
    
    program = [item.strip('\r\n') for item in program]
    program = [item.split('\t') for item in program]
    for index, line in enumerate(program):
        newline = []
        for part in line:
            if "#" in part:
                break
            else:
                newline.append(part)
        program[index] = newline

    program = list(filter(lambda x: x != [""] and x != [], program))

    if len(program) > 100:
        return [0 for x in range(100)]
    
    for index, line in enumerate(program):
        for otherline in program:
            if len(line) ==3:
                if line[2] == otherline[0]:
                    program[index][2] = program.index(otherline)
                    break
    compiledoutput = []

    for line in program:
        if line[1] == "ADD":
            



    return compiledoutput
    

print(compile("program.txt"))
