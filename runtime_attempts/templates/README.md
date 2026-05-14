# Runtime Attempt Templates

These templates are draft starting points for reference-device lab testing.

Use them by copying a template to a new dated file before filling values.

Do not edit `runtime_attempts/examples/` during live testing.

## Templates

| Device | Template | Purpose |
| --- | --- | --- |
| TP-Link Archer AX55 | `tplink_archer_ax55_tftp_direction_probe_template.json` | Determine whether TFTP is involved and classify active/passive direction |
| ASUS RT-AX86U | `asus_rt_ax86u_passive_tftp_template.json` | Test passive TFTP PUT and timing/port behavior |
| NETGEAR RAX40 | `netgear_rax40_tftp_orchestration_template.json` | Capture timing-sensitive TFTP/NMRP/orchestration behavior |

## Validation

After filling a copied template:

```text
python3 tools/validate_runtime_attempts.py <filled-attempt-file>
```

## Privacy

Keep these defaults unless there is an explicit reviewed reason to change them:

- `firmware_file.local_path_recorded: false`
- `privacy.local_only_by_default: true`
- `privacy.user_export_approved: false`
- `privacy.private_paths_redacted: true`
- `privacy.serials_redacted: true`

## Incident Rule

If a test fails, remains ambiguous, or reveals a timing/detail issue that can improve App success rate, keep the runtime attempt and create an incident candidate instead of editing a model profile directly.

Generate a first draft with:

```text
python3 tools/create_incident_from_runtime_attempt.py \
  --input <filled-runtime-attempt.json> \
  --output incidents/lab/<incident-id>.json \
  --symptom "<short symptom summary>"
```

Then review and edit the incident before treating it as evidence.
