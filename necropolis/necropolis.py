
GENS_SEPORATE = 300
MAX_REWARDS = 500000000000000000000

f1 = 10
f2 = 100
f4 = 10000
f7 = 1000000
f6 = 10000000
f9 = 100000000
f11 = 10000000000
f12 = 100000000000
f13 = 1000000000000
f15 = 100000000000000
f16 = 1000000000000000
f17 = 10000000000000000
f18 = 100000000000000000
f19 = 1000000000000000000
f20 = 10000000000000000000
f21 = 100000000000000000000
f23 = 10000000000000000000000
f22 = 100000000000000000000000
f25 = 1000000000000000000000000
f26 = 10000000000000000000000000
f27 = 100000000000000000000000000
f29 = 10000000000000000000000000000
f31 = 1000000000000000000000000000000
f33 = 100000000000000000000000000000000
f35 = 10000000000000000000000000000000000
f37 = 1000000000000000000000000000000000000
f39 = 100000000000000000000000000000000000000
f41 = 10000000000000000000000000000000000000000
f43 = 1000000000000000000000000000000000000000000

def get_combat_gen(gens, f):
  return gens % f // (f // f2)

def get_face_gen(gens, f):
  return gens % f // (f // f1)

def next_face_gen(sub, f, l):
  n = get_face_gen(sub, f)

  return n + l

def calc_face_gens(gens):
  sub = gens % f27
  aura = sub // f26
  horns = next_face_gen(sub, f25, aura)
  scales = next_face_gen(sub, f22, horns)
  spots = next_face_gen(sub, f20, scales)
  tail = next_face_gen(sub, f18, spots)
  wings = next_face_gen(sub, f16, tail)
  body = next_face_gen(sub, f12, wings)
  eyes = next_face_gen(sub, f9, body)
  head = next_face_gen(sub, f6, eyes)

  return (head * 10**18) // 4

def calc_combat_gens(gens):
  g0 = get_combat_gen(gens, f43)
  g1 = get_combat_gen(gens, f41)
  g2 = get_combat_gen(gens, f39)
  g3 = get_combat_gen(gens, f37)
  g4 = get_combat_gen(gens, f35)
  g5 = get_combat_gen(gens, f33)
  g6 = get_combat_gen(gens, f31)
  g7 = get_combat_gen(gens, f29)
  g8 = get_combat_gen(gens, f27)
  g9 = get_combat_gen(gens, f25)
  g10 = get_combat_gen(gens, f23)
  g11 = get_combat_gen(gens, f21)
  g12 = get_combat_gen(gens, f19)
  g13 = get_combat_gen(gens, f17)
  g14 = get_combat_gen(gens, f15)
  g15 = get_combat_gen(gens, f13)
  g16 = get_combat_gen(gens, f11)
  g17 = get_combat_gen(gens, f9)
  g18 = get_combat_gen(gens, f7)
  g19 = get_combat_gen(gens, f4)
  g20 = get_combat_gen(gens, f2)

  gens_sum = g0 + g1 + g2 + g3 + g4 + g5 + g6 + g7 + g8 + g9 + g10 + g11 + g12 + g13 + g14 + g15 + g16 + g17 + g18 + g19 + g20

  return (gens_sum * 10**18) // GENS_SEPORATE

def calc_gen_lab(start_price, use_count, multiplicator):
  if (use_count == 0):
    return 0
  return multiplicator ** use_count * (start_price / 2)

def calc_amoun(zlp_amount, dmz_total_supply, token_id):
  return zlp_amount // ((dmz_total_supply * token_id) / 800)

def calc_rewards(supply, gen_lab, combat, face):
  if (supply > MAX_REWARDS):
    return MAX_REWARDS

  return supply + gen_lab + combat + face


ZLP_AMOUNT = 16344308266940854272735
DMZ_SUPPLY = 3678
TOKEN_ID = 300

gen_lab = calc_gen_lab(10000000000000000000, 1, 2)
combat = calc_combat_gens(113557207084082392001653552727254081999999999999999999999999999999999999999999)
supply = calc_amoun(ZLP_AMOUNT, DMZ_SUPPLY, TOKEN_ID)
face = calc_face_gens(77754644081635302349351242132)
rewards = calc_rewards(supply, gen_lab, combat, face)

print('gen_lab %i ZLP' % (gen_lab))
print('combat %i ZLP' % (combat))
print('face %i ZLP' % (face))
print('supply %i ZLP' % (supply))
print('rewards %i ZLP' % (rewards))
