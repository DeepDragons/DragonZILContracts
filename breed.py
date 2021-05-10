half = 50
two = 2
one = 1
one_hundred = 100
factor_24 = 1000000000000000000000000
factor_18 = 1000000000000000000
factor_12 = 1000000000000
factor_6 = 1000000

def split(gens, factor):
    return (gens // factor) % factor_6

def cut_gen(g0, g1, n, f):
    if (n < half):
        return split(g0, f)
    else:
        return split(g1, f)

def combinate_image_gens(gens0, gens1, random):
    n = random % one_hundred

    if (n < half):
        gen5 = gens0 % factor_6
    else:
        gen5 = gens1 % factor_6
    r_next = random / two
    n = r_next % one_hundred

    gen4 = cut_gen(gens0, gens1, n, factor_6)

    r_next = random / two
    n = r_next % one_hundred

    gen3 = cut_gen(gens0, gens1, n, factor_12)
    
    r_next = random / two
    n = r_next % one_hundred

    gen2 = cut_gen(gens0, gens1, n, factor_18)
    
    r_next = random / two
    n = r_next % one_hundred

    if (n < half):
        gen1 =  gens0 // factor_24
    else:
        gen1 = gens1 // factor_24

    return gen1 * factor_24 + gen2 * factor_18 + gen3 * factor_12 + gen4 * factor_6 + gen5
    # return [gen1, gen2, gen3, gen4, gen5]


gen0 = 77742020474220424231014055026
gen1 = 77723710180045032147252032241
r = 8842241887348121053642943213174811942429995499481999421099999928807063991194

print(combinate_image_gens(gen0, gen1, r))
