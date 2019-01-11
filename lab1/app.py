import processor as p

proc1 = p.EquationProcessor(0.01, p.eq1, p.filepath1)
proc1.simple_iteration_method((1.6, 2.5))

proc21 = p.EquationProcessor(0.01, p.eq2, p.filepath21)
proc21.division_method([-1.5, -1])

proc22 = p.EquationProcessor(0.01, p.eq2, p.filepath22)
proc22.secant_method([-1.5, -1])

proc3 = p.EquationProcessor(0.01, p.eq3, p.filepath3)
roots = proc3.lobachevskyy_method(p.coefs)
proc3.clarify_roots_by_Newton_method(roots)
