# Test Repository for Tiered GitHub Actions Framework

This repository is used to test the Tiered GitHub Actions Framework implementation.

## Purpose
- Test fail-fast execution
- Validate skip label governance
- Measure CI resource savings
- Verify emergency override path

## Test Scenarios

### 1. Happy Path
- Small PR (<500 lines)
- Proper branch naming
- Valid ticket in title
- Reviewers assigned
- Expected: All tiers pass in ~3 minutes

### 2. Fail-Fast Tier 1
- Large PR (>500 lines)
- Expected: Auto-closed in ~15 seconds

### 3. Fail-Fast Tier 1.5
- Security vulnerability in code
- Expected: AI blocks, downstream cancelled in ~2 minutes

### 4. Emergency Override
- Invalid branch naming
- Add `emergency-override-approved` label
- Expected: All checks bypassed, audit trail logged

### 5. Skip Label Governance
- Try `skip:security` as non-admin
- Expected: Validation fails, check blocked

## Status
🧪 **Testing Phase 1 Pilot**
