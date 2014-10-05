"""
The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13->40->20->10->5->16->8->4->2->1

13: 9
40:8
20:7

It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

"""

import time

#BRUTE FORCE METHOD:

def use_rule(n):
    if n%2 ==0:
        n /= 2
    else:
        n = 3*n+1

    return n

def brute_max_chain(highest):
    max_count=0
    max_value=1
    for i in range (2, highest+1):
        latest = i
        chain_length=0
        while(latest != 1):
             latest =use_rule(latest)
             chain_length+=1

        if(chain_length>max_count):
            max_count=chain_length
            max_value=i
    return (max_value, max_count)

t0 = time.time()
print ("The longest Collatz chain is produced by %s, with a length of %s" % brute_max_chain(1000000))
t1 = time.time()
total = t1-t0
print "The brute force method takes: "
print total

#DICTIONARY METHOD:

def dict_max_chain(highest):
    known_chains = dict()
    max_count=0
    max_value=1
    for i in range(2,highest+1):
        new_knowns=dict()
        latest = i
        while(latest != 1):
            if latest in known_chains:  
                for entry in new_knowns:
                    new_knowns[entry] += known_chains[latest]
                latest=1
            else:
                new_knowns[latest]=0;
                latest =use_rule(latest)
                for entry in new_knowns:
                    new_knowns[entry] += 1

        for entry in new_knowns:
            known_chains[entry] = new_knowns[entry]
            if new_knowns[entry] > max_count:
                max_count= new_knowns[entry]
                max_value = entry

     
    return (max_value, max_count)

t0 = time.time()
print ("The longest Collatz chain is produced by %s, with a length of %s" % dict_max_chain(1000000))
t1 = time.time()
total = t1-t0
print "The dictionary method takes: "
print total


#LIST METHOD:
def list_max_chain(highest):
    known_chains = [0]*(highest+1)
    known_chains[2]=1
    max_count=1
    max_value=2
    for i in range(3,highest+1):
        current_chain_numbers = []
        latest = i
        while(latest != 1):
            if latest > highest or known_chains[latest]==0:  #code doesn't stop numbers in the sequence from going higher than 1000000 during calculations, but doesn't record the resulting chain length for those numbers
                current_chain_numbers.append(latest)
                latest=use_rule(latest)
                
            else:
                for entry in current_chain_numbers:
                    if entry <= highest:
                        known_chains[entry] += known_chains[latest]+(len(current_chain_numbers) - current_chain_numbers.index(entry))
                        if known_chains[entry]>max_count:
                            max_count=known_chains[entry]
                            max_value=entry
                latest=1

     
    return (max_value, max_count)

t0 = time.time()
print ("The longest Collatz chain is produced by %s, with a length of %s" % list_max_chain(1000000))
t1 = time.time()
total = t1-t0
print "The list method takes: "
print total


#RECURSIVE METHOD:

highest = 1000000
known_chains = [0] * (highest+1)
known_chains[2] = 1

def recursive_method(n):
    if n < highest:
        if known_chains[n]: #i.e. known_chains[n]!=0
           return known_chains[n]
        elif n%2: #if the number is odd
            known_chains[n] = 1 + recursive_method(3*n + 1)
        else:
            known_chains[n] = 1 + recursive_method(n/2)
        return known_chains[n]
    elif n%2:
        return 1 + recursive_method(3*n + 1)
    else:
        return 1 + recursive_method(n/2)

t0 = time.time()

max_count = 0
max_value = 1

for i in range(2, highest+1):
    chain_length = recursive_method(i)
    if chain_length > max_count:
        max_count = chain_length
        max_value = i

print ("The longest Collatz chain is produced by %s, with a length of %s" % (max_value, max_count))
t1 = time.time()
total=t1-t0
print "The recursive method takes: "
print total

