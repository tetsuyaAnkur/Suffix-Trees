import preprocess as r
import Suffix_functions as s


Tales = []
val = r.extract('dataset.txt',Tales)
inp = 'this is a WOLF'  # here inp is the query string

print("\n\n")

#s.first_problem(inp,val,Tales)

#s.second_problem(inp,val,Tales)

s.third_problem(inp,val,Tales)
