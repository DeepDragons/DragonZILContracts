half = 50
two = 2
one = 1
one_hundred = 100
factor_60 = 1000000000000000000000000000000000000000000000000000000000000
factor_54 = 1000000000000000000000000000000000000000000000000000000
factor_48 = 1000000000000000000000000000000000000000000000000
factor_42 = 1000000000000000000000000000000000000000000
factor_36 = 1000000000000000000000000000000000000
factor_30 = 1000000000000000000000000000000
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

def combinate_combat_gens(gens0, gens1, random):
    n = random % one_hundred

    if (n < half):
        gen10 = gens0 % factor_6
    else:
        gen10 = gens1 % factor_6

    r_next = random / two
    n = r_next % one_hundred

    gen9 = cut_gen(gens0, gens1, n, factor_6)

    r_next = random / two
    n = r_next % one_hundred

    gen8 = cut_gen(gens0, gens1, n, factor_12)

    r_next = random / two
    n = r_next % one_hundred

    gen7 = cut_gen(gens0, gens1, n, factor_18)

    r_next = random / two
    n = r_next % one_hundred

    gen6 = cut_gen(gens0, gens1, n, factor_24)

    r_next = random / two
    n = r_next % one_hundred

    gen5 = cut_gen(gens0, gens1, n, factor_30)

    r_next = random / two
    n = r_next % one_hundred

    gen4 = cut_gen(gens0, gens1, n, factor_36)

    r_next = random / two
    n = r_next % one_hundred

    gen3 = cut_gen(gens0, gens1, n, factor_42)

    r_next = random / two
    n = r_next % one_hundred

    gen2 = cut_gen(gens0, gens1, n, factor_48)

    r_next = random / two
    n = r_next % one_hundred

    gen1 = cut_gen(gens0, gens1, n, factor_54)

    r_next = random / two
    n = r_next % one_hundred

    if (n < half):
        gen0 = gens0 // factor_60
    else:
        gen0 = gens1 // factor_60

    return (gen0 * factor_60) + (gen1 * factor_54) + (gen2 * factor_48) + (gen3 * factor_42) + (gen4 * factor_36) + (gen5 * factor_30) + (gen6 * factor_24) + (gen7 * factor_18) + (gen8 * factor_12) + (gen9 * factor_6) + gen10



gen0 = 101647673406769880573901220984528846221301586515024944091799042138004426191841
gen1 = 101647673406769880573901220984528846221301586515024944091799042138004426191841
r = 8842241887348121053642943213174811942429995499481999421099999928807063991194

print(combinate_image_gens(gen0, gen1, r))
