# Control Tower Guardrails/Controls - Favstar Financial

## Mandatory (auto-applied by Control Tower on OU registration)

These were applied automatically the moment the Workloads OU was registered - not manually selected. Most protect Control Tower's own governance infrastructure (its Lambda functions, Config rules, CloudWatch, SNS topics) from being tampered with.

|Control|Type|
|-|-|
|Disallow changes to AWS Config Rules set up by Control Tower|Preventive|
|Disallow changes to Lambda functions set up by Control Tower|Preventive|
|Disallow changes to CloudWatch set up by Control Tower|Preventive|
|Disallow changes to Amazon SNS set up by Control Tower|Preventive|
|Disallow changes to IAM roles set up by AWS Control Tower and CloudFormation|Preventive|
|Disallow configuration changes to AWS Config|Preventive|
|Enable AWS Config in all available regions|Preventive|
|Disallow modifications to AWS Config recorder S3 buckets|Preventive|
|Disallow modifications to S3 buckets managed by Control Tower|Preventive|
|Disallow changes to CloudWatch Logs Log Groups|Preventive|

## Elective (deliberately selected for Workloads OU)

These were chosen manually, one of each control behavior type, to demonstrate the difference between stopping something before it happens, blocking it at creation, and catching it after the fact.

|Control|Type|Rationale|
|-|-|-|
|\[AWS-GR\_DISALLOW\_VPC\_INTERNET\_ACCESS] Disallow internet access for VPC instances|Preventive|Blocks internet exposure at the network layer|
|\[CT.S3.PR.1] Require S3 bucket block public access settings configured|Proactive|Stops non-compliant public S3 buckets at creation time|
|\[AWS-GR\_S3\_BUCKET\_PUBLIC\_READ\_PROHIBITED] Disallow public read access to S3 buckets|Detective|Catches public exposure if it ever drifts after creation|

## Key distinction learned

* **Mandatory** controls are non-negotiable and applied automatically by Control Tower the moment an OU is registered - mostly protecting Control Tower's own machinery.
* **Elective** controls are opt-in, chosen deliberately based on the workload's risk profile - in this case, a fintech environment prioritizing network isolation and data exposure prevention.

