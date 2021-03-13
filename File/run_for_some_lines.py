fname = "SP500.txt"
calc=0
sp=list()
ir=list()
with open(fname, 'r') as fileref:
    for line in fileref.readlines()[1:]:
        line=line.rstrip().split(",")
        if line[0]=="6/1/2016":
            calc=1
        if calc:
            sp.append(float(line[1]))
            ir.append(float(line[5]))
        if line[0].startswith("5"):
            calc=0
mean_SP=sum(sp)/len(sp)
max_interest=max(ir)
print(str(mean_SP)+"\n"+str(max_interest))