#!/usr/bin/env python3
"""Compatibility entry point for repository validation."""

import sys

from agent_os import validate_source


report = validate_source()
report.print()
sys.exit(1 if report.errors else 0)
