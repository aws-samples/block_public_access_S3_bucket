## Automate blocking public access to Amazon S3 bucket using AWS event-driven solution

Data is a valuable asset for an organization and protecting it from internal or external unauthorized access guards the organization from financial loss, reputational harm, consumer trust degradation, and brand erosion. 

Storage solutions like Amazon Simple Storage Service (Amazon S3) can be used for a wide variety of use cases including cloud applications, dynamic websites, content distribution, mobile and gaming applications, and Big Data analytics. As Amazon S3 becomes an organization's multi-faceted and centralized datastore, it’s crucial to keep them private unless public access is absolutely necessary. By default, Amazon S3 has Block Public Access enabled at the bucket and the account level, access control lists (ACLs) disabled, and all new objects encrypted. Although these new defaults create a strong security posture, it does not prevent someone from either provisioning a new S3 bucket with block public access disabled or inadvertently disabling the  block public access on an existing S3 bucket. 

In this post, we will walk you through a proactive approach to detect public S3 buckets and automatically block all public access. This solution is built on event driven architecture which is cost effective and easy to deploy.

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.

