import hashlib, pathlib, sys
expected='e351c1fc3f39e97f73d2d058bee9b8bf26bc00d6b7a90deeefd838519356f851'
folder=pathlib.Path(sys.argv[1])
wheels=list(folder.glob('opensim-4.6-2-cp313-cp313-manylinux*.whl'))
if len(wheels)!=1:
    raise SystemExit(f'Expected exactly one CPython 3.13 Linux wheel; found {len(wheels)}')
wheel=wheels[0]
actual=hashlib.file_digest(wheel.open('rb'),'sha256').hexdigest()
(folder/'SHA256SUMS.txt').write_text(f'{actual}  {wheel.name}\n')
print('wheel:',wheel.name,'SHA256:',actual)
if actual!=expected: raise SystemExit('FAIL: pinned SHA-256 mismatch; aborting')
print('PASS: wheel digest verified')
