

data_structure = [[1,2,3],{'a':4,'b':5},(6,{'cube':7,'drum':8}),'hello',((),[{(2,'Urban',('Urban2',35))}])]
def calculate(*arg):
    total_sum = 0
    for arg in arg:
        if isinstance(arg,(list,tuple, set)):
            total_sum +=calculate(*arg)
        elif isinstance(arg, dict):
            total_sum += calculate(*arg.items())
        elif isinstance(arg, str):
            total_sum += len(arg)
        elif isinstance(arg,(int,float)):
            total_sum += arg
    return(total_sum)
print (calculate(data_structure))
