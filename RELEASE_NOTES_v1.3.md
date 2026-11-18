## Janus String Calculator v1.3

**What's new**
- Numba-accelerated core and multi-field modules (`core_jit`, `mf_jit`, `mfms`, `mfms_nc`).
- The SERAPIS pipeline and an exact Mukhanov–Sasaki checker (`tools/serapis_calc`: pipeline, ms_jit, nstar, relation, strings, meter, emulator).
- Standalone imports fixed, so the package runs from a plain clone.
- `requirements.txt` and `smoketest.py`: `pip install -r requirements.txt && python smoketest.py` gives 3/3 checks (φ², Starobinsky, SERAPIS-E) in about 20 s.

**Validation** is unchanged from v1.2 (Batteries A and B, J3–J7d; see README): n_s errors of about 10⁻⁶ against an exact solver, better than ASPIC at every scored point.

**License:** from v1.3, the AEGIS Community License. It is free for individuals, scientists, students, schools, nonprofits and public research. Any business or for-profit use needs the AEGIS Commercial License (COMMERCIAL_LICENSE.md). v1.0–v1.2 remain MIT.

**Support:** this is built by one independent researcher with the help of AI. To donate, email dannyeldridge54@gmail.com.

Zenodo: doi:10.5281/zenodo.24298159 (concept DOI).
