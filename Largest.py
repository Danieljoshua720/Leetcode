# 1
''' 
TCS NQT Twist Level 1 ⭐
Problem Statement

A logistics company receives packages from multiple warehouses.

A package with weight 0 means the package was cancelled.
A package with a negative weight indicates corrupted data and must be ignored.

Find the heaviest valid package.

Input
8
25 -1 0 78 65 -5 91 45
Output
91
'''

'''
def largest_valid_package(arr):
    filtered=[]
    if len(filtered)==0:
        return "No valid packages"
    for num in arr:
        if num>0:
            filtered.append(num)

        else:
            continue
    return max(filtered)


n=int(input("Enter the number of packages: "))
arr=list(map(int,input().split()))
print(largest_valid_package(arr))


def largest_valid_package(arr):
    maximum = -1

    for num in arr:
        if num > 0 and num > maximum:TCS NQT Twist Level 4 ⭐⭐⭐⭐
Problem Statement

A warehouse records package IDs and weights.

Some package IDs appear multiple times because the package was scanned repeatedly.

Consider only the latest scan of each package and determine the heaviest package.
Input

6

ID Weight

101 40
102 75
101 85
103 50
102 60
104 90

Output

90

Explanation

Latest scans

101 → 85
102 → 60
103 → 50
104 → 90

Largest = 90

            maximum = num

    if maximum == -1:
        return "No Valid Package"

    return maximum


n = int(input())
arr = list(map(int, input().split()))

print(largest_valid_package(arr))

'''

# 2
'''
TCS NQT Twist Level 2 ⭐⭐
Problem Statement

A truck can carry packages only if

Weight is positive.
Weight is divisible by 5.
Weight does not exceed the truck capacity C.

Find the heaviest package that can be loaded.

If no package satisfies the conditions, print "No Package".

Input
7
120
40 125 85 150 95 130 100
Output
100

Explanation:

125 > 120 ❌
150 > 120 ❌
130 > 120 ❌
100 ✅ Largest valid
'''

'''
def heaviest_package(arr,C):
    largest=-1
    for weight in arr:
        if weight>0 and weight%5==0 and weight<=C:
            if weight>largest:
                largest=weight
    if largest==-1:
        return "No Package"
    return largest


n=int(input("Enter the number of packages: "))
C=int(input("Enter the capacity of the truck: "))
arr=list(map(int,input().split()))
print(heaviest_package(arr,C))

'''

# 3
'''
TCS NQT Twist Level 3 ⭐⭐⭐
Problem Statement

Each package has

Weight
Priority

Only packages having Priority ≥ P are eligible.

Find the heaviest eligible package.

If multiple packages have the same weight, choose the one with the highest priority.

Input
5
3

Weight Priority
45 2
90 5
90 4
70 5
100 2
Output
90
'''


'''
def heaviest_eligible_package(n,p):
    max_weight=-1
    max_priority=-1
    
    for _ in range(n):
        weight,priority=map(int,input().split())
        if priority>=p:
            if weight>max_weight:
                max_weight=weight
                max_priority=priority
            elif weight==max_weight and priority>max_priority:
                max_priority=priority

    if max_weight==-1:
        return "No eligible packages"
    return max_weight
    
n=int(input("Enter the number of packages: "))
p=int(input("Enter the minimum priority: "))
print(heaviest_eligible_package(n,p))
'''


# 4

'''
TCS NQT Twist Level 4 ⭐⭐⭐⭐
Problem Statement

A warehouse records package IDs and weights.

Some package IDs appear multiple times because the package was scanned repeatedly.

Consider only the latest scan of each package and determine the heaviest package.

Input
6

ID Weight

101 40
102 75
101 85
103 50
102 60
104 90
Output
90

Explanation

Latest scans

101 → 85
102 → 60
103 → 50
104 → 90

Largest = 90

'''
'''
n = int(input())

packages = {}

for _ in range(n):
    package_id, weight = map(int, input().split())
    packages[package_id] = weight      # Latest scan replaces old one

print(max(packages.values()))

'''

#5
'''
TCS NQT Twist Level 5 ⭐⭐⭐⭐⭐
Problem Statement

A logistics company monitors package movement.

Each package has

Weight
Status

Status can be

L → Loaded
P → Pending
D → Damaged

Only loaded packages can be dispatched.

If two loaded packages have the same weight, dispatch the one that appeared first.

Print the maximum dispatchable weight.

Input
7

40 L
95 P
120 D
110 L
150 P
110 L
90 L
Output
110
'''

'''
def maximum_dispatchable_weight(n):
    
    max_weight=-1
    for _ in range(n):
        weight,status=input().split()
        weight=int(weight)
        
        if weight>max_weight and status=='L':
            max_weight=weight

    if max_weight==-1:
        return "No dispatchable packages"
    return max_weight

n=int(input("Enter the number of packages: "))
print(maximum_dispatchable_weight(n))   
'''