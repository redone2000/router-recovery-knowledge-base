# Submitting Router Recovery Reports

Public recovery reports help improve this knowledge base, but not every support request belongs in a public issue.

Use this guide to decide what to share, what to remove, and where to send it.

## Use a GitHub Issue When

Open a public GitHub issue when your report can help other users and does not contain private information.

Good public reports include:

- exact router vendor, model, and hardware version
- firmware version before and after the attempt
- recovery method used
- computer IP address and router IP address
- whether the router acted as TFTP client or TFTP server
- whether upload completed
- whether the router actually booted and became usable
- official documentation links
- logs, packet notes, or screenshots with private data removed

Public reports are most useful when they separate observed facts from assumptions.

## Use Official Support When

Use the official Router Recovery support page when the request should not be public:

https://www.router-recovery.com/en/support

Use official support for:

- screenshots that may contain private information
- device identifiers that cannot be safely removed
- purchase, account, or app-specific questions
- recovery attempts that require back-and-forth troubleshooting
- cases where you are unsure what can be shared publicly

## Remove Sensitive Information

Do not publish:

- serial numbers
- MAC addresses
- passwords
- vendor account details
- unrelated private network names or devices
- proprietary firmware contents

If a screenshot is useful, crop or redact it before posting.

## What a Strong Report Looks Like

```text
Vendor: ASUS
Model: RT-AC86U
Hardware version / region: visible on label
Firmware before: unknown
Firmware attempted: official vendor firmware URL
Computer IP: 192.168.1.10
Router IP observed: 192.168.1.1
Method: TFTP recovery
TFTP direction: router requested file from computer
Transfer result: upload completed
Final result: router booted / router did not boot / still unknown
Evidence: packet notes, TFTP log, official source link
Unknowns: whether this applies to other hardware revisions
```

## Important Boundary

Do not report "recovery completed" just because a firmware transfer finished.

Use:

- "upload completed" when the file transfer completed
- "firmware accepted" only when there is evidence the router accepted the file
- "recovery completed" only when the router booted and became usable again

This distinction prevents misleading recovery instructions.
