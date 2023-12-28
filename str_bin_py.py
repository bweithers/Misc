a = 'abcdefghijklmnopqrstuvwyxz'

alpha_zip = {c: n+1 for n,c in zip(range(26),a)}

def str_bin(s, chunks = 0, chunks_per_line = 0, chunk_size = 8):
    out = ''
    if not chunks:
        for c in s: 
            out += str.rjust(str(bin(alpha_zip[c]))[2:],chunk_size,'0') + ' ' 
    else:
        i = 0
        while chunks > 0:
            out += str.rjust(str(bin(alpha_zip[s[i]]))[2:],chunk_size,'0') + ' '
            i += 1
            i %= len(s)
            chunks -= 1
    return out[:-1]

print(str_bin('hello', chunks=10, chunk_size=6))
