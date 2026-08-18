## Trusted Advisor Review
Reviewed the Security category in the management account. 5 core checks available on Basic support tier:
- Amazon S3 Bucket Permissions - Green (0 of 5 buckets have permission properties that grant global access)
- MFA on Root Account - Green (MFA is enabled on the root account)
- Security Groups - Specific Ports Unrestricted - Green (0 of 0 security group rules allow unrestricted access to a specific port)
- Amazon EBS Public Snapshots - Green (0 EBS snapshots marked as public)
- Amazon RDS Public Snapshots - Green (0 RDS snapshots marked as public)

Required a manual "Refresh all checks" for the first three to populate - they initially
showed as unevaluated (grey dash) rather than a pass/fail result.

Approximately 276 additional checks are listed but sourced from AWS Security Hub, not native
Trusted Advisor - these show no results since Security Hub isn't enabled in this account
(deliberately deferred to a future dedicated project).

## Organizations Integration
Enabling org-wide Trusted Advisor requires Business or Enterprise support. Not enabled for
this project, as upgrading solely to unlock this feature wasn't justified for a learning
environment. Conceptually understood: it would provide a consolidated view of Trusted Advisor
findings across all member accounts, similar in purpose to the Config aggregator built previously.
