#!/usr/bin/env bash
# Run the validator against its fixtures: good_* must pass, bad_* must fail.
cd "$(dirname "$0")/.."
fail=0
for f in tests/usfm/good*.usfm; do
  python3 -I scripts/check_usfm.py "$f" >/dev/null || { echo "FAIL (should pass): $f"; fail=1; }
done
for f in tests/usfm/bad_*.usfm; do
  python3 -I scripts/check_usfm.py "$f" >/dev/null && { echo "FAIL (should be rejected): $f"; fail=1; }
done
[ $fail = 0 ] && echo "all validator tests passed"
exit $fail
