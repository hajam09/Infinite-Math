total = 0

with open('Points.txt', 'r') as inp, open('output.txt', 'w') as outp:
   for line in inp:
       try:
           num = int(line)
           total += num
           outp.write(line)
       except ValueError:
           print('{} is not a number!'.format(line))

x = format(total)
print(x)
