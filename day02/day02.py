from copy import copy

DESIRED_OUTCOME = 19690720

ops = list(map(lambda str : int(str), open("input.txt").read().split(",")))

def read_program(ops):
  ip = 0
  while ip < len(ops):
    opcode = ops[ip]
    if opcode == 1:
      # sum
      a = ops[ip + 1]
      b = ops[ip + 2]
      out = ops[ip + 3]
      ip = ip + 4
      ops[out] = ops[a] + ops[b]
    elif opcode == 2:
      # product
      a = ops[ip + 1]
      b = ops[ip + 2]
      out = ops[ip + 3]
      ip = ip + 4
      ops[out] = ops[a] * ops[b]
    elif opcode == 99:
      return ops[0]
    else:
      raise "Encountered unpected opcode " + opcode
  raise "EOF"

part1_ops = copy(ops)
part1_ops[1] = 12
part1_ops[2] = 2
print(read_program(part1_ops))

# part 2


def find_noun_verb(ops):
  for noun in range(1, len(ops), 1):
    for verb in range(1, len(ops), 1):
      ops_copy = copy(ops)
      ops_copy[1] = noun
      ops_copy[2] = verb
      if read_program(ops_copy) == DESIRED_OUTCOME:
        return 100 * noun + verb
  raise "No result found"


print(find_noun_verb(ops))