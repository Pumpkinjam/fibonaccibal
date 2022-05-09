import time

n = int(input())

pib_table = dict();
pib_table[1] = 1;
pib_table[2] = 1;

def fibonacci(n: int):
    
    for i in range(3,n+1):
        pib_table[i] = pib_table[i-2] + pib_table[i-1];

    return pib_table[n];
    

start = time.time();
print(fibonacci(n));
end = time.time();

print(f'time spent for dynamic fibonacci(): {end-start}');
