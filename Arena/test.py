import os

ten = 10

factor0 = 100
factor1 = 10000
factor2 = 1000000
factor3 = 100000000
factor4 = 10000000000
factor5 = 1000000000000
factor6 = 100000000000000
factor7 = 10000000000000000
factor8 = 1000000000000000000
factor9 = 100000000000000000000
factor10 = 10000000000000000000000
factor11 = 1000000000000000000000000
factor12 = 100000000000000000000000000
factor13 = 10000000000000000000000000000
factor14 = 1000000000000000000000000000000
factor15 = 100000000000000000000000000000000
factor16 = 10000000000000000000000000000000000
factor17 = 1000000000000000000000000000000000000
factor18 = 100000000000000000000000000000000000000
factor19 = 10000000000000000000000000000000000000000
factor20 = 1000000000000000000000000000000000000000000
factor21 = 100000000000000000000000000000000000000000000
factor22 = 10000000000000000000000000000000000000000000000
factor23 = 1000000000000000000000000000000000000000000000000
factor24 = 100000000000000000000000000000000000000000000000000
factor25 = 10000000000000000000000000000000000000000000000000000
factor26 = 1000000000000000000000000000000000000000000000000000000
factor27 = 100000000000000000000000000000000000000000000000000000000
factor28 = 10000000000000000000000000000000000000000000000000000000000
factor29 = 1000000000000000000000000000000000000000000000000000000000000
factor30 = 100000000000000000000000000000000000000000000000000000000000000
factor31 = 10000000000000000000000000000000000000000000000000000000000000000
factor32 = 1000000000000000000000000000000000000000000000000000000000000000000
factor33 = 100000000000000000000000000000000000000000000000000000000000000000000
factor34 = 10000000000000000000000000000000000000000000000000000000000000000000000
factor35 = 1000000000000000000000000000000000000000000000000000000000000000000000000
factor36 = 100000000000000000000000000000000000000000000000000000000000000000000000000
factor37 = 10000000000000000000000000000000000000000000000000000000000000000000000000000
factor38 = 100000000000000000000000000000000000000000000000000000000000000000000000000000

def an_attack(a: int, b: int):
  return b - a

def calc_by_attack(a: int, b: int):
  if a > b:
    return 0

  return 1

def get_gene(last: int, genes: int, factor: int, decimal: int):
  return (genes % factor // decimal) + last

def get_attack_gene(last: int, genes: int, factor: int, decimal: int, entropy: int):
  gene = get_gene(last, genes, factor, decimal)
  crit = (entropy // factor) % ten

  return gene + crit

def get_attack(entropy: int, genes: int, luck: int):
  g0 = genes % factor0
  g1 = get_attack_gene(g0, genes, factor1, factor0, entropy)
  g2 = get_attack_gene(g1, genes, factor2, factor1, entropy)
  g3 = get_attack_gene(g2, genes, factor3, factor2, entropy)
  g4 = get_attack_gene(g3, genes, factor4, factor3, entropy)
  g5 = get_attack_gene(g4, genes, factor5, factor4, entropy)
  g6 = get_attack_gene(g5 ,genes, factor6, factor5, entropy)
  g7 = get_attack_gene(g6, genes, factor7, factor6, entropy)
  g8 = get_attack_gene(g7, genes, factor8, factor7, entropy)
  g9 = get_attack_gene(g8, genes, factor9, factor8, entropy)
  g10 = get_attack_gene(g9, genes, factor10, factor9, entropy)
  g11 = get_attack_gene(g10, genes, factor11, factor10, entropy)
  g12 = get_attack_gene(g11, genes, factor12, factor11, entropy)
  g13 = get_attack_gene(g12, genes, factor13, factor12, entropy)
  g14 = get_attack_gene(g13, genes, factor14, factor13, entropy)
  g15 = get_attack_gene(g14, genes, factor15, factor14, entropy)
  g16 = get_attack_gene(g15, genes, factor16, factor15, entropy)
  g17 = get_attack_gene(g16, genes, factor17, factor16, entropy)
  g18 = get_attack_gene(g17, genes, factor18, factor17, entropy)
  g19 = get_attack_gene(g18, genes, factor19, factor18, entropy)

  entropy_number = entropy % ten

  if entropy_number < luck:
    value = g19 * entropy_number // factor0
    return g19 + value

  return g19

def get_defence_genes(genes: int, defence: bool, percent: int):
  g20 = get_gene(0, genes, factor20, factor19)
  g21 = get_gene(g20, genes, factor21, factor20)
  g22 = get_gene(g21, genes, factor22, factor21)
  g23 = get_gene(g22, genes, factor23, factor22)
  g24 = get_gene(g23, genes, factor24, factor23)
  g25 = get_gene(g24, genes, factor25, factor24)
  g26 = get_gene(g25, genes, factor26, factor25)
  g27 = get_gene(g26, genes, factor27, factor26)
  g28 = get_gene(g27, genes, factor28, factor27)
  g29 = get_gene(g28, genes, factor29, factor28)
  g30 = get_gene(g29, genes, factor30, factor29)
  g31 = get_gene(g30, genes, factor31, factor30)
  g32 = get_gene(g31, genes, factor32, factor31)
  g33 = get_gene(g32, genes, factor33, factor32)
  g34 = get_gene(g33, genes, factor34, factor33)
  g35 = get_gene(g34, genes, factor35, factor34)
  g36 = get_gene(g35, genes, factor36, factor35)
  g37 = get_gene(g36, genes, factor37, factor36)

  if defence:
    increase = g37 * percent // factor0
    return g37 + increase

  return g37

def get_dragon_stats(genes: int, defence: int, percent: int):
  b32 = os.urandom(32)
  entropy_number = int.from_bytes(b32, "big")
  # entropy_number = 115085169065819247984225582025768412064576353692739060426961360543845990284306

  luck = get_gene(0, genes, factor38, factor37)
  attack = get_attack(entropy_number, genes, luck)
  defence = get_defence_genes(genes, defence, percent)

  return {
    'attack': attack,
    'defence': defence
  }

def start_fight(defender: int, attacker: int):
  percent = 1
  dragon0 = get_dragon_stats(defender, True, percent)
  dragon1 = get_dragon_stats(attacker, False, percent)

  defence0 = an_attack(dragon1['attack'], dragon0['defence'])
  defence1 = an_attack(dragon0['attack'], dragon1['defence'])

  if defence0 > defence1:
    return 0

  return 1

defender = 0
attacker = 0

for _ in range(1000000):
  b32 = os.urandom(32)
  entropy_number = int.from_bytes(b32, "big")
  value = entropy_number % 30

  if value > 29:
    print(value)
  # won = start_fight(
  #   110076663326186735694065157349154850016621919904094611281317450973914607307198,
  #   110154428326032843508749688438399367999999909999999999889999999999999999999934
  # )

  # if won == 0:
  #   defender += 1

  # if won == 1:
  #   attacker += 1
  

# print(defender, attacker)