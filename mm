#!/bin/bash
# MASTERMIND CLI — Run from mastermind/ or workspace root
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
exec python3 "$DIR/scripts/mm.py" "$@"
