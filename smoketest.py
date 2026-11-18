# AEGIS-FP 423Z455VLLHUHXHB · (c) Danny Lee Eldridge · AEGIS Community License (business use needs the Commercial License)
"""Quick check after install:  pip install -r requirements.txt && python smoketest.py"""
import sys, time
t = time.time(); ok = []
from janus_calc import models, core, anyV
s = anyV.from_formula('0.5*phi**2'); r = core.spectra3(s, 60.0)
ok.append(abs(r['ns'] - (1 - 2/60.5)) < 2e-3); print('phi^2 N*=60  n_s', r['ns'], 'r', r['r'])
st = anyV.from_formula('(1-exp(-sqrt(2/3)*phi))**2'); q = core.spectra3(st, 55.0)
ok.append(0.962 < q['ns'] < 0.968 and 0.003 < q['r'] < 0.005); print('Starobinsky N*=55  n_s', q['ns'], 'r', q['r'])
m = models.serapis_E(1.15e-6); e = core.spectra3(m, 50.0)
ok.append(0.95 < e['ns'] < 0.99); print('SERAPIS-E N*=50  n_s', e['ns'], 'r', e['r'], 'alpha_s', e.get('alpha_s'))
print(f"{sum(ok)}/{len(ok)} passed in {time.time()-t:.1f}s"); sys.exit(0 if all(ok) else 1)
