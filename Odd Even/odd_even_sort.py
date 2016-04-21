
import multiprocessing

def compare(x):
    change = False
    if x[0] > x[1]:
        x[0], x[1] = x[1], x[0]
        change = True
    return (x, change)

def oddevensort(x):
    
    phase, flag = 0, 0  
    while (flag != 2):
        split = [[x[i], x[i+1]] for i in range(phase, len(x)-1, 2)]
        
        process_pool = multiprocessing.Pool(2)
        split_after_comparison = process_pool.map(compare, split)
        
        process_pool.close()

        
        temp = []
        if len(x)%2 == 0:
            if (phase == 1):
                temp.append(x[0])
                for i in split_after_comparison:
                    temp += i[0]
                temp.append(x[-1])
            else:  
                for i in split_after_comparison:
                    temp += i[0]
        else:                  
            if (phase == 1):   
                temp.append(x[0])
                for i in split_after_comparison: 
                    temp += i[0]
            else:              
                for i in split_after_comparison: 
                    temp += i[0]
                temp.append(x[-1])
        
        x = temp
        phase = (phase + 1)%2
        
        if any([i[1] for i in split_after_comparison]):
            flag = 0
        else:
            flag += 1
    
    print "The sorted list", x
    return x
    
