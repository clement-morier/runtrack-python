initial=10000
rendement=5
gain=initial+(initial*rendement/100)
print(gain)
initial=initial+5000
rendement=rendement+2
gain2=initial+(initial*rendement/100)
print(gain2)
initial=initial-initial/10
rendement=rendement-1
gain3=initial+(initial*rendement/100)
print(gain3)