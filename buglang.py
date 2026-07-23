import sys, random, re

# Rune digit values
RUNES = [
    'ᚠ','ᚢ','ᚦ','ᚨ','ᚱ','ᚲ','ᚷ','ᚹ','ᚺ',
    'ᚻ','ᚼ','ᚽ','ᚾ','ᛁ','ᛃ','ᛇ','ᛈ','ᛉ','ᛊ'
]
VAL = {r:i for i,r in enumerate(RUNES)}

# Rune commands
RUNE_CMD = {
    'ᛉᚨᚦᚱ': 'putc',   # putc
    'ᚻᚦᛁᚦ': 'halt',   # halt
}

C_EQS = [
"(ᛇ+(ᚼ*(ᛁ*ᛃ)))",
"(ᛇ+(ᚼ*(ᛃ*ᛁ)))",
"(ᛇ+(ᛁ*(ᚼ*ᛃ)))",
"(ᛇ+(ᛁ*(ᛃ*ᚼ)))",
"(ᛇ+(ᛃ*(ᚼ*ᛁ)))",
"(ᛇ+(ᛃ*(ᛁ*ᚼ)))",
"(ᛇ+((ᚼ*ᛁ)*ᛃ))",
"(ᛇ+((ᚼ*ᛃ)*ᛁ))",
"(ᛇ+((ᛁ*ᚼ)*ᛃ))",
"(ᛇ+((ᛁ*ᛃ)*ᚼ))",
"(ᛇ+((ᛃ*ᚼ)*ᛁ))",
"(ᛇ+((ᛃ*ᛁ)*ᚼ))",
"((ᚼ*(ᛁ*ᛃ))+ᛇ)",
"((ᚼ*(ᛃ*ᛁ))+ᛇ)",
"((ᛁ*(ᚼ*ᛃ))+ᛇ)",
"((ᛁ*(ᛃ*ᚼ))+ᛇ)",
"((ᛃ*(ᚼ*ᛁ))+ᛇ)",
"((ᛃ*(ᛁ*ᚼ))+ᛇ)",
"(((ᚼ*ᛁ)*ᛃ)+ᛇ)",
"(((ᚼ*ᛃ)*ᛁ)+ᛇ)",
"(((ᛁ*ᚼ)*ᛃ)+ᛇ)",
"(((ᛁ*ᛃ)*ᚼ)+ᛇ)",
"(((ᛃ*ᚼ)*ᛁ)+ᛇ)",
"(((ᛃ*ᛁ)*ᚼ)+ᛇ)"
]

def rune_expr_to_python(expr):
    out = ""
    for ch in expr:
        if ch in VAL:
            out += str(VAL[ch])
        else:
            out += ch
    return out

chosen = random.choice(C_EQS)
C = eval(rune_expr_to_python(chosen))

print(chosen)

def runes_to_int(s):
    val = 0
    for ch in s:
        val = val * 19 + VAL[ch]
    return val

# Load program from sys.argv[1]
if len(sys.argv) < 2:
    print("No input file provided.")
    sys.exit(1)

with open(sys.argv[1], "r", encoding="utf-8") as f:
    program = f.read().strip().splitlines()

for line in program:
    line = line.strip()
    if not line:
        continue

    # Match (runes,runes)C <rune-command>
    m = re.match(r'\(([^,]+),([^)]*)\)'+str(C)+r'\s*(.*)', line)
    if m:
        a_runes, b_runes, cmd_runes = m.groups()
        a = runes_to_int(a_runes.strip())
        cmd = RUNE_CMD.get(cmd_runes.strip(), None)

        if cmd == 'putc':
            sys.stdout.write(chr(a))
        elif cmd == 'halt':
            break
    else:
        # maybe just a command
        cmd = RUNE_CMD.get(line.strip(), None)
        if cmd == 'halt':
            break

sys.stdout.flush()
