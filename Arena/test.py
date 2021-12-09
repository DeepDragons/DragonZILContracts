GENES = 94971868430698218815550784762969701691290030012016199912601261219107712080824

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
factor38 = 1000000000000000000000000000000000000000000000000000000000000000000000000000000

def get_gene(genes: int, factor: int, decimal: int, entropy: int):
  return genes % factor // decimal

def get_attack_amoun(entropy: int, genes: int):
  g0 = genes % factor0
  g1 = get_gene(genes, factor1, factor0, entropy)
  g2 = get_gene(genes, factor2, factor1, entropy)
  g3 = get_gene(genes, factor3, factor2, entropy)

  g4 = get_gene(genes, factor4, factor3, entropy)
  g5 = get_gene(genes, factor5, factor4, entropy)
  g6 = get_gene(genes, factor6, factor5, entropy)
  g7 = get_gene(genes, factor7, factor6, entropy)
  g8 = get_gene(genes, factor8, factor7, entropy)
  g9 = get_gene(genes, factor9, factor8, entropy)

  g10 = get_gene(genes, factor10, factor9, entropy)
  g11 = get_gene(genes, factor11, factor10, entropy)
  g12 = get_gene(genes, factor12, factor11, entropy)
  g13 = get_gene(genes, factor13, factor12, entropy)
  g14 = get_gene(genes, factor14, factor13, entropy)
  g15 = get_gene(genes, factor15, factor14, entropy)
  g16 = get_gene(genes, factor16, factor15, entropy)
  g17 = get_gene(genes, factor17, factor16, entropy)
  g18 = get_gene(genes, factor18, factor17, entropy)
  g19 = get_gene(genes, factor19, factor18, entropy)
  g20 = get_gene(genes, factor20, factor19, entropy)

  g21 = get_gene(genes, factor21, factor20, entropy)
  g22 = get_gene(genes, factor22, factor21, entropy)
  g23 = get_gene(genes, factor23, factor22, entropy)
  g24 = get_gene(genes, factor24, factor23, entropy)
  g25 = get_gene(genes, factor25, factor24, entropy)
  g26 = get_gene(genes, factor26, factor25, entropy)
  g27 = get_gene(genes, factor27, factor26, entropy)
  g28 = get_gene(genes, factor28, factor27, entropy)
  g29 = get_gene(genes, factor29, factor28, entropy)
  g30 = get_gene(genes, factor30, factor29, entropy)

  g31 = get_gene(genes, factor31, factor30, entropy)
  g32 = get_gene(genes, factor32, factor31, entropy)
  g33 = get_gene(genes, factor33, factor32, entropy)
  g34 = get_gene(genes, factor34, factor33, entropy)
  g35 = get_gene(genes, factor35, factor34, entropy)
  g36 = get_gene(genes, factor36, factor35, entropy)
  g37 = get_gene(genes, factor37, factor36, entropy)
  g38 = get_gene(genes, factor38, factor37, entropy)

  return (g0, g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11, g12, g13, g14, g15, g16, g17, g18, g19, g20, g21, g22, g23, g24, g25, g26, g27, g28, g29, g30, g31, g32, g33, g34, g35, g36, g37, g38)


print(get_attack_amoun(0, GENES))
