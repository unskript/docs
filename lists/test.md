---
description: >-
  Many AWS services have quotas built in, but it can be tricky to discover the
  Service_code and quota code.
---

# AWS Service Quota list

```markdown
| Service Name | Quota Name | Quota Code | Quota Value | Quota Unit | Global? | Adjustable? |
| -------- | --- | --- | --- | --- | --- | --- |
| AWSCloudMap | DiscoverInstances operation per account steady rate | L-514A639A | 1000.0 | None | False | True | 
| AWSCloudMap | DiscoverInstances operation per account burst rate | L-76CF203B | 2000.0 | None | False | True | 
| AWSCloudMap | Namespaces per Region | L-0FE3F50E | 50.0mark | None | False | True | 
| access-analyzer | Policy generation CloudTrail time range | L-96F55078 | 90.0 | None | False | False | 
| access-analyzer | Archive rules per analyzer | L-1E51937C | 100.0 | None | False | True | 
| access-analyzer | CloudTrail log files processed per policy generation | L-5EFCE71D | 100000.0 | None | False | False | 
| access-analyzer | Concurrent policy generations | L-4599575C | 1.0 | None | False | False | 
| access-analyzer | Analyzers with an organization zone of trust | L-6F85FE0C | 5.0 | None | False | True | 
| access-analyzer | Policy generation CloudTrail data size | L-94099EDD | 25.0 | Gigabytes | False | False | 
| access-analyzer | Access previews per analyzer per hour | L-8750DAE0 | 1000.0 | None | False | True | 
| access-analyzer | Analyzers with an account zone of trust | L-2F63646F | 1.0 | None | False | False | 
| access-analyzer | Policy generations per day | L-FD4CD927 | 50.0 | None | False | False | 
| acm-pca | Rate of CreateCertificateAuthority requests | L-01B8608D | 1.0 | None | False | False | 
| acm-pca | Rate of PutPolicy requests | L-506CC328 | 5.0 | None | False | False | 
| acm-pca | Rate of DeleteCertificateAuthority requests | L-4065FDCB | 10.0 | None | False | False | 
| acm-pca | Rate of CreatePermission requests | L-773738D3 | 1.0 | None | False | False | 
| acm-pca | Rate of ListCertificateAuthorities requests | L-5A3CF806 | 20.0 | None | False | False | 
| acm-pca | Rate of CreateCertificateAuthorityAuditReport requests | L-C0A08797 | 1.0 | None | False | False | 
| acm-pca | Rate of GetPolicy requests | L-3549B861 | 5.0 | None | False | False | 
| acm-pca | Rate of ListTags requests | L-AF91D77C | 20.0 | None | False | False | 
| acm-pca | Number of revoked private certificates per CA | L-DFF54388 | 1000000.0 | None | False | False | 
| acm-pca | Rate of ImportCertificateAuthorityCertificate requests | L-D0C21409 | 10.0 | None | False | False | 
| acm-pca | Rate of IssueCertificate requests | L-CAFB4993 | 25.0 | None | False | True | 
| acm-pca | Rate of DeletePolicy requests | L-F4B48431 | 5.0 | None | False | False | 
| acm-pca | Rate of ListPermissions requests | L-20AFF03D | 5.0 | None | False | False | 
| acm-pca | Rate of DeletePermission requests | L-511291FD | 1.0 | None | False | False | 
| acm-pca | Rate of GetCertificate requests | L-1725E639 | 75.0 | None | False | True | 
| acm-pca | Rate of GetCertificateAuthorityCertificate requests | L-6C533034 | 20.0 | None | False | False | 
| acm-pca | Number of private certificate authorities (CAs) | L-799883CD | 200.0 | None | False | True | 
| acm-pca | Number of private certificates per CA | L-F99AB81B | 1000000.0 | None | False | True | 
| acm-pca | Rate of DescribeCertificateAuthority requests | L-46ADAC63 | 20.0 | None | False | False | 
| acm-pca | Rate of UntagCertificateAuthority requests | L-0CD1C07A | 10.0 | None | False | False | 
| acm-pca | Rate of GetCertificateAuthorityCsr requests | L-7D3D103D | 10.0 | None | False | False | 
| acm-pca | Rate of DescribeCertificateAuthorityAuditReport requests | L-6C9448CC | 20.0 | None | False | False | 
| acm-pca | Rate of RestoreCertificateAuthority requests | L-F3EBB4C3 | 20.0 | None | False | False | 
| acm-pca | Rate of UpdateCertificateAuthority requests | L-8FDDE81D | 10.0 | None | False | False | 
| acm-pca | Rate of TagCertificateAuthority requests | L-E464E2C8 | 10.0 | None | False | False | 
| acm-pca | Rate of RevokeCertificate requests | L-8842A328 | 20.0 | None | False | False | 
| airflow | Environments per account per Region | L-67D41C6B | 10.0 | None | False | True | 
| airflow | Workers per environment | L-78AC1883 | 25.0 | None | False | True | 
| amplify | Maximum app creations per hour | L-2FC3A2FA | 25.0 | None | False | False | 
| amplify | Domains per app | L-AD277529 | 5.0 | None | False | True | 
| amplify | Webhooks per app | L-4113FC04 | 50.0 | None | False | True | 
| amplify | Branches per app | L-A6716586 | 50.0 | None | False | True | 
| amplify | Environment cache artifact size | L-A0FC4951 | 5.0 | Gigabytes | False | False | 
| amplify | Manual deploy ZIP file size | L-D95E5509 | 5.0 | Gigabytes | False | False | 
| amplify | Subdomains per domain | L-85685B2E | 50.0 | None | False | True | 
| amplify | Concurrent jobs | L-2A8ABB91 | 5.0 | None | False | True | 
| amplify | Cache artifact size | L-EC4C0FC7 | 5.0 | Gigabytes | False | False | 
| amplify | Build artifact size | L-895E890C | 5.0 | Gigabytes | False | False | 
| amplify | Apps | L-1BED97F3 | 25.0 | None | False | True | 
| apigateway | Stage Variable Value Length | L-B2CF62DC | 512.0 | None | False | False | 
| apigateway | WebSocket new connections rate | L-9ED1E49A | 500.0 | None | False | True | 
| apigateway | Stage variables per stage | L-95BA6EA5 | 100.0 | None | False | False | 
| apigateway | API keys | L-1D180A63 | 10000.0 | None | False | False | 
| apigateway | API Payload Size | L-46624B39 | 10.0 | Megabytes | False | False | 
| apigateway | Client certificates | L-824C9E42 | 60.0 | None | False | True | 
| apigateway | Maximum integration timeout in milliseconds | L-E5AE38E3 | 29000.0 | Milliseconds | False | False | 
| apigateway | Regional APIs | L-AA0FF27B | 600.0 | None | False | False | 
| apigateway | Method ARN Length | L-5244589D | 1600.0 | Bytes | False | False | 
| apigateway | Maximum resource policy size in bytes | L-8B81B02C | 8192.0 | None | False | True | 
| apigateway | Subnets per VPC link(V2) | L-668C9B28 | 10.0 | None | False | True | 
| apigateway | WebSocket message payload size | L-FD0EB744 | 128.0 | Kilobytes | False | False | 
| apigateway | Throttle rate | L-8A5B8E43 | 10000.0 | None | False | True | 
| apigateway | Private APIs | L-A966AB5C | 600.0 | None | False | False | 
| apigateway | Custom Domain Names | L-A93447B8 | 120.0 | None | False | True | 
| apigateway | Usage plans per API key | L-985EB478 | 10.0 | None | False | True | 
| apigateway | Stages per API | L-379E48B0 | 10.0 | None | False | True | 
| apigateway | AWS Lambda authorizer result size | L-20859C74 | 8.0 | Kilobytes | False | False | 
| apigateway | WebSocket new connections burst rate | L-E1465507 | 500.0 | None | False | False | 
| apigateway | Stage Variable Key Length | L-3A613F94 | 64.0 | None | False | False | 
| apigateway | Throttle burst rate | L-CDF5615A | 5000.0 | None | False | False | 
| apigateway | Maximum Iterations In Mapping Template | L-8E6A5A87 | 1000.0 | None | False | False | 
| apigateway | VPC links(V2) | L-608BDCD4 | 10.0 | None | False | True | 
| apigateway | Tags Per Stage | L-FB4F0270 | 50.0 | None | False | False | 
| apigateway | Resources/Routes per REST/WebSocket API | L-01C8A9E0 | 300.0 | None | False | True | 
| apigateway | Maximum Combined Header Size | L-E9EEB922 | 10240.0 | Bytes | False | False | 
| apigateway | Edge-optimized APIs | L-B97207D0 | 120.0 | None | False | False | 
| apigateway | Regional API URL Length | L-A7033131 | 10240.0 | None | False | False | 
| apigateway | WebSocket Idle Connection Timeout | L-60AC41CD | 600.0 | Seconds | False | False | 
| apigateway | Maximum Cached Response Size | L-CC2525B6 | 1048576.0 | Bytes | False | False | 
| apigateway | Routes per HTTP API | L-65B5C802 | 300.0 | None | False | True | 
| apigateway | Connection duration for WebSocket API | L-A6CCE716 | 7200.0 | Seconds | False | False | 
| apigateway | Maximum API caching TTL | L-8C2F9A1D | 3600.0 | Seconds | False | False | 
| apigateway | API Stage throttles in a usage plan | L-A9DBC573 | 100.0 | None | False | False | 
| apigateway | VPC links | L-A4C7274F | 20.0 | None | False | True | 
| apigateway | Edge API URL Length | L-9C147DE4 | 8192.0 | None | False | False | 
| apigateway | WebSocket frame size | L-E11F7D5D | 32.0 | Kilobytes | False | False | 
| apigateway | Usage plans | L-E8693075 | 300.0 | None | False | True | 
| app-integrations | Data integration associations per data integration | L-3DEFA101 | 10.0 | None | False | True | 
| app-integrations | Event integration associations per event integration | L-C1BC25C8 | 10.0 | None | False | True | 
| app-integrations | Event integrations per region | L-152D3E9E | 10.0 | None | False | True | 
| app-integrations | Data integrations per region | L-013E1287 | 10.0 | None | False | True | 
| appconfig | Configuration size limit in AWS AppConfig hosted configuration store | L-48F9B951 | 1024.0 | Kilobytes | False | True | 
| appconfig | Maximum number of deployment strategies | L-F59D302B | 20.0 | None | False | True | 
| appconfig | Maximum number of configuration profiles per application | L-FA210A1F | 100.0 | None | False | True | 
| appconfig | Deployment size limit | L-A5FC0339 | 1024.0 | Kilobytes | False | True | 
| appconfig | Maximum number of environments per application | L-A52E46BE | 20.0 | None | False | True | 
| appconfig | Maximum number of applications | L-EEB0151E | 100.0 | None | False | True | 
| application-autoscaling | Scalable targets for EC2 | L-297D9EC9 | 500.0 | None | False | True | 
| application-autoscaling | Scaling policies per scalable target | L-B395C81B | 50.0 | None | False | False | 
| application-autoscaling | Scalable targets for Comprehend | L-17D5F681 | 500.0 | None | False | True | 
| application-autoscaling | Scalable targets for Amazon Keyspaces | L-799ACCDF | 500.0 | None | False | True | 
| application-autoscaling | Scalable targets for AppStream | L-8998F403 | 500.0 | None | False | True | 
| application-autoscaling | Scalable targets for EMR | L-D75CA9D2 | 500.0 | None | False | True | 
| application-autoscaling | Step adjustments per step scaling policy | L-9C25247C | 20.0 | None | False | False | 
| application-autoscaling | Scalable targets for custom resources | L-4A11ECEB | 500.0 | None | False | True | 
| application-autoscaling | Scheduled actions per scalable target | L-95848B5F | 200.0 | None | False | False | 
| application-autoscaling | Scalable targets for Lambda | L-A2AD6458 | 500.0 | None | False | True | 
| application-autoscaling | Scalable targets for SageMaker | L-1AAF0700 | 500.0 | None | False | True | 
| application-autoscaling | Scalable targets for ECS | L-782A3EE2 | 3000.0 | None | False | True | 
| application-autoscaling | Scalable targets for DynamoDB | L-A1D42901 | 5000.0 | None | False | True | 
| application-autoscaling | Scalable targets for RDS | L-800F6F7B | 500.0 | None | False | True | 
| application-autoscaling | Scalable targets for Amazon MSK | L-1A11EB4B | 500.0 | None | False | True | 
| appmesh | Connected Envoy processes per virtual node | L-606A910B | 50.0 | None | False | True | 
| appmesh | Connected Envoy processes per virtual gateway | L-33E8F9C9 | 50.0 | None | False | True | 
| appmesh | Gateway routes per virtual gateway | L-F6F26D09 | 10.0 | None | False | True | 
| appmesh | Virtual services per mesh | L-DA7495A7 | 200.0 | None | False | True | 
| appmesh | Meshes per account | L-AC861A39 | 15.0 | None | False | True | 
| appmesh | Weighted targets per route | L-AE1D9567 | 10.0 | None | False | False | 
| appmesh | Virtual gateways per mesh | L-87E74146 | 3.0 | None | False | True | 
| appmesh | Backends per virtual node | L-8775AB18 | 50.0 | None | False | False | 
| appmesh | Virtual routers per mesh | L-50F6C35A | 200.0 | None | False | True | 
| appmesh | Virtual nodes per mesh | L-E043DFB4 | 200.0 | None | False | True | 
| appmesh | Routes per virtual router | L-BB90B7FF | 50.0 | None | False | True | 
| athena | Active DDL queries | L-3CE0BBA0 | 20.0 | None | False | True | 
| athena | Active DML queries | L-FC5F6546 | 150.0 | None | False | True | 
| athena | Apache Spark DPU concurrency | L-5A8D5237 | 160.0 | None | False | False | 
| athena | DDL query timeout | L-56A94400 | 600.0 | None | False | False | 
| athena | DML query timeout | L-E80DC288 | 30.0 | None | False | True | 
| auditmanager | Custom controls | L-0255B75F | 500.0 | None | False | True | 
| auditmanager | Custom frameworks | L-8935A6F1 | 100.0 | None | False | True | 
| auditmanager | Running assessments | L-92B50F18 | 100.0 | None | False | True | 
| autoscaling | Launch configurations per region | L-6B80B8FA | 200.0 | None | False | True | 
| autoscaling | Auto Scaling groups per region | L-CDE20ADC | 500.0 | None | False | True | 
| autoscaling-plans | Scaling plans | L-BD401546 | 100.0 | None | False | True | 
| batch | Compute environment limit | L-144F0CA5 | 50.0 | None | False | False | 
| batch | Job dependencies limit | L-AD075A76 | 20.0 | None | False | False | 
| batch | Job payload size limit | L-6B86CF1E | 30.0 | None | False | False | 
| batch | Maximum array size limit | L-F9381E33 | 10000.0 | None | False | False | 
| batch | Submitted state jobs limit | L-65F8BA2C | 1000000.0 | None | False | False | 
| batch | Job queue limit | L-4CEA37AD | 50.0 | None | False | False | 
| batch | Compute environments per job queue limit. | L-F8102809 | 3.0 | None | False | False | 
| braket | Maximum number of instances of ml.g5.48xlarge for jobs | L-273D7A29 | 0.0 | None | False | False | 
| braket | Rate of SearchJobs requests | L-622972C3 | 5.0 | None | False | True | 
| braket | Rate of GetQuantumTask requests | L-69571C39 | 100.0 | None | False | True | 
| braket | Maximum number of instances of ml.p2.16xlarge for jobs | L-8FFA00B6 | 0.0 | None | False | True | 
| braket | Rate of GetJob requests | L-C4A587F5 | 5.0 | None | False | True | 
| braket | Maximum number of instances of ml.g5.8xlarge for jobs | L-F286AE81 | 0.0 | None | False | False | 
| braket | Rate of CreateJob requests | L-1E4A0B71 | 1.0 | None | False | True | 
| braket | Maximum number of instances of ml.c5.9xlarge for jobs | L-6717BDE3 | 1.0 | None | False | True | 
| braket | Number of concurrent jobs | L-65BEB721 | 5.0 | None | False | True | 
| braket | Maximum number of instances of ml.g4dn.16xlarge for jobs | L-D0B25526 | 0.0 | None | False | True | 
| braket | Number of concurrent SV1 tasks | L-5C6AF476 | 100.0 | None | False | False | 
| braket | Maximum number of instances of ml.c5.2xlarge for jobs | L-1DE68820 | 5.0 | None | False | True | 
| braket | Rate of SearchDevices requests | L-13BD7EBA | 5.0 | None | False | True | 
| braket | Maximum number of instances of ml.p3.2xlarge for jobs | L-BC259EA2 | 0.0 | None | False | True | 
| braket | Rate of API requests | L-C9622EC0 | 140.0 | None | False | True | 
| braket | Maximum number of instances of ml.p4d.24xlarge for jobs | L-6EBE29BC | 0.0 | None | False | False | 
| braket | Maximum number of instances of ml.m5.2xlarge for jobs | L-B4BD4D05 | 5.0 | None | False | True | 
| braket | Maximum number of instances of ml.m4.2xlarge for jobs | L-35C855B5 | 5.0 | None | False | True | 
| braket | Maximum number of instances of ml.m5.xlarge for jobs | L-CEDB9365 | 5.0 | None | False | True | 
| braket | Maximum number of instances of ml.g5.2xlarge for jobs | L-6ECB9FCD | 0.0 | None | False | False | 
| braket | Maximum number of instances of ml.m4.10xlarge for jobs | L-20DF4C21 | 0.0 | None | False | True | 
| braket | Maximum number of instances of ml.c4.4xlarge for jobs | L-96E0F810 | 5.0 | None | False | True | 
| braket | Maximum number of instances of ml.m4.xlarge for jobs | L-A7DE49A7 | 5.0 | None | False | True | 
| braket | Maximum number of instances of ml.c5n.9xlarge for jobs | L-F39A58EA | 0.0 | None | False | True | 
| braket | Maximum number of instances of ml.g4dn.xlarge for jobs | L-A95AE26D | 0.0 | None | False | True | 
| braket | Maximum number of instances of ml.c5.xlarge for jobs | L-6976A449 | 5.0 | None | False | True | 
| braket | Maximum number of instances of ml.c5n.18xlarge for jobs | L-9E03561A | 0.0 | None | False | True | 
| braket | Maximum number of instances of ml.p3.8xlarge for jobs | L-9716E5CC | 0.0 | None | False | True | 
| braket | Maximum number of instances of ml.g4dn.4xlarge for jobs | L-348592A9 | 0.0 | None | False | True | 
| braket | Number of concurrent DM1 tasks | L-B1492482 | 100.0 | None | False | False | 
| braket | Rate of SearchQuantumTasks requests | L-D6597555 | 5.0 | None | False | True | 
| braket | Maximum number of instances of ml.c5n.4xlarge for jobs | L-C32F31F5 | 0.0 | None | False | True | 
| braket | Rate of CreateQuantumTask requests | L-7DF279A8 | 20.0 | None | False | True | 
| braket | Maximum number of instances of ml.c4.8xlarge for jobs | L-196E4F38 | 5.0 | None | False | True | 
| braket | Maximum number of instances of ml.m5.4xlarge for jobs | L-935DC112 | 5.0 | None | False | True | 
| braket | Maximum number of instances of ml.m4.4xlarge for jobs | L-E4856358 | 2.0 | None | False | True | 
| braket | Maximum number of instances of ml.m5.24xlarge for jobs | L-8F2E9AB0 | 0.0 | None | False | True | 
| braket | Maximum number of instances of ml.g4dn.8xlarge for jobs | L-C3A58F27 | 0.0 | None | False | True | 
| braket | Maximum number of instances of ml.g5.xlarge for jobs | L-BC5AC149 | 0.0 | None | False | False | 
| braket | Maximum number of instances of ml.p3.16xlarge for jobs | L-949DCF20 | 0.0 | None | False | True | 
| braket | Maximum number of instances of ml.g4dn.2xlarge for jobs | L-05622A08 | 0.0 | None | False | True | 
| braket | Maximum number of instances of ml.c5n.xlarge for jobs | L-5A303583 | 0.0 | None | False | True | 
| braket | Maximum number of instances of ml.p2.xlarge for jobs | L-2145059B | 0.0 | None | False | True | 
| braket | Maximum number of instances of ml.c4.xlarge for jobs | L-899E4166 | 5.0 | None | False | True | 
| braket | Maximum number of instances of ml.p3dn.24xlarge for jobs | L-786BEA40 | 0.0 | None | False | False | 
| braket | Rate of GetDevice requests | L-08E356CB | 5.0 | None | False | True | 
| braket | Rate of CancelQuantumTask requests | L-4ADC64FC | 2.0 | None | False | True | 
| braket | Maximum number of instances of ml.g5.4xlarge for jobs | L-7D59777E | 0.0 | None | False | False | 
| braket | Maximum number of instances of ml.p2.8xlarge for jobs | L-135B0588 | 0.0 | None | False | True | 
| braket | Maximum number of instances of ml.m5.12xlarge for jobs | L-8EBDBB73 | 0.0 | None | False | True | 
| braket | Maximum number of instances of ml.c5.4xlarge for jobs | L-0454F2B6 | 1.0 | None | False | True | 
| braket | Maximum number of instances of ml.g5.12xlarge for jobs | L-223B68D6 | 0.0 | None | False | False | 
| braket | Rate of CancelJob requests | L-9F76E1C6 | 2.0 | None | False | True | 
| braket | Maximum number of instances of ml.g5.24xlarge for jobs | L-DFDAABC1 | 0.0 | None | False | False | 
| braket | Maximum number of instances of ml.g5.16xlarge for jobs | L-6E6AF581 | 0.0 | None | False | False | 
| braket | Maximum number of instances of ml.g4dn.12xlarge for jobs | L-3A92FCE1 | 0.0 | None | False | True | 
| braket | Maximum number of instances of ml.m5.large for jobs | L-D01386EB | 5.0 | None | False | True | 
| braket | Maximum number of instances of ml.c5.18xlarge for jobs | L-D76EFBC9 | 0.0 | None | False | True | 
| braket | Number of concurrent TN1 tasks | L-A41DADC7 | 10.0 | None | False | True | 
| braket | Maximum number of instances of ml.c5n.2xlarge for jobs | L-8B0E23AD | 0.0 | None | False | True | 
| braket | Maximum number of instances of ml.c4.2xlarge for jobs | L-BDA9BB2A | 5.0 | None | False | True | 
| braket | Maximum number of instances of ml.m4.16xlarge for jobs | L-15DC2286 | 0.0 | None | False | True | 
| cases | CreateField burst quota | L-F4DAA62B | 5.0 | None | False | True | 
| cases | UpdateCase rate quota | L-6FE92BD9 | 2.0 | None | False | True | 
| cases | SearchRelatedItems burst quota | L-5E8805C5 | 10.0 | None | False | True | 
| cases | ListTagsForResource burst quota | L-4CE16517 | 10.0 | None | False | True | 
| cases | UpdateCase burst quota | L-1D2B06EC | 10.0 | None | False | True | 
| cases | CreateDomain rate quota | L-9BEF063B | 2.0 | None | False | True | 
| cases | SearchRelatedItems rate quota | L-3B58A5D3 | 2.0 | None | False | True | 
| cases | CreateRelatedItem burst quota | L-5A125C02 | 10.0 | None | False | True | 
| cases | Fields per domain | L-C5B69356 | 50.0 | None | False | True | 
| cases | UpdateLayout rate quota | L-D69D3749 | 2.0 | None | False | True | 
| cases | UntagResource rate quota | L-515ED5E2 | 2.0 | None | False | True | 
| cases | CreateField rate quota | L-497703F2 | 2.0 | None | False | True | 
| cases | ListFields rate quota | L-D750A577 | 2.0 | None | False | True | 
| cases | UpdateField rate quota | L-CC009CC4 | 2.0 | None | False | True | 
| cases | ListFieldOptions rate quota | L-B7E2C410 | 6.0 | None | False | True | 
| cases | Domains | L-C2B81BC3 | 5.0 | None | False | True | 
| cases | BatchPutFieldOptions burst quota | L-A298B896 | 5.0 | None | False | True | 
| cases | CreateRelatedItem rate quota | L-1F185B9F | 2.0 | None | False | True | 
| cases | ListFields burst quota | L-7CF7A4F0 | 5.0 | None | False | True | 
| cases | ListCasesForContact rate quota | L-A246B577 | 2.0 | None | False | True | 
| cases | ListTemplates rate quota | L-1F4F11B7 | 2.0 | None | False | True | 
| cases | GetCase burst quota | L-7D6B0EAF | 15.0 | None | False | True | 
| cases | ListLayouts rate quota | L-4B3D8F5F | 2.0 | None | False | True | 
| cases | CreateCase rate quota | L-8FEA710A | 2.0 | None | False | True | 
| cases | UpdateTemplate rate quota | L-B5BE889D | 2.0 | None | False | True | 
| cases | ListFieldOptions burst quota | L-85809F5E | 15.0 | None | False | True | 
| cases | GetTemplate burst quota | L-1320C83D | 20.0 | None | False | True | 
| cases | SearchCases rate quota | L-AA3996A0 | 2.0 | None | False | True | 
| cases | CreateLayout rate quota | L-7736E0FB | 2.0 | None | False | True | 
| cases | Case fields per layout | L-5B5E62BD | 30.0 | None | False | True | 
| cases | UpdateLayout burst quota | L-6743683C | 5.0 | None | False | True | 
| cases | BatchGetField burst quota | L-D3F1EBFD | 25.0 | None | False | True | 
| cases | GetTemplate rate quota | L-8AA97C3E | 6.0 | None | False | True | 
| cases | PutCaseEventConfiguration rate quota | L-5462CD7A | 2.0 | None | False | True | 
| cases | GetLayout rate quota | L-E5EE4EDA | 6.0 | None | False | True | 
| cases | SearchCases burst quota | L-533535BF | 10.0 | None | False | True | 
| cases | ListTemplates burst quota | L-B3BCA676 | 10.0 | None | False | True | 
| cases | CreateCase burst quota | L-085C6605 | 10.0 | None | False | True | 
| cases | GetLayout burst quota | L-B3860F14 | 20.0 | None | False | True | 
| cases | ListLayouts burst quota | L-960AA7D7 | 10.0 | None | False | True | 
| cases | CreateLayout burst quota | L-FF9E638C | 5.0 | None | False | True | 
| cases | TagResource burst quota | L-1ECD16ED | 10.0 | None | False | True | 
| cases | PutCaseEventConfiguration burst quota | L-D4F270D6 | 10.0 | None | False | True | 
| cases | CreateDomain burst quota | L-B4BF7E31 | 5.0 | None | False | True | 
| cases | BatchGetField rate quota | L-2A8092BB | 8.0 | None | False | True | 
| cases | UpdateField burst quota | L-A96CA735 | 5.0 | None | False | True | 
| cases | Templates per domain | L-0482161A | 25.0 | None | False | True | 
| cases | ListDomains rate quota | L-97677C0C | 2.0 | None | False | True | 
| cases | GetCaseEventConfiguration burst quota | L-74EA148C | 10.0 | None | False | True | 
| cases | Field options per field | L-E52A0E46 | 100.0 | None | False | True | 
| cases | Layouts per domain | L-D0ED993F | 25.0 | None | False | True | 
| cases | BatchPutFieldOptions rate quota | L-F5011010 | 2.0 | None | False | True | 
| cases | GetDomain burst quota | L-9B7552E3 | 5.0 | None | False | True | 
| cases | CreateTemplate burst quota | L-E77680D7 | 5.0 | None | False | True | 
| cases | GetCase rate quota | L-8B6DA341 | 4.0 | None | False | True | 
| cases | ListCasesForContact burst quota | L-FF304B65 | 10.0 | None | False | True | 
| cases | GetDomain rate quota | L-FD0EC666 | 2.0 | None | False | True | 
| cases | TagResource rate quota | L-C0E6C678 | 2.0 | None | False | True | 
| cases | ListTagsForResource rate quota | L-F62E3726 | 2.0 | None | False | True | 
| cases | Related items per case | L-C1AF8D37 | 50.0 | None | False | True | 
| cases | ListDomains burst quota | L-3255B73C | 5.0 | None | False | True | 
| cases | UpdateTemplate burst quota | L-2AD9F9AD | 5.0 | None | False | True | 
| cases | GetCaseEventConfiguration rate quota | L-D69B27B2 | 2.0 | None | False | True | 
| cases | UntagResource burst quota | L-AE0F3125 | 10.0 | None | False | True | 
| cases | CreateTemplate rate quota | L-26EE2CFC | 2.0 | None | False | True | 
| cassandra | Table-level read throughput quota | L-17766544 | 40000.0 | None | False | True | 
| cassandra | Max clustering key size | L-0659E12E | 850.0 | Bytes | False | False | 
| cassandra | Max row size | L-66AD5703 | 1.0 | Megabytes | False | False | 
| cassandra | Max partition key size | L-324B5396 | 2048.0 | Bytes | False | False | 
| cassandra | Max concurrent table restores using Point-in-time Recovery (PITR) | L-F41E662B | 4.0 | None | False | True | 
| cassandra | Max amount of data restored using Point-in-time Recovery (PITR) | L-4C49F3DB | 5.0 | Terabytes | False | True | 
| cassandra | Max static data per logical partition | L-5823D982 | 1.0 | Megabytes | False | False | 
| cassandra | Account-level write throughput quota (Provisioned mode) | L-2C5B14BD | 80000.0 | None | False | True | 
| cassandra | Table-level write throughput quota | L-3D8ED127 | 40000.0 | None | False | True | 
| cassandra | Max Schema size | L-E08A04C1 | 358400.0 | Bytes | False | False | 
| cassandra | Keyspaces per region | L-677FFD22 | 256.0 | None | False | True | 
| cassandra | Account-level read throughput quota (Provisioned mode) | L-E7DB0CFF | 80000.0 | None | False | True | 
| cassandra | Concurrent DDL operations | L-29E90199 | 50.0 | None | False | False | 
| cassandra | Tables per region | L-BF48748A | 256.0 | None | False | True | 
| chime | Chime SDK Meetings - all meeting management API requests rate limit in transactions per second | L-F147F728 | 10.0 | None | False | False | 
| chime | Chime SDK Meetings - CreateMeeting burst limit | L-FE9F896D | 20.0 | None | False | False | 
| chime | Chime SDK Meetings - DeleteAttendee burst limit | L-398B2BD6 | 20.0 | None | False | False | 
| chime | Chime SDK Meetings - all meeting management API requests burst limit | L-63907FE3 | 20.0 | None | False | False | 
| chime | Chime SDK Meetings - GetMeeting burst limit | L-58F5D62D | 20.0 | None | False | False | 
| chime | Chime SDK Meetings - TagResource rate limit in transactions per second | L-3BB10AA7 | 10.0 | None | False | False | 
| chime | Amazon Chime SDK Media Pipelines - total active media pipelines per account | L-7F583998 | 10.0 | None | False | True | 
| chime | Chime SDK Meetings - maximum concurrent video streams published per meeting | L-AC1D2091 | 25.0 | None | False | True | 
| chime | Chime SDK Meetings - CreateAttendee burst limit | L-6B38EB2F | 20.0 | None | False | False | 
| chime | Chime SDK Meetings - ListAttendees burst limit | L-C875D9AA | 20.0 | None | False | False | 
| chime | Chime SDK Meetings - UnTagResource rate limit in transactions per second | L-1AB05505 | 10.0 | None | False | False | 
| chime | Chime SDK Meetings - DeleteAttendee rate limit in transactions per second | L-2C15A6A8 | 10.0 | None | False | False | 
| chime | Chime SDK Meetings - UpdateAttendeeCapabilities burst limit | L-674630CB | 20.0 | None | False | False | 
| chime | Chime SDK Meetings - DeleteMeeting rate limit in transactions per second | L-48F4CA7A | 10.0 | None | False | False | 
| chime | Chime SDK Meetings - CreateMeetingWithAttendees rate limit in transactions per second | L-5F1ABF39 | 10.0 | None | False | False | 
| chime | Chime SDK Meetings - ListTagsForResource burst limit | L-E79A53C7 | 20.0 | None | False | False | 
| chime | Chime SDK Meetings - BatchCreateAttendees burst limit | L-98193B78 | 20.0 | None | False | False | 
| chime | Chime SDK Meetings - attendees per meeting | L-B1CE561B | 250.0 | None | False | False | 
| chime | Chime SDK Meetings - BatchUpdateAttendeeCapabilitiesExcept burst limit | L-7846C766 | 20.0 | None | False | False | 
| chime | Chime SDK Meetings - CreateAttendee rate limit in transactions per second | L-563605EA | 10.0 | None | False | False | 
| chime | Chime SDK Meetings - BatchCreateAttendees rate limit in transactions per second | L-7B4DA565 | 10.0 | None | False | False | 
| chime | Chime SDK Meetings - TagResource burst limit | L-DA021F73 | 20.0 | None | False | False | 
| chime | Amazon Chime SDK Media Pipelines - rate limit for all media pipeline API requests in transactions per second | L-804108DA | 10.0 | None | False | True | 
| chime | Chime SDK Meetings - CreateMeeting rate limit in transactions per second | L-8A6E3C7B | 10.0 | None | False | False | 
| chime | Chime SDK Meetings - maximum concurrent video streams subscribed per attendee | L-0E2E2226 | 25.0 | None | False | False | 
| chime | Chime SDK Meetings - UpdateAttendeeCapabilities rate limit in transactions per second | L-3CC08C2F | 10.0 | None | False | False | 
| chime | Chime SDK Meetings - ListMeetings burst limit | L-771FFB29 | 20.0 | None | False | False | 
| chime | Chime SDK Meetings - BatchUpdateAttendeeCapabilitiesExcept rate limit in transactions per second | L-44BD764A | 10.0 | None | False | False | 
| chime | Chime SDK Meetings - UnTagResource burst limit | L-FA316003 | 20.0 | None | False | False | 
| chime | Chime SDK Meetings - ListTagsForResource rate limit in transactions per second | L-B103920E | 10.0 | None | False | False | 
| chime | Chime SDK Meetings - CreateMeetingWithAttendees burst limit | L-91426809 | 20.0 | None | False | False | 
| chime | Chime SDK Meetings - replica meetings per primary meeting | L-154D84D0 | 4.0 | None | False | True | 
| chime | Chime SDK Meetings - DeleteMeeting burst limit | L-A42FC7C2 | 20.0 | None | False | False | 
| chime | Chime SDK Meetings - ListAttendees rate limit in transactions per second | L-37BA0833 | 10.0 | None | False | False | 
| chime | Chime SDK Meetings - GetMeeting rate limit in transactions per second | L-6FAB55D2 | 10.0 | None | False | False | 
| chime | Chime SDK Meetings - ListMeetings rate limit in transactions per second | L-793B6D9C | 10.0 | None | False | False | 
| cloudformation | Stack instance operations per administrator account | L-6A4B2F69 | 10000.0 | None | False | True | 
| cloudformation | Stack instances per stack set | L-C8225BA5 | 100000.0 | None | False | True | 
| cloudformation | Stack sets per administrator account | L-EC62D81A | 1000.0 | None | False | True | 
| cloudformation | Output count in CloudFormation template | L-87D14FB7 | 200.0 | None | False | False | 
| cloudformation | Stack count | L-0485CB21 | 2000.0 | None | False | True | 
| cloudhsm | Clusters per AWS Region and AWS account | L-4B16B391 | 4.0 | None | False | True | 
| cloudhsm | HSMs per AWS Region and AWS account | L-95BA35D1 | 6.0 | None | False | True | 
| codeguru-profiler | Number of profiling groups per account and region. | L-DA8D4E8D | 50.0 | None | False | True | 
| codeguru-reviewer | Allowed Code Reviews | L-F5129FC6 | 5000.0 | None | False | True | 
| cognito-idp | Rate of UserAccountRecovery requests | L-7D6E8ED3 | 30.0 | None | False | False | 
| cognito-idp | Rate of UserCreation requests | L-5987B8A0 | 50.0 | None | False | True | 
| cognito-idp | Rate of UserPoolResourceUpdate requests per account | L-B7575496 | 15.0 | None | False | False | 
| cognito-idp | Rate of UserRead requests | L-D6BD5178 | 120.0 | None | False | True | 
| cognito-idp | User pools per account | L-66E6DF30 | 1000.0 | None | False | True | 
| cognito-idp | Resource servers per user pool | L-7CDAF993 | 25.0 | None | False | True | 
| cognito-idp | Rate of UserResourceUpdate requests | L-574C86AE | 25.0 | None | False | False | 
| cognito-idp | Rate of UserPoolUpdate requests | L-60A0B411 | 15.0 | None | False | False | 
| cognito-idp | Rate of UserPoolClientUpdate requests per account | L-12C4D74A | 15.0 | None | False | False | 
| cognito-idp | Rate of UserList requests | L-259E3368 | 30.0 | None | False | False | 
| cognito-idp | Rate of UserAuthentication requests | L-026ADBA3 | 120.0 | None | False | True | 
| cognito-idp | Rate of UserPoolClientRead requests per account | L-A412573D | 15.0 | None | False | False | 
| cognito-idp | Rate of UserFederation requests | L-BB3E7CCF | 25.0 | None | False | True | 
| cognito-idp | Identity providers per user pool | L-1B44D826 | 300.0 | None | False | True | 
| cognito-idp | Rate of UserPoolRead requests | L-CFFBE34A | 15.0 | None | False | False | 
| cognito-idp | Rate of UserResourceRead requests | L-55545DC8 | 50.0 | None | False | True | 
| cognito-idp | User import jobs per user pool | L-681BB884 | 1000.0 | None | False | True | 
| cognito-idp | Rate of UserUpdate requests | L-6621E65D | 25.0 | None | False | False | 
| cognito-idp | Rate of UserPoolResourceRead requests per account | L-A01C9633 | 20.0 | None | False | False | 
| cognito-idp | Rate of UserToken requests | L-F21F8BB4 | 120.0 | None | False | True | 
| cognito-idp | Apps per user pool | L-5EAB0605 | 1000.0 | None | False | True | 
| comprehend | DeleteEntityRecognizer throttle limit in transactions per second | L-E7F70588 | 1.0 | None | False | False | 
| comprehend | DetectEntities max active jobs | L-2B8ECCAB | 10.0 | None | False | False | 
| comprehend | DetectDominantLanguage throttle limit in transactions per second | L-1F3990DA | 40.0 | None | False | True | 
| comprehend | DescribeEntityRecognizer throttle limit in transactions per second | L-F039F1E3 | 10.0 | None | False | False | 
| comprehend | TagResource throttle limit in transactions per second | L-9A845B3A | 1.0 | None | False | False | 
| comprehend | StopTrainingEntityRecognizer throttle limit in transactions per second | L-CF92EEE2 | 1.0 | None | False | False | 
| comprehend | StopKeyPhrasesDetectionJob throttle limit in transactions per second | L-C7E12CA2 | 1.0 | None | False | False | 
| comprehend | Endpoints max active endpoints | L-55642075 | 10.0 | None | False | True | 
| comprehend | DeleteDocumentClassifier throttle limit in transactions per second | L-D6BBB77F | 1.0 | None | False | False | 
| comprehend | DescribeTopicsDetectionJob throttle limit in transactions per second | L-13A0494F | 10.0 | None | False | False | 
| comprehend | CreateDocumentClassifier throttle limit in transactions per second | L-243FFDDD | 1.0 | None | False | False | 
| comprehend | StopEntitiesDetectionJob throttle limit in transactions per second | L-0B530363 | 1.0 | None | False | False | 
| comprehend | BatchDetectKeyPhrases throttle limit in transactions per second | L-DFE056B4 | 10.0 | None | False | True | 
| comprehend | CreateEntityRecognizer throttle limit in transactions per second | L-A207C175 | 1.0 | None | False | False | 
| comprehend | StopSentimentDetectionJob throttle limit in transactions per second | L-10AEC0BE | 1.0 | None | False | False | 
| comprehend | ListDocumentClassificationJobs throttle limit in transactions per second | L-A1F7E693 | 10.0 | None | False | False | 
| comprehend | ListTagsForResource throttle limit in transactions per second | L-D4C039C8 | 10.0 | None | False | False | 
| comprehend | Endpoints max inference units per endpoint | L-70EC2949 | 10.0 | None | False | True | 
| comprehend | DescribeDocumentClassificationJob throttle limit in transactions per second | L-91446453 | 10.0 | None | False | False | 
| comprehend | StartSentimentDetectionJob throttle limit in transactions per second | L-7B91C94D | 1.0 | None | False | False | 
| comprehend | DetectDominantLanguage max active jobs | L-7AC96081 | 10.0 | None | False | False | 
| comprehend | ListDocumentClassifiers throttle limit in transactions per second | L-7820536E | 10.0 | None | False | False | 
| comprehend | StopDominantLanguageDetectionJob throttle limit in transactions per second | L-67D99149 | 1.0 | None | False | False | 
| comprehend | StartDominantLanguageDetectionJob throttle limit in transactions per second | L-3FD9ACEB | 1.0 | None | False | False | 
| comprehend | DetectEntities throttle limit in transactions per second | L-F7FB6495 | 20.0 | None | False | True | 
| comprehend | DetectSyntax throttle limit in transactions per second | L-6823DD44 | 20.0 | None | False | True | 
| comprehend | DescribeSentimentDetectionJob throttle limit in transactions per second | L-E0EFA344 | 10.0 | None | False | False | 
| comprehend | BatchDetectSyntax throttle limit in transactions per second | L-223FEB32 | 10.0 | None | False | True | 
| comprehend | DescribeDominantLanguageDetectionJob throttle limit in transactions per second | L-60ABC79C | 10.0 | None | False | False | 
| comprehend | ListEntitiesDetectionJobs throttle limit in transactions per second | L-40A899B3 | 10.0 | None | False | False | 
| comprehend | ListDominantLanguageDetectionJobs throttle limit in transactions per second | L-8532F92C | 10.0 | None | False | False | 
| comprehend | StopTrainingDocumentClassifier throttle limit in transactions per second | L-E1D53C9F | 1.0 | None | False | False | 
| comprehend | Endpoints max inference units per account | L-2A73DEBC | 100.0 | None | False | True | 
| comprehend | StartKeyPhrasesDetectionJob throttle limit in transactions per second | L-4D712CC8 | 1.0 | None | False | False | 
| comprehend | BatchDetectSentiment throttle limit in transactions per second | L-F48BA15E | 10.0 | None | False | True | 
| comprehend | BatchDetectEntities throttle limit in transactions per second | L-4CF72A70 | 10.0 | None | False | True | 
| comprehend | DetectKeyPhrases throttle limit in transactions per second | L-D11AB353 | 20.0 | None | False | True | 
| comprehend | DetectSentiment throttle limit in transactions per second | L-370FF492 | 20.0 | None | False | True | 
| comprehend | ListSentimentDetectionJobs throttle limit in transactions per second | L-13861BA2 | 10.0 | None | False | False | 
| comprehend | ListKeyPhrasesDetectionJobs throttle limit in transactions per second | L-E9B0ABA2 | 10.0 | None | False | False | 
| comprehend | DescribeKeyPhrasesDetectionJob throttle limit in transactions per second | L-3E342F88 | 10.0 | None | False | False | 
| comprehend | DocumentClassification max active jobs | L-E65FE76A | 10.0 | None | False | False | 
| comprehend | DetectSentiment max active jobs | L-32ABBB12 | 10.0 | None | False | False | 
| comprehend | StartDocumentClassificationJob throttle limit in transactions per second | L-5674A323 | 1.0 | None | False | False | 
| comprehend | DocumentClassifier max active jobs | L-94042C4D | 10.0 | None | False | False | 
| comprehend | TopicsDetection max active jobs | L-F2BED405 | 10.0 | None | False | False | 
| comprehend | UntagResource throttle limit in transactions per second | L-6ECBDFF6 | 1.0 | None | False | False | 
| comprehend | DescribeEntitiesDetectionJob throttle limit in transactions per second | L-428EEE9B | 10.0 | None | False | False | 
| comprehend | StartTopicsDetectionJob throttle limit in transactions per second | L-F91E977B | 1.0 | None | False | False | 
| comprehend | ListEntityRecognizers throttle limit in transactions per second | L-5BADD54F | 10.0 | None | False | False | 
| comprehend | DescribeDocumentClassifier throttle limit in transactions per second | L-C39735E0 | 10.0 | None | False | False | 
| comprehend | StartEntitiesDetectionJob throttle limit in transactions per second | L-8DD67684 | 1.0 | None | False | False | 
| comprehend | ListTopicsDetectionJobs throttle limit in transactions per second | L-438FD9AD | 10.0 | None | False | False | 
| comprehend | DetectKeyPhrases max active jobs | L-BFFD1421 | 10.0 | None | False | False | 
| comprehend | BatchDetectDominantLanguage throttle limit in transactions per second | L-FD6FC352 | 10.0 | None | False | True | 
| comprehend | EntityRecognizer max active jobs | L-4BDB4A9D | 10.0 | None | False | False | 
| connect | Amazon Connect instance count | L-AA17A6B9 | 2.0 | None | False | True | 
| connect-campaigns | Amazon Connect High-Volume Outbound Communications campaign count | L-7F7B4C39 | 25.0 | None | False | True | 
| databrew | Rulesets per dataset | L-131D2768 | 10.0 | None | False | True | 
| databrew | Jobs per AWS account | L-0D2C4DFC | 100.0 | None | False | True | 
| databrew | Recipes per AWS account | L-EE2782A4 | 100.0 | None | False | True | 
| databrew | Schedules per AWS account | L-BF3E0A94 | 10.0 | None | False | True | 
| databrew | Rulesets per AWS account | L-955A1FA6 | 100.0 | None | False | True | 
| databrew | Rules per ruleset | L-640ABD4F | 100.0 | None | False | True | 
| databrew | Concurrent jobs per AWS account | L-935D4120 | 10.0 | None | False | True | 
| databrew | Open projects per AWS account | L-5748848E | 10.0 | None | False | True | 
| databrew | Datasets per AWS account | L-940C8930 | 100.0 | None | False | True | 
| databrew | Projects per AWS account | L-CE9E9D8D | 100.0 | None | False | True | 
| databrew | Versions per recipe | L-A386FCB8 | 100.0 | None | False | True | 
| dataexchange | Revisions per Amazon S3 data access data set | L-70B0F91E | 5.0 | None | False | True | 
| dataexchange | Revisions per addRevisions change set | L-916D9CEE | 5.0 | None | False | False | 
| dataexchange | AWS Lake Formation data permission assets per revision | L-D470FF0C | 20.0 | None | False | True | 
| dataexchange | Products per data set | L-D05CF9CD | 100.0 | None | False | True | 
| dataexchange | Concurrent in progress jobs to import assets from an AWS Lake Formation tag policy | L-426BE746 | 5.0 | None | False | False | 
| dataexchange | Concurrent in progress jobs to import assets from Amazon S3 | L-307F71B5 | 10.0 | None | False | False | 
| dataexchange | Revisions per data set | L-375806A0 | 10000.0 | None | False | True | 
| dataexchange | Concurrent in progress jobs to create Amazon S3 data access assets from S3 buckets | L-7878C4C3 | 5.0 | None | False | False | 
| dataexchange | Assets per import job from Amazon S3 | L-694A226E | 100.0 | None | False | False | 
| dataexchange | Concurrent in progress jobs to export assets to a signed URL | L-52FCAA8A | 10.0 | None | False | False | 
| dataexchange | Assets per revision | L-92FCD39C | 10000.0 | None | False | True | 
| dataexchange | Asset per export job from Amazon S3 | L-B13AFAD0 | 100.0 | None | False | False | 
| dataexchange | Concurrent in progress jobs to import assets from Amazon API Gateway | L-A1C96D1F | 10.0 | None | False | False | 
| dataexchange | Revisions per AWS Lake Formation data permission data set | L-A15CB065 | 20.0 | None | False | True | 
| dataexchange | Concurrent in progress jobs to export assets to Amazon S3 | L-37C425C6 | 10.0 | None | False | False | 
| dataexchange | Asset size in GB | L-514CB613 | 100.0 | Gigabytes | False | False | 
| dataexchange | Amazon API Gateway API assets per revision | L-4F329808 | 20.0 | None | False | True | 
| dataexchange | Amazon S3 data access assets per revision | L-60973A49 | 5.0 | None | False | True | 
| dataexchange | Concurrent in progress jobs to import assets from a signed URL | L-50515269 | 10.0 | None | False | False | 
| dataexchange | Data sets per account | L-52E2E63A | 3000.0 | None | False | True | 
| dataexchange | Revisions per Amazon API Gateway API data set | L-237CFF3D | 20.0 | None | False | True | 
| dataexchange | Concurrent in progress jobs to export revisions to Amazon S3 | L-09B749AD | 5.0 | None | False | False | 
| dlm | Policies per Region | L-5407D8DA | 100.0 | None | False | True | 
| dlm | Target accounts per sharing rule | L-DCA05F2F | 50.0 | None | False | True | 
| dms | Event subscriptions | L-D97343A2 | 60.0 | None | False | True | 
| dms | Endpoint count | L-E17328E9 | 1000.0 | None | False | True | 
| dms | Endpoints per instance | L-2146F1FD | 100.0 | None | False | True | 
| dms | Certificate count | L-FE918D88 | 100.0 | None | False | True | 
| dms | Replication instances | L-C2341CDC | 60.0 | None | False | True | 
| dms | Total storage | L-BBDCBDC8 | 30000.0 | Gigabytes | False | True | 
| dms | Task count | L-7FD3593B | 600.0 | None | False | True | 
| dms | Subnets per subnet group | L-4182EDE9 | 60.0 | None | False | True | 
| dms | Subnet groups | L-27B24FAD | 60.0 | None | False | True | 
| drs | Concurrent jobs in progress | L-D88FAC3A | 20.0 | None | False | False | 
| drs | Max Total replicating source servers Per AWS Account | L-C1D14A2B | 300.0 | None | False | True | 
| drs | Max source servers in all Jobs | L-05AFA8C6 | 200.0 | None | False | False | 
| drs | Max Total source servers Per AWS Account | L-E28BE5E0 | 3000.0 | None | False | True | 
| drs | Max source servers in a single Job | L-B827C881 | 200.0 | None | False | False | 
| drs | Max concurrent Jobs per source server | L-DD6D028C | 1.0 | None | False | False | 
| dynamodb | Concurrent control plane operations | L-1BB77E89 | 500.0 | None | False | True | 
| dynamodb | Provisioned capacity decreases per day | L-F3CA5463 | 27.0 | None | False | True | 
| dynamodb | Global Secondary Indexes per table | L-F7858A77 | 20.0 | None | False | True | 
| dynamodb | Write throughput limit for DynamoDB Streams (Provisioned mode) | L-923BEB7A | 40000.0 | None | False | True | 
| dynamodb | Maximum number of tables | L-F98FE922 | 2500.0 | None | False | True | 
| dynamodb | Table-level write throughput limit | L-AB614373 | 40000.0 | None | False | True | 
| dynamodb | Account-level write throughput limit (Provisioned mode) | L-34F8CCC8 | 80000.0 | None | False | True | 
| dynamodb | Table-level read throughput limit | L-CF0CBE56 | 40000.0 | None | False | True | 
| dynamodb | Account-level read throughput limit (Provisioned mode) | L-34F6A552 | 80000.0 | None | False | True | 
| ebs | PutSnapshotBlock requests per snapshot | L-1774F84A | 1000.0 | None | False | False | 
| ebs | ListSnapshotBlocks requests per account | L-18E976AB | 50.0 | None | False | False | 
| ebs | Pending snapshots per account | L-94D7AB7D | 100.0 | None | False | False | 
| ebs | ListChangedBlocks requests per account | L-DB2FBAA1 | 50.0 | None | False | False | 
| ebs | GetSnapshotBlock requests per account | L-C125AE42 | 1000.0 | None | False | True | 
| ebs | CompleteSnapshot requests per account | L-1D4D9345 | 10.0 | None | False | False | 
| ebs | GetSnapshotBlock requests per snapshot | L-028ACFB9 | 1000.0 | None | False | False | 
| ebs | PutSnapshotBlock requests per account | L-AFAE1BE8 | 1000.0 | None | False | True | 
| ebs | StartSnapshot requests per account | L-AFEBDF7A | 10.0 | None | False | False | 
| ebs | Storage modifications for General Purpose SSD (gp2) volumes in TiB | L-F06E64A8 | 500.0 | None | False | True | 
| ebs | Storage modifications for Throughput Optimized HDD (st1) volumes in TiB | L-87C9DEA6 | 500.0 | None | False | True | 
| ebs | Storage modifications for Provisioned IOPS SSD (io2) volumes in TiB | L-9A0E0F82 | 20.0 | None | False | True | 
| ebs | IOPS modifications for Provisioned IOPS SSD (io1) volumes | L-98A0B26D | 500000.0 | None | False | True | 
| ebs | Storage for Provisioned IOPS SSD (io2) volumes in TiB | L-09BD8365 | 20.0 | None | False | True | 
| ebs | Storage for General Purpose SSD (gp2) volumes in TiB | L-D18FCD1D | 89.0 | None | False | True | 
| ebs | Storage modifications for General Purpose SSD (gp3) volumes in TiB | L-59C8FC87 | 500.0 | None | False | True | 
| ebs | Storage for General Purpose SSD (gp3) volumes in TiB | L-7A658B76 | 50.0 | None | False | True | 
| ebs | Snapshots per Region | L-309BACF6 | 100000.0 | None | False | True | 
| ebs | In-progress snapshot restores from archive per account | L-07399329 | 5.0 | None | False | True | 
| ebs | Storage modifications for Provisioned IOPS SSD (io1) volumes in TiB | L-5F80CA91 | 500.0 | None | False | True | 
| ebs | IOPS for Provisioned IOPS SSD (io1) volumes | L-B3A130E6 | 300000.0 | None | False | True | 
| ebs | Storage modifications for Cold HDD (sc1) volumes in TiB | L-651D1834 | 500.0 | None | False | True | 
| ebs | Storage for Magnetic (standard) volumes in TiB | L-9CF3C2EB | 50.0 | None | False | True | 
| ebs | IOPS for Provisioned IOPS SSD (io2) volumes | L-8D977E7E | 100000.0 | None | False | True | 
| ebs | In-progress snapshot archives per account | L-3A0E616D | 25.0 | None | False | True | 
| ebs | Archived snapshots per volume | L-E20676C1 | 25.0 | None | False | True | 
| ebs | Storage for Cold HDD (sc1) volumes in TiB | L-17AF77E8 | 50.0 | None | False | True | 
| ebs | Storage for Provisioned IOPS SSD (io1) volumes in TiB | L-FD252861 | 50.0 | None | False | True | 
| ebs | Storage modifications for Magnetic (standard) volumes in TiB | L-B9F7C487 | 500.0 | None | False | True | 
| ebs | Storage for Throughput Optimized HDD (st1) volumes in TiB | L-82ACEF56 | 50.0 | None | False | True | 
| ebs | IOPS modifications for Provisioned IOPS SSD (io2) volumes | L-35B31D98 | 100000.0 | None | False | True | 
| ebs | Fast snapshot restore | L-631ECBD3 | 5.0 | None | False | True | 
| ec2 | Running Dedicated r6idn Hosts | L-C4EABC2C | 2.0 | None | False | True | 
| ec2 | Running Dedicated mac2 Hosts | L-5D8DADF5 | 5.0 | None | False | True | 
| ec2 | Running Dedicated c4 Hosts | L-E4BF28E0 | 2.0 | None | False | True | 
| ec2 | All F Spot Instance Requests | L-88CF9481 | 128.0 | None | False | True | 
| ec2 | Running Dedicated inf Hosts | L-5480EFD2 | 2.0 | None | False | True | 
| ec2 | Running Dedicated m5 Hosts | L-8B7BF662 | 2.0 | None | False | True | 
| ec2 | Running Dedicated m5zn Hosts | L-BD9BD803 | 2.0 | None | False | True | 
| ec2 | Running Dedicated m5dn Hosts | L-DA07429F | 2.0 | None | False | True | 
| ec2 | Running Dedicated g3 Hosts | L-DE82EABA | 0.0 | None | False | True | 
| ec2 | Running Dedicated c6id Hosts | L-1BBC5241 | 2.0 | None | False | True | 
| ec2 | Running Dedicated r6g Hosts | L-B6D6065D | 2.0 | None | False | True | 
| ec2 | Running Dedicated g5 Hosts | L-A6E7FE5E | 0.0 | None | False | True | 
| ec2 | Running Dedicated r5 Hosts | L-EA4FD6CF | 2.0 | None | False | True | 
| ec2 | Running On-Demand G and VT instances | L-DB2E81BA | 64.0 | None | False | True | 
| ec2 | Running Dedicated g5g Hosts | L-4714FFEA | 0.0 | None | False | True | 
| ec2 | Running On-Demand Inf instances | L-1945791B | 64.0 | None | False | True | 
| ec2 | Running Dedicated m5n Hosts | L-24D7D4AD | 2.0 | None | False | True | 
| ec2 | Running Dedicated i4i Hosts | L-0300530D | 2.0 | None | False | True | 
| ec2 | Running On-Demand High Memory instances | L-43DA4232 | 448.0 | None | False | True | 
| ec2 | Running Dedicated is4gen Hosts | L-CB4F5825 | 2.0 | None | False | True | 
| ec2 | Running Dedicated u-12tb1 Hosts | L-D6994875 | 0.0 | None | False | True | 
| ec2 | Running Dedicated im4gn Hosts | L-93155D6F | 2.0 | None | False | True | 
| ec2 | Running Dedicated u-18tb1 Hosts | L-5F7FD336 | 0.0 | None | False | True | 
| ec2 | Running Dedicated r5b Hosts | L-A2D59C67 | 1.0 | None | False | True | 
| ec2 | Running Dedicated c6in Hosts | L-6C2C40CC | 1.0 | None | False | True | 
| ec2 | Running Dedicated m5ad Hosts | L-74F41837 | 2.0 | None | False | True | 
| ec2 | Running Dedicated r6a Hosts | L-BC1589C5 | 2.0 | None | False | True | 
| ec2 | Running Dedicated m6in Hosts | L-D037CF10 | 2.0 | None | False | True | 
| ec2 | Running Dedicated c7g Hosts | L-13B8FCE8 | 2.0 | None | False | True | 
| ec2 | Running Dedicated x2iezn Hosts | L-888B4496 | 1.0 | None | False | True | 
| ec2 | Running Dedicated c5a Hosts | L-03F01FD8 | 2.0 | None | False | True | 
| ec2 | Running Dedicated x2idn Hosts | L-A84ABF80 | 1.0 | None | False | True | 
| ec2 | Running Dedicated mac1 Hosts | L-A8448DC5 | 3.0 | None | False | True | 
| ec2 | Running Dedicated m5a Hosts | L-B10F70D6 | 2.0 | None | False | True | 
| ec2 | Running Dedicated m6id Hosts | L-FDB0A352 | 2.0 | None | False | True | 
| ec2 | Running Dedicated z1d Hosts | L-F035E935 | 2.0 | None | False | True | 
| ec2 | Running Dedicated f1 Hosts | L-5C4CD236 | 2.0 | None | False | True | 
| ec2 | Running Dedicated u-9tb1 Hosts | L-98E1FFAC | 0.0 | None | False | True | 
| ec2 | Running Dedicated m5d Hosts | L-8CCBD91B | 2.0 | None | False | True | 
| ec2 | Running Dedicated m4 Hosts | L-EF30B25E | 2.0 | None | False | True | 
| ec2 | Running Dedicated c5 Hosts | L-81657574 | 2.0 | None | False | True | 
| ec2 | Running Dedicated p3dn Hosts | L-B601B3B6 | 0.0 | None | False | True | 
| ec2 | Running Dedicated p3 Hosts | L-A0A19F79 | 0.0 | None | False | True | 
| ec2 | Running Dedicated r5ad Hosts | L-EC7178B6 | 2.0 | None | False | True | 
| ec2 | Running Dedicated g4ad Hosts | L-FD8E9B9A | 0.0 | None | False | True | 
| ec2 | Running Dedicated m6g Hosts | L-D50A37FA | 2.0 | None | False | True | 
| ec2 | Running On-Demand P instances | L-417A185B | 64.0 | None | False | True | 
| ec2 | All X Spot Instance Requests | L-E3A00192 | 128.0 | None | False | True | 
| ec2 | Running Dedicated i2 Hosts | L-6222C1B6 | 2.0 | None | False | True | 
| ec2 | Running Dedicated r5dn Hosts | L-4AB14223 | 2.0 | None | False | True | 
| ec2 | Running On-Demand Standard (A C D H I M R T Z) instances | L-1216C47A | 640.0 | None | False | True | 
| ec2 | Running Dedicated c6a Hosts | L-D75D2E84 | 2.0 | None | False | True | 
| ec2 | Running Dedicated m6gd Hosts | L-84FB37AA | 2.0 | None | False | True | 
| ec2 | Running Dedicated t3 Hosts | L-1586174D | 2.0 | None | False | True | 
| ec2 | Running Dedicated r6i Hosts | L-F13A970A | 2.0 | None | False | True | 
| ec2 | All P Spot Instance Requests | L-7212CCBC | 64.0 | None | False | True | 
| ec2 | Running Dedicated u-6tb1 Hosts | L-89870E8E | 0.0 | None | False | True | 
| ec2 | Running Dedicated r7g Hosts | L-67B8B4C7 | 2.0 | None | False | True | 
| ec2 | All DL Spot Instance Requests | L-85EED4F7 | 96.0 | None | False | True | 
| ec2 | Running Dedicated r6in Hosts | L-EA99608B | 2.0 | None | False | True | 
| ec2 | Running Dedicated x2gd Hosts | L-5CC9EA82 | 2.0 | None | False | True | 
| ec2 | Running Dedicated c5d Hosts | L-C93F66A2 | 2.0 | None | False | True | 
| ec2 | Running Dedicated p2 Hosts | L-2753CF59 | 0.0 | None | False | True | 
| ec2 | Running On-Demand F instances | L-74FC7D96 | 128.0 | None | False | True | 
| ec2 | Running Dedicated r4 Hosts | L-313524BA | 2.0 | None | False | True | 
| ec2 | All Standard (A C D H I M R T Z) Spot Instance Requests | L-34B43A08 | 640.0 | None | False | True | 
| ec2 | All Trn Spot Instance Requests | L-6B0D517C | 256.0 | None | False | True | 
| ec2 | Running Dedicated vt1 Hosts | L-A68CFBF7 | 2.0 | None | False | True | 
| ec2 | Running Dedicated r6id Hosts | L-B89271A9 | 2.0 | None | False | True | 
| ec2 | Running On-Demand DL instances | L-6E869C2A | 96.0 | None | False | True | 
| ec2 | Running Dedicated x1e Hosts | L-DEF8E115 | 1.0 | None | False | True | 
| ec2 | Running Dedicated r5a Hosts | L-8FE30D52 | 2.0 | None | False | True | 
| ec2 | Running Dedicated r5n Hosts | L-52EF324A | 2.0 | None | False | True | 
| ec2 | Running Dedicated r5d Hosts | L-8814B54F | 2.0 | None | False | True | 
| ec2 | Running Dedicated g3s Hosts | L-9675FDCD | 0.0 | None | False | True | 
| ec2 | Running Dedicated r6gd Hosts | L-EF284EFB | 2.0 | None | False | True | 
| ec2 | Running Dedicated c5n Hosts | L-20F13EBD | 1.0 | None | False | True | 
| ec2 | Members per transit gateway multicast group | L-C768F2D6 | 100.0 | None | False | True | 
| ec2 | Customer gateways per region | L-4FB7FF5D | 50.0 | None | False | True | 
| ec2 | Virtual private gateways per region | L-7029FAB6 | 5.0 | None | False | True | 
| ec2 | Client VPN endpoints per Region | L-8EA77D34 | 5.0 | None | False | True | 
| ec2 | VPN connections per region | L-3E6EC3A3 | 50.0 | None | False | True | 
| ec2 | Routes per Client VPN endpoint | L-401D78F7 | 10.0 | None | False | True | 
| ec2 | Multicast domain associations per VPC | L-9F8FA74B | 20.0 | None | False | True | 
| ec2 | EC2-VPC Elastic IPs | L-0263D0A3 | 20.0 | None | False | True | 
| ec2 | New Reserved Instances per month | L-D0B7243C | 20.0 | None | False | True | 
| ec2 | Sources per transit gateway multicast group | L-4F2F99E3 | 1.0 | None | False | True | 
| ec2 | AMI sharing | L-70015FFA | 1000.0 | None | False | True | 
| ec2 | EC2-Classic Elastic IPs | L-CEED54BB | 5.0 | None | False | True | 
| ec2 | Attachments per VPC | L-6DA43717 | 5.0 | None | False | False | 
| ec2 | Authorization rules per Client VPN endpoint | L-9A1BC94B | 50.0 | None | False | True | 
| ec2 | Multicast domains per transit gateway | L-31775423 | 20.0 | None | False | True | 
| ec2 | Routes per transit gateway | L-BCC1FB47 | 10000.0 | None | False | True | 
| ec2 | VPN connections per VGW | L-B91E5754 | 10.0 | None | False | True | 
| ec2 | Attachments per transit gateway | L-E0233F82 | 5000.0 | None | False | True | 
| ec2 | Peering attachments per transit gateway | L-A1B5A36F | 50.0 | None | False | True | 
| ec2 | Public AMIs | L-0E3CBAB9 | 5.0 | None | False | True | 
| ec2 | AMIs | L-B665C33B | 50000.0 | None | False | True | 
| ec2 | Pending peering attachments per transit gateway | L-62499967 | 10.0 | None | False | True | 
| ec2 | Transit gateways per account | L-A2478D36 | 5.0 | None | False | True | 
| ec2 | Running On-Demand HPC instances | L-F7808C92 | 768.0 | None | False | True | 
| ec2 | Running Dedicated m3 Hosts | L-3C82F907 | 2.0 | None | False | True | 
| ec2 | Running Dedicated c6gn Hosts | L-5E3A299D | 2.0 | None | False | True | 
| ec2 | Running Dedicated x2iedn Hosts | L-D0AA08B1 | 1.0 | None | False | True | 
| ec2 | Running Dedicated i3en Hosts | L-77EE2B11 | 2.0 | None | False | True | 
| ec2 | Running Dedicated m7g Hosts | L-9126620E | 2.0 | None | False | True | 
| ec2 | Running Dedicated m6a Hosts | L-80F2B67F | 2.0 | None | False | True | 
| ec2 | Running Dedicated g2 Hosts | L-74BBB7CB | 0.0 | None | False | True | 
| ec2 | Running Dedicated c6gd Hosts | L-545AED39 | 2.0 | None | False | True | 
| ec2 | Running Dedicated c3 Hosts | L-8D142A2E | 2.0 | None | False | True | 
| ec2 | Running Dedicated m6i Hosts | L-D269BEFD | 2.0 | None | False | True | 
| ec2 | All Inf Spot Instance Requests | L-B5D1601B | 64.0 | None | False | True | 
| ec2 | Running On-Demand Trn instances | L-2C3B7624 | 256.0 | None | False | True | 
| ec2 | Running Dedicated x1 Hosts | L-DE3D9563 | 1.0 | None | False | True | 
| ec2 | Running Dedicated m6idn Hosts | L-9721EDD9 | 2.0 | None | False | True | 
| ec2 | Running Dedicated i3 Hosts | L-8E60B0B1 | 2.0 | None | False | True | 
| ec2 | Running Dedicated r3 Hosts | L-B7208018 | 2.0 | None | False | True | 
| ec2 | Running Dedicated trn1 Hosts | L-5E4FB836 | 0.0 | None | False | True | 
| ec2 | Running Dedicated a1 Hosts | L-949445B0 | 2.0 | None | False | True | 
| ec2 | Running Dedicated p4d Hosts | L-86A789C3 | 0.0 | None | False | True | 
| ec2 | Running Dedicated h1 Hosts | L-84391ECC | 2.0 | None | False | True | 
| ec2 | All G and VT Spot Instance Requests | L-3819A6DF | 64.0 | None | False | True | 
| ec2 | Running On-Demand X instances | L-7295265B | 128.0 | None | False | True | 
| ec2 | Running Dedicated c6g Hosts | L-A749B537 | 2.0 | None | False | True | 
| ec2 | Running Dedicated c6i Hosts | L-5FA3355A | 2.0 | None | False | True | 
| ec2 | Running Dedicated g4dn Hosts | L-CAE24619 | 0.0 | None | False | True | 
| ec2 | Running Dedicated d2 Hosts | L-8B27377A | 2.0 | None | False | True | 
| ec2 | Running Dedicated dl1 Hosts | L-AD667A3D | 1.0 | None | False | True | 
| ec2 | Running Dedicated u-3tb1 Hosts | L-7F5506AB | 0.0 | None | False | True | 
| ec2 | Multicast Network Interfaces per transit gateway | L-C673935A | 10000.0 | None | False | True | 
| ec2 | Concurrent client connections per Client VPN endpoint | L-C4B238BF | 126000.0 | None | False | True | 
| ec2-ipam | IPAM pool depth | L-047C0565 | 10.0 | None | False | True | 
| ec2-ipam | CIDRs per IPAM pool | L-0BC051D6 | 50.0 | None | False | True | 
| ec2-ipam | Pools per IPAM scope | L-7319AFC3 | 50.0 | None | False | True | 
| ec2-ipam | Scopes per IPAM | L-F493CFD2 | 5.0 | None | False | True | 
| ec2-ipam | IPAMs per Region | L-F8B4A9E6 | 1.0 | None | False | False | 
| ec2fastlaunch | Parallel instance launches | L-DC79B53E | 20.0 | None | False | True | 
| ecr | Rate of BatchCheckLayerAvailability requests | L-B9173138 | 1000.0 | None | False | True | 
| ecr | Rate of GetAuthorizationToken requests | L-55A41110 | 500.0 | None | False | True | 
| ecr | Rate of CompleteLayerUpload requests | L-44194860 | 100.0 | None | False | True | 
| ecr | Rate of PutImage requests | L-AD52DFB2 | 10.0 | None | False | True | 
| ecr | Rate of InitiateLayerUpload requests | L-95B28F8D | 100.0 | None | False | True | 
| ecr | Rate of BatchGetImage requests | L-16E70933 | 2000.0 | None | False | True | 
| ecr | Rate of GetDownloadUrlForLayer requests | L-A60A366D | 3000.0 | None | False | True | 
| ecr | Rate of UploadLayerPart requests | L-A1670B10 | 500.0 | None | False | True | 
| eks | Registered clusters | L-FDFA5F81 | 10.0 | None | False | True | 
| eks | Label pairs per Fargate profile selector | L-23414FF3 | 5.0 | None | False | True | 
| eks | Selectors per Fargate profile | L-D78D8AF8 | 5.0 | None | False | True | 
| eks | Control plane security groups per cluster | L-11427A54 | 4.0 | None | False | False | 
| eks | Nodes per managed node group | L-BD136A63 | 450.0 | None | False | True | 
| eks | Clusters | L-1194D53C | 100.0 | None | False | True | 
| eks | Fargate profiles per cluster | L-33415657 | 10.0 | None | False | True | 
| eks | Managed node groups per cluster | L-6D54EA21 | 30.0 | None | False | True | 
| eks | Public endpoint access CIDR ranges per cluster | L-93A74D60 | 40.0 | None | False | False | 
| elasticfilesystem | Rate of file system operations | L-336A920F | 35000.0 | None | False | False | 
| elasticfilesystem | Active users per NFS client | L-FA0AAA42 | 128.0 | None | False | False | 
| elasticfilesystem | Throughput per NFS client | L-06519EB8 | 524.288 | Megabytes | False | False | 
| elasticfilesystem | File system symbolic link (symlink) length | L-B8B14E21 | 4080.0 | Bytes | False | False | 
| elasticfilesystem | File systems per account | L-848C634D | 1000.0 | None | False | True | 
| elasticfilesystem | File system name length | L-207AE8E0 | 255.0 | Bytes | False | False | 
| elasticfilesystem | Mount targets per VPC | L-7391004C | 400.0 | None | False | False | 
| elasticfilesystem | Provisioned throughput | L-BFB6FB19 | 1024.0 | Megabytes | False | False | 
| elasticfilesystem | Minimum wait time between Provisioned Throughput decreases | L-1E30FF38 | 86400.0 | Seconds | False | False | 
| elasticfilesystem | VPCs per file system | L-03A6A61D | 1.0 | None | False | False | 
| elasticfilesystem | Tags | L-29770CF9 | 50.0 | None | False | False | 
| elasticfilesystem | Bursting throughput | L-CDCE244F | 3072.0 | Megabytes | False | False | 
| elasticfilesystem | Open files per NFS client | L-48B15094 | 32768.0 | None | False | False | 
| elasticfilesystem | File size | L-7FEABCD7 | 52673613135872.0 | Bytes | False | False | 
| elasticfilesystem | Minimum wait time between Throughput mode changes | L-D6548EE7 | 86400.0 | Seconds | False | False | 
| elasticfilesystem | EFS file locks | L-509A1582 | 512.0 | None | False | False | 
| elasticfilesystem | Security groups per mount target | L-3D348029 | 5.0 | None | False | False | 
| elasticfilesystem | Directory depth | L-F3C5D9EF | 1000.0 | None | False | False | 
| elasticfilesystem | Mount targets per Availability Zone | L-6D380DD0 | 1.0 | None | False | False | 
| elasticfilesystem | Locks across unique file/process pairs | L-C8C0D2A0 | 65536.0 | None | False | False | 
| elasticfilesystem | File hard links | L-A139E5A7 | 177.0 | None | False | False | 
| elasticloadbalancing | Rules per Application Load Balancer | L-7EED9B64 | 100.0 | None | False | True | 
| elasticloadbalancing | Network Load Balancer ENIs per VPC | L-23568085 | 1200.0 | None | False | True | 
| elasticloadbalancing | Target Groups per Application Load Balancer | L-822D1B1B | 100.0 | None | False | False | 
| elasticloadbalancing | Listeners per Application Load Balancer | L-B6DF7632 | 50.0 | None | False | True | 
| elasticloadbalancing | Certificates per Network Load Balancer | L-52964454 | 25.0 | None | False | True | 
| elasticloadbalancing | Certificates per Application Load Balancer | L-9365A611 | 25.0 | None | False | True | 
| elasticloadbalancing | Listeners per Classic Load Balancer | L-1A491844 | 100.0 | None | False | True | 
| elasticloadbalancing | Targets per Availability Zone per Network Load Balancer | L-B211E961 | 500.0 | None | False | True | 
| elasticloadbalancing | Targets per Network Load Balancer | L-EEF1AD04 | 3000.0 | None | False | True | 
| elasticloadbalancing | Condition Values per Rule | L-EBC0C08B | 5.0 | None | False | False | 
| elasticloadbalancing | Condition Wildcards per Rule | L-A012D4E8 | 5.0 | None | False | False | 
| elasticloadbalancing | Target Groups per Region | L-B22855CB | 3000.0 | None | False | True | 
| elasticloadbalancing | Target Groups per Action per Application Load Balancer | L-057ECE54 | 5.0 | None | False | False | 
| elasticloadbalancing | Listeners per Network Load Balancer | L-57A373D6 | 50.0 | None | False | False | 
| elasticloadbalancing | Targets per Target Group per Region | L-A0D0B863 | 1000.0 | None | False | True | 
| elasticloadbalancing | Targets per Application Load Balancer | L-7E6692B2 | 1000.0 | None | False | True | 
| elasticloadbalancing | Application Load Balancers per Region | L-53DA6B97 | 50.0 | None | False | True | 
| elasticloadbalancing | Network Load Balancers per Region | L-69A177A2 | 50.0 | None | False | True | 
| elasticloadbalancing | Registered Instances per Classic Load Balancer | L-CE3125E5 | 1000.0 | None | False | True | 
| elasticloadbalancing | Target Groups per Action per Network Load Balancer | L-AFDDADBF | 1.0 | None | False | False | 
| elasticloadbalancing | Number of times a target can be registered per Application Load Balancer | L-4E7B68E9 | 1000.0 | None | False | False | 
| elasticloadbalancing | Classic Load Balancers per Region | L-E9E9831D | 20.0 | None | False | True | 
| elasticmapreduce | The maximum number of DescribeStep API requests that you can make per second. | L-B810434D | 10.0 | None | False | True | 
| elasticmapreduce | The maximum number of DeleteSecurityConfiguration API requests that you can make per second. | L-F0B1A0AC | 5.0 | None | False | True | 
| elasticmapreduce | Replenishment rate of ListInstanceFleets calls | L-C0B235E1 | 0.5 | None | False | True | 
| elasticmapreduce | The maximum number of ListInstanceFleets API requests that you can make per second. | L-85BA8360 | 5.0 | None | False | True | 
| elasticmapreduce | The maximum number of RunJobFlow API requests that you can make per second. | L-A21DE5E2 | 10.0 | None | False | True | 
| elasticmapreduce | The maximum number of ModifyCluster API requests that you can make per second. | L-A552C9A0 | 10.0 | None | False | True | 
| elasticmapreduce | Replenishment rate of DescribeStep calls | L-72BCD5B1 | 0.5 | None | False | True | 
| elasticmapreduce | The maximum number of active clusters can be run at the same time | L-1EE7982C | 500.0 | None | False | True | 
| elasticmapreduce | The maximum number of API requests that you can make per second. | L-283CCA2A | 25.0 | None | False | True | 
| elasticmapreduce | The maximum number of ListInstances API requests that you can make per second. | L-41AA02AE | 10.0 | None | False | True | 
| elasticmapreduce | Replenishment rate of AddJobFlowSteps calls | L-40A3F1BE | 0.5 | None | False | True | 
| elasticmapreduce | Replenishment rate of AddInstanceGroups calls | L-0224B14B | 0.2 | None | False | True | 
| elasticmapreduce | The maximum number of ListClusters API requests that you can make per second. | L-2C4B0A7F | 20.0 | None | False | True | 
| elasticmapreduce | The maximum number of RemoveTags API requests that you can make per second. | L-C00B9F83 | 5.0 | None | False | True | 
| elasticmapreduce | Replenishment rate of ListSteps calls | L-8AF88BF0 | 0.5 | None | False | True | 
| elasticmapreduce | Replenishment rate of DescribeSecurityConfiguration calls | L-8029315A | 0.5 | None | False | True | 
| elasticmapreduce | Replenishment rate of AddTags calls | L-9CCE25C7 | 0.5 | None | False | True | 
| elasticmapreduce | Replenishment rate of TerminateJobFlows calls | L-4D731391 | 0.5 | None | False | True | 
| elasticmapreduce | The maximum rate at which your bucket replenishes for all EMR operations. | L-432FAB44 | 5.0 | None | False | True | 
| elasticmapreduce | The maximum number of PutAutoScalingPolicy API requests that you can make per second. | L-888B48A6 | 5.0 | None | False | True | 
| elasticmapreduce | Replenishment rate of RemoveTags calls | L-67E5FE4A | 0.5 | None | False | True | 
| elasticmapreduce | The maximum number of ModifyInstanceFleet API requests that you can make per second. | L-5E87FF33 | 5.0 | None | False | True | 
| elasticmapreduce | Replenishment rate of ModifyInstanceGroups calls | L-87EDCC64 | 0.5 | None | False | True | 
| elasticmapreduce | The maximum number of ListInstanceGroups API requests that you can make per second. | L-2266B3CF | 10.0 | None | False | True | 
| elasticmapreduce | Replenishment rate of PutAutoScalingPolicy calls | L-985D82D4 | 0.5 | None | False | True | 
| elasticmapreduce | The maximum number of DescribeSecurityConfiguration API requests that you can make per second. | L-27AD4F43 | 5.0 | None | False | True | 
| elasticmapreduce | The maximum number of AddJobFlowSteps API requests that you can make per second. | L-7E42A979 | 10.0 | None | False | True | 
| elasticmapreduce | The maximum number of DescribeJobFlows API requests that you can make per second. | L-9F63B487 | 20.0 | None | False | True | 
| elasticmapreduce | Replenishment rate of ListClusters calls | L-ECF78C67 | 0.5 | None | False | True | 
| elasticmapreduce | The maximum number of AddInstanceGroups API requests that you can make per second. | L-E5202B33 | 5.0 | None | False | True | 
| elasticmapreduce | Replenishment rate of AddInstanceFleet calls | L-3AD9CD3B | 0.5 | None | False | True | 
| elasticmapreduce | Replenishment rate of SetVisibleToAllUsers calls | L-41EE964A | 0.2 | None | False | True | 
| elasticmapreduce | Replenishment rate of ModifyInstanceFleet calls | L-9EFF5880 | 0.5 | None | False | True | 
| elasticmapreduce | The maximum number of active instances per instance group | L-77B909B1 | 2000.0 | None | False | True | 
| elasticmapreduce | Replenishment rate of DescribeCluster calls | L-D74118B4 | 1.0 | None | False | True | 
| elasticmapreduce | Replenishment rate of SetTerminationProtection calls | L-8027FD2D | 0.2 | None | False | True | 
| elasticmapreduce | Replenishment rate of ListBootstrapActions calls | L-CCF40647 | 1.0 | None | False | True | 
| elasticmapreduce | The maximum number of ListBootstrapActions API requests that you can make per second. | L-BF4AD168 | 10.0 | None | False | True | 
| elasticmapreduce | Replenishment rate of CancelSteps calls | L-A90C264E | 0.5 | None | False | True | 
| elasticmapreduce | The maximum number of ModifyInstanceGroups API requests that you can make per second. | L-A3F85680 | 5.0 | None | False | True | 
| elasticmapreduce | Replenishment rate of RemoveAutoScalingPolicy calls | L-F902E21E | 0.5 | None | False | True | 
| elasticmapreduce | The maximum number of CreateSecurityConfiguration API requests that you can make per second. | L-49AA2AC0 | 5.0 | None | False | True | 
| elasticmapreduce | The maximum number of ListSteps API requests that you can make per second. | L-7D1BF903 | 10.0 | None | False | True | 
| elasticmapreduce | The maximum number of RemoveAutoScalingPolicy API requests that you can make per second. | L-361D364D | 5.0 | None | False | True | 
| elasticmapreduce | The maximum number of AddInstanceFleet API requests that you can make per second. | L-0E64D90C | 5.0 | None | False | True | 
| elasticmapreduce | The maximum number of SetVisibileToAllUsers API requests that you can make per second. | L-2268EC50 | 5.0 | None | False | True | 
| elasticmapreduce | The maximum number of CancelSteps API requests that you can make per second. | L-815103CB | 10.0 | None | False | True | 
| elasticmapreduce | The maximum number of DescribeCluster API requests that you can make per second. | L-81AF5123 | 10.0 | None | False | True | 
| elasticmapreduce | Replenishment rate of ModifyCluster calls | L-73E44B2E | 0.5 | None | False | True | 
| elasticmapreduce | The maximum number of SetTerminationProtection API requests that you can make per second. | L-F06A869F | 5.0 | None | False | True | 
| elasticmapreduce | Replenishment rate of DescribeJobFlows calls | L-68268EEB | 0.2 | None | False | True | 
| elasticmapreduce | Replenishment rate of DeleteSecurityConfiguration calls | L-EB8F427D | 0.5 | None | False | True | 
| elasticmapreduce | Replenishment rate of ListInstanceGroups calls | L-84D58688 | 1.0 | None | False | True | 
| elasticmapreduce | The maximum number of TerminateJobFlows API requests that you can make per second. | L-2625B75B | 10.0 | None | False | True | 
| elasticmapreduce | The maximum number of ListSecurityConfigurations API requests that you can make per second. | L-160E516B | 5.0 | None | False | True | 
| elasticmapreduce | The maximum number of AddTags API requests that you can make per second. | L-9547F71F | 5.0 | None | False | True | 
| elasticmapreduce | Replenishment rate of CreateSecurityConfiguration calls | L-16E4E927 | 0.5 | None | False | True | 
| elasticmapreduce | Replenishment rate of RunJobFlow calls | L-62231AC0 | 0.5 | None | False | True | 
| elasticmapreduce | Replenishment rate of ListInstances calls | L-76CEF085 | 0.5 | None | False | True | 
| elasticmapreduce | Replenishment rate of ListSecurityConfigurations calls | L-D145AF1C | 0.5 | None | False | True | 
| emr-serverless | Max concurrent vCPUs per account | L-D05C8A75 | 4000.0 | None | False | True | 
| es | Domains per Region | L-076D529E | 100.0 | None | False | True | 
| es | Warm instances per domain | L-1F053E6F | 150.0 | None | False | False | 
| es | Instances per domain | L-6408ABDE | 80.0 | None | False | True | 
| es | Dedicated master instances per domain | L-AE676A72 | 5.0 | None | False | False | 
| es | Instances per domain (T2 instance type) | L-E9BC8C95 | 10.0 | None | False | False | 
| events | Endpoints | L-EAC9A2AC | 100.0 | None | False | True | 
| events | Targets per rule | L-388D1D08 | 5.0 | None | False | False | 
| events | CreateEndpoint throttle limit in transactions per second | L-CB72B930 | 5.0 | None | False | False | 
| events | Invocations throttle limit in transactions per second | L-5540C5E3 | 18750.0 | None | False | True | 
| events | Rate of invocations per API destination | L-755FD01C | 300.0 | None | False | True | 
| events | Number of rules | L-244521F2 | 300.0 | None | False | True | 
| events | UpdateEndpoint throttle limit in transactions per second | L-A8AFA624 | 5.0 | None | False | False | 
| events | DeleteEndpoint throttle limit in transactions per second | L-5425B7E9 | 5.0 | None | False | False | 
| events | Api destinations | L-FB1C3A6D | 3000.0 | None | False | True | 
| events | PutEvents throttle limit in transactions per second | L-9B653E91 | 10000.0 | None | False | True | 
| events | Throttle limit in transactions per second | L-3C47459F | 50.0 | None | False | True | 
| events | Connections | L-595D6D42 | 3000.0 | None | False | True | 
| fargate | Fargate Spot vCPU resource count | L-36FBB829 | 4000.0 | None | False | True | 
| fargate | Fargate On-Demand vCPU resource count | L-3032A538 | 4000.0 | None | False | True | 
| firehose | Delivery streams | L-14BB0BE7 | 50.0 | None | False | True | 
| fis | Target Subnets for aws:network:disrupt-connectivity | L-1F59732D | 5.0 | None | False | True | 
| fis | Stop conditions per experiment template | L-872EC72B | 5.0 | None | False | False | 
| fis | Active experiments | L-F5FCA485 | 5.0 | None | False | False | 
| fis | Parallel actions per experiment | L-EB051440 | 10.0 | None | False | False | 
| fis | Experiment duration in hours | L-6C1E4427 | 12.0 | None | False | False | 
| fis | Target Clusters for aws:ecs:drain-container-instances | L-B2CDA938 | 5.0 | None | False | True | 
| fis | Target Instances for aws:ssm:send-command | L-D0A62255 | 5.0 | None | False | True | 
| fis | Target Tasks for aws:ecs:stop-task | L-48D12416 | 5.0 | None | False | True | 
| fis | Target Instances for aws:ec2:reboot-instances | L-9C6F1F94 | 5.0 | None | False | True | 
| fis | Actions per experiment template | L-0BFE6B67 | 20.0 | None | False | False | 
| fis | Target Nodegroups for aws:eks:terminate-nodegroup-instances | L-CCA14F79 | 5.0 | None | False | True | 
| fis | Target SpotInstances for aws:ec2:send-spot-instance-interruptions | L-F3F4B54A | 5.0 | None | False | True | 
| fis | Action duration in hours | L-A7622DAA | 12.0 | None | False | False | 
| fis | Target Instances for aws:ec2:stop-instances | L-3F98B425 | 5.0 | None | False | True | 
| fis | Completed experiment data retention in days | L-9D601129 | 120.0 | None | False | False | 
| fis | Target Clusters for aws:rds:failover-db-cluster | L-7D222253 | 5.0 | None | False | True | 
| fis | Target DBInstances for aws:rds:reboot-db-instances | L-6CBFC7D2 | 5.0 | None | False | True | 
| fis | Target Instances for aws:ec2:terminate-instances | L-EE64095D | 5.0 | None | False | True | 
| fis | Experiment templates | L-2FF3254A | 500.0 | None | False | False | 
| forecast | Maximum parallel running CreateForecastExportJob tasks | L-02D995E1 | 3.0 | None | False | True | 
| forecast | Maximum parallel running CreateDatasetImportJob tasks | L-407BD890 | 3.0 | None | False | True | 
| forecast | The maximum number of What-if Analyses | L-235B11D6 | 500.0 | None | False | True | 
| forecast | Maximum number of forecast export jobs | L-561FC25E | 1000.0 | None | False | True | 
| forecast | Maximum parallel running CreateWhatIfAnalysis tasks | L-3DED4AA6 | 3.0 | None | False | True | 
| forecast | Maximum forecast horizon | L-57E6FE87 | 500.0 | None | False | False | 
| forecast | Maximum parallel running QueryForecast API tasks | L-B77118AF | 10.0 | None | False | False | 
| forecast | The maximum number of What-if Forecasts | L-762142D9 | 100.0 | None | False | True | 
| forecast | Maximum number of files in your Amazon S3 bucket | L-3F8C5D53 | 10000.0 | None | False | False | 
| forecast | Maximum number of forecasts | L-884F7F75 | 100.0 | None | False | True | 
| forecast | Maximum number of tags you can add to a resource | L-60743B41 | 50.0 | None | False | False | 
| forecast | Maximum number of dataset groups | L-5054D782 | 500.0 | None | False | True | 
| forecast | Maximum time for which a forecast can be queried on console or QueryForecast API | L-B8197A69 | 30.0 | None | False | False | 
| forecast | Maximum number of predictors | L-9C589A93 | 500.0 | None | False | True | 
| forecast | Maximum number of backtest windows | L-4F7B6EC8 | 5.0 | None | False | False | 
| forecast | The maximum number of What-if Forecasts in a CreateWhatIfForecastExport task | L-50FA8F07 | 3.0 | None | False | False | 
| forecast | Maximum number of columns in a related time series dataset | L-3D30706E | 25.0 | None | False | False | 
| forecast | Maximum parallel running CreateWhatIfForecast tasks | L-5EC8963B | 3.0 | None | False | True | 
| forecast | Maximum number of time series per predictor | L-4A218FD9 | 5000000.0 | None | False | True | 
| forecast | Maximum number of datasets | L-D613D53B | 1500.0 | None | False | True | 
| forecast | The maximum number of What-if Forecast Exports | L-6AD28BD9 | 1000.0 | None | False | True | 
| forecast | Maximum parallel running CreatePredictorBacktestExportJob tasks | L-C4147F5F | 3.0 | None | False | True | 
| forecast | Maximum number of columns in a target time series dataset | L-9FD32A46 | 13.0 | None | False | False | 
| forecast | Maximum number of predictor backtest export jobs | L-E1AC300F | 1000.0 | None | False | True | 
| forecast | Maximum number of rows in a dataset | L-618F5043 | 3000000000.0 | None | False | True | 
| forecast | Maximum cumulative size of all files in your Amazon S3 bucket | L-690B4DB2 | 30.0 | Gigabytes | False | True | 
| forecast | Maximum parallel running CreateForecast tasks | L-10DDC31D | 3.0 | None | False | True | 
| forecast | Maximum number of columns in an item metadata dataset | L-F37CCDC6 | 10.0 | None | False | False | 
| forecast | Maximum parallel running CreateWhatIfForecastExport tasks | L-B50F9B6C | 3.0 | None | False | True | 
| forecast | Maximum number of dataset import jobs | L-1306EC42 | 1000.0 | None | False | True | 
| forecast | Maximum number of datasets in a dataset group | L-D71794C7 | 3.0 | None | False | False | 
| forecast | Maximum parallel running CreatePredictor tasks | L-3154C698 | 3.0 | None | False | True | 
| forecast | Maximum parallel running CreatePredictor tasks using AutoML | L-BDD6E332 | 3.0 | None | False | True | 
| frauddetector | Outcomes per account | L-A8E1A12A | 5000.0 | None | False | False | 
| frauddetector | Detectors per account | L-EB925C6F | 100.0 | None | False | False | 
| frauddetector | Versions per model | L-17F80A78 | 200.0 | None | False | False | 
| frauddetector | Rules per account | L-4CB84A5D | 5000.0 | None | False | False | 
| frauddetector | Total concurrent training jobs | L-9729D5BB | 3.0 | None | False | False | 
| frauddetector | Training data size | L-FD6E2577 | 5.0 | Gigabytes | False | False | 
| frauddetector | Models per account | L-A499790A | 50.0 | None | False | False | 
| frauddetector | Size of GetPrediction requests | L-B866C3AA | 256.0 | Kilobytes | False | False | 
| frauddetector | Variables per account | L-6A39223B | 5000.0 | None | False | False | 
| frauddetector | Models including external models per detector version | L-A9872AF8 | 10.0 | None | False | False | 
| frauddetector | Versions per detector | L-10D6B82C | 100.0 | None | False | False | 
| frauddetector | Rate of GetPrediction requests | L-7D855745 | 200.0 | None | False | True | 
| frauddetector | Concurrent training jobs per model | L-46EB4650 | 1.0 | None | False | False | 
| frauddetector | Deployed model versions | L-2A06444E | 5.0 | None | False | False | 
| fsx | ONTAP backups | L-C431DBA3 | 10000.0 | None | False | True | 
| fsx | Lustre Cache_1 storage capacity | L-15D9FE87 | 100800.0 | None | False | True | 
| fsx | ONTAP SSD storage capacity | L-E2C89679 | 524288.0 | None | False | True | 
| fsx | Lustre Scratch file systems | L-C48231E5 | 100.0 | None | False | True | 
| fsx | Windows SSD storage capacity | L-E43BDB2E | 524288.0 | None | False | True | 
| fsx | Windows throughput capacity | L-FD89CA8A | 10240.0 | None | False | True | 
| fsx | ONTAP file systems | L-C28C1403 | 100.0 | None | False | True | 
| fsx | Lustre Persistent_1 file systems | L-9AFA1F09 | 100.0 | None | False | True | 
| fsx | Lustre Persistent_2 storage capacity | L-8F1B9C74 | 100800.0 | None | False | True | 
| fsx | Lustre backups | L-CD5E0524 | 500.0 | None | False | True | 
| fsx | Lustre Cache_1 caches | L-60836D3E | 100.0 | None | False | True | 
| fsx | Lustre Scratch storage capacity | L-AD2FC696 | 100800.0 | None | False | True | 
| fsx | OpenZFS backups | L-DD0F7417 | 10000.0 | None | False | True | 
| fsx | Windows HDD storage capacity | L-84EAF187 | 524288.0 | None | False | True | 
| fsx | ONTAP throughput capacity | L-C5F860DD | 10240.0 | None | False | True | 
| fsx | ONTAP SSD IOPS | L-57578687 | 1000000.0 | None | False | True | 
| fsx | Windows file systems | L-5B89F9CE | 100.0 | None | False | True | 
| fsx | OpenZFS throughput capacity | L-4EDE4065 | 10240.0 | None | False | True | 
| fsx | OpenZFS SSD storage capacity | L-88479C21 | 262144.0 | None | False | True | 
| fsx | Lustre Persistent HDD storage capacity (per file system) | L-736F3D6F | 102000.0 | None | False | True | 
| fsx | Windows backups | L-E94C1C19 | 500.0 | None | False | True | 
| fsx | OpenZFS file systems | L-59D0763F | 100.0 | None | False | True | 
| fsx | OpenZFS SSD storage capacity (per file system) | L-7D5FDD38 | 524288.0 | None | False | True | 
| fsx | Lustre Persistent_1 storage capacity | L-C8640C82 | 100800.0 | None | False | True | 
| fsx | Lustre Persistent_2 file systems | L-FD6F2F22 | 100.0 | None | False | True | 
| fsx | OpenZFS disk IOPS | L-E24B4DE4 | 400000.0 | None | False | True | 
| geo | Rate of UpdateTracker API requests | L-5C766737 | 10.0 | None | False | True | 
| geo | Rate of CreateTracker API requests | L-0316544D | 10.0 | None | False | True | 
| geo | Rate of BatchDeleteGeofence API requests | L-93F5D44A | 50.0 | None | False | True | 
| geo | Rate of ListPlaceIndexes API requests | L-E3E8B4BC | 10.0 | None | False | True | 
| geo | Rate of DescribeTracker API requests | L-4BA89359 | 10.0 | None | False | True | 
| geo | Rate of CreateRouteCalculator API requests | L-AF53BB1C | 10.0 | None | False | True | 
| geo | Rate of GetDevicePositionHistory API requests | L-9A60EA62 | 50.0 | None | False | True | 
| geo | Rate of CreatePlaceIndex API requests | L-0A4EAAD0 | 10.0 | None | False | True | 
| geo | Rate of SearchPlaceIndexForText API requests | L-20F1367A | 50.0 | None | False | True | 
| geo | Rate of UpdateMap API requests | L-123EEE95 | 10.0 | None | False | True | 
| geo | Rate of ListDevicePositions API requests | L-B26E5E95 | 50.0 | None | False | True | 
| geo | Rate of DeleteMap API requests | L-66B4C7B5 | 10.0 | None | False | True | 
| geo | Rate of UpdateGeofenceCollection API requests | L-4D54A4EF | 10.0 | None | False | True | 
| geo | Route Calculator resources per account | L-D4E15F64 | 40.0 | None | False | True | 
| geo | Rate of DescribeMap API requests | L-3B6F7C26 | 10.0 | None | False | True | 
| geo | Rate of BatchDeleteDevicePositionHistory API requests | L-CA16DE37 | 50.0 | None | False | True | 
| geo | Tracker consumers per tracker | L-7B55057C | 5.0 | None | False | False | 
| geo | Rate of DescribeRouteCalculator API requests | L-EA3098B7 | 10.0 | None | False | True | 
| geo | Rate of DeleteTracker API requests | L-24CBFF24 | 10.0 | None | False | True | 
| geo | Rate of DeleteGeofenceCollection API requests | L-779B9CA5 | 10.0 | None | False | True | 
| geo | Rate of ListGeofences API requests | L-2A3A5399 | 50.0 | None | False | True | 
| geo | Rate of DeletePlaceIndex API requests | L-D012773A | 10.0 | None | False | True | 
| geo | Geofences per Geofence Collection | L-DDC336FA | 50000.0 | None | False | False | 
| geo | Rate of DisassociateTrackerConsumer API requests | L-32299313 | 10.0 | None | False | True | 
| geo | Rate of GetGeofence API requests | L-E2B35742 | 50.0 | None | False | True | 
| geo | Geofence Collection resources per account | L-93FB3073 | 1500.0 | None | False | True | 
| geo | Rate of BatchEvaluateGeofences API requests | L-9A0A3162 | 50.0 | None | False | True | 
| geo | Rate of UpdateRouteCalculator API requests | L-85DB3370 | 10.0 | None | False | True | 
| geo | Rate of ListTrackers API requests | L-F0E58BD7 | 10.0 | None | False | True | 
| geo | Tracker resources per account | L-8CDBA5E9 | 500.0 | None | False | True | 
| geo | Rate of BatchGetDevicePosition API requests | L-1D4EB556 | 50.0 | None | False | True | 
| geo | Rate of GetMapSprites API requests | L-C2D15753 | 50.0 | None | False | True | 
| geo | Rate of ListTagsForResource API requests | L-E976E608 | 10.0 | None | False | True | 
| geo | Rate of CreateMap API requests | L-8A769EC2 | 10.0 | None | False | True | 
| geo | Rate of UpdatePlaceIndex API requests | L-AE2D8C2E | 10.0 | None | False | True | 
| geo | Rate of BatchUpdateDevicePosition API requests | L-16C77FC0 | 50.0 | None | False | True | 
| geo | Place Index resources per account | L-AF0CC293 | 40.0 | None | False | True | 
| geo | Rate of ListRouteCalculators API requests | L-D3A51B68 | 10.0 | None | False | True | 
| geo | Rate of GetMapTile API requests | L-7FB5719A | 500.0 | None | False | True | 
| geo | Rate of TagResource API requests | L-2CA6C84D | 10.0 | None | False | True | 
| geo | Rate of PutGeofence API requests | L-8C4D918C | 50.0 | None | False | True | 
| geo | Map resources per account | L-A94FDED2 | 40.0 | None | False | True | 
| geo | Rate of BatchPutGeofence API requests | L-4D8FB6E2 | 50.0 | None | False | True | 
| geo | Rate of SearchPlaceIndexForSuggestions API requests | L-EC3CCC13 | 50.0 | None | False | True | 
| geo | Rate of CreateGeofenceCollection API requests | L-DFE2C362 | 10.0 | None | False | True | 
| geo | Rate of GetMapGlyphs API requests | L-25528367 | 50.0 | None | False | True | 
| geo | Rate of CalculateRoute API requests | L-44B9F1A6 | 10.0 | None | False | True | 
| geo | Rate of SearchPlaceIndexForPosition API requests | L-201B3D58 | 50.0 | None | False | True | 
| geo | Rate of ListMaps API requests | L-004FBC04 | 10.0 | None | False | True | 
| geo | Rate of GetMapStyleDescriptor API requests | L-05EFD12D | 50.0 | None | False | True | 
| geo | Rate of GetPlace API requests | L-CF1B7B95 | 50.0 | None | False | True | 
| geo | Rate of UntagResource API requests | L-C236DAD6 | 10.0 | None | False | True | 
| geo | Rate of DeleteRouteCalculator API requests | L-EF11EFBE | 10.0 | None | False | True | 
| geo | Rate of ListGeofenceCollections API requests | L-42524A80 | 10.0 | None | False | True | 
| geo | Rate of DescribePlaceIndex API requests | L-772C0B77 | 10.0 | None | False | True | 
| geo | Rate of AssociateTrackerConsumer API requests | L-664067C5 | 10.0 | None | False | True | 
| geo | Rate of CalculateRouteMatrix API requests | L-0E174A76 | 5.0 | None | False | True | 
| geo | Rate of ListTrackerConsumers API requests | L-3B5E6DAC | 10.0 | None | False | True | 
| geo | Rate of DescribeGeofenceCollection API requests | L-68C0FF09 | 10.0 | None | False | True | 
| geo | Rate of GetDevicePosition API requests | L-55FCDA52 | 50.0 | None | False | True | 
| glue | Label file size | L-B78896B9 | 10.0 | Megabytes | False | True | 
| glue | Max jobs per account | L-611FDDE4 | 1000.0 | None | False | True | 
| glue | Max databases per catalog | L-A57B5BCE | 10000.0 | None | False | True | 
| glue | Number of crawlers per account | L-11FA2C1A | 1000.0 | None | False | True | 
| glue | Max functions per database | L-1DD415D5 | 100.0 | None | False | True | 
| glue | Max task DPUs per account | L-08F3B322 | 1000.0 | None | False | True | 
| glue | Max triggers per account | L-F1653A6D | 1000.0 | None | False | True | 
| glue | Concurrent machine learning task runs per transform | L-E15CE20A | 3.0 | None | False | True | 
| glue | Max connection per account | L-4256D6D2 | 1000.0 | None | False | True | 
| glue | Number of machine learning transforms | L-04CEE988 | 100.0 | None | False | True | 
| glue | Max partitions per table | L-2C3F5401 | 10000000.0 | None | False | True | 
| glue | Max partitions per account | L-FEBBFA7A | 20000000.0 | None | False | True | 
| glue | Total concurrent machine learning task runs for transforms per account | L-83A59AA6 | 30.0 | None | False | True | 
| glue | Max spare compute capacity consumed in data processing units (DPUs) per account. | L-096DBB95 | 50.0 | None | False | True | 
| glue | Max development endpoint per account | L-DBA56E2F | 25.0 | None | False | True | 
| glue | Max security configurations per account | L-83192DBF | 250.0 | None | False | True | 
| glue | Max functions per account | L-D987EC31 | 100.0 | None | False | True | 
| glue | Max databases per account | L-F953935E | 10000.0 | None | False | True | 
| glue | Max concurrent job runs per job | L-F574AED9 | 1000.0 | None | False | True | 
| glue | Max DPUs per dev endpoint | L-76EC689B | 50.0 | None | False | True | 
| glue | Max concurrent job runs per account | L-5E4153CA | 200.0 | None | False | True | 
| glue | Max table versions per table | L-071ABE08 | 100000.0 | None | False | True | 
| glue | Max tables per database | L-B8497671 | 200000.0 | None | False | True | 
| glue | Max tables per account | L-94D025B7 | 1000000.0 | None | False | True | 
| glue | Number of crawlers running concurrently per account | L-4071B0E3 | 150.0 | None | False | True | 
| glue | Max jobs per trigger | L-EEC98450 | 50.0 | None | False | True | 
| glue | Max table versions per account | L-337244C9 | 1000000.0 | None | False | True | 
| glue | Number of workflows | L-7DD7C33A | 250.0 | None | False | True | 
| grafana | Number of workspaces | L-2C2D5119 | 5.0 | None | False | True | 
| groundstation | Config limit | L-5CCF0BC2 | 100.0 | None | False | True | 
| groundstation | Scheduled Contacts Limit | L-DF7B6DEC | 100.0 | None | False | True | 
| groundstation | Ephemeris Validation limit | L-DE376FC5 | 10.0 | None | False | True | 
| groundstation | Contact Lead Time Maximum | L-09DEC198 | 7.0 | None | False | True | 
| groundstation | Scheduled Minutes Limit | L-FED20749 | 1000.0 | None | False | True | 
| groundstation | Maximum Contact Duration | L-CCFDE387 | 20.0 | None | False | True | 
| groundstation | Mission profile limit | L-5342B9BF | 100.0 | None | False | True | 
| groundstation | Dataflow endpoint group limit | L-D6A1915B | 100.0 | None | False | True | 
| groundstation | Dataflow endpoints per group limit | L-98A63A85 | 20.0 | None | False | True | 
| guardduty | Filters | L-9ABF7A23 | 100.0 | None | False | False | 
| guardduty | Threat intel sets | L-2C0E14B9 | 6.0 | None | False | False | 
| imagebuilder | Container recipes | L-28A502FD | 1000.0 | None | False | True | 
| imagebuilder | Component size | L-D5DC1FB3 | 64.0 | Kilobytes | False | True | 
| imagebuilder | Launch templates modified per distribution configuration | L-D5665818 | 5.0 | None | False | True | 
| imagebuilder | Image recipes | L-1DF98342 | 1000.0 | None | False | True | 
| imagebuilder | Parameters per component | L-A58CFBED | 25.0 | None | False | True | 
| imagebuilder | Concurrent builds | L-BA4D191B | 100.0 | None | False | True | 
| imagebuilder | Infrastructure configurations | L-D9EF98D9 | 1000.0 | None | False | True | 
| imagebuilder | Components per image recipe | L-59EC76F6 | 20.0 | None | False | False | 
| imagebuilder | Distribution configurations | L-2BAA05D8 | 1000.0 | None | False | True | 
| imagebuilder | Docker template size | L-84F5AB81 | 64.0 | Kilobytes | False | True | 
| imagebuilder | Components | L-9B183655 | 1000.0 | None | False | True | 
| imagebuilder | Component parameter length | L-10D22E0D | 1024.0 | None | False | True | 
| imagebuilder | Image pipelines | L-7A0E01E3 | 75.0 | None | False | True | 
| imagebuilder | Concurrent AMI copies per distribution configuration | L-69312229 | 50.0 | None | False | True | 
| iotanalytics | Number of StartPipelineReprocessing requests | L-EFB6780D | 1000.0 | None | False | True | 
| iotcore | ListThingGroups API TPS | L-1E5260D6 | 10.0 | None | False | True | 
| iotcore | DeleteThingGroup API TPS | L-FCAB1AF4 | 15.0 | None | False | True | 
| iotcore | CreateThingGroup API TPS | L-512F449C | 25.0 | None | False | True | 
| iotcore | ListPrincipalThings API TPS | L-C481616A | 10.0 | None | False | True | 
| iotcore | DescribeBillingGroup API TPS | L-23DF46E7 | 100.0 | None | False | True | 
| iotcore | UntagResource API TPS | L-8996ACA8 | 10.0 | None | False | True | 
| iotcore | ListBillingGroups API TPS | L-BB923BC2 | 10.0 | None | False | True | 
| iotcore | TagResource API TPS | L-06E76376 | 10.0 | None | False | True | 
| iotcore | DescribeThing API TPS | L-0EF0F5EE | 350.0 | None | False | True | 
| iotcore | DeleteBillingGroup API TPS | L-6C20C764 | 15.0 | None | False | True | 
| iotcore | DescribeThingType API TPS | L-DDCF8E97 | 100.0 | None | False | True | 
| iotcore | RemoveThingFromBillingGroup API TPS | L-FAF5733F | 15.0 | None | False | True | 
| iotcore | ListThingsInBillingGroup API TPS | L-E8797DCC | 25.0 | None | False | True | 
| iotcore | UpdateThing API TPS | L-211F680E | 100.0 | None | False | True | 
| iotcore | ListThingsInThingGroup API TPS | L-D33FD5F9 | 25.0 | None | False | True | 
| iotcore | DeprecateThingType API TPS | L-7F1DBFAE | 15.0 | None | False | True | 
| iotcore | RemoveThingFromThingGroup API TPS | L-2A81A394 | 100.0 | None | False | True | 
| iotcore | CreateThing API TPS | L-64CBACAC | 100.0 | None | False | True | 
| iotcore | ListThingTypes API TPS | L-F9EBF527 | 10.0 | None | False | True | 
| iotcore | DescribeThingGroup API TPS | L-52E1E197 | 100.0 | None | False | True | 
| iotcore | DeleteThingType API TPS | L-CFBDB489 | 15.0 | None | False | True | 
| iotcore | ListThings API TPS | L-57AAC135 | 10.0 | None | False | True | 
| iotcore | CreateDynamicThingGroup API TPS | L-7E0F5745 | 5.0 | None | False | True | 
| iotcore | DeleteThing API TPS | L-889800F7 | 100.0 | None | False | True | 
| iotcore | DeleteDynamicThingGroup API TPS | L-9DF61146 | 5.0 | None | False | True | 
| iotcore | AddThingToThingGroup API TPS | L-2904683A | 100.0 | None | False | True | 
| iotcore | DetachThingPrincipal API TPS | L-B5EE4A16 | 100.0 | None | False | True | 
| iotcore | UpdateBillingGroup API TPS | L-88CA286A | 15.0 | None | False | True | 
| iotcore | CreateThingType API TPS | L-8650816F | 15.0 | None | False | True | 
| iotcore | CreateBillingGroup API TPS | L-F2D09BC8 | 25.0 | None | False | True | 
| iotcore | ListThingPrincipals API TPS | L-FC3EF4D9 | 10.0 | None | False | True | 
| iotcore | ListTagsForResource API TPS | L-D127B7BE | 10.0 | None | False | True | 
| iotcore | ListThingGroupsForThing API TPS | L-75F129AD | 100.0 | None | False | True | 
| iotcore | AddThingToBillingGroup API TPS | L-1F4BE39E | 60.0 | None | False | True | 
| iotcore | UpdateThingGroup API TPS | L-5D84F9FE | 15.0 | None | False | True | 
| iotcore | AttachThingPrincipal API TPS | L-F64D1AA6 | 100.0 | None | False | True | 
| iotcore | UpdateDynamicThingGroup API TPS | L-E06BBD5F | 5.0 | None | False | True | 
| iottwinmaker | Entities per workspace | L-ADB4D9B9 | 10000.0 | None | False | True | 
| iottwinmaker | Depth of component type hierarchy | L-C511254B | 10.0 | None | False | True | 
| iottwinmaker | Workspaces in this account in the current Region | L-3BCB51AD | 15.0 | None | False | True | 
| iottwinmaker | Parent component types per child component type | L-0169BFDB | 10.0 | None | False | False | 
| iottwinmaker | Depth of entity hierarchy | L-019A0AE4 | 10.0 | None | False | True | 
| iottwinmaker | Component types per workspace | L-E97A4C92 | 150.0 | None | False | True | 
| iottwinmaker | Components per entity | L-FE672086 | 10.0 | None | False | True | 
| iottwinmaker | Tags per resource | L-6A666826 | 50.0 | None | False | False | 
| iottwinmaker | Scenes per workspace | L-8E0F7923 | 100.0 | None | False | True | 
| iottwinmaker | Child entities per parent entity | L-07A30954 | 100.0 | None | False | True | 
| iottwinmaker | Properties per component type or component | L-D8DF6F6C | 200.0 | None | False | True | 
| iotwireless | TPS limit for UpdateEventConfigurationByResourceTypes | L-882084A6 | 10.0 | None | False | True | 
| iotwireless | TPS limit for DisassociateAwsAccountFromPartnerAccount | L-A432E505 | 10.0 | None | False | True | 
| iotwireless | TPS limit for ListEventConfigurations | L-A2058506 | 10.0 | None | False | True | 
| iotwireless | TPS limit for DeleteWirelessGatewayTask | L-B0F3D444 | 10.0 | None | False | False | 
| iotwireless | TPS limit for GetWirelessGatewayTaskDefinition | L-7AF1469B | 10.0 | None | False | False | 
| iotwireless | TPS limit for GetDestination | L-8E7EAF51 | 10.0 | None | False | True | 
| iotwireless | TPS limit for ListWirelessDevices | L-35D1818B | 10.0 | None | False | True | 
| iotwireless | TPS limit for UntagResource | L-DF869DBB | 10.0 | None | False | True | 
| iotwireless | TPS limit for DisassociateWirelessDeviceFromFuotaTask | L-0C83FCE2 | 10.0 | None | False | True | 
| iotwireless | TPS limit for GetWirelessDevice | L-2639F0B0 | 10.0 | None | False | True | 
| iotwireless | TPS limit for StartNetworkAnalyzerStream | L-9E25CA04 | 10.0 | None | False | True | 
| iotwireless | TPS limit for UpdateResourcePosition | L-E01F1EA2 | 10.0 | None | False | True | 
| iotwireless | TPS limit for GetResourceLogLevel | L-6175FC12 | 10.0 | None | False | True | 
| iotwireless | TPS limit for GetPositionEstimate | L-D6B79324 | 10.0 | None | False | True | 
| iotwireless | TPS limit for UpdateLogLevelsByResourceTypes | L-0D8E249D | 10.0 | None | False | True | 
| iotwireless | TPS limit for GetResourceEventConfiguration | L-E4F0512E | 10.0 | None | False | True | 
| iotwireless | TPS limit for AssociateWirelessDeviceWithThing | L-6407631C | 10.0 | None | False | True | 
| iotwireless | TPS limit for CreateWirelessGatewayTaskDefinition | L-8FFCC81A | 10.0 | None | False | False | 
| iotwireless | TPS limit for TagResource | L-9D5A90BD | 10.0 | None | False | True | 
| iotwireless | TPS limit for CreateWirelessGateway | L-C2F6FC68 | 10.0 | None | False | True | 
| iotwireless | TPS limit for ListPartnerAccounts | L-FB636C37 | 10.0 | None | False | True | 
| iotwireless | TPS limit for ListServiceProfiles | L-647D6C46 | 10.0 | None | False | True | 
| iotwireless | TPS limit for DeleteMulticastGroup | L-93C5A1DB | 10.0 | None | False | True | 
| iotwireless | TPS limit for UpdateMulticastGroup | L-8E864D54 | 10.0 | None | False | True | 
| iotwireless | TPS limit for GetMulticastGroup | L-72A5D5E0 | 10.0 | None | False | True | 
| iotwireless | TPS limit for ListDestinations | L-E54A2621 | 10.0 | None | False | True | 
| iotwireless | TPS limit for ResetAllResourceLogLevels | L-96FA888E | 10.0 | None | False | True | 
| iotwireless | TPS limit for GetWirelessGatewayStatistics | L-3103F50C | 10.0 | None | False | False | 
| iotwireless | TPS limit for StartFuotaTask | L-DB770805 | 10.0 | None | False | True | 
| iotwireless | TPS limit for GetNetworkAnalyzerConfiguration | L-6AF47E8B | 10.0 | None | False | True | 
| iotwireless | TPS limit for AssociateMulticastGroupWithFuotaTask | L-E91B60DF | 10.0 | None | False | True | 
| iotwireless | TPS limit for ListWirelessGatewayTaskDefinitions | L-CC2D61C3 | 10.0 | None | False | False | 
| iotwireless | TPS limit for AssociateAwsAccountWithPartnerAccount | L-13EE3A12 | 10.0 | None | False | True | 
| iotwireless | TPS limit for ListDeviceProfiles | L-E6CBA335 | 10.0 | None | False | True | 
| iotwireless | TPS limit for GetLogLevelsByResourceTypes | L-C2175B1E | 10.0 | None | False | True | 
| iotwireless | TPS limit for StartMulticastGroupSession | L-6FC5E39D | 10.0 | None | False | True | 
| iotwireless | TPS limit for SendDataToMulticastGroup | L-1346D5EC | 10.0 | None | False | True | 
| iotwireless | TPS limit for CreateDeviceProfile | L-6829C2D4 | 10.0 | None | False | True | 
| iotwireless | TPS limit for DeleteQueuedMessages | L-B6937DF9 | 10.0 | None | False | True | 
| iotwireless | TPS limit for GetEventConfigurationByResourceTypes | L-FAE31118 | 10.0 | None | False | True | 
| iotwireless | TPS limit for GetWirelessGatewayCertificate | L-81B64868 | 10.0 | None | False | False | 
| iotwireless | TPS limit for ListNetworkAnalyzerConfigurations | L-0F5F17D1 | 10.0 | None | False | True | 
| iotwireless | TPS limit for CreateFuotaTask | L-E3C6A79E | 10.0 | None | False | True | 
| iotwireless | TPS limit for DisassociateMulticastGroupFromFuotaTask | L-61A27891 | 10.0 | None | False | True | 
| iotwireless | TPS limit for GetResourcePosition | L-F654617D | 10.0 | None | False | True | 
| iotwireless | TPS limit for ListWirelessGateways | L-F881E3D9 | 10.0 | None | False | True | 
| iotwireless | TPS limit for ListTagsForResource | L-DEC8385B | 10.0 | None | False | True | 
| iotwireless | TPS limit for UpdateFuotaTask | L-5369BF7E | 10.0 | None | False | True | 
| iotwireless | TPS limit for ListMulticastGroups | L-4DEB3C3F | 10.0 | None | False | True | 
| iotwireless | TPS limit for CreateDestination | L-0641E5DC | 10.0 | None | False | True | 
| iotwireless | TPS limit for CreateServiceProfile | L-F8530DBD | 10.0 | None | False | True | 
| iotwireless | TPS limit for UpdateNetworkAnalyzerConfiguration | L-8367137B | 10.0 | None | False | True | 
| iotwireless | TPS limit for GetWirelessGatewayTask | L-334EA895 | 10.0 | None | False | False | 
| iotwireless | TPS limit for GetWirelessGateway | L-42B55186 | 10.0 | None | False | True | 
| iotwireless | TPS limit for GetDeviceProfile | L-4FCAEFF0 | 10.0 | None | False | True | 
| iotwireless | TPS limit for DeleteWirelessGatewayTaskDefinition | L-182F8619 | 10.0 | None | False | False | 
| iotwireless | TPS limit for GetWirelessGatewayFirmwareInformation | L-0C3B538C | 10.0 | None | False | False | 
| iotwireless | TPS limit for UpdatePartnerAccount | L-3AC27648 | 10.0 | None | False | True | 
| iotwireless | TPS limit for GetWirelessDeviceStatistics | L-CCEFD4AF | 10.0 | None | False | False | 
| iotwireless | TPS limit for CancelMulticastGroupSession | L-72AB9EAE | 10.0 | None | False | True | 
| iotwireless | TPS limit for DeleteDeviceProfile | L-50B185BA | 10.0 | None | False | True | 
| iotwireless | TPS limit for DeleteFuotaTask | L-89C556FB | 10.0 | None | False | True | 
| iotwireless | TPS limit for UpdateDestination | L-AA413BB8 | 10.0 | None | False | True | 
| iotwireless | TPS limit for AssociateWirelessGatewayWithThing | L-B29C7ECC | 10.0 | None | False | True | 
| iotwireless | TPS limit for ListPositionConfigurations | L-F4D43AC0 | 10.0 | None | False | True | 
| iotwireless | TPS limit for UpdateWirelessDevice | L-B4636E40 | 10.0 | None | False | True | 
| iotwireless | TPS limit for PutPositionConfiguration | L-A4CD53FD | 10.0 | None | False | True | 
| iotwireless | TPS limit for GetServiceProfile | L-905ED905 | 10.0 | None | False | True | 
| iotwireless | TPS limit for ResetResourceLogLevel | L-9CF47CC5 | 10.0 | None | False | True | 
| iotwireless | TPS limit for AssociateWirelessDeviceWithMulticastGroup | L-92ECAB75 | 10.0 | None | False | True | 
| iotwireless | TPS limit for UpdateWirelessGateway | L-A1F96616 | 10.0 | None | False | True | 
| iotwireless | TPS limit for DeleteWirelessGateway | L-6DEF44D2 | 10.0 | None | False | True | 
| iotwireless | TPS limit for AssociateWirelessGatewayWithCertificate | L-4915A563 | 10.0 | None | False | False | 
| iotwireless | TPS limit for CreateNetworkAnalyzerConfiguration | L-6796B05C | 10.0 | None | False | True | 
| iotwireless | TPS limit for DisassociateWirelessDeviceFromThing | L-4951240E | 10.0 | None | False | True | 
| iotwireless | TPS limit for DisassociateWirelessDeviceFromMulticastGroup | L-1DF3438B | 10.0 | None | False | True | 
| iotwireless | TPS limit for GetServiceEndpoint | L-13F3B5DD | 10.0 | None | False | False | 
| iotwireless | TPS limit for DeleteServiceProfile | L-A25EC315 | 10.0 | None | False | True | 
| iotwireless | TPS limit for GetPosition | L-B8A41F6F | 10.0 | None | False | True | 
| iotwireless | TPS limit for GetFuotaTask | L-D33E220F | 10.0 | None | False | True | 
| iotwireless | TPS limit for GetMulticastGroupSession | L-9C8C92B3 | 10.0 | None | False | True | 
| iotwireless | TPS limit for UpdatePosition | L-C80BC655 | 10.0 | None | False | True | 
| iotwireless | TPS limit for TestWirelessDevice | L-FC84B266 | 10.0 | None | False | True | 
| iotwireless | TPS limit for CreateMulticastGroup | L-D07E0E7A | 10.0 | None | False | True | 
| iotwireless | TPS limit for CreateWirelessGatewayTask | L-05BE3C0D | 10.0 | None | False | False | 
| iotwireless | TPS limit for DeleteWirelessDevice | L-A755236A | 10.0 | None | False | True | 
| iotwireless | TPS limit for StartBulkDisassociateWirelessDeviceFromMulticastGroup | L-8DBB3861 | 10.0 | None | False | True | 
| iotwireless | TPS limit for ListQueuedMessages | L-D91B7067 | 10.0 | None | False | True | 
| iotwireless | TPS limit for UpdateResourceEventConfiguration | L-70D824D9 | 10.0 | None | False | True | 
| iotwireless | TPS limit for CreateWirelessDevice | L-3B5AF547 | 10.0 | None | False | True | 
| iotwireless | TPS limit for SendDataToWirelessDevice | L-0E4BA92F | 10.0 | None | False | True | 
| iotwireless | TPS limit for GetPositionConfiguration | L-5FCBB48D | 10.0 | None | False | True | 
| iotwireless | TPS limit for GetPartnerAccount | L-DEFAE009 | 10.0 | None | False | True | 
| iotwireless | TPS limit for ListMulticastGroupsByFuotaTask | L-7CE08A6C | 10.0 | None | False | True | 
| iotwireless | TPS limit for DisassociateWirelessGatewayFromThing | L-33206197 | 10.0 | None | False | True | 
| iotwireless | TPS limit for PutResourceLogLevel | L-12D6182B | 10.0 | None | False | True | 
| iotwireless | TPS limit for DeleteDestination | L-EB538AAC | 10.0 | None | False | True | 
| iotwireless | TPS limit for StartBulkAssociateWirelessDeviceWithMulticastGroup | L-F930F6AD | 10.0 | None | False | True | 
| iotwireless | TPS limit for DisassociateWirelessGatewayFromCertificate | L-907EFF6F | 10.0 | None | False | False | 
| iotwireless | TPS limit for ListFuotaTasks | L-0604C085 | 10.0 | None | False | True | 
| iotwireless | TPS limit for DeleteNetworkAnalyzerConfiguration | L-4F7C7CD3 | 10.0 | None | False | True | 
| iotwireless | TPS limit for AssociateWirelessDeviceWithFuotaTask | L-4AC6BBEA | 10.0 | None | False | True | 
| ivs | Concurrent views | L-77A18D5D | 15000.0 | None | False | True | 
| ivs | Stream Key | L-80F95143 | 1.0 | None | False | False | 
| ivs | Concurrent streams | L-FD1EB8A7 | 100.0 | None | False | True | 
| ivs | Recording configurations | L-90ABAB37 | 20.0 | None | False | True | 
| ivs | Channels | L-C01DFF58 | 5000.0 | None | False | True | 
| ivschat | Rate of DisconnectUser requests | L-0CF8D910 | 100.0 | None | False | True | 
| ivschat | Rooms | L-85B84D18 | 50000.0 | None | False | True | 
| ivschat | Message review handler timeout period | L-12580D29 | 200.0 | Milliseconds | False | False | 
| ivschat | Logging Configurations | L-F87B0F22 | 10.0 | None | False | True | 
| ivschat | Concurrent chat connections | L-2D7A45DA | 50000.0 | None | False | True | 
| ivschat | Rate of SendMessage requests | L-B11841BF | 1000.0 | None | False | True | 
| ivschat | Rate of messaging requests per connection | L-B96AB553 | 10.0 | None | False | False | 
| ivschat | Rate of DeleteMessage requests | L-766F0845 | 100.0 | None | False | True | 
| kafka | Number of configurations per account | L-B2FDE22A | 100.0 | None | False | True | 
| kafka | Number of revisions per configuration | L-36D29E8C | 50.0 | None | False | True | 
| kafka | Number of brokers per cluster | L-FAB9E493 | 30.0 | None | False | True | 
| kafka | Number of brokers per account | L-EDD31C36 | 90.0 | None | False | True | 
| kinesis | Shards per Region | L-0918CF54 | 500.0 | None | False | True | 
| kinesisvideo | Rate of UpdateStreamAPI requests | L-AEE268C4 | 50.0 | None | False | True | 
| kinesisvideo | Rate of GetICEServerConfigAPI requests per signaling channel | L-6A7E955C | 5.0 | None | False | False | 
| kinesisvideo | Rate of TagResourceAPI requests | L-84C54DF4 | 50.0 | None | False | True | 
| kinesisvideo | Rate of UpdateSignalingChannelAPI requests | L-00B1F645 | 50.0 | None | False | True | 
| kinesisvideo | ConnectAsMaster idle connection timeout | L-CCD54BEE | 600.0 | Seconds | False | False | 
| kinesisvideo | SendSDPAnswer message payload size | L-AD15B1B2 | 10.0 | Kilobytes | False | False | 
| kinesisvideo | GetMediaForFragmentList bandwidth | L-2FC7D6B2 | 200.0 | Megabits | False | True | 
| kinesisvideo | ConnectAsViewer GO_AWAY message grace period | L-912086DE | 60.0 | Seconds | False | False | 
| kinesisvideo | Rate of UntagStreamAPI requests | L-4E1944F3 | 50.0 | None | False | True | 
| kinesisvideo | Rate of UntagResourceAPI requests per resource | L-C0373393 | 5.0 | None | False | True | 
| kinesisvideo | Rate of ListSignalingChannelsAPI requests | L-66B2FAAB | 50.0 | None | False | True | 
| kinesisvideo | Rate of SendSDPOfferAPI requests per websocket connection | L-F6EB90C7 | 5.0 | None | False | False | 
| kinesisvideo | ConnectAsMaster connections per signaling channel | L-C122494E | 1.0 | None | False | False | 
| kinesisvideo | Rate of SendICECandidateAPI requests per websocket connection | L-85B46D1C | 20.0 | None | False | False | 
| kinesisvideo | Rate of GetMP4MediaFragmentAPI requests per session | L-7D08463B | 20.0 | None | False | True | 
| kinesisvideo | Rate of ConnectAsMasterAPI requests per signaling channel | L-65A25202 | 3.0 | None | False | False | 
| kinesisvideo | TURN session expiration | L-AD9AD2F3 | 300.0 | Seconds | False | False | 
| kinesisvideo | Rate of TagStreamAPI requests per stream | L-8F38419A | 5.0 | None | False | True | 
| kinesisvideo | TURN session bandwidth | L-E4F56E4A | 5.0 | Megabits | False | False | 
| kinesisvideo | GetMedia concurrent connections per stream | L-B71B4FEE | 3.0 | None | False | True | 
| kinesisvideo | Rate of DeleteSignalingChannelAPI requests | L-F7EF17C6 | 50.0 | None | False | True | 
| kinesisvideo | Rate of ListTagsForResourceAPI requests | L-FD6244B8 | 50.0 | None | False | True | 
| kinesisvideo | Rate of CreateSignalingChannelAPI requests | L-32D5DC79 | 50.0 | None | False | True | 
| kinesisvideo | Rate of DeleteSignalingChannelAPI requests per signaling channel | L-FDF11C98 | 5.0 | None | False | True | 
| kinesisvideo | Rate of UpdateStreamAPI requests per stream | L-007A0A1E | 5.0 | None | False | True | 
| kinesisvideo | ConnectAsViewer idle connection timeout | L-0528E1BD | 600.0 | Seconds | False | False | 
| kinesisvideo | PutMedia minimum fragment duration | L-2C56AD83 | 1.0 | Seconds | False | False | 
| kinesisvideo | GetDASHManifestPlaylist fragments | L-87FBA326 | 5000.0 | None | False | False | 
| kinesisvideo | PutMedia tracks | L-F42E49F0 | 3.0 | None | False | False | 
| kinesisvideo | Rate of SendAlexaOfferToMasterAPI requests per signaling channel | L-782F9031 | 5.0 | None | False | False | 
| kinesisvideo | Rate of TagResourceAPI requests per resource | L-A34DF4E5 | 5.0 | None | False | True | 
| kinesisvideo | Rate of ListTagsForResourceAPI requests per resource | L-F10078DD | 5.0 | None | False | True | 
| kinesisvideo | Rate of GetHLSMasterPlaylistAPI requests per session | L-031A11B8 | 5.0 | None | False | True | 
| kinesisvideo | Rate of GetHLSStreamingSessionURLAPI requests per stream | L-C2CB1AD1 | 25.0 | None | False | True | 
| kinesisvideo | TURN session concurrent allocations per signaling channel | L-AB63770C | 50.0 | None | False | False | 
| kinesisvideo | Rate of ConnectAsViewerAPI requests per signaling channel | L-3DF8FB52 | 3.0 | None | False | False | 
| kinesisvideo | PutMedia fragment duration | L-EDC0C00D | 10.0 | Seconds | False | True | 
| kinesisvideo | Number of signaling channels | L-B7F419CA | 10000.0 | None | False | True | 
| kinesisvideo | GetMediaForFragmentList connections per stream | L-DE85179A | 5.0 | None | False | False | 
| kinesisvideo | Rate of GetHLSMediaPlaylistAPI requests per session | L-EDC81B7E | 5.0 | None | False | True | 
| kinesisvideo | Rate of UntagStreamAPI requests per stream | L-409E30B3 | 5.0 | None | False | True | 
| kinesisvideo | SendICECandidate message payload size | L-F43C3E04 | 10.0 | Kilobytes | False | False | 
| kinesisvideo | GetMedia bandwidth | L-BF0D282F | 200.0 | Megabits | False | True | 
| kinesisvideo | Rate of GetMediaAPI requests per stream | L-885A87A1 | 5.0 | None | False | True | 
| kinesisvideo | PutMedia fragment size | L-6F5F7717 | 50.0 | Megabytes | False | False | 
| kinesisvideo | Rate of SendSDPAnswerAPI requests per websocket connection | L-38A739F2 | 5.0 | None | False | False | 
| kinesisvideo | Number of video streams | L-F06528A6 | 10000.0 | None | False | True | 
| kinesisvideo | Rate of DescribeStreamAPI requests | L-BAA6C939 | 300.0 | None | False | True | 
| kinesisvideo | Rate of GetDASHStreamingSessionURLAPI requests per stream | L-2087401F | 25.0 | None | False | True | 
| kinesisvideo | Rate of TagStreamAPI requests | L-CAEB7065 | 50.0 | None | False | True | 
| kinesisvideo | PutMedia concurrent connections per stream | L-08EC4D9E | 1.0 | None | False | False | 
| kinesisvideo | Rate of DeleteStreamAPI requests | L-A34FDF94 | 50.0 | None | False | True | 
| kinesisvideo | ConnectAsMaster connection duration | L-33EBA7A5 | 3600.0 | Seconds | False | False | 
| kinesisvideo | ConnectAsMaster GO_AWAY message grace period | L-1FE8DF31 | 60.0 | Seconds | False | False | 
| kinesisvideo | Rate of UpdateDataRetentionAPI requests per stream | L-B7CB457B | 5.0 | None | False | True | 
| kinesisvideo | Rate of DescribeSignalingChannelAPI requests | L-99F327D1 | 300.0 | None | False | True | 
| kinesisvideo | Rate of ListTagsForStreamAPI requests | L-A8327CB5 | 50.0 | None | False | True | 
| kinesisvideo | Rate of GetSignalingChannelEndpointAPI requests per signaling channel | L-35D8C370 | 5.0 | None | False | True | 
| kinesisvideo | ConnectAsViewer connection duration | L-F0B5EFE9 | 3600.0 | Seconds | False | False | 
| kinesisvideo | Rate of GetDataEndpointAPI requests per stream | L-DCCB6A93 | 5.0 | None | False | True | 
| kinesisvideo | Rate of UpdateSignalingChannelAPI requests per signaling channel | L-1190DACE | 5.0 | None | False | True | 
| kinesisvideo | Rate of CreateStreamAPI requests | L-08F65F09 | 50.0 | None | False | True | 
| kinesisvideo | Rate of UntagResourceAPI requests | L-C030232D | 50.0 | None | False | True | 
| kinesisvideo | PutMedia bandwidth | L-354AF9F0 | 100.0 | Megabits | False | True | 
| kinesisvideo | Rate of UpdateDataRetentionAPI requests | L-6C5E79A7 | 50.0 | None | False | True | 
| kinesisvideo | GetClip file size | L-FD863935 | 100.0 | Megabytes | False | False | 
| kinesisvideo | Rate of GetSignalingChannelEndpointAPI requests | L-A0781139 | 300.0 | None | False | True | 
| kinesisvideo | GetHLSMediaPlaylist fragments | L-DAAD01CD | 5000.0 | None | False | False | 
| kinesisvideo | GetMediaForFragmentList fragments | L-EDF96A63 | 1000.0 | None | False | False | 
| kinesisvideo | SendSDPOffer message payload size | L-3E968CB6 | 10.0 | Kilobytes | False | False | 
| kinesisvideo | Rate of GetTSFragmentAPI requests per session | L-08A947EC | 20.0 | None | False | True | 
| kinesisvideo | Rate of DescribeSignalingChannelAPI requests per signaling channel | L-9A1B0418 | 5.0 | None | False | True | 
| kinesisvideo | Rate of GetDASHManifestPlaylistAPI requests per session | L-004D0B56 | 5.0 | None | False | True | 
| kinesisvideo | Rate of GetDataEndpointAPI requests | L-0AB4413A | 300.0 | None | False | True | 
| kinesisvideo | GetClip fragments | L-00CBFFF8 | 200.0 | None | False | False | 
| kinesisvideo | Rate of DeleteStreamAPI requests per stream | L-18823A76 | 5.0 | None | False | True | 
| kinesisvideo | ConnectAsViewer connections per signaling channel | L-8F974349 | 10.0 | None | False | True | 
| kinesisvideo | Rate of ListTagsForStreamAPI requests per stream | L-4450B3B7 | 5.0 | None | False | True | 
| kinesisvideo | Rate of PutMediaAPI requests per stream | L-D87CE70F | 5.0 | None | False | True | 
| kinesisvideo | Rate of ListStreamsAPI requests | L-B16CD5E1 | 50.0 | None | False | True | 
| kinesisvideo | Rate of DescribeStreamAPI requests per stream | L-07A0DA4B | 5.0 | None | False | True | 
| kinesisvideo | Rate of GetMP4InitFragmentAPI requests per session | L-F65F9A02 | 5.0 | None | False | True | 
| kms | UpdateCustomKeyStore request rate | L-275D92F3 | 5.0 | None | False | True | 
| kms | ListKeys request rate | L-8A08DAEA | 500.0 | None | False | True | 
| kms | ListResourceTags request rate | L-FB6513A2 | 2000.0 | None | False | True | 
| kms | Key policy document size | L-8D683C05 | 32768.0 | Bytes | False | False | 
| kms | GetParametersForImport request rate | L-515A0541 | 0.25 | None | False | True | 
| kms | GetPublicKey request rate | L-E4FBCA5E | 2000.0 | None | False | True | 
| kms | GetKeyRotationStatus request rate | L-D7711EF4 | 1000.0 | None | False | True | 
| kms | ReplicateKey request rate | L-E1C93865 | 5.0 | None | False | True | 
| kms | DisableKeyRotation request rate | L-CE1DB614 | 5.0 | None | False | True | 
| kms | EnableKey request rate | L-BD96F100 | 5.0 | None | False | True | 
| kms | UntagResource request rate | L-6375F442 | 5.0 | None | False | True | 
| kms | GenerateDataKeyPair (RSA_3072) request rate | L-AE57B391 | 0.5 | None | False | True | 
| kms | ListRetirableGrants request rate | L-161E93A6 | 100.0 | None | False | True | 
| kms | DeleteAlias request rate | L-1F75ADD1 | 15.0 | None | False | True | 
| kms | Cryptographic operations (RSA) request rate | L-2AC98190 | 500.0 | None | False | True | 
| kms | ScheduleKeyDeletion request rate | L-88313D4A | 15.0 | None | False | True | 
| kms | Cryptographic operations (ECC) request rate | L-DC14942D | 300.0 | None | False | True | 
| kms | GenerateDataKeyPair (RSA_4096) request rate | L-FCE4492D | 0.1 | None | False | True | 
| kms | GetKeyPolicy request rate | L-A2A30EC6 | 1000.0 | None | False | True | 
| kms | ConnectCustomKeyStore request rate | L-705B9E79 | 5.0 | None | False | True | 
| kms | ListAliases request rate | L-BF3F8F1D | 500.0 | None | False | True | 
| kms | UpdatePrimaryRegion request rate | L-F83AC7F7 | 5.0 | None | False | True | 
| kms | RetireGrant request rate | L-74021A59 | 30.0 | None | False | True | 
| kms | DisableKey request rate | L-6B8C93BD | 5.0 | None | False | True | 
| kms | GenerateDataKeyPair (ECC_NIST_P521) request rate | L-1D966DA0 | 5.0 | None | False | True | 
| kms | GenerateDataKeyPair (ECC_SECG_P256K1) request rate | L-3B372FA9 | 25.0 | None | False | True | 
| kms | CreateAlias request rate | L-F7504F73 | 5.0 | None | False | True | 
| kms | Grants per CMK | L-D594A657 | 50000.0 | None | False | True | 
| kms | UpdateAlias request rate | L-DB3BF542 | 5.0 | None | False | True | 
| kms | CreateGrant request rate | L-0428A42E | 50.0 | None | False | True | 
| kms | ListGrants request rate | L-D39AB822 | 100.0 | None | False | True | 
| kms | DescribeCustomKeyStores request rate | L-E20AA94C | 5.0 | None | False | True | 
| kms | DisconnectCustomKeyStore request rate | L-9F1FCF6D | 5.0 | None | False | True | 
| kms | ListKeyPolicies request rate | L-79E0D0AB | 100.0 | None | False | True | 
| kms | Custom Key Stores | L-F33DCFEB | 10.0 | None | False | False | 
| kms | Customer Master Keys (CMKs) | L-C2F1777E | 100000.0 | None | False | True | 
| kms | PutKeyPolicy request rate | L-9DDDE6CA | 15.0 | None | False | True | 
| kms | DeleteImportedKeyMaterial request rate | L-1233BF9B | 5.0 | None | False | True | 
| kms | CreateCustomKeyStore request rate | L-08932E37 | 5.0 | None | False | True | 
| kms | UpdateKeyDescription request rate | L-A3828E1F | 5.0 | None | False | True | 
| kms | Cryptographic operations (symmetric) request rate | L-6E3AF000 | 50000.0 | None | False | True | 
| kms | TagResource request rate | L-7D6DE447 | 10.0 | None | False | True | 
| kms | GenerateDataKeyPair (ECC_NIST_P384) request rate | L-16B46EF0 | 10.0 | None | False | True | 
| kms | ImportKeyMaterial request rate | L-99631835 | 5.0 | None | False | True | 
| kms | Aliases per CMK | L-340F62FB | 50.0 | None | False | True | 
| kms | CancelKeyDeletion request rate | L-635264CC | 5.0 | None | False | True | 
| kms | GenerateDataKeyPair (ECC_NIST_P256) request rate | L-D2EEB5E0 | 25.0 | None | False | True | 
| kms | DeleteCustomKeyStore request rate | L-E99520CB | 5.0 | None | False | True | 
| kms | CreateKey request rate | L-32B67F4A | 5.0 | None | False | True | 
| kms | DescribeKey request rate | L-FAE8F084 | 2000.0 | None | False | True | 
| kms | RevokeGrant request rate | L-F20EBCB7 | 30.0 | None | False | True | 
| kms | GenerateDataKeyPair (RSA_2048) request rate | L-77042783 | 1.0 | None | False | True | 
| kms | EnableKeyRotation request rate | L-BE799B67 | 15.0 | None | False | True | 
| lambda | Function and layer storage | L-2ACBD22F | 75.0 | Gigabytes | False | True | 
| lambda | Concurrent executions | L-B99A9384 | 1000.0 | None | False | True | 
| lex | Custom slot type values and synonyms per bot locale (V2) | L-824BBA1D | 50000.0 | None | False | False | 
| lex | Slots per bot locale (V2) | L-9030FC28 | 2000.0 | None | False | False | 
| lex | Bots per account (V2) | L-36FA8BD2 | 100.0 | None | False | True | 
| lex | Characters per sample utterance (V2) | L-4F321B43 | 500.0 | None | False | False | 
| lex | Sample utterances per intent (V2) | L-ED50DA7C | 1500.0 | None | False | True | 
| lex | Versions per bot (V2) | L-BCD96794 | 100.0 | None | False | False | 
| lex | Values and synonyms per custom slot type (V2) | L-52297D95 | 10000.0 | None | False | False | 
| lex | Custom slot types per bot locale (V2) | L-3D56827F | 100.0 | None | False | False | 
| lex | Slots per intent (V2) | L-311093B9 | 100.0 | None | False | False | 
| lex | Total characters in sample utterances per bot locale (V2) | L-606F3490 | 200000.0 | None | False | False | 
| lex | Bot channel associations per bot alias (V2) | L-DA28F59B | 10.0 | None | False | False | 
| lex | Sample utterances per slot (V2) | L-77D6C60C | 10.0 | None | False | True | 
| lex | Characters per custom slot type value (V2) | L-9E828085 | 500.0 | None | False | False | 
| license-manager | License configurations | L-CDB75D7A | 25.0 | None | False | True | 
| license-manager | License configuration associations per resource | L-0B08C8C5 | 10.0 | None | False | True | 
| logs | DescribeSubscriptionFilters throttle limit in transactions per second | L-9D43025B | 5.0 | None | False | False | 
| logs | DeleteSubscriptionFilter throttle limit in transactions per second | L-56B91A0A | 5.0 | None | False | False | 
| logs | ListTagsLogGroup throttle limit in transactions per second | L-3E4C85B1 | 5.0 | None | False | False | 
| logs | DeleteMetricFilter throttle limit in transactions per second | L-363FC8B0 | 5.0 | None | False | False | 
| logs | PutRetentionPolicy throttle limit in transactions per second | L-0397E41F | 5.0 | None | False | False | 
| logs | TestMetricFilter throttle limit in transactions per second | L-1CD226BD | 5.0 | None | False | False | 
| logs | Batch size | L-29A639F6 | 1.0 | Megabytes | False | False | 
| logs | Event size | L-91470774 | 256.0 | Kilobytes | False | False | 
| logs | UntagLogGroup throttle limit in transactions per second | L-EEEC3365 | 5.0 | None | False | False | 
| logs | Active export task | L-EEC839DF | 1.0 | None | False | False | 
| logs | StartQuery throttle limit in transactions per second | L-4FC2190A | 5.0 | None | False | False | 
| logs | ListTagsForResource throttle limit in transactions per second | L-E6EF8674 | 5.0 | None | False | False | 
| logs | CreateLogGroup throttle limit in transactions per second | L-D2832119 | 5.0 | None | False | True | 
| logs | CancelExportTask throttle limit in transactions per second | L-97393AE2 | 5.0 | None | False | False | 
| logs | DescribeLogGroups throttle limit in transactions per second | L-4284EEDE | 5.0 | None | False | True | 
| logs | FilterLogEvents throttle limit in transactions per second | L-55E3CA17 | 10.0 | None | False | False | 
| logs | TagLogGroup throttle limit in transactions per second | L-BBECF742 | 5.0 | None | False | False | 
| logs | AssociateKmsKey throttle limit in transactions per second | L-7A4B5D2F | 5.0 | None | False | False | 
| logs | DescribeLogStreams throttle limit in transactions per second | L-3F243AD0 | 5.0 | None | False | True | 
| logs | DeleteLogStream throttle limit in transactions per second | L-C029A21C | 5.0 | None | False | False | 
| logs | CreateLogStream throttle limit in transactions per second | L-76507CEF | 50.0 | None | False | True | 
| logs | PutMetricFilter throttle limit in transactions per second | L-E5FB5933 | 5.0 | None | False | False | 
| logs | PutSubscriptionFilter throttle limit in transactions per second | L-A5D79081 | 5.0 | None | False | False | 
| logs | PutDestination throttle limit in transactions per second | L-7A9B3427 | 5.0 | None | False | False | 
| logs | DeleteRetentionPolicy throttle limit in transactions per second | L-66F5762A | 5.0 | None | False | False | 
| logs | UntagResource throttle limit in transactions per second | L-B501C43C | 5.0 | None | False | False | 
| logs | CreateExportTask throttle limit in transactions per second | L-BD9DB0EB | 5.0 | None | False | False | 
| logs | PutDestinationPolicy throttle limit in transactions per second | L-7EB1C513 | 5.0 | None | False | False | 
| logs | Log groups | L-C7B9AAAB | 1000000.0 | None | False | True | 
| logs | GetLogEvents throttle limit in transactions per second | L-4FE15505 | 10.0 | None | False | False | 
| logs | DescribeDestinations throttle limit in transactions per second | L-BEB90E24 | 5.0 | None | False | False | 
| logs | PutLogEvents throttle limit in transactions per second | L-7E1FAE88 | 1500.0 | None | False | True | 
| logs | Metrics filters per log group | L-3D5753EA | 100.0 | None | False | False | 
| logs | GetQueryResults  throttle limit in transactions per second | L-FAF0999A | 5.0 | None | False | False | 
| logs | DescribeMetricFilters throttle limit in transactions per second | L-69BF6BAC | 5.0 | None | False | False | 
| logs | DeleteDestination throttle limit in transactions per second | L-BE2A59B1 | 5.0 | None | False | False | 
| logs | Subscription filters per log group | L-87E7D306 | 2.0 | None | False | False | 
| logs | DescribeExportTasks throttle limit in transactions per second | L-ACAEE94E | 5.0 | None | False | False | 
| logs | TagResource throttle limit in transactions per second | L-956BB71D | 5.0 | None | False | False | 
| logs | Data archiving | L-A33040DC | 5.0 | Gigabytes | False | False | 
| logs | DeleteLogGroup throttle limit in transactions per second | L-07A912D5 | 5.0 | None | False | True | 
| lookoutmetrics | Throttle rate (CreateAnomalyDetector) | L-56F61C6F | 1.0 | None | False | True | 
| lookoutmetrics | Throttle rate (DescribeMetricSet) | L-020F22D6 | 2.0 | None | False | True | 
| lookoutmetrics | Dimensions per dataset | L-3F1EEFE9 | 10.0 | None | False | False | 
| lookoutmetrics | Time series per interval (5m) | L-367E0B91 | 5000.0 | None | False | False | 
| lookoutmetrics | Throttle rate (ListAnomalyDetectors) | L-5D0258C0 | 2.0 | None | False | True | 
| lookoutmetrics | Throttle rate (GetSampleData) | L-0F70E4A0 | 2.0 | None | False | True | 
| lookoutmetrics | Records per interval (5m) | L-943788CD | 15000.0 | None | False | True | 
| lookoutmetrics | Records per interval (1h) | L-535C09C0 | 150000.0 | None | False | True | 
| lookoutmetrics | Throttle rate (GetAnomalyGroup) | L-D87ABA33 | 2.0 | None | False | True | 
| lookoutmetrics | Throttle rate (UpdateAnomalyDetector) | L-29051655 | 1.0 | None | False | True | 
| lookoutmetrics | Throttle rate (ListAlerts) | L-E7EB46AB | 2.0 | None | False | True | 
| lookoutmetrics | Throttle rate (DescribeAlert) | L-F2FA38BF | 2.0 | None | False | True | 
| lookoutmetrics | Throttle rate (ListAnomalyGroupRelatedMetrics) | L-2CD2EB7E | 2.0 | None | False | True | 
| lookoutmetrics | Files per interval (1h) | L-1FDF7B91 | 10.0 | None | False | True | 
| lookoutmetrics | Throttle rate (ActivateAnomalyDetector) | L-7548F78A | 1.0 | None | False | True | 
| lookoutmetrics | Time series per interval (1d) | L-989594D2 | 50000.0 | None | False | True | 
| lookoutmetrics | Throttle rate | L-F75BB1C7 | 10.0 | None | False | True | 
| lookoutmetrics | Throttle rate (DescribeAnomalyDetectionExecutions) | L-A384774A | 2.0 | None | False | True | 
| lookoutmetrics | Alerts | L-3AA7C566 | 10.0 | None | False | True | 
| lookoutmetrics | Throttle rate (UpdateMetricSet) | L-970F0018 | 1.0 | None | False | True | 
| lookoutmetrics | Throttle rate (CreateAlert) | L-F84BD970 | 1.0 | None | False | True | 
| lookoutmetrics | Datasets per detector | L-FF74E011 | 1.0 | None | False | False | 
| lookoutmetrics | Throttle rate (GetFeedback) | L-2AF7F498 | 2.0 | None | False | True | 
| lookoutmetrics | Measures per dataset | L-E09315CD | 10.0 | None | False | False | 
| lookoutmetrics | Records per interval (10m) | L-B7D162E6 | 24000.0 | None | False | True | 
| lookoutmetrics | Throttle rate (ListAnomalyGroupSummaries) | L-F256354A | 2.0 | None | False | True | 
| lookoutmetrics | Files per interval (1d) | L-46692FC3 | 10.0 | None | False | True | 
| lookoutmetrics | Files per interval (5m) | L-7C0C1E87 | 5.0 | None | False | True | 
| lookoutmetrics | Throttle rate (GetDataQualityMetrics) | L-1EFB34E0 | 2.0 | None | False | True | 
| lookoutmetrics | Files per interval (10m) | L-0BC408F8 | 5.0 | None | False | True | 
| lookoutmetrics | Throttle rate (BackTestAnomalyDetector) | L-4B1617A5 | 1.0 | None | False | True | 
| lookoutmetrics | Throttle rate (DeleteAlert) | L-AA1B9C20 | 1.0 | None | False | True | 
| lookoutmetrics | Throttle rate (ListAnomalyGroupTimeSeries) | L-B10A1291 | 2.0 | None | False | True | 
| lookoutmetrics | Throttle rate (ListMetricSets) | L-E907B4C2 | 2.0 | None | False | True | 
| lookoutmetrics | Value length | L-5F537F31 | 40.0 | Bytes | False | True | 
| lookoutmetrics | Throttle rate (CreateMetricSet) | L-42533647 | 1.0 | None | False | True | 
| lookoutmetrics | Datasources per dataset | L-8BAF8991 | 1.0 | None | False | False | 
| lookoutmetrics | Time series per interval (10m) | L-9A2D9472 | 10000.0 | None | False | False | 
| lookoutmetrics | Records per interval (1d) | L-4CDD974B | 150000.0 | None | False | True | 
| lookoutmetrics | Throttle rate (DescribeAnomalyDetector) | L-70CC6666 | 2.0 | None | False | True | 
| lookoutmetrics | Throttle rate (PutFeedback) | L-17A5470E | 1.0 | None | False | True | 
| lookoutmetrics | Throttle rate (DeleteAnomalyDetector) | L-8C031EB7 | 1.0 | None | False | True | 
| lookoutmetrics | Detectors | L-5EB8352D | 10.0 | None | False | True | 
| lookoutmetrics | Time series per interval (1h) | L-61F79416 | 50000.0 | None | False | True | 
| m2 | Max number of EFS filesystems per environment | L-5D943D0B | 1.0 | None | False | True | 
| m2 | Max Instances Per High Availability Environment | L-24ACBEAE | 12.0 | None | False | True | 
| m2 | Max Applications Per AWS Account | L-00464274 | 20.0 | None | False | True | 
| m2 | Max Environments Per AWS Account | L-6851C542 | 20.0 | None | False | True | 
| m2 | Max number of FSX filesystems per environment | L-C1C41257 | 1.0 | None | False | True | 
| macie2 | Sensitive data discovery per month per account | L-FEB8D34D | 5.0 | Terabytes | False | True | 
| mediaconnect | Flows | L-A99016A8 | 20.0 | None | False | True | 
| mediaconnect | Entitlements | L-F1F62F5D | 50.0 | None | False | False | 
| mediaconnect | Outputs | L-CB77E87E | 50.0 | None | False | False | 
| medialive | Channels | L-D1AFAF75 | 5.0 | None | False | True | 
| medialive | Device Inputs | L-BDF24E14 | 100.0 | None | False | True | 
| medialive | UHD Channels | L-DDE858F0 | 1.0 | None | False | True | 
| medialive | Pull Inputs | L-4D7207DE | 100.0 | None | False | True | 
| medialive | CDI Channels | L-3FDA265B | 2.0 | None | False | True | 
| medialive | HEVC Channels | L-05A796F2 | 5.0 | None | False | True | 
| medialive | Push Inputs | L-9E233AF7 | 5.0 | None | False | True | 
| medialive | VPC Inputs | L-68E02936 | 50.0 | None | False | True | 
| medialive | Multiplexes | L-8B49C5C1 | 2.0 | None | False | True | 
| medialive | Input Security Groups | L-6A0116BB | 5.0 | None | False | True | 
| medialive | Reservations | L-1F6E2FAF | 50.0 | None | False | True | 
| mediapackage | Tracks per ingest stream (VOD) | L-81A8E99B | 10.0 | None | False | False | 
| mediapackage | Tracks per ingest stream (Live) | L-258E8DBA | 10.0 | None | False | False | 
| mediapackage | Packaging groups | L-66FFDBE4 | 10.0 | None | False | True | 
| mediapackage | Rate of manifest egress requests per asset | L-1E11547D | 1000.0 | None | False | False | 
| mediapackage | Live manifest length | L-F7CB14AC | 5.0 | None | False | True | 
| mediapackage | Rate of REST API requests (Live) | L-2FF063D2 | 5.0 | None | False | False | 
| mediapackage | Content retention | L-3C7827C4 | 336.0 | None | False | False | 
| mediapackage | Rate of manifest egress requests per origin endpoint | L-BC1EEC38 | 5000.0 | None | False | False | 
| mediapackage | Assets per packaging group | L-563EE697 | 10000.0 | None | False | True | 
| mediapackage | Endpoints per channel | L-7F7EDDDF | 10.0 | None | False | True | 
| mediapackage | Burst rate of REST API requests (Live) | L-F0A6E997 | 50.0 | None | False | False | 
| mediapackage | Rate of segment egress requests per origin endpoint | L-BEF6A5C5 | 300.0 | None | False | False | 
| mediapackage | Burst rate of REST API requests (VOD) | L-1D216601 | 50.0 | None | False | False | 
| mediapackage | Ingest streams per channel | L-5625C794 | 20.0 | None | False | False | 
| mediapackage | Rate of REST API requests (VOD) | L-20E16360 | 5.0 | None | False | False | 
| mediapackage | Concurrent harvest jobs | L-B1B90B42 | 10.0 | None | False | True | 
| mediapackage | Channels | L-352B8598 | 30.0 | None | False | True | 
| mediapackage | Rate of ingest requests per channel | L-F461E421 | 50.0 | None | False | False | 
| mediapackage | Packaging configurations per packaging group | L-1E1258F1 | 10.0 | None | False | True | 
| mediapackage | Time-shifted manifest length | L-8D3D8B62 | 24.0 | None | False | False | 
| mediapackage | Ingest streams per asset | L-4D5703CE | 20.0 | None | False | False | 
| mediapackage | Rate of segment egress requests per asset | L-80529300 | 600.0 | None | False | False | 
| mediastore | Rate of PutObject API requests for chunked transfer encoding (also known as streaming upload availability) | L-CAF2EF73 | 10.0 | None | False | True | 
| mediastore | Rate of DeleteObject API requests | L-2FCDD326 | 100.0 | None | False | True | 
| mediastore | Rate of GetObject API requests for standard upload availability | L-DB1D877F | 1000.0 | None | False | True | 
| mediastore | Rate of ListItems API requests | L-97AEAA6B | 5.0 | None | False | True | 
| mediastore | Rate of PutObject API requests for standard upload availability | L-CA39FABB | 100.0 | None | False | True | 
| mediastore | Rate of GetObject API requests for streaming upload availability | L-FA6DBE33 | 25.0 | None | False | True | 
| mediastore | Rate of DescribeObject API requests | L-8038710B | 1000.0 | None | False | True | 
| mgn | Max active applications | L-D5507441 | 200.0 | None | False | False | 
| mgn | Max archived waves | L-BB9C7114 | 10000.0 | None | False | False | 
| mgn | Max Total Source Servers Per AWS Account | L-967C958D | 50000.0 | None | False | False | 
| mgn | Max actions per source server | L-0E532B45 | 100.0 | None | False | False | 
| mgn | Max actions per template | L-322CA331 | 100.0 | None | False | False | 
| mgn | Max active waves | L-9FD6E875 | 200.0 | None | False | False | 
| mgn | Max Active Source Servers | L-9A599620 | 20.0 | None | False | True | 
| mgn | Max source servers per application | L-90A3F9F5 | 200.0 | None | False | False | 
| mgn | Max applications per wave | L-CBE9E36A | 1000.0 | None | False | False | 
| mgn | Max archived applications | L-391504A2 | 10000.0 | None | False | False | 
| monitoring | Rate of GetMetricWidgetImage requests | L-6FCAAA2E | 20.0 | None | False | True | 
| monitoring | Rate of ListDashboards requests | L-69C44FFD | 10.0 | None | False | True | 
| monitoring | Rate of DescribeAlarmsForMetric requests | L-E2310E7A | 3.0 | None | False | False | 
| monitoring | Rate of EnableAlarmActions requests | L-CA907765 | 3.0 | None | False | False | 
| monitoring | Rate of GetMetricData requests | L-5E141212 | 50.0 | None | False | True | 
| monitoring | Canary limit | L-C1FE0F5C | 300.0 | None | False | True | 
| monitoring | Rate of GetMetricStatistics requests | L-EE839489 | 400.0 | None | False | True | 
| monitoring | Rate of PutDashboard requests | L-6753900D | 10.0 | None | False | True | 
| monitoring | Rate of DeleteAlarms requests | L-25E8DC37 | 3.0 | None | False | False | 
| monitoring | Rate of PutMetricAlarm requests | L-0720E68F | 3.0 | None | False | True | 
| monitoring | Rate of PutMetricData requests | L-8BC498D4 | 500.0 | None | False | True | 
| monitoring | Rate of TagResource requests | L-4609795C | 1.0 | None | False | False | 
| monitoring | Rate of DescribeAlarmHistory requests | L-7193C790 | 3.0 | None | False | False | 
| monitoring | Rate of GetDashboard requests | L-E82C279D | 10.0 | None | False | True | 
| monitoring | Rate of UntagResource requests | L-6929DE8C | 1.0 | None | False | False | 
| monitoring | Rate of SetAlarmState requests | L-68B0DFE2 | 3.0 | None | False | False | 
| monitoring | Rate of ListTagsForResource requests | L-B6C4D57E | 10.0 | None | False | False | 
| monitoring | Number of Contributor Insights rules | L-DBD11BCC | 100.0 | None | False | True | 
| monitoring | Rate of DisableAlarmActions requests | L-D750D224 | 3.0 | None | False | False | 
| monitoring | Rate of DescribeAlarms requests | L-21CB40A4 | 9.0 | None | False | True | 
| monitoring | Rate of ListMetrics requests | L-05D334F0 | 50.0 | None | False | True | 
| monitoring | Rate of DeleteDashboards requests | L-E1508405 | 10.0 | None | False | True | 
| network-firewall | Stateless rulegroups | L-EAE8E19E | 50.0 | None | False | True | 
| network-firewall | Stateful rulegroups | L-2D7A0EE2 | 50.0 | None | False | True | 
| network-firewall | Firewall policies | L-0814492B | 20.0 | None | False | True | 
| network-firewall | Firewalls | L-DE163D32 | 5.0 | None | False | True | 
| nimble | Shared file system studio components per studio | L-1D1DDB85 | 10.0 | None | False | True | 
| nimble | Active Directory studio components per studio | L-D3E713C7 | 1.0 | None | False | False | 
| nimble | Streaming sessions per studio | L-0FA462CE | 2.0 | None | False | True | 
| nimble | Streaming session backups per studio | L-43D04A58 | 100.0 | None | False | True | 
| nimble | Studio components per studio | L-35089300 | 50.0 | None | False | True | 
| nimble | Launch profiles per studio | L-84ECA733 | 50.0 | None | False | True | 
| nimble | G5 streaming sessions per studio | L-83B00607 | 0.0 | None | False | True | 
| nimble | Studio creation per account | L-B88BF938 | 1.0 | None | False | False | 
| nimble | Custom streaming images per studio | L-D5A30A08 | 10.0 | None | False | True | 
| omics | Maximum Active Runs | L-A30FD31B | 3.0 | None | False | True | 
| omics | Maximum Activation Jobs | L-911E26A1 | 25.0 | None | False | True | 
| omics | Maximum Runs | L-C9679DBC | 200.0 | None | False | True | 
| omics | Maximum Active CPUs | L-7F5E4C03 | 512.0 | None | False | True | 
| omics | Maximum ReferenceStores | L-9CB08D77 | 1.0 | None | False | False | 
| omics | Maximum Export Jobs | L-473E274D | 5.0 | None | False | True | 
| omics | Maximum References | L-F34A3FC2 | 50.0 | None | False | True | 
| omics | Maximum Run Groups | L-176A1BA9 | 10.0 | None | False | True | 
| omics | Maximum Import Jobs | L-F57A8D18 | 5.0 | None | False | True | 
| omics | Maximum Duration | L-7B9E5416 | 604800.0 | Seconds | False | True | 
| omics | Maximum Import Job Read Sets | L-89F31D1A | 100.0 | None | False | True | 
| omics | Maximum SequenceStores | L-BFFBB2FD | 20.0 | None | False | True | 
| omics | Maximum Run Tasks | L-25504C8C | 10.0 | None | False | True | 
| omics | Maximum ReadSets | L-BE766427 | 1000000.0 | None | False | True | 
| omics | Maximum Export Job Read Sets | L-5BDDEC28 | 100.0 | None | False | True | 
| omics | Maximum Workflows | L-7CAE62CF | 100.0 | None | False | True | 
| omics | Maximum Activation Job Read Sets | L-18B646D8 | 20.0 | None | False | True | 
| outposts | Outpost sites | L-3D389D34 | 100.0 | None | False | True | 
| outposts | Outposts per site | L-0B277C74 | 10.0 | None | False | True | 
| personalize | Rate of DescribeAlgorithm requests | L-D551DB19 | 1.0 | None | False | False | 
| personalize | Rate of CreateEventTracker requests | L-D1699476 | 1.0 | None | False | False | 
| personalize | Rate of ListCampaigns requests | L-AE7FD4E5 | 1.0 | None | False | False | 
| personalize | Rate of ListRecipes requests | L-3A79BA38 | 1.0 | None | False | False | 
| personalize | Rate of CreateSolutionVersion requests | L-1B982452 | 1.0 | None | False | False | 
| personalize | Rate of UpdateDataset requests | L-76C4D7A9 | 1.0 | None | False | False | 
| personalize | Pending or In Progress solution versions | L-9C16B368 | 20.0 | None | False | True | 
| personalize | Active dataset groups | L-14011066 | 5.0 | None | False | True | 
| personalize | Number of interactions for model training | L-A6A4AB70 | 500000000.0 | None | False | True | 
| personalize | Amount of data for HRNN recipe | L-DD6792CA | 100.0 | Gigabytes | False | False | 
| personalize | Rate of DeleteSolution requests | L-7E76619B | 1.0 | None | False | False | 
| personalize | Rate of DescribeDatasetImportJob requests | L-6A61577D | 1.0 | None | False | False | 
| personalize | Amount of interactions data for HRNN-coldstart recipe | L-8CF67C84 | 100.0 | Gigabytes | False | False | 
| personalize | Rate of CreateDatasetGroup requests | L-141B5F3C | 1.0 | None | False | False | 
| personalize | Rate of CreateSolution requests | L-A527EF3A | 1.0 | None | False | False | 
| personalize | Rate of ListSolutions requests | L-3A329490 | 1.0 | None | False | False | 
| personalize | Active filters per dataset group | L-B9CFBC8B | 10.0 | None | False | True | 
| personalize | Rate of GetSolutionMetrics requests | L-89B2007E | 1.0 | None | False | False | 
| personalize | Rate of DescribeSchema requests | L-159027CF | 1.0 | None | False | False | 
| personalize | Rate of ListDatasets requests | L-CA34375E | 1.0 | None | False | False | 
| personalize | Rate of CreateDatasetImportJob requests | L-7AA65A3D | 1.0 | None | False | False | 
| personalize | Rate of CreateSchema requests | L-C044F2CA | 1.0 | None | False | False | 
| personalize | Rate of DeleteEventTracker requests | L-353C3E7E | 1.0 | None | False | False | 
| personalize | Rate of UpdateCampaign requests | L-12101E4A | 1.0 | None | False | False | 
| personalize | Amount of data per incremental import. | L-C5A4FD57 | 1.0 | Gigabytes | False | True | 
| personalize | Event size | L-FA8BB2FC | 10.0 | Kilobytes | False | False | 
| personalize | Rate of DeleteDatasetGroup requests | L-1CAC7664 | 1.0 | None | False | False | 
| personalize | Active campaigns per dataset group | L-052ECD67 | 5.0 | None | False | True | 
| personalize | Rate of DescribeEventTracker requests | L-5E3F1253 | 1.0 | None | False | False | 
| personalize | Rate of DeleteCampaign requests | L-BD0DF30D | 1.0 | None | False | False | 
| personalize | Rate of ListDatasetImportJobs requests | L-B9C7903C | 1.0 | None | False | False | 
| personalize | Minimum unique users for model training | L-ADCAE478 | 25.0 | None | False | False | 
| personalize | Rate of ListDatasetGroups requests | L-1513644C | 1.0 | None | False | False | 
| personalize | Rate of DescribeDatasetGroup requests | L-9B095670 | 1.0 | None | False | False | 
| personalize | Amount of users and items data combined for HRNN-coldstart recipe | L-DEDA9DCF | 5.0 | Gigabytes | False | False | 
| personalize | Active solutions per dataset group | L-D9DD83B7 | 10.0 | None | False | True | 
| personalize | Rate of DescribeFeatureTransformation requests | L-FAB63F14 | 1.0 | None | False | False | 
| personalize | Amount of data for Personalized-Ranking recipe | L-B33ADDC3 | 100.0 | Gigabytes | False | False | 
| personalize | Rate of transactions per account | L-5667F87F | 2500.0 | None | False | False | 
| personalize | Rate of CreateDataset requests | L-5D7942B8 | 1.0 | None | False | False | 
| personalize | Amount of data for SIMS recipe | L-E427562C | 100.0 | Gigabytes | False | False | 
| personalize | Maximum number of recommenders per dataset group | L-4D685096 | 5.0 | None | False | False | 
| personalize | Minimum data points for model training | L-4DFC060E | 1000.0 | None | False | False | 
| personalize | Maximum number of interactions per event type per user considered by a filter. | L-A8FE1453 | 100.0 | None | False | True | 
| personalize | Amount of interactions data for HRNN-metadata recipe | L-A2675B6E | 100.0 | Gigabytes | False | False | 
| personalize | Rate of ListDatasetImportJobRuns requests | L-5282CC49 | 1.0 | None | False | False | 
| personalize | Rate of DescribeCampaign requests | L-D98A73E8 | 1.0 | None | False | False | 
| personalize | Amount of users and items data combined for HRNN-metadata recipe | L-2EE592C4 | 5.0 | Gigabytes | False | False | 
| personalize | Pending or In Progress batch inference jobs | L-69B72005 | 5.0 | None | False | True | 
| personalize | Rate of DeleteDatasetImportJob requests | L-ACBBDC27 | 1.0 | None | False | False | 
| personalize | Rate of DeleteSchema requests | L-34736E70 | 1.0 | None | False | False | 
| personalize | Rate of CreateCampaign requests | L-9FDB137B | 1.0 | None | False | False | 
| personalize | Number of events in PutEvents call | L-A2738B0F | 10.0 | None | False | False | 
| personalize | Rate of DescribeSolution requests | L-ECA454DD | 1.0 | None | False | False | 
| personalize | Number of items used in model training | L-49CC69B6 | 750000.0 | None | False | False | 
| personalize | Number of schemas | L-037D5A71 | 500.0 | None | False | False | 
| personalize | Rate of GetPersonalizedRanking requests per campaign | L-83D79D48 | 500.0 | None | False | False | 
| personalize | Rate of ListEventTrackers requests | L-896849F5 | 1.0 | None | False | False | 
| personalize | Rate of DeleteDataset requests | L-E1ABE5BE | 1.0 | None | False | False | 
| personalize | Rate of DescribeRecipe requests | L-3A81D0FF | 1.0 | None | False | False | 
| personalize | Rate of GetRecommendations requests per campaign | L-E5F8E322 | 500.0 | None | False | False | 
| personalize | Rate of PutEvents requests per dataset group | L-8047B3A8 | 1000.0 | None | False | True | 
| personalize | Rate of DescribeDataset requests | L-DC96DE0A | 1.0 | None | False | False | 
| personalize | Rate of ListSchemas requests | L-542429F0 | 1.0 | None | False | False | 
| personalize | Rate of ListSolutionVersions requests | L-76D6B0AB | 1.0 | None | False | False | 
| personalize | Amount of data for Popularity-Count recipe | L-A6D35102 | 100.0 | Gigabytes | False | False | 
| pinpoint | Active campaigns per account | L-75AFB9F3 | 200.0 | None | False | True | 
| pinpoint | Active in-app campaigns per project | L-952D08C7 | 25.0 | None | False | True | 
| pinpoint | Maximum number of active event triggered journeys per account | L-692A3DD2 | 40.0 | None | False | True | 
| pinpoint | Maximum number of active journeys per account | L-D9507B3D | 50.0 | None | False | True | 
| pinpoint | Number of event-based campaigns | L-CC53764D | 25.0 | None | False | True | 
| pinpoint | Maximum number of journey activities per journey | L-08122D1D | 40.0 | None | False | True | 
| profile | Amazon Connect Customer Profiles domain count | L-6603B252 | 100.0 | None | False | True | 
| profile | Maximum size of all objects for a profile | L-63975AF3 | 51200.0 | Kilobytes | False | True | 
| profile | Maximum expiration in days | L-3217D1F1 | 1098.0 | None | False | True | 
| profile | Object and profile maximum size | L-3A29C525 | 250.0 | Kilobytes | False | False | 
| profile | Keys per object type | L-A7ED412C | 10.0 | None | False | True | 
| profile | Object types per domain | L-14092FF4 | 100.0 | None | False | True | 
| profile | Objects per profile | L-E17DC7C3 | 1000.0 | None | False | True | 
| profile | Maximum number of integrations | L-4A5ECB8E | 50.0 | None | False | True | 
| proton | Service instances per service | L-E8182F7E | 20.0 | None | False | True | 
| proton | Components per account | L-8FBB60E3 | 100.0 | None | False | True | 
| proton | Templates per account | L-405DC02B | 100.0 | None | False | True | 
| proton | Template versions per template | L-A1B6A95A | 500.0 | None | False | True | 
| proton | Services per account | L-1C8983C3 | 1000.0 | None | False | True | 
| proton | Environments per account | L-37A692EA | 100.0 | None | False | True | 
| proton | Environment account connections per environment account | L-6CC8209C | 5.0 | None | False | True | 
| qldb | QLDB streams per ledger | L-91B08359 | 5.0 | None | False | True | 
| qldb | Ledgers | L-CD70CADB | 5.0 | None | False | True | 
| qldb | QLDB exports per ledger | L-22B6E165 | 2.0 | None | False | True | 
| ram | Number of resource shares | L-595828F9 | 25000.0 | None | False | True | 
| ram | Number of resource associations | L-4A6CEE66 | 25000.0 | None | False | True | 
| rds | Data API maximum concurrent cluster-secret pairs | L-E3721453 | 30.0 | None | False | False | 
| rds | Data API HTTP request body size | L-D87A28C7 | 4.0 | Megabytes | False | False | 
| rds | Proxies | L-D94C7EA3 | 20.0 | None | False | True | 
| rds | Data API maximum concurrent requests | L-E79969BF | 500.0 | None | False | False | 
| rds | Data API maximum result set size | L-BDB2F348 | 1.0 | Megabytes | False | False | 
| rds | Data API requests per second | L-ECDFB241 | 1000.0 | None | False | False | 
| rds | Data API maximum size of JSON response string | L-C0506D15 | 10.0 | Megabytes | False | False | 
| rds | Parameter groups | L-DE55804A | 50.0 | None | False | True | 
| rds | Read replicas per primary | L-5BC124EF | 15.0 | None | False | True | 
| rds | Reserved DB instances | L-78E853F4 | 40.0 | None | False | True | 
| rds | Subnets per DB subnet group | L-6F3ACC36 | 20.0 | None | False | False | 
| rds | IAM roles per DB cluster | L-E094F43D | 5.0 | None | False | True | 
| rds | DB subnet groups | L-48C6BF61 | 50.0 | None | False | True | 
| rds | Manual DB cluster snapshots | L-9B510759 | 100.0 | None | False | True | 
| rds | Event subscriptions | L-A59F4C87 | 20.0 | None | False | True | 
| rds | DB instances | L-7B6409FD | 40.0 | None | False | True | 
| rds | Manual DB instance snapshots | L-272F1212 | 100.0 | None | False | True | 
| rds | Option groups | L-9FA33840 | 20.0 | None | False | True | 
| rds | IAM roles per DB instance | L-DD2301CA | 5.0 | None | False | True | 
| rds | DB cluster parameter groups | L-E4C808A8 | 50.0 | None | False | False | 
| rds | DB clusters | L-952B80B8 | 40.0 | None | False | True | 
| rds | Authorizations per DB security group | L-AA8B1026 | 20.0 | None | False | False | 
| rds | Total storage for all DB instances | L-7ADDB58A | 100000.0 | Gigabytes | False | True | 
| rds | Security groups | L-732153D0 | 25.0 | None | False | True | 
| refactor-spaces | Environments | L-DEF84811 | 50.0 | None | False | True | 
| refactor-spaces | Routes | L-CE52EEA2 | 1000.0 | None | False | True | 
| refactor-spaces | Applications | L-EACEDE8E | 600.0 | None | False | True | 
| refactor-spaces | Services | L-B19E8A2B | 500.0 | None | False | True | 
| rekognition | Transactions per second per account for the Amazon Rekognition Video stored video get operation GetSegmentDetection | L-F54C1CEA | 20.0 | None | False | True | 
| rekognition | Transactions per second per account for the Amazon Rekognition Image operation ListCollections | L-0366BB0F | 5.0 | None | False | True | 
| rekognition | Transactions per second per account for the Amazon Rekognition Custom Labels operation: UpdateDatasetEntries | L-513570CC | 5.0 | None | False | True | 
| rekognition | Maximum inference units per running Amazon Rekognition Custom Labels model. | L-4FA65ECB | 5.0 | None | False | True | 
| rekognition | Transactions per second per account for the Amazon Rekognition Image operation DeleteFaces | L-220834FB | 5.0 | None | False | True | 
| rekognition | Transactions per second per account for the Amazon Rekognition operation: ListTagsForResource | L-711B1E8A | 10.0 | None | False | True | 
| rekognition | Transactions per second per account for the Amazon Rekognition Image operation SearchFacesByImage | L-43CBEB68 | 50.0 | None | False | True | 
| rekognition | Amazon Rekognition Streaming Video Events stream processors per Amazon Kinesis video input stream. | L-3269D948 | 1.0 | None | False | False | 
| rekognition | Amazon Rekognition Streaming Video Events label detection stream processors per account that can be processed concurrently | L-0A2A7683 | 200.0 | None | False | True | 
| rekognition | Transactions per second per account for the Amazon Rekognition Custom Labels operation CreateProject | L-AB95BCCD | 5.0 | None | False | True | 
| rekognition | Maximum number of ProjectPolicies per Amazon Rekognition Custom Labels Project | L-0B2CE4DD | 5.0 | None | False | True | 
| rekognition | Transactions per second per account for the Amazon Rekognition Custom Labels operation: ListDatasetEntries | L-41805FEB | 5.0 | None | False | True | 
| rekognition | Transactions per second per account for the Amazon Rekognition operation: TagResource | L-C141F2F9 | 10.0 | None | False | True | 
| rekognition | Concurrent Amazon Rekognition Video stored video jobs per account | L-A6079699 | 20.0 | None | False | True | 
| rekognition | Transactions per second per account for the Amazon Rekognition Custom Labels operation ListProjectPolicies | L-5AA330BC | 5.0 | None | False | True | 
| rekognition | Transactions per second per account for the Amazon Rekognition Custom Labels operation StartProjectVersion | L-C46E6F2E | 5.0 | None | False | True | 
| rekognition | Transactions per second per account for the Amazon Rekognition Image operation GetCelebrityInfo | L-973FFF99 | 50.0 | None | False | True | 
| rekognition | Transactions per second per account for the Amazon Rekognition Video stored video start operation StartContentModeration | L-E082B236 | 5.0 | None | False | True | 
| rekognition | Transactions per second per account for the Amazon Rekognition Image operation DeleteCollection | L-5346A13A | 5.0 | None | False | True | 
| rekognition | Amazon Rekognition Streaming Video Events face search stream processors per account that can be processed concurrently | L-8D9029A2 | 10.0 | None | False | True | 
| rekognition | Transactions per second per account for the Amazon Rekognition Custom Labels operation StopProjectVersion | L-9802772B | 5.0 | None | False | True | 
| rekognition | Transactions per second per account for the Amazon Rekognition Streaming Video Events operation CreateStreamProcessor | L-D6034D02 | 20.0 | None | False | True | 
| rekognition | Amazon Rekognition Custom Labels models per project | L-9CF05323 | 100.0 | None | False | True | 
| rekognition | Transactions per second per account for the Amazon Rekognition Image operation CompareFaces | L-73A341CE | 100.0 | None | False | True | 
| rekognition | Transactions per second per account for the Amazon Rekognition Video stored video start operation StartLabelDetection | L-FBD555BC | 5.0 | None | False | True | 
| rekognition | Transactions per second per account for the Amazon Rekognition Custom Labels operation DeleteProject | L-BDE2ACBF | 5.0 | None | False | True | 
| rekognition | Transactions per second per account for the Amazon Rekognition Video stored video start operation StartTextDetection | L-90C845BC | 5.0 | None | False | True | 
| rekognition | Transactions per second per account for the Amazon Rekognition Video stored video get operation GetFaceDetection | L-4E7ADAC1 | 20.0 | None | False | True | 
| rekognition | Transactions per second per account for the Amazon Rekognition Custom Labels operation: ListDatasetLabels | L-108100B3 | 5.0 | None | False | True | 
| rekognition | Transactions per second per account for the Amazon Rekognition Video stored video get operation GetContentModeration | L-A33540CC | 20.0 | None | False | True | 
| rekognition | Transactions per second per account for the Amazon Rekognition Video stored video start operation StartPersonTracking | L-DFE4726A | 5.0 | None | False | True | 
| rekognition | Transactions per second per account for the Amazon Rekognition Image operation RecognizeCelebrities | L-5FF750C4 | 50.0 | None | False | True | 
| rekognition | Transactions per second per account for the Amazon Rekognition Custom Labels operation DescribeProjectVersions | L-12019FB0 | 5.0 | None | False | True | 
| rekognition | Transactions per second per account for the Amazon Rekognition Custom Labels operation: DescribeDataset | L-EF2DFA3A | 5.0 | None | False | True | 
| rekognition | Transactions per second per account for the Amazon Rekognition Video stored video get operation GetTextDetection | L-5C10FBD9 | 20.0 | None | False | True | 
| rekognition | Transactions per second per account for the Amazon Rekognition operation: UntagResource | L-BC04C31B | 10.0 | None | False | True | 
| rekognition | Transactions per second per account for the Amazon Rekognition Image operation DetectLabels | L-E29B542B | 50.0 | None | False | True | 
| rekognition | Transactions per second per account for the Amazon Rekognition Video stored video get operation GetFaceSearch | L-3B051C64 | 20.0 | None | False | True | 
| rekognition | Transactions per second per account for the Amazon Rekognition Streaming Video Events operation StopStreamProcessor | L-85890340 | 1.0 | None | False | True | 
| rekognition | Transactions per second per account for the Amazon Rekognition Image operation DetectText | L-87CF5BA6 | 50.0 | None | False | True | 
| rekognition | Transactions per second per account for individual Amazon Rekognition Custom Labels data plane operation DetectCustomLabels | L-EA71C84A | 50.0 | None | False | True | 
| rekognition | Concurrent Amazon Rekognition Custom Labels training jobs per account | L-F1558568 | 2.0 | None | False | True | 
| rekognition | Transactions per second per account for the Amazon Rekognition Image operation CreateCollection | L-CE977716 | 5.0 | None | False | True | 
| rekognition | Transactions per second per account for the Amazon Rekognition Custom Labels operation: CreateDataset | L-39854D9A | 5.0 | None | False | True | 
| rekognition | Transactions per second per account for the Amazon Rekognition Streaming Video Events operation DescribeStreamProcessor | L-82C6694D | 20.0 | None | False | True | 
| rekognition | Transactions per second per account for the Amazon Rekognition Custom Labels operation DeleteProjectVersion | L-D66335E5 | 5.0 | None | False | True | 
| rekognition | Transactions per second per account for the Amazon Rekognition Custom Labels operation DeleteProjectPolicy | L-AA6AE486 | 5.0 | None | False | True | 
| rekognition | Transactions per second per account for the Amazon Rekognition Video stored video get operation GetCelebrityRecognition | L-A144FAD3 | 20.0 | None | False | True | 
| rekognition | Maximum number of images per Amazon Rekognition Custom Labels classification training dataset | L-96D6749B | 250000.0 | None | False | True | 
| rekognition | Amazon Rekognition Custom Labels projects per account | L-14D0BC19 | 100.0 | None | False | True | 
| rekognition | Transactions per second per account for the Amazon Rekognition Streaming Video Events operation StartStreamProcessor | L-71793F35 | 20.0 | None | False | True | 
| rekognition | Transactions per second per account for the Amazon Rekognition Image operation ListFaces | L-970B5808 | 50.0 | None | False | True | 
| rekognition | Transactions per second per account for the Amazon Rekognition Image operation DetectModerationLabels | L-7F4D1AC4 | 50.0 | None | False | True | 
| rekognition | Transactions per second per account for the Amazon Rekognition Custom Labels operation PutProjectPolicy | L-A958BCFA | 5.0 | None | False | True | 
| rekognition | Transactions per second per account for the Amazon Rekognition Custom Labels operation CopyProjectVersion | L-C8E3347A | 5.0 | None | False | True | 
| rekognition | Transactions per second per account for the Amazon Rekognition Video stored video start operation StartSegmentDetection | L-55A22B20 | 5.0 | None | False | True | 
| rekognition | Transactions per second per account for the Amazon Rekognition Streaming Video Events operation ListStreamProcessors | L-CF317234 | 5.0 | None | False | True | 
| rekognition | Transactions per second per account for the Amazon Rekognition Video stored video get operation GetLabelDetection | L-5EAC8E57 | 20.0 | None | False | True | 
| rekognition | Transactions per second per account for the Amazon Rekognition Video stored video start operation StartFaceDetection | L-AA48F869 | 5.0 | None | False | True | 
| rekognition | Transactions per second per account for the Amazon Rekognition Image operation DetectFaces | L-A5121FD7 | 100.0 | None | False | True | 
| rekognition | Transactions per second per account for the Amazon Rekognition Image personal protective equipment operation DetectProtectiveEquipment | L-6F294C5B | 5.0 | None | False | True | 
| rekognition | Transactions per second per account for the Amazon Rekognition Streaming Video Events operation DeleteStreamProcessor | L-66AB9558 | 20.0 | None | False | True | 
| rekognition | Maximum number of images per Amazon Rekognition Custom Labels detection test dataset | L-7E97BCDC | 250000.0 | None | False | False | 
| rekognition | Amazon Rekognition Streaming Video Events stream processors per account that can simultaneously exist | L-01C8D885 | 10000.0 | None | False | True | 
| rekognition | Transactions per second per account for the Amazon Rekognition Video stored video start operation StartFaceSearch | L-8CA99658 | 5.0 | None | False | True | 
| rekognition | Amazon Rekognition Streaming Video Events face search stream processors per Amazon Kinesis data output stream. | L-70336415 | 1.0 | None | False | False | 
| rekognition | Transactions per second per account for the Amazon Rekognition Video stored video start operation StartCelebrityRecognition | L-08B7635A | 5.0 | None | False | True | 
| rekognition | Transactions per second per account for the Amazon Rekognition Image operation SearchFaces | L-99829151 | 50.0 | None | False | True | 
| rekognition | Transactions per second per account for the Amazon Rekognition Video stored video get operation GetPersonTracking | L-71159A7C | 20.0 | None | False | True | 
| rekognition | Transactions per second per account for the Amazon Rekognition Streaming Video Events operation UpdateStreamProcessor | L-0FB781AE | 20.0 | None | False | True | 
| rekognition | Maximum number of images per Amazon Rekognition Custom Labels classification test dataset | L-CCFEF1AD | 250000.0 | None | False | True | 
| rekognition | Transactions per second per account for the Amazon Rekognition Image operation DescribeCollection | L-6FDFFAF5 | 5.0 | None | False | True | 
| rekognition | Transactions per second per account for the Amazon Rekognition Custom Labels operation CreateProjectVersion | L-03F18989 | 5.0 | None | False | True | 
| rekognition | Transactions per second per account for the Amazon Rekognition Custom Labels operation: DeleteDataset | L-F72BEA0D | 5.0 | None | False | True | 
| rekognition | Concurrent Amazon Rekognition Custom Labels model copy jobs per account | L-B3EE7891 | 5.0 | None | False | True | 
| rekognition | Maximum number of images per Amazon Rekognition Custom Labels detection training dataset | L-D8895012 | 250000.0 | None | False | False | 
| rekognition | Concurrently running Amazon Rekognition Custom Labels models per account | L-5E225387 | 2.0 | None | False | True | 
| rekognition | Transactions per second per account for the Amazon Rekognition Image operation IndexFaces | L-7C13EBAD | 50.0 | None | False | True | 
| rekognition | Transactions per second per account for the Amazon Rekognition Custom Labels operation DescribeProjects | L-06ACBDE8 | 5.0 | None | False | True | 
| rekognition | Transactions per second per account for the Amazon Rekognition Custom Labels operation: DistributeDatasetEntries | L-AD2642BA | 5.0 | None | False | True | 
| resiliencehub | Number of assessments per application per month | L-BF1D24DC | 200.0 | None | False | True | 
| resiliencehub | Number of Resiliency Policies | L-F9AC239A | 10.0 | None | False | True | 
| resiliencehub | Number of applications | L-CBE304D4 | 10.0 | None | False | True | 
| resiliencehub | Number of recommendation templates per application per month | L-37EF5CB4 | 100.0 | None | False | True | 
| resource-explorer-2 | Non-aggregator Region search monthly quota | L-C5E31461 | 500.0 | None | False | True | 
| resource-explorer-2 | Aggregator Region search monthly quota | L-A28429E9 | 10000.0 | None | False | True | 
| resource-explorer-2 | Search TPS quota | L-0C73063D | 5.0 | None | False | True | 
| robomaker | Minimum simulation duration | L-CEB47779 | 5.0 | None | False | False | 
| robomaker | Batch timeout | L-0DED0FF4 | 14.0 | None | False | False | 
| robomaker | Versions per simulation application | L-4D288B5C | 40.0 | None | False | True | 
| robomaker | Simulation Job Creation Rate Per Minute | L-04ECBB71 | 10.0 | None | False | False | 
| robomaker | Source size | L-3CD5069F | 5.0 | Gigabytes | False | False | 
| robomaker | Worlds Per Generation Job | L-335D1CF0 | 50.0 | None | False | False | 
| robomaker | GPU Simulation Job Creation Rate Per Minute | L-99FBC089 | 2.0 | None | False | False | 
| robomaker | Simulation duration | L-7E2BA58F | 14.0 | None | False | False | 
| robomaker | Concurrent deployment jobs | L-15E423AD | 20.0 | None | False | True | 
| robomaker | Simulation applications | L-D6554FB1 | 40.0 | None | False | True | 
| robomaker | Concurrent World Export Jobs | L-B47404F4 | 3.0 | None | False | True | 
| robomaker | Concurrent World Generation Jobs | L-7651BB34 | 3.0 | None | False | True | 
| robomaker | Versions per robot application | L-AE5043DD | 40.0 | None | False | True | 
| robomaker | Robot applications | L-E5D0EA7D | 40.0 | None | False | True | 
| robomaker | Concurrent simulation job batches | L-6CFB8C09 | 5.0 | None | False | True | 
| robomaker | Concurrent simulation jobs | L-FE0C173F | 1.0 | None | False | True | 
| robomaker | World Templates Per Account | L-C2C8236B | 40.0 | None | False | True | 
| robomaker | Worlds Per Export Job | L-D5AF2EE5 | 1.0 | None | False | False | 
| robomaker | Fleets | L-19B1F5F2 | 20.0 | None | False | True | 
| robomaker | Robots per fleet | L-275E9052 | 100.0 | None | False | True | 
| robomaker | Simulation job requests per batch | L-949954FD | 20.0 | None | False | True | 
| robomaker | Minimum batch timeout | L-925F020F | 5.0 | None | False | False | 
| robomaker | Robots | L-40FACCBF | 100.0 | None | False | True | 
| robomaker | Concurrent GPU simulation jobs | L-61591119 | 1.0 | None | False | True | 
| rolesanywhere | Rate of CreateSession requests | L-A9D9612A | 10.0 | None | False | True | 
| rolesanywhere | CRLs per trust anchor | L-19368711 | 2.0 | None | False | False | 
| rolesanywhere | Trust anchors | L-AB49EEA7 | 50.0 | None | False | True | 
| rolesanywhere | Combined rate of profile requests | L-F8680437 | 1.0 | None | False | True | 
| rolesanywhere | Combined rate of CRL requests | L-0017E049 | 1.0 | None | False | True | 
| rolesanywhere | Combined rate of trust anchor requests | L-E7B077D9 | 1.0 | None | False | True | 
| rolesanywhere | Combined rate of subject requests | L-1A26F220 | 1.0 | None | False | True | 
| rolesanywhere | Certificates per trust anchor | L-471D7A75 | 2.0 | None | False | False | 
| rolesanywhere | Combined rate of tagging requests | L-BCE17F1C | 1.0 | None | False | True | 
| rolesanywhere | Profiles | L-950ED79F | 250.0 | None | False | True | 
| route53resolver | Target IP addresses per resolver rule | L-D74B6237 | 6.0 | None | False | False | 
| route53resolver | Resolver rules per AWS Region | L-51D8A1FB | 1000.0 | None | False | True | 
| route53resolver | Domains in a file imported from S3 | L-1B2BDF0A | 250000.0 | None | False | True | 
| route53resolver | DNS Firewall rule group associations per VPC | L-15219E1D | 5.0 | None | False | False | 
| route53resolver | DNS Firewall rules groups per Region | L-02CC8B74 | 1000.0 | None | False | True | 
| route53resolver | IP addresses per resolver endpoint | L-D2FE9758 | 6.0 | None | False | True | 
| route53resolver | Domains per account | L-740A4B31 | 100000.0 | None | False | True | 
| route53resolver | Maximum number of resolver endpoints per AWS Region | L-4A669CC0 | 4.0 | None | False | True | 
| route53resolver | Associations between resolver rules and VPCs per AWS Region | L-94E19253 | 2000.0 | None | False | True | 
| route53resolver | Domain lists per account | L-9FA3C0A4 | 1000.0 | None | False | True | 
| route53resolver | Rules in a DNS Firewall rule group | L-F763F4D9 | 100.0 | None | False | True | 
| sagemaker | ml.c6i.8xlarge for endpoint usage | L-18904FF8 | 2.0 | None | False | True | 
| sagemaker | ml.m6g.large for endpoint usage | L-C1E62DF0 | 16.0 | None | False | True | 
| sagemaker | ml.r5dn.4xlarge for endpoint usage | L-DDDCDBAA | 2.0 | None | False | True | 
| sagemaker | ml.g4dn.4xlarge for endpoint usage | L-31522FA6 | 2.0 | None | False | True | 
| sagemaker | Number of instances across all spot training jobs | L-93958082 | 20.0 | None | False | True | 
| sagemaker | ml.p2.xlarge for training warm pool usage | L-6C5BAAA9 | 0.0 | None | False | True | 
| sagemaker | Total number of trials allowed in a single experiment excluding those automatically created by SageMaker | L-E1A153C2 | 300.0 | None | False | False | 
| sagemaker | Maximum number of steps allowed per pipeline | L-729F2471 | 50.0 | None | False | False | 
| sagemaker | ml.c4.8xlarge for training warm pool usage | L-8B308035 | 0.0 | None | False | True | 
| sagemaker | ml.g4dn.12xlarge for processing job usage | L-6C7C4F4E | 0.0 | None | False | True | 
| sagemaker | RSessionGateway Apps running on ml.m5.16xlarge instance | L-7B7E548F | 2.0 | None | False | True | 
| sagemaker | ml.m5.2xlarge for endpoint usage | L-C88C8F13 | 8.0 | None | False | True | 
| sagemaker | RSessionGateway Apps running on ml.m5d.4xlarge instance | L-53138E1F | 6.0 | None | False | True | 
| sagemaker | ml.m4.xlarge for notebook instance usage | L-E1249695 | 30.0 | None | False | True | 
| sagemaker | ml.g4dn.2xlarge for training warm pool usage | L-C35F807B | 0.0 | None | False | True | 
| sagemaker | ml.c5.xlarge for training job usage | L-E2BB44FE | 30.0 | None | False | True | 
| sagemaker | ml.c5d.4xlarge for notebook instance usage | L-484388A9 | 4.0 | None | False | True | 
| sagemaker | ml.m6gd.12xlarge for endpoint usage | L-B25B9B93 | 2.0 | None | False | True | 
| sagemaker | ml.eia1.large for endpoint usage | L-58672BCE | 20.0 | None | False | True | 
| sagemaker | Rate of UpdateTrainingJob requests | L-5C11C23E | 1.0 | None | False | False | 
| sagemaker | ml.g5.16xlarge for spot training job usage | L-E3DCB664 | 1.0 | None | False | True | 
| sagemaker | ml.g4dn.12xlarge for transform job usage | L-BA5C7A54 | 0.0 | None | False | True | 
| sagemaker | ml.g5.24xlarge for spot training job usage | L-8345B953 | 0.0 | None | False | True | 
| sagemaker | ml.m5d.8xlarge for endpoint usage | L-A7702AF9 | 4.0 | None | False | True | 
| sagemaker | Maximum number of A2I human task UIs | L-3036C9CA | 2000.0 | None | False | True | 
| sagemaker | Rate of StopTransformJob requests | L-9EB87FF0 | 1.0 | None | False | False | 
| sagemaker | ml.g5.2xlarge for training warm pool usage | L-822C5A39 | 0.0 | None | False | True | 
| sagemaker | ml.m5.2xlarge for transform job usage | L-F5689004 | 4.0 | None | False | True | 
| sagemaker | ml.g4dn.16xlarge for endpoint usage | L-8679F6F3 | 0.0 | None | False | True | 
| sagemaker | Studio KernelGateway Apps running on ml.r5.12xlarge instance | L-EF2BF7DC | 2.0 | None | False | True | 
| sagemaker | ml.c4.4xlarge for endpoint usage | L-605A110B | 2.0 | None | False | True | 
| sagemaker | RSessionGateway Apps running on ml.c5.9xlarge instance | L-D205D3F0 | 4.0 | None | False | True | 
| sagemaker | ml.m6gd.4xlarge for endpoint usage | L-CCA2CA42 | 4.0 | None | False | True | 
| sagemaker | ml.g4dn.xlarge for notebook instance usage | L-D8B97089 | 16.0 | None | False | True | 
| sagemaker | ml.inf1.xlarge for endpoint usage | L-B2B3BA64 | 2.0 | None | False | True | 
| sagemaker | ml.c5d.2xlarge for endpoint usage | L-529E971B | 4.0 | None | False | True | 
| sagemaker | ml.trn1.2xlarge for training warm pool usage | L-AA6A4B7A | 0.0 | None | False | True | 
| sagemaker | ml.g5.16xlarge for endpoint usage | L-962705EA | 0.0 | None | False | True | 
| sagemaker | ml.g5.48xlarge for training job usage | L-6BC98A55 | 0.0 | None | False | True | 
| sagemaker | ml.r5.16xlarge for notebook instance usage | L-924D392D | 2.0 | None | False | True | 
| sagemaker | ml.g5.2xlarge for notebook instance usage | L-19973BE2 | 5.0 | None | False | True | 
| sagemaker | RSessionGateway Apps running on ml.c5.24xlarge instance | L-1271DF32 | 2.0 | None | False | True | 
| sagemaker | ml.c6gd.4xlarge for endpoint usage | L-C4B5BAD2 | 2.0 | None | False | True | 
| sagemaker | ml.m4.16xlarge for notebook instance usage | L-85E60595 | 8.0 | None | False | True | 
| sagemaker | ml.m4.16xlarge for training warm pool usage | L-F4F08D88 | 0.0 | None | False | True | 
| sagemaker | ml.g4dn.8xlarge for transform job usage | L-213CD3BC | 0.0 | None | False | True | 
| sagemaker | ml.c4.2xlarge for transform job usage | L-589B0DBC | 8.0 | None | False | True | 
| sagemaker | ml.g4dn.2xlarge for training job usage | L-C2495BC4 | 1.0 | None | False | True | 
| sagemaker | RSessionGateway Apps running on ml.m5.2xlarge instance | L-09249843 | 11.0 | None | False | True | 
| sagemaker | Total number of notebook instances | L-04CE2E67 | 30.0 | None | False | True | 
| sagemaker | Maximum total concurrency that can be allocated across all serverless endpoints | L-96300102 | 1000.0 | None | False | True | 
| sagemaker | ml.m5n.8xlarge for endpoint usage | L-1F61C5BC | 4.0 | None | False | True | 
| sagemaker | ml.c5n.9xlarge for endpoint usage | L-124679C5 | 1.0 | None | False | True | 
| sagemaker | Total EBS volume size in GB across all notebook instances | L-E4B12EA2 | 102400.0 | None | False | False | 
| sagemaker | ml.c5n.xlarge for spot training job usage | L-DD508305 | 1.0 | None | False | True | 
| sagemaker | ml.m6gd.2xlarge for endpoint usage | L-AB53E0CA | 8.0 | None | False | True | 
| sagemaker | ml.m5dn.16xlarge for endpoint usage | L-D075BB65 | 2.0 | None | False | True | 
| sagemaker | ml.c5n.large for endpoint usage | L-0F4F99A1 | 16.0 | None | False | True | 
| sagemaker | ml.c6g.8xlarge for endpoint usage | L-6D865216 | 2.0 | None | False | True | 
| sagemaker | ml.m4.4xlarge for notebook instance usage | L-BE78F29C | 15.0 | None | False | True | 
| sagemaker | Maximum number of SageMaker Model Package Groups allowed per account | L-BC8DC54C | 1000.0 | None | False | True | 
| sagemaker | ml.m4.xlarge for processing job usage | L-F97C6864 | 16.0 | None | False | True | 
| sagemaker | ml.g4dn.2xlarge for processing job usage | L-41C11899 | 0.0 | None | False | True | 
| sagemaker | ml.m4.16xlarge for transform job usage | L-7FEDBA4C | 1.0 | None | False | True | 
| sagemaker | ml.r5.2xlarge for notebook instance usage | L-8CB23490 | 11.0 | None | False | True | 
| sagemaker | Studio KernelGateway Apps running on ml.p3dn.24xlarge instance | L-1CF85412 | 0.0 | None | False | True | 
| sagemaker | ml.m5n.24xlarge for endpoint usage | L-A2C9F8F4 | 1.0 | None | False | True | 
| sagemaker | ml.g4dn.8xlarge for processing job usage | L-9C72BEE2 | 0.0 | None | False | True | 
| sagemaker | ml.t3.2xlarge for processing job usage | L-1E2072C0 | 5.0 | None | False | True | 
| sagemaker | ml.g4dn.8xlarge for spot training job usage | L-15F329FB | 1.0 | None | False | True | 
| sagemaker | RSessionGateway Apps running on ml.m5d.12xlarge instance | L-7F2FEE7C | 2.0 | None | False | True | 
| sagemaker | ml.c6gd.2xlarge for endpoint usage | L-FD9E9507 | 4.0 | None | False | True | 
| sagemaker | Number of instances across all processing jobs | L-F311B08F | 75.0 | None | False | True | 
| sagemaker | ml.g4dn.4xlarge for training job usage | L-2908B1E9 | 1.0 | None | False | True | 
| sagemaker | ml.p3.2xlarge for training job usage | L-D438008E | 1.0 | None | False | True | 
| sagemaker | ml.r5dn.16xlarge for endpoint usage | L-1DA91421 | 0.0 | None | False | True | 
| sagemaker | Maximum number of serverless endpoints | L-99AD19BF | 50.0 | None | False | True | 
| sagemaker | ml.p3.2xlarge for processing job usage | L-0323EDB4 | 0.0 | None | False | True | 
| sagemaker | RSessionGateway Apps running on ml.r5.2xlarge instance | L-751BCA3E | 11.0 | None | False | True | 
| sagemaker | ml.g5.xlarge for notebook instance usage | L-E8917BB7 | 5.0 | None | False | True | 
| sagemaker | Number of elastic inference accelerators across active endpoints | L-07D0651D | 20.0 | None | False | True | 
| sagemaker | ml.c4.8xlarge for endpoint usage | L-DF052B7B | 1.0 | None | False | True | 
| sagemaker | ml.r5d.24xlarge for endpoint usage | L-D71E726A | 0.0 | None | False | True | 
| sagemaker | ml.p3dn.24xlarge for spot training job usage | L-477D3300 | 0.0 | None | False | True | 
| sagemaker | ml.p3.8xlarge for endpoint usage | L-CB985DC5 | 1.0 | None | False | True | 
| sagemaker | ml.r5d.large for endpoint usage | L-E0299BF7 | 4.0 | None | False | True | 
| sagemaker | Maximum number of instances per training job | L-622CFD70 | 20.0 | None | False | False | 
| sagemaker | Total number of trial components allowed in a single trial excluding those automatically created by SageMaker | L-479D8F33 | 50.0 | None | False | False | 
| sagemaker | Rate of UpdateMonitoringAlert requests | L-1A647398 | 1.0 | None | False | False | 
| sagemaker | RSessionGateway Apps running on ml.p3dn.24xlarge instance | L-94B31A5D | 0.0 | None | False | True | 
| sagemaker | ml.m6gd.xlarge for endpoint usage | L-4F185009 | 0.0 | None | False | True | 
| sagemaker | Studio Jupyter Apps running on system instances | L-8276C21E | 40.0 | None | False | True | 
| sagemaker | ml.c5n.xlarge for training job usage | L-04CD765C | 1.0 | None | False | True | 
| sagemaker | ml.c6g.12xlarge for endpoint usage | L-35E5433E | 2.0 | None | False | True | 
| sagemaker | ml.m4.10xlarge for spot training job usage | L-C17B05C4 | 5.0 | None | False | True | 
| sagemaker | ml.r5d.8xlarge for endpoint usage | L-17BBB387 | 1.0 | None | False | True | 
| sagemaker | ml.m5n.2xlarge for endpoint usage | L-F8B07B25 | 8.0 | None | False | True | 
| sagemaker | ml.m5d.xlarge for notebook instance usage | L-7AA0FEE8 | 11.0 | None | False | True | 
| sagemaker | ml.c4.4xlarge for notebook instance usage | L-27768634 | 30.0 | None | False | True | 
| sagemaker | ml.m5.24xlarge for training warm pool usage | L-B21D8B36 | 0.0 | None | False | True | 
| sagemaker | Total number of trial components allowed from a SageMaker context excluding those automatically created by SageMaker | L-D62610A9 | 20000.0 | None | False | False | 
| sagemaker | ml.r5dn.8xlarge for endpoint usage | L-E8AF0CC9 | 2.0 | None | False | True | 
| sagemaker | ml.m5d.8xlarge for notebook instance usage | L-AEB45880 | 3.0 | None | False | True | 
| sagemaker | Rate of ListMonitoringAlerts requests | L-4E8CFCC7 | 2.0 | None | False | False | 
| sagemaker | ml.c4.8xlarge for transform job usage | L-334DC079 | 2.0 | None | False | True | 
| sagemaker | ml.g4dn.4xlarge for spot training job usage | L-246C5638 | 1.0 | None | False | True | 
| sagemaker | RSessionGateway Apps running on ml.m5d.24xlarge instance | L-00DAC655 | 2.0 | None | False | True | 
| sagemaker | ml.m5.xlarge for training job usage | L-CCE2AFA6 | 30.0 | None | False | True | 
| sagemaker | ml.c5.18xlarge for training job usage | L-81482A8C | 8.0 | None | False | True | 
| sagemaker | Studio KernelGateway Apps running on ml.g5.24xlarge instance | L-9D9F9978 | 0.0 | None | False | True | 
| sagemaker | ml.m5d.24xlarge for notebook instance usage | L-956703D9 | 2.0 | None | False | True | 
| sagemaker | Rate of ListEndpoints requests | L-35C54F5F | 2.0 | None | False | False | 
| sagemaker | ml.m5d.16xlarge for endpoint usage | L-F6E740CB | 2.0 | None | False | True | 
| sagemaker | ml.g4dn.2xlarge for transform job usage | L-180A6F2D | 0.0 | None | False | True | 
| sagemaker | Maximum subsampled dataset size AutoML job can be run on | L-4556354E | 5.0 | None | False | False | 
| sagemaker | Studio KernelGateway Apps running on ml.g4dn.12xlarge instance | L-09D3DD58 | 0.0 | None | False | True | 
| sagemaker | Number of instances across active endpoints | L-7A3DF611 | 200.0 | None | False | True | 
| sagemaker | RSessionGateway Apps running on ml.t3.small instance | L-E833CC8B | 0.0 | None | False | True | 
| sagemaker | ml.c5.4xlarge for training warm pool usage | L-7BDD9EA3 | 0.0 | None | False | True | 
| sagemaker | ml.r5n.xlarge for endpoint usage | L-4DD84AF9 | 4.0 | None | False | True | 
| sagemaker | ml.m6gd.16xlarge for endpoint usage | L-B46EE84C | 2.0 | None | False | True | 
| sagemaker | ml.eia1.xlarge for endpoint usage | L-8D013305 | 20.0 | None | False | True | 
| sagemaker | ml.g5.24xlarge for training warm pool usage | L-6F46EF71 | 0.0 | None | False | True | 
| sagemaker | ml.g4dn.16xlarge for spot training job usage | L-AD4C1352 | 1.0 | None | False | True | 
| sagemaker | Maximum number of instances per spot training job | L-DB62C864 | 20.0 | None | False | False | 
| sagemaker | ml.g5.48xlarge for notebook instance usage | L-D266139B | 2.0 | None | False | True | 
| sagemaker | ml.m4.4xlarge for training warm pool usage | L-CF81ED81 | 0.0 | None | False | True | 
| sagemaker | ml.g4dn.12xlarge for training job usage | L-7BD2C9FA | 1.0 | None | False | True | 
| sagemaker | ml.c7g.8xlarge for endpoint usage | L-52008469 | 0.0 | None | False | True | 
| sagemaker | ml.r5.xlarge for notebook instance usage | L-85870296 | 11.0 | None | False | True | 
| sagemaker | ml.p3.16xlarge for training job usage | L-A99E0304 | 0.0 | None | False | True | 
| sagemaker | ml.r5.24xlarge for processing job usage | L-A28AF48F | 0.0 | None | False | True | 
| sagemaker | ml.t3.xlarge for notebook instance usage | L-E5884D25 | 30.0 | None | False | True | 
| sagemaker | ml.c5n.2xlarge for training job usage | L-D04B88E2 | 1.0 | None | False | True | 
| sagemaker | ml.c5.2xlarge for processing job usage | L-C1EBA9C5 | 8.0 | None | False | True | 
| sagemaker | ml.m5.large for training warm pool usage | L-2DD73636 | 0.0 | None | False | True | 
| sagemaker | RSessionGateway Apps running on ml.p3.16xlarge instance | L-C5A57F3A | 0.0 | None | False | True | 
| sagemaker | Studio KernelGateway Apps running on ml.m5d.8xlarge instance | L-019DC79D | 2.0 | None | False | True | 
| sagemaker | ml.m5.xlarge for notebook instance usage | L-76AB2C05 | 11.0 | None | False | True | 
| sagemaker | ml.c6g.xlarge for endpoint usage | L-525AAB0A | 8.0 | None | False | True | 
| sagemaker | ml.t2.2xlarge for notebook instance usage | L-BE44390B | 30.0 | None | False | True | 
| sagemaker | ml.c5.2xlarge for training job usage | L-49679826 | 30.0 | None | False | True | 
| sagemaker | RSessionGateway Apps running on ml.g4dn.2xlarge instance | L-7FD92B01 | 1.0 | None | False | True | 
| sagemaker | ml.t2.large for notebook instance usage | L-94C3A7A1 | 30.0 | None | False | True | 
| sagemaker | ml.c5.4xlarge for endpoint usage | L-FEF755D6 | 4.0 | None | False | True | 
| sagemaker | ml.c4.large for endpoint usage | L-6DF60D19 | 16.0 | None | False | True | 
| sagemaker | ml.c5.4xlarge for spot training job usage | L-36C5FA8E | 5.0 | None | False | True | 
| sagemaker | ml.p4d.24xlarge for endpoint usage | L-09F79647 | 0.0 | None | False | True | 
| sagemaker | ml.p3dn.24xlarge for notebook instance usage | L-2E21A1FA | 1.0 | None | False | True | 
| sagemaker | ml.eia1.medium for endpoint usage | L-01E4E529 | 20.0 | None | False | True | 
| sagemaker | ml.p2.xlarge for processing job usage | L-61E3D6FC | 0.0 | None | False | True | 
| sagemaker | ml.m5d.24xlarge for endpoint usage | L-24B12C23 | 1.0 | None | False | True | 
| sagemaker | ml.m6g.2xlarge for endpoint usage | L-BCBC84AA | 8.0 | None | False | True | 
| sagemaker | Studio KernelGateway Apps running on ml.p3.16xlarge instance | L-0DADC663 | 0.0 | None | False | True | 
| sagemaker | ml.m5.24xlarge for spot training job usage | L-D0EA3DC8 | 2.0 | None | False | True | 
| sagemaker | ml.t3.xlarge for processing job usage | L-DABA7ED5 | 10.0 | None | False | True | 
| sagemaker | Maximum number of training jobs that each hyperparameter tuning job with Random search strategy can create | L-52DB9D33 | 500.0 | None | False | False | 
| sagemaker | ml.c5.9xlarge for spot training job usage | L-A2512F8F | 5.0 | None | False | True | 
| sagemaker | ml.c6g.16xlarge for endpoint usage | L-60986E7E | 1.0 | None | False | True | 
| sagemaker | ml.inf1.2xlarge for endpoint usage | L-495AAEE0 | 2.0 | None | False | True | 
| sagemaker | ml.c5d.18xlarge for notebook instance usage | L-6C73443F | 4.0 | None | False | True | 
| sagemaker | ml.eia2.xlarge for notebook instance accelerator type usage | L-A394C7DA | 20.0 | None | False | True | 
| sagemaker | Maximum number of SageMakerImage images allowed per account | L-DDDC1D15 | 1000.0 | None | False | True | 
| sagemaker | ml.m6gd.8xlarge for endpoint usage | L-95B12835 | 4.0 | None | False | True | 
| sagemaker | Rate of StartNotebookInstance requests | L-FCF4DD1A | 1.0 | None | False | False | 
| sagemaker | ml.p3.2xlarge for transform job usage | L-45F58E7E | 1.0 | None | False | True | 
| sagemaker | RSessionGateway Apps running on ml.m5d.2xlarge instance | L-DCD9DBD1 | 11.0 | None | False | True | 
| sagemaker | ml.t2.2xlarge for endpoint usage | L-20700136 | 30.0 | None | False | True | 
| sagemaker | Studio KernelGateway Apps running on ml.m5d.2xlarge instance | L-4A8D754D | 11.0 | None | False | True | 
| sagemaker | Rate of ListEndpointConfigs requests | L-206CAD5E | 2.0 | None | False | False | 
| sagemaker | ml.trn1.32xlarge for spot training job usage | L-F594DE31 | 0.0 | None | False | True | 
| sagemaker | ml.c6gd.12xlarge for endpoint usage | L-CCE6D1FE | 1.0 | None | False | True | 
| sagemaker | Studio KernelGateway Apps running on ml.m5d.12xlarge instance | L-BCDEC7B7 | 2.0 | None | False | True | 
| sagemaker | RSessionGateway Apps running on ml.g4dn.4xlarge instance | L-A7B1AACC | 0.0 | None | False | True | 
| sagemaker | ml.c6gn.4xlarge for endpoint usage | L-DA37C575 | 2.0 | None | False | True | 
| sagemaker | RSessionGateway Apps running on ml.r5.xlarge instance | L-C720D775 | 11.0 | None | False | True | 
| sagemaker | ml.r5.4xlarge for notebook instance usage | L-B74ED3C1 | 4.0 | None | False | True | 
| sagemaker | ml.p3.16xlarge for notebook instance usage | L-4689E606 | 1.0 | None | False | True | 
| sagemaker | ml.g4dn.16xlarge for processing job usage | L-47F095C9 | 0.0 | None | False | True | 
| sagemaker | ml.m5n.4xlarge for endpoint usage | L-63D6BD37 | 4.0 | None | False | True | 
| sagemaker | Rate of CreateTransformJob requests | L-9C2FFCB7 | 1.0 | None | False | False | 
| sagemaker | Number of instances across all transform jobs | L-60D2A6F0 | 20.0 | None | False | True | 
| sagemaker | ml.g4dn.xlarge for endpoint usage | L-B67CFA0C | 100.0 | None | False | True | 
| sagemaker | ml.m5.large for spot training job usage | L-29688C85 | 20.0 | None | False | True | 
| sagemaker | ml.c5.xlarge for transform job usage | L-09C9B23C | 16.0 | None | False | True | 
| sagemaker | ml.eia2.large for notebook instance accelerator type usage | L-862A7C0B | 20.0 | None | False | True | 
| sagemaker | RSessionGateway Apps running on ml.r5.large instance | L-FEEC5811 | 11.0 | None | False | True | 
| sagemaker | ml.inf1.24xlarge for endpoint usage | L-F971E784 | 1.0 | None | False | True | 
| sagemaker | Rate of ListNotebookInstances requests | L-1743E120 | 2.0 | None | False | False | 
| sagemaker | Studio KernelGateway Apps running on ml.g4dn.xlarge instance | L-F3C955A3 | 1.0 | None | False | True | 
| sagemaker | ml.c6i.12xlarge for endpoint usage | L-2AD0234B | 1.0 | None | False | True | 
| sagemaker | ml.m6g.xlarge for endpoint usage | L-2D2AAC6C | 1.0 | None | False | True | 
| sagemaker | ml.c4.8xlarge for spot training job usage | L-C5B2C408 | 16.0 | None | False | True | 
| sagemaker | ml.g5.4xlarge for training job usage | L-FE869B40 | 1.0 | None | False | True | 
| sagemaker | ml.g5.16xlarge for training job usage | L-9FAC65F7 | 1.0 | None | False | True | 
| sagemaker | Studio KernelGateway Apps running on ml.g4dn.16xlarge instance | L-D9B45548 | 0.0 | None | False | True | 
| sagemaker | ml.m5d.12xlarge for notebook instance usage | L-1DD0FB59 | 3.0 | None | False | True | 
| sagemaker | RSessionGateway Apps running on ml.c5.2xlarge instance | L-8B9D0385 | 11.0 | None | False | True | 
| sagemaker | ml.c4.xlarge for notebook instance usage | L-786E9B47 | 30.0 | None | False | True | 
| sagemaker | ml.c4.8xlarge for processing job usage | L-58B96098 | 2.0 | None | False | True | 
| sagemaker | ml.g4dn.4xlarge for processing job usage | L-B1C4D018 | 0.0 | None | False | True | 
| sagemaker | Maximum number of hyper parameter tuning jobs that can run at once in parallel | L-9D782CC7 | 100.0 | None | False | False | 
| sagemaker | ml.g5.12xlarge for training job usage | L-C6383286 | 1.0 | None | False | True | 
| sagemaker | ml.m5d.2xlarge for notebook instance usage | L-6829423A | 11.0 | None | False | True | 
| sagemaker | Maximum number of SageMaker Projects allowed per account | L-5CED4195 | 500.0 | None | False | False | 
| sagemaker | Total number of experiments allowed excluding those automatically created by SageMaker | L-A0C828DC | 5000.0 | None | False | False | 
| sagemaker | ml.c5.2xlarge for endpoint usage | L-E091038E | 4.0 | None | False | True | 
| sagemaker | ml.m6g.8xlarge for endpoint usage | L-DE9841A6 | 4.0 | None | False | True | 
| sagemaker | ml.p3.8xlarge for processing job usage | L-23EDF20C | 0.0 | None | False | True | 
| sagemaker | ml.m5.2xlarge for spot training job usage | L-4A823FAB | 20.0 | None | False | True | 
| sagemaker | ml.m5.2xlarge for processing job usage | L-1D84B9D2 | 8.0 | None | False | True | 
| sagemaker | ml.c4.4xlarge for transform job usage | L-90765203 | 4.0 | None | False | True | 
| sagemaker | ml.r5.12xlarge for endpoint usage | L-23FF30BF | 1.0 | None | False | True | 
| sagemaker | ml.m5.12xlarge for notebook instance usage | L-9AD04286 | 3.0 | None | False | True | 
| sagemaker | Maximum number of A2I flow definitions | L-73C1B556 | 100.0 | None | False | True | 
| sagemaker | Rate of DeleteEndpointConfig requests | L-C4717561 | 1.0 | None | False | False | 
| sagemaker | ml.c5d.xlarge for notebook instance usage | L-4E9EE949 | 11.0 | None | False | True | 
| sagemaker | ml.c5.4xlarge for processing job usage | L-EFB2F063 | 4.0 | None | False | True | 
| sagemaker | Maximum number of parameters allowed per pipeline | L-CED6A634 | 200.0 | None | False | False | 
| sagemaker | Canvas Apps running on system instances | L-65D1CFE4 | 40.0 | None | False | True | 
| sagemaker | ml.g4dn.2xlarge for notebook instance usage | L-1C2E1B03 | 8.0 | None | False | True | 
| sagemaker | ml.c6gn.12xlarge for endpoint usage | L-78B3DA25 | 1.0 | None | False | True | 
| sagemaker | Maximum number of training jobs each hyper parameter tuning job can run in parallel at once | L-11294128 | 10.0 | None | False | False | 
| sagemaker | ml.m4.xlarge for training warm pool usage | L-AFEEB9EB | 0.0 | None | False | True | 
| sagemaker | ml.p3.2xlarge for endpoint usage | L-1623D0BE | 2.0 | None | False | True | 
| sagemaker | ml.eia2.large for endpoint usage | L-9E017069 | 20.0 | None | False | True | 
| sagemaker | ml.c5.18xlarge for notebook instance usage | L-EF662387 | 2.0 | None | False | True | 
| sagemaker | ml.r5.12xlarge for notebook instance usage | L-5869E902 | 4.0 | None | False | True | 
| sagemaker | ml.m4.4xlarge for processing job usage | L-B3FC00CD | 4.0 | None | False | True | 
| sagemaker | Rate of CreateEndpoint requests | L-56A14E33 | 1.0 | None | False | False | 
| sagemaker | ml.m4.16xlarge for processing job usage | L-ED93A43F | 1.0 | None | False | True | 
| sagemaker | Longest run time for a training job | L-33A961FD | 432000.0 | Seconds | False | False | 
| sagemaker | ml.trn1.2xlarge for training job usage | L-74F2FC79 | 0.0 | None | False | True | 
| sagemaker | Maximum number of concurrently running model card export jobs allowed per account. | L-860ED60D | 0.0 | None | False | True | 
| sagemaker | ml.g4dn.8xlarge for training warm pool usage | L-769E114F | 0.0 | None | False | True | 
| sagemaker | ml.r6g.12xlarge for endpoint usage | L-DACE30FC | 1.0 | None | False | True | 
| sagemaker | RSessionGateway Apps running on ml.r5.4xlarge instance | L-005C1A21 | 4.0 | None | False | True | 
| sagemaker | ml.m4.xlarge for training job usage | L-A373146E | 30.0 | None | False | True | 
| sagemaker | ml.c5n.9xlarge for training job usage | L-D0327E29 | 1.0 | None | False | True | 
| sagemaker | Studio KernelGateway Apps running on ml.g5.4xlarge instance | L-DCE2AE7E | 0.0 | None | False | True | 
| sagemaker | ml.m4.10xlarge for training warm pool usage | L-1BF9151C | 0.0 | None | False | True | 
| sagemaker | ml.m4.2xlarge for training job usage | L-D589112D | 30.0 | None | False | True | 
| sagemaker | ml.t3.large for notebook instance usage | L-8E454C05 | 30.0 | None | False | True | 
| sagemaker | ml.c5.large for endpoint usage | L-4D27DFDD | 16.0 | None | False | True | 
| sagemaker | ml.m6g.16xlarge for endpoint usage | L-AF1BC9E1 | 2.0 | None | False | True | 
| sagemaker | ml.eia1.medium for notebook instance accelerator type usage | L-11667971 | 20.0 | None | False | True | 
| sagemaker | ml.r5.large for endpoint usage | L-B156D5EC | 4.0 | None | False | True | 
| sagemaker | ml.c4.2xlarge for training job usage | L-C5B4EE09 | 30.0 | None | False | True | 
| sagemaker | ml.g4dn.xlarge for transform job usage | L-4C5C5CA8 | 1.0 | None | False | True | 
| sagemaker | Studio KernelGateway Apps running on ml.m5d.large instance | L-32F895F6 | 11.0 | None | False | True | 
| sagemaker | Rate of CreateModel requests | L-BA5EF415 | 1.0 | None | False | False | 
| sagemaker | ml.g5.8xlarge for training job usage | L-43F5FC95 | 1.0 | None | False | True | 
| sagemaker | ml.r5.2xlarge for processing job usage | L-F0132B48 | 0.0 | None | False | True | 
| sagemaker | ml.r6gd.large for endpoint usage | L-7432A529 | 4.0 | None | False | True | 
| sagemaker | ml.r5dn.2xlarge for endpoint usage | L-DDD9E4D2 | 2.0 | None | False | True | 
| sagemaker | ml.m5.12xlarge for transform job usage | L-76A7309C | 1.0 | None | False | True | 
| sagemaker | Rate of DeleteModel requests | L-E2274DDA | 1.0 | None | False | False | 
| sagemaker | ml.c5.18xlarge for training warm pool usage | L-C8044861 | 0.0 | None | False | True | 
| sagemaker | RSessionGateway Apps running on ml.r5.24xlarge instance | L-D2CAE1E9 | 2.0 | None | False | True | 
| sagemaker | ml.g5.4xlarge for training warm pool usage | L-88E48241 | 0.0 | None | False | True | 
| sagemaker | Rate of CreateEndpointConfig requests | L-C48C555A | 1.0 | None | False | False | 
| sagemaker | Maximum number of concurrent pipeline executions allowed per account | L-F88776CD | 200.0 | None | False | True | 
| sagemaker | Studio KernelGateway Apps running on ml.m5.2xlarge instance | L-D4D7435A | 11.0 | None | False | True | 
| sagemaker | ml.p2.16xlarge for transform job usage | L-1F6E213E | 0.0 | None | False | True | 
| sagemaker | ml.eia1.large for notebook instance accelerator type usage | L-1E1D231A | 20.0 | None | False | True | 
| sagemaker | ml.m5.4xlarge for processing job usage | L-379E85A3 | 4.0 | None | False | True | 
| sagemaker | ml.c6gn.8xlarge for endpoint usage | L-DB5B82A8 | 1.0 | None | False | True | 
| sagemaker | ml.m5n.large for endpoint usage | L-AD7FD6A6 | 16.0 | None | False | True | 
| sagemaker | ml.r5.8xlarge for endpoint usage | L-7DD21282 | 1.0 | None | False | True | 
| sagemaker | ml.p3.16xlarge for transform job usage | L-A0B4500D | 0.0 | None | False | True | 
| sagemaker | ml.m5.4xlarge for training warm pool usage | L-03767DF9 | 0.0 | None | False | True | 
| sagemaker | ml.c5.9xlarge for training warm pool usage | L-ABFCF5A2 | 0.0 | None | False | True | 
| sagemaker | ml.c4.xlarge for training warm pool usage | L-1DA286AA | 0.0 | None | False | True | 
| sagemaker | ml.r5d.12xlarge for endpoint usage | L-283CDA96 | 1.0 | None | False | True | 
| sagemaker | ml.r5.24xlarge for notebook instance usage | L-D7FF3362 | 2.0 | None | False | True | 
| sagemaker | ml.c5n.18xlarge for spot training job usage | L-266C4F52 | 1.0 | None | False | True | 
| sagemaker | ml.trn1.32xlarge for training job usage | L-79A1FE57 | 0.0 | None | False | True | 
| sagemaker | ml.r6gd.4xlarge for endpoint usage | L-AE2F2D88 | 2.0 | None | False | True | 
| sagemaker | ml.c5d.18xlarge for endpoint usage | L-6A6E4B44 | 1.0 | None | False | True | 
| sagemaker | ml.m5.4xlarge for training job usage | L-AFB011B4 | 30.0 | None | False | True | 
| sagemaker | ml.p2.16xlarge for processing job usage | L-756F8AFB | 0.0 | None | False | True | 
| sagemaker | Studio KernelGateway Apps running on ml.g5.16xlarge instance | L-E66E2C21 | 0.0 | None | False | True | 
| sagemaker | ml.c6i.16xlarge for endpoint usage | L-FE72E327 | 1.0 | None | False | True | 
| sagemaker | ml.g5.8xlarge for endpoint usage | L-065D610E | 1.0 | None | False | True | 
| sagemaker | RSessionGateway Apps running on ml.c5.large instance | L-6958265E | 11.0 | None | False | True | 
| sagemaker | Rate of CreateTrainingJob requests | L-21A1652A | 1.0 | None | False | False | 
| sagemaker | ml.c5.xlarge for notebook instance usage | L-39F5FD98 | 11.0 | None | False | True | 
| sagemaker | ml.g5.4xlarge for notebook instance usage | L-127D4C65 | 5.0 | None | False | True | 
| sagemaker | ml.p2.8xlarge for transform job usage | L-0C630A26 | 0.0 | None | False | True | 
| sagemaker | ml.p2.16xlarge for training warm pool usage | L-2D3D338A | 0.0 | None | False | True | 
| sagemaker | ml.m4.xlarge for spot training job usage | L-2ECAA15F | 20.0 | None | False | True | 
| sagemaker | Maximum number of Ground Truth Streaming labeling jobs | L-C3E706F6 | 20.0 | None | False | True | 
| sagemaker | ml.m5d.4xlarge for endpoint usage | L-2BF1C629 | 4.0 | None | False | True | 
| sagemaker | Rate of DeleteNotebookInstanceLifecycleConfig requests | L-C98EE842 | 1.0 | None | False | False | 
| sagemaker | ml.g5.12xlarge for spot training job usage | L-03E19172 | 1.0 | None | False | True | 
| sagemaker | ml.m4.10xlarge for processing job usage | L-BB72E7FA | 2.0 | None | False | True | 
| sagemaker | ml.t3.large for processing job usage | L-C076FA77 | 20.0 | None | False | True | 
| sagemaker | ml.m5.xlarge for endpoint usage | L-2F737F8D | 16.0 | None | False | True | 
| sagemaker | RSessionGateway Apps running on ml.r5.16xlarge instance | L-2B2789AA | 2.0 | None | False | True | 
| sagemaker | ml.p3.8xlarge for training warm pool usage | L-5CA5BEE6 | 0.0 | None | False | True | 
| sagemaker | ml.t2.large for endpoint usage | L-1410387A | 30.0 | None | False | True | 
| sagemaker | ml.r5d.4xlarge for endpoint usage | L-C4DFBAA1 | 2.0 | None | False | True | 
| sagemaker | ml.g5.24xlarge for endpoint usage | L-6821867B | 0.0 | None | False | True | 
| sagemaker | ml.r6g.2xlarge for endpoint usage | L-862299A2 | 2.0 | None | False | True | 
| sagemaker | ml.r5.4xlarge for processing job usage | L-E4F6EF77 | 0.0 | None | False | True | 
| sagemaker | Studio KernelGateway Apps running on ml.t3.large instance | L-8BD17C20 | 30.0 | None | False | True | 
| sagemaker | ml.c4.xlarge for transform job usage | L-E3C0D615 | 16.0 | None | False | True | 
| sagemaker | ml.c4.xlarge for spot training job usage | L-9BA5373F | 20.0 | None | False | True | 
| sagemaker | ml.c5n.18xlarge for training warm pool usage | L-566A905C | 0.0 | None | False | True | 
| sagemaker | Studio KernelGateway Apps running on ml.t3.2xlarge instance | L-5AF0D27D | 30.0 | None | False | True | 
| sagemaker | ml.p3dn.24xlarge for training job usage | L-8DCA2E97 | 0.0 | None | False | True | 
| sagemaker | RSessionGateway Apps running on ml.t3.large instance | L-0FCBFBBD | 30.0 | None | False | True | 
| sagemaker | ml.c5n.18xlarge for training job usage | L-A1E21094 | 1.0 | None | False | True | 
| sagemaker | ml.c5n.4xlarge for spot training job usage | L-37059D02 | 1.0 | None | False | True | 
| sagemaker | ml.m5dn.xlarge for endpoint usage | L-D16917AC | 16.0 | None | False | True | 
| sagemaker | ml.m4.2xlarge for processing job usage | L-0309C694 | 8.0 | None | False | True | 
| sagemaker | Maximum number of Ground Truth labeling jobs | L-150039CA | 20.0 | None | False | True | 
| sagemaker | ml.r5.large for processing job usage | L-43562353 | 0.0 | None | False | True | 
| sagemaker | ml.p4d.24xlarge for training job usage | L-09B4A649 | 0.0 | None | False | True | 
| sagemaker | Rate of DeleteStudioLifecycleConfig requests | L-3D52557B | 1.0 | None | False | False | 
| sagemaker | Maximum number of device-fleets | L-384D4DB3 | 10.0 | None | False | True | 
| sagemaker | RSessionGateway Apps running on ml.r5.12xlarge instance | L-1C84ABBF | 2.0 | None | False | True | 
| sagemaker | Studio KernelGateway Apps running on ml.g5.xlarge instance | L-60470224 | 0.0 | None | False | True | 
| sagemaker | ml.c5.4xlarge for transform job usage | L-98742DAD | 4.0 | None | False | True | 
| sagemaker | ml.c5.9xlarge for endpoint usage | L-C15ACFF4 | 2.0 | None | False | True | 
| sagemaker | RSessionGateway Apps running on ml.m5d.16xlarge instance | L-8101A535 | 2.0 | None | False | True | 
| sagemaker | ml.p3.8xlarge for notebook instance usage | L-619D6E43 | 2.0 | None | False | True | 
| sagemaker | ml.t3.medium for notebook instance usage | L-E17566B7 | 30.0 | None | False | True | 
| sagemaker | ml.g5.8xlarge for spot training job usage | L-DD18D5D6 | 1.0 | None | False | True | 
| sagemaker | ml.g4dn.16xlarge for notebook instance usage | L-64067773 | 2.0 | None | False | True | 
| sagemaker | ml.c5n.4xlarge for training job usage | L-E215EF33 | 1.0 | None | False | True | 
| sagemaker | Studio KernelGateway Apps running on ml.t3.xlarge instance | L-3A44AF4B | 30.0 | None | False | True | 
| sagemaker | ml.g4dn.4xlarge for notebook instance usage | L-529379E4 | 4.0 | None | False | True | 
| sagemaker | ml.g5.12xlarge for notebook instance usage | L-EC374A06 | 2.0 | None | False | True | 
| sagemaker | ml.eia2.xlarge for endpoint usage | L-448C2416 | 20.0 | None | False | True | 
| sagemaker | ml.c5.xlarge for endpoint usage | L-E9EE5599 | 8.0 | None | False | True | 
| sagemaker | ml.r5.xlarge for processing job usage | L-B2D8E643 | 0.0 | None | False | True | 
| sagemaker | Rate of ListStudioLifecycleConfigs requests | L-FF0345A7 | 2.0 | None | False | False | 
| sagemaker | ml.g5.4xlarge for spot training job usage | L-DB4D51CF | 1.0 | None | False | True | 
| sagemaker | Studio KernelGateway Apps running on ml.m5.4xlarge instance | L-0132CA88 | 6.0 | None | False | True | 
| sagemaker | ml.c4.xlarge for processing job usage | L-2BAB231B | 16.0 | None | False | True | 
| sagemaker | ml.m5d.2xlarge for endpoint usage | L-8F28AFFB | 8.0 | None | False | True | 
| sagemaker | ml.c5.24xlarge for endpoint usage | L-B5714749 | 1.0 | None | False | True | 
| sagemaker | ml.g5.12xlarge for training warm pool usage | L-29508C65 | 0.0 | None | False | True | 
| sagemaker | Rate of CreateStudioLifecycleConfig requests | L-06E121F0 | 1.0 | None | False | False | 
| sagemaker | RSessionGateway Apps running on ml.t3.2xlarge instance | L-4755F613 | 30.0 | None | False | True | 
| sagemaker | ml.eia2.medium for endpoint usage | L-77C35A0F | 20.0 | None | False | True | 
| sagemaker | ml.r6gd.8xlarge for endpoint usage | L-593EF138 | 1.0 | None | False | True | 
| sagemaker | Studio KernelGateway Apps running on ml.r5.large instance | L-59F3BE31 | 11.0 | None | False | True | 
| sagemaker | ml.m6gd.large for endpoint usage | L-1630284B | 16.0 | None | False | True | 
| sagemaker | ml.c5n.9xlarge for spot training job usage | L-D144443B | 1.0 | None | False | True | 
| sagemaker | Studio KernelGateway Apps running on ml.m5.xlarge instance | L-CD017EBE | 11.0 | None | False | True | 
| sagemaker | ml.r5n.12xlarge for endpoint usage | L-9F47FCE3 | 1.0 | None | False | True | 
| sagemaker | Studio KernelGateway Apps running on ml.c5.xlarge instance | L-F2F8BB60 | 11.0 | None | False | True | 
| sagemaker | Studio KernelGateway Apps running on ml.r5.xlarge instance | L-CC73B658 | 11.0 | None | False | True | 
| sagemaker | ml.c4.4xlarge for training job usage | L-505634D0 | 30.0 | None | False | True | 
| sagemaker | ml.c4.4xlarge for processing job usage | L-6F6C723E | 4.0 | None | False | True | 
| sagemaker | ml.g4dn.4xlarge for transform job usage | L-EAB0CBAB | 0.0 | None | False | True | 
| sagemaker | ml.c5.18xlarge for transform job usage | L-B538D5DB | 1.0 | None | False | True | 
| sagemaker | ml.m4.xlarge for transform job usage | L-DAB6AA41 | 16.0 | None | False | True | 
| sagemaker | ml.m5.4xlarge for spot training job usage | L-2A6ACFF7 | 10.0 | None | False | True | 
| sagemaker | ml.r5d.2xlarge for endpoint usage | L-A40ED4BA | 2.0 | None | False | True | 
| sagemaker | ml.c5n.2xlarge for endpoint usage | L-DDF361A9 | 4.0 | None | False | True | 
| sagemaker | ml.p2.16xlarge for spot training job usage | L-2E99C6D1 | 0.0 | None | False | True | 
| sagemaker | Rate of DescribeEndpoint requests | L-A0EB0A2A | 5.0 | None | False | False | 
| sagemaker | ml.m5dn.12xlarge for endpoint usage | L-5EF89E74 | 2.0 | None | False | True | 
| sagemaker | ml.c5.9xlarge for notebook instance usage | L-B5F303BE | 4.0 | None | False | True | 
| sagemaker | ml.c5.12xlarge for endpoint usage | L-DD50A8E1 | 2.0 | None | False | True | 
| sagemaker | ml.c4.4xlarge for spot training job usage | L-C087612A | 20.0 | None | False | True | 
| sagemaker | Rate of InvokeEndpoint requests | L-612DD414 | 10000.0 | None | False | False | 
| sagemaker | Number of workteams | L-1BAEE5A7 | 25.0 | None | False | False | 
| sagemaker | Rate of DescribeEndpointConfig requests | L-B50E4FC3 | 5.0 | None | False | False | 
| sagemaker | ml.m4.2xlarge for notebook instance usage | L-CE6894AA | 30.0 | None | False | True | 
| sagemaker | Rate of DeleteNotebookInstance requests | L-E20CA2A9 | 1.0 | None | False | False | 
| sagemaker | RSessionGateway Apps running on ml.t3.micro instance | L-E127AD95 | 0.0 | None | False | True | 
| sagemaker | RSessionGateway Apps running on ml.c5.12xlarge instance | L-21962CDA | 4.0 | None | False | True | 
| sagemaker | RSessionGateway Apps running on ml.g4dn.16xlarge instance | L-144A2794 | 0.0 | None | False | True | 
| sagemaker | ml.c7g.large for endpoint usage | L-3F48ACC6 | 0.0 | None | False | True | 
| sagemaker | ml.r5dn.12xlarge for endpoint usage | L-599D6573 | 1.0 | None | False | True | 
| sagemaker | ml.p2.8xlarge for training warm pool usage | L-59DEBE1F | 0.0 | None | False | True | 
| sagemaker | Rate of CreateNotebookInstanceLifecycleConfig requests | L-B9F1A904 | 1.0 | None | False | False | 
| sagemaker | RSessionGateway Apps running on ml.m5.12xlarge instance | L-4FC1E99C | 2.0 | None | False | True | 
| sagemaker | ml.r5.2xlarge for endpoint usage | L-AA5E2462 | 2.0 | None | False | True | 
| sagemaker | Time at which pipeline executions time out | L-A24D873D | 672.0 | None | False | False | 
| sagemaker | ml.c6i.xlarge for endpoint usage | L-28FF72CA | 8.0 | None | False | True | 
| sagemaker | ml.p3.8xlarge for spot training job usage | L-0201B959 | 0.0 | None | False | True | 
| sagemaker | ml.m5dn.8xlarge for endpoint usage | L-178948BA | 4.0 | None | False | True | 
| sagemaker | ml.m5.8xlarge for endpoint usage | L-92566F3C | 4.0 | None | False | True | 
| sagemaker | ml.p2.8xlarge for endpoint usage | L-BD0BDFDA | 1.0 | None | False | True | 
| sagemaker | ml.m5d.xlarge for endpoint usage | L-3E65B286 | 16.0 | None | False | True | 
| sagemaker | ml.r5.large for notebook instance usage | L-8BED04E5 | 11.0 | None | False | True | 
| sagemaker | Canvas Apps running on ml.m5.4xlarge instances | L-23A89612 | 40.0 | None | False | True | 
| sagemaker | Studio KernelGateway Apps running on ml.g5.12xlarge instance | L-037F309A | 0.0 | None | False | True | 
| sagemaker | ml.m4.16xlarge for spot training job usage | L-A50827DD | 5.0 | None | False | True | 
| sagemaker | Rate of UpdateNotebookInstanceLifecycleConfig requests | L-1AF0C909 | 1.0 | None | False | False | 
| sagemaker | ml.g4dn.12xlarge for training warm pool usage | L-CB4A3655 | 0.0 | None | False | True | 
| sagemaker | ml.c4.2xlarge for training warm pool usage | L-72EF9D60 | 0.0 | None | False | True | 
| sagemaker | Maximum number of instances per endpoint | L-ED8DEE9B | 200.0 | None | False | True | 
| sagemaker | Studio KernelGateway Apps running on ml.p3.2xlarge instance | L-9D41067A | 0.0 | None | False | True | 
| sagemaker | ml.c5n.xlarge for endpoint usage | L-B3A1B2F7 | 8.0 | None | False | True | 
| sagemaker | Rate of DeleteEndpoint requests | L-0AFC5B08 | 1.0 | None | False | False | 
| sagemaker | ml.m5.2xlarge for notebook instance usage | L-95E39457 | 11.0 | None | False | True | 
| sagemaker | ml.m4.xlarge for endpoint usage | L-97CF11BE | 16.0 | None | False | True | 
| sagemaker | ml.t2.xlarge for endpoint usage | L-B82FDF78 | 30.0 | None | False | True | 
| sagemaker | Rate of CreatePresignedNotebookInstanceUrl requests | L-704CC035 | 1.0 | None | False | False | 
| sagemaker | ml.g4dn.16xlarge for training warm pool usage | L-C960C80D | 0.0 | None | False | True | 
| sagemaker | Studio KernelGateway Apps running on ml.c5.12xlarge instance | L-C47C8B74 | 4.0 | None | False | True | 
| sagemaker | ml.c5n.2xlarge for training warm pool usage | L-2952557B | 0.0 | None | False | True | 
| sagemaker | ml.m5d.large for notebook instance usage | L-195A207B | 11.0 | None | False | True | 
| sagemaker | ml.m5.12xlarge for spot training job usage | L-29B03627 | 3.0 | None | False | True | 
| sagemaker | ml.m4.2xlarge for training warm pool usage | L-E312D77E | 0.0 | None | False | True | 
| sagemaker | Studio KernelGateway Apps running on ml.c5.24xlarge instance | L-CBCD290E | 2.0 | None | False | True | 
| sagemaker | ml.g5.12xlarge for endpoint usage | L-65C4BD00 | 0.0 | None | False | True | 
| sagemaker | ml.g5.8xlarge for notebook instance usage | L-5D8382CB | 5.0 | None | False | True | 
| sagemaker | Studio KernelGateway Apps running on ml.g4dn.2xlarge instance | L-E5775070 | 1.0 | None | False | True | 
| sagemaker | Studio KernelGateway Apps running on ml.p3.8xlarge instance | L-D12B1AA4 | 0.0 | None | False | True | 
| sagemaker | ml.c5.xlarge for spot training job usage | L-6FA0D387 | 20.0 | None | False | True | 
| sagemaker | RSessionGateway Apps running on ml.g4dn.xlarge instance | L-050981C0 | 1.0 | None | False | True | 
| sagemaker | Rate of StopNotebookInstance requests | L-01341C09 | 1.0 | None | False | False | 
| sagemaker | ml.m5.24xlarge for notebook instance usage | L-BD97DD7F | 2.0 | None | False | True | 
| sagemaker | ml.c6g.large for endpoint usage | L-4E81EEAC | 16.0 | None | False | True | 
| sagemaker | ml.g5.24xlarge for training job usage | L-ED7BD217 | 0.0 | None | False | True | 
| sagemaker | ml.r5n.large for endpoint usage | L-FE3BF22B | 4.0 | None | False | True | 
| sagemaker | ml.c4.8xlarge for notebook instance usage | L-D0B132AA | 30.0 | None | False | True | 
| sagemaker | RSessionGateway Apps running on ml.m5d.large instance | L-B6744048 | 11.0 | None | False | True | 
| sagemaker | ml.r5.12xlarge for processing job usage | L-20546400 | 0.0 | None | False | True | 
| sagemaker | ml.p2.8xlarge for spot training job usage | L-ACF1D2B2 | 0.0 | None | False | True | 
| sagemaker | Studio KernelGateway Apps running on ml.g4dn.4xlarge instance | L-0E846ECD | 0.0 | None | False | True | 
| sagemaker | ml.p2.xlarge for transform job usage | L-89843D09 | 1.0 | None | False | True | 
| sagemaker | ml.m5dn.24xlarge for endpoint usage | L-62190228 | 1.0 | None | False | True | 
| sagemaker | ml.r6g.4xlarge for endpoint usage | L-713F6743 | 2.0 | None | False | True | 
| sagemaker | Number of instances across all training jobs | L-00C91CB5 | 30.0 | None | False | True | 
| sagemaker | Maximum number of parallel edge-deployments | L-9D69F80D | 20.0 | None | False | True | 
| sagemaker | Studio KernelGateway Apps running on ml.m5.large instance | L-22BC3627 | 11.0 | None | False | True | 
| sagemaker | ml.g5.2xlarge for spot training job usage | L-CAEE7DB7 | 1.0 | None | False | True | 
| sagemaker | Number of elastic inference accelerators across all notebook instances | L-173933E7 | 20.0 | None | False | True | 
| sagemaker | ml.c5.18xlarge for spot training job usage | L-239B242B | 5.0 | None | False | True | 
| sagemaker | Rate of ListTransformJobs requests | L-3AAF267A | 2.0 | None | False | False | 
| sagemaker | ml.c6i.32xlarge for endpoint usage | L-769D172E | 1.0 | None | False | True | 
| sagemaker | Rate of StopTrainingJob requests | L-B57580F5 | 1.0 | None | False | False | 
| sagemaker | Studio KernelGateway Apps running on ml.g5.8xlarge instance | L-76D497CD | 0.0 | None | False | True | 
| sagemaker | ml.c7g.xlarge for endpoint usage | L-4A5B28AA | 0.0 | None | False | True | 
| sagemaker | ml.p2.xlarge for notebook instance usage | L-BBB3C62F | 8.0 | None | False | True | 
| sagemaker | ml.m5.large for transform job usage | L-236AE59F | 16.0 | None | False | True | 
| sagemaker | Studio KernelGateway Apps running on ml.m5.24xlarge instance | L-1DA9A185 | 2.0 | None | False | True | 
| sagemaker | ml.inf1.6xlarge for endpoint usage | L-574C8A05 | 2.0 | None | False | True | 
| sagemaker | ml.c5d.large for endpoint usage | L-919688C1 | 16.0 | None | False | True | 
| sagemaker | ml.c5.xlarge for processing job usage | L-486519E6 | 16.0 | None | False | True | 
| sagemaker | ml.r5.xlarge for endpoint usage | L-BCA2C892 | 4.0 | None | False | True | 
| sagemaker | ml.c5.18xlarge for processing job usage | L-2D8CD70A | 1.0 | None | False | True | 
| sagemaker | ml.g4dn.12xlarge for notebook instance usage | L-47461EBA | 2.0 | None | False | True | 
| sagemaker | RSessionGateway Apps running on ml.c5.4xlarge instance | L-8733EEBD | 4.0 | None | False | True | 
| sagemaker | ml.p2.xlarge for spot training job usage | L-21545BA5 | 1.0 | None | False | True | 
| sagemaker | ml.m5.large for training job usage | L-611FA074 | 30.0 | None | False | True | 
| sagemaker | ml.m5d.12xlarge for endpoint usage | L-B7AC53F5 | 2.0 | None | False | True | 
| sagemaker | ml.c6g.4xlarge for endpoint usage | L-4C2FABCC | 4.0 | None | False | True | 
| sagemaker | ml.g5.8xlarge for training warm pool usage | L-40E8018C | 0.0 | None | False | True | 
| sagemaker | RSessionGateway Apps running on ml.t3.xlarge instance | L-D7932DDD | 30.0 | None | False | True | 
| sagemaker | ml.c4.2xlarge for processing job usage | L-50AA109F | 8.0 | None | False | True | 
| sagemaker | ml.g5.48xlarge for endpoint usage | L-0100B823 | 0.0 | None | False | True | 
| sagemaker | ml.c6g.2xlarge for endpoint usage | L-B87A968D | 4.0 | None | False | True | 
| sagemaker | ml.g5.xlarge for endpoint usage | L-1928E07B | 4.0 | None | False | True | 
| sagemaker | ml.m5.xlarge for transform job usage | L-7939E4EC | 8.0 | None | False | True | 
| sagemaker | RSessionGateway Apps running on ml.c5.18xlarge instance | L-21552510 | 2.0 | None | False | True | 
| sagemaker | Maximum number of running Studio apps per domain | L-4E39DDC4 | 80.0 | None | False | True | 
| sagemaker | ml.r6g.xlarge for endpoint usage | L-B8A3B4CE | 4.0 | None | False | True | 
| sagemaker | Studio KernelGateway Apps running on ml.m5.8xlarge instance | L-19734703 | 2.0 | None | False | True | 
| sagemaker | ml.m5.24xlarge for processing job usage | L-E2E903C6 | 1.0 | None | False | True | 
| sagemaker | Studio KernelGateway Apps running on ml.g5.48xlarge instance | L-94E271A3 | 0.0 | None | False | True | 
| sagemaker | ml.p3.16xlarge for processing job usage | L-C5621FC4 | 0.0 | None | False | True | 
| sagemaker | RSessionGateway Apps running on ml.g4dn.12xlarge instance | L-5392B59D | 0.0 | None | False | True | 
| sagemaker | ml.r6gd.xlarge for endpoint usage | L-660E0683 | 4.0 | None | False | True | 
| sagemaker | ml.c6gn.2xlarge for endpoint usage | L-5F238DF4 | 4.0 | None | False | True | 
| sagemaker | ml.m4.2xlarge for transform job usage | L-5B86ED31 | 8.0 | None | False | True | 
| sagemaker | ml.m4.4xlarge for endpoint usage | L-3727EAE2 | 8.0 | None | False | True | 
| sagemaker | RSessionGateway Apps running on ml.m5.large instance | L-BDDC56AF | 11.0 | None | False | True | 
| sagemaker | ml.g4dn.xlarge for spot training job usage | L-944F78BB | 1.0 | None | False | True | 
| sagemaker | Maximum number of devices | L-987E0769 | 10000.0 | None | False | True | 
| sagemaker | Total number of trials a single trial component can be associated to | L-67A4559B | 500.0 | None | False | False | 
| sagemaker | RStudioServerPro Apps running on ml.c5.9xlarge instances | L-D9E59670 | 1.0 | None | False | True | 
| sagemaker | ml.m5dn.2xlarge for endpoint usage | L-DCC57354 | 8.0 | None | False | True | 
| sagemaker | ml.p3.16xlarge for training warm pool usage | L-763CF8E3 | 0.0 | None | False | True | 
| sagemaker | ml.c6gn.large for endpoint usage | L-941884ED | 16.0 | None | False | True | 
| sagemaker | ml.c5d.2xlarge for notebook instance usage | L-FF78806F | 11.0 | None | False | True | 
| sagemaker | ml.g4dn.4xlarge for training warm pool usage | L-3408A20D | 0.0 | None | False | True | 
| sagemaker | ml.r5n.8xlarge for endpoint usage | L-54340DBD | 2.0 | None | False | True | 
| sagemaker | ml.m4.16xlarge for endpoint usage | L-BCA7D0DE | 4.0 | None | False | True | 
| sagemaker | Studio KernelGateway Apps running on ml.m5d.xlarge instance | L-669A1EF3 | 11.0 | None | False | True | 
| sagemaker | Maximum number of model card versions allowed per account. | L-EF24FBDB | 0.0 | None | False | True | 
| sagemaker | ml.eia1.xlarge for notebook instance accelerator type usage | L-F8266BD5 | 20.0 | None | False | True | 
| sagemaker | RSessionGateway Apps running on ml.t3.medium instance | L-7A45086A | 30.0 | None | False | True | 
| sagemaker | Size of EBS volume for a training job instance | L-C5A266EB | 1024.0 | None | False | False | 
| sagemaker | Studio KernelGateway Apps running on ml.r5.2xlarge instance | L-1747114E | 11.0 | None | False | True | 
| sagemaker | RSessionGateway Apps running on ml.p3.2xlarge instance | L-ADBE66E5 | 0.0 | None | False | True | 
| sagemaker | ml.c6gd.8xlarge for endpoint usage | L-4027057F | 1.0 | None | False | True | 
| sagemaker | Longest run time for an AutoML job from creation to termination | L-05D71277 | 2592000.0 | Seconds | False | False | 
| sagemaker | ml.m5.24xlarge for transform job usage | L-5F2D4124 | 1.0 | None | False | True | 
| sagemaker | ml.g4dn.xlarge for training job usage | L-3F53BF0F | 1.0 | None | False | True | 
| sagemaker | Rate of DescribeTrainingJob requests | L-96E3A68C | 5.0 | None | False | False | 
| sagemaker | ml.c5.18xlarge for endpoint usage | L-409A03CD | 1.0 | None | False | True | 
| sagemaker | ml.m4.4xlarge for transform job usage | L-5F5255E9 | 4.0 | None | False | True | 
| sagemaker | ml.m5.2xlarge for training warm pool usage | L-1686EE8B | 0.0 | None | False | True | 
| sagemaker | ml.g5.24xlarge for notebook instance usage | L-4ACAC7A4 | 2.0 | None | False | True | 
| sagemaker | ml.t2.medium for endpoint usage | L-29C181D7 | 30.0 | None | False | True | 
| sagemaker | ml.c5.9xlarge for transform job usage | L-2441079A | 2.0 | None | False | True | 
| sagemaker | ml.p2.16xlarge for notebook instance usage | L-39F2D553 | 2.0 | None | False | True | 
| sagemaker | Studio KernelGateway Apps running on ml.m5.12xlarge instance | L-9772863B | 2.0 | None | False | True | 
| sagemaker | ml.c5d.9xlarge for notebook instance usage | L-9944ECC4 | 4.0 | None | False | True | 
| sagemaker | ml.m5.xlarge for training warm pool usage | L-0BEF44E8 | 0.0 | None | False | True | 
| sagemaker | ml.m4.10xlarge for endpoint usage | L-C4008A6B | 4.0 | None | False | True | 
| sagemaker | ml.m5.12xlarge for training job usage | L-6F6C8949 | 5.0 | None | False | True | 
| sagemaker | ml.m5.12xlarge for processing job usage | L-BC1C7D38 | 2.0 | None | False | True | 
| sagemaker | Rate of CreateNotebookInstance requests | L-C1A208ED | 1.0 | None | False | False | 
| sagemaker | Rate of ListMonitoringAlertHistory requests | L-C899B716 | 2.0 | None | False | False | 
| sagemaker | ml.r6gd.12xlarge for endpoint usage | L-177D4E91 | 1.0 | None | False | True | 
| sagemaker | ml.p3.16xlarge for endpoint usage | L-6A85BC13 | 0.0 | None | False | True | 
| sagemaker | Size of EBS volume for a transform job instance | L-DDA1AAD8 | 1024.0 | None | False | False | 
| sagemaker | ml.t3.medium for processing job usage | L-0CE343FE | 50.0 | None | False | True | 
| sagemaker | ml.c6i.4xlarge for endpoint usage | L-B5612E02 | 2.0 | None | False | True | 
| sagemaker | ml.m5n.xlarge for endpoint usage | L-943961F3 | 16.0 | None | False | True | 
| sagemaker | Maximum number of dataset objects per labeling job | L-EF62EAFA | 10000.0 | None | False | False | 
| sagemaker | ml.p2.8xlarge for notebook instance usage | L-AC3A6D59 | 2.0 | None | False | True | 
| sagemaker | ml.g5.xlarge for training job usage | L-B6D80D9C | 1.0 | None | False | True | 
| sagemaker | Studio KernelGateway Apps running on ml.c5.18xlarge instance | L-A4519BF1 | 2.0 | None | False | True | 
| sagemaker | ml.g4dn.xlarge for training warm pool usage | L-955074FD | 0.0 | None | False | True | 
| sagemaker | ml.g4dn.12xlarge for spot training job usage | L-199558F0 | 1.0 | None | False | True | 
| sagemaker | ml.c6i.large for endpoint usage | L-3C2EBC55 | 16.0 | None | False | True | 
| sagemaker | ml.r5dn.24xlarge for endpoint usage | L-FF424265 | 0.0 | None | False | True | 
| sagemaker | ml.m5dn.4xlarge for endpoint usage | L-EC92C7B3 | 4.0 | None | False | True | 
| sagemaker | ml.m5.4xlarge for endpoint usage | L-E2649D46 | 4.0 | None | False | True | 
| sagemaker | ml.m5.xlarge for processing job usage | L-0307F515 | 16.0 | None | False | True | 
| sagemaker | ml.c5.2xlarge for spot training job usage | L-4581C083 | 20.0 | None | False | True | 
| sagemaker | ml.r5n.16xlarge for endpoint usage | L-C14C7B0C | 0.0 | None | False | True | 
| sagemaker | ml.g5.2xlarge for training job usage | L-2D6DEB3C | 1.0 | None | False | True | 
| sagemaker | ml.p3.2xlarge for training warm pool usage | L-E3709F6E | 0.0 | None | False | True | 
| sagemaker | ml.m4.4xlarge for training job usage | L-E60A61DF | 15.0 | None | False | True | 
| sagemaker | ml.r5.8xlarge for processing job usage | L-154D0022 | 0.0 | None | False | True | 
| sagemaker | ml.m5.24xlarge for endpoint usage | L-329751EB | 1.0 | None | False | True | 
| sagemaker | ml.m6g.4xlarge for endpoint usage | L-8EE25AE3 | 4.0 | None | False | True | 
| sagemaker | ml.r5.16xlarge for processing job usage | L-06A1E8BB | 0.0 | None | False | True | 
| sagemaker | RSessionGateway Apps running on ml.m5.4xlarge instance | L-30ABD943 | 6.0 | None | False | True | 
| sagemaker | ml.m5.large for endpoint usage | L-614B09FD | 16.0 | None | False | True | 
| sagemaker | Rate of DescribeModel requests | L-7FADB696 | 5.0 | None | False | False | 
| sagemaker | Maximum number of deployment plans that can be simultaneously created | L-A9A47E0F | 20.0 | None | False | True | 
| sagemaker | ml.p2.8xlarge for training job usage | L-33BA8B57 | 0.0 | None | False | True | 
| sagemaker | Rate of UpdateEndpointWeightsAndCapacities requests | L-AD9316E0 | 1.0 | None | False | False | 
| sagemaker | Studio KernelGateway Apps running on ml.m5d.24xlarge instance | L-F43A1825 | 2.0 | None | False | True | 
| sagemaker | Studio KernelGateway Apps running on ml.g5.2xlarge instance | L-4918D123 | 0.0 | None | False | True | 
| sagemaker | Studio KernelGateway Apps running on ml.r5.8xlarge instance | L-8536F2DB | 2.0 | None | False | True | 
| sagemaker | ml.eia2.medium for notebook instance accelerator type usage | L-C2D5FF36 | 20.0 | None | False | True | 
| sagemaker | ml.r5dn.large for endpoint usage | L-842D5E10 | 4.0 | None | False | True | 
| sagemaker | ml.c7g.2xlarge for endpoint usage | L-85DBDADC | 0.0 | None | False | True | 
| sagemaker | ml.r5n.2xlarge for endpoint usage | L-581DD22D | 2.0 | None | False | True | 
| sagemaker | ml.c5d.xlarge for endpoint usage | L-F30D287E | 8.0 | None | False | True | 
| sagemaker | Studio KernelGateway Apps running on ml.c5.9xlarge instance | L-9F2E8F67 | 4.0 | None | False | True | 
| sagemaker | ml.m4.10xlarge for transform job usage | L-63443CBC | 2.0 | None | False | True | 
| sagemaker | Studio KernelGateway Apps running on ml.m5d.16xlarge instance | L-4F2BEC71 | 2.0 | None | False | True | 
| sagemaker | ml.p4d.24xlarge for training warm pool usage | L-A8827666 | 0.0 | None | False | True | 
| sagemaker | ml.c5d.4xlarge for endpoint usage | L-A06D6E01 | 2.0 | None | False | True | 
| sagemaker | ml.c4.2xlarge for endpoint usage | L-54106F23 | 4.0 | None | False | True | 
| sagemaker | Maximum number of parallel edge-packaging jobs | L-4C681076 | 20.0 | None | False | True | 
| sagemaker | ml.r6gd.2xlarge for endpoint usage | L-93490D80 | 2.0 | None | False | True | 
| sagemaker | ml.c5n.2xlarge for spot training job usage | L-C1E6B202 | 1.0 | None | False | True | 
| sagemaker | ml.c6gd.large for endpoint usage | L-C10DAD58 | 16.0 | None | False | True | 
| sagemaker | ml.g4dn.8xlarge for endpoint usage | L-7D28AD75 | 1.0 | None | False | True | 
| sagemaker | ml.c5.4xlarge for training job usage | L-E7898792 | 8.0 | None | False | True | 
| sagemaker | Longest run time for a processing job | L-EA47BDD3 | 432000.0 | Seconds | False | False | 
| sagemaker | Maximum number of pipelines allowed per account | L-E8EADE50 | 500.0 | None | False | False | 
| sagemaker | ml.g5.xlarge for spot training job usage | L-DE07CBDF | 1.0 | None | False | True | 
| sagemaker | ml.c5.2xlarge for notebook instance usage | L-5F356922 | 11.0 | None | False | True | 
| sagemaker | Size of EBS volume for a processing job instance | L-D7BEE2A3 | 1024.0 | None | False | False | 
| sagemaker | ml.c4.8xlarge for training job usage | L-6BE85179 | 16.0 | None | False | True | 
| sagemaker | ml.r5dn.xlarge for endpoint usage | L-48F0F627 | 4.0 | None | False | True | 
| sagemaker | ml.p3.2xlarge for notebook instance usage | L-1F4A5AAB | 8.0 | None | False | True | 
| sagemaker | ml.c5.9xlarge for processing job usage | L-945D1F1D | 2.0 | None | False | True | 
| sagemaker | ml.p2.16xlarge for training job usage | L-7FC32A75 | 0.0 | None | False | True | 
| sagemaker | ml.c4.2xlarge for notebook instance usage | L-A028E7A2 | 30.0 | None | False | True | 
| sagemaker | ml.g5.4xlarge for endpoint usage | L-C1B9A48D | 2.0 | None | False | True | 
| sagemaker | ml.t2.medium for notebook instance usage | L-7B2FD69B | 30.0 | None | False | True | 
| sagemaker | ml.m5d.4xlarge for notebook instance usage | L-EDE09F63 | 6.0 | None | False | True | 
| sagemaker | Studio KernelGateway Apps running on ml.c5.2xlarge instance | L-A56EEC3D | 11.0 | None | False | True | 
| sagemaker | ml.c7g.12xlarge for endpoint usage | L-57850F1B | 0.0 | None | False | True | 
| sagemaker | ml.r5.16xlarge for endpoint usage | L-DCB12F9E | 0.0 | None | False | True | 
| sagemaker | ml.g4dn.12xlarge for endpoint usage | L-07BEB181 | 1.0 | None | False | True | 
| sagemaker | ml.m5.24xlarge for training job usage | L-56C564CA | 3.0 | None | False | True | 
| sagemaker | Rate of ListModels requests | L-254EBA2C | 2.0 | None | False | False | 
| sagemaker | ml.g5.16xlarge for training warm pool usage | L-F6B8A3A3 | 0.0 | None | False | True | 
| sagemaker | Studio KernelGateway Apps running on ml.m5.16xlarge instance | L-7E95878B | 2.0 | None | False | True | 
| sagemaker | ml.c4.xlarge for training job usage | L-85D4BAF3 | 30.0 | None | False | True | 
| sagemaker | ml.c5.2xlarge for training warm pool usage | L-0D58D77C | 0.0 | None | False | True | 
| sagemaker | ml.m6g.12xlarge for endpoint usage | L-9D10CA98 | 2.0 | None | False | True | 
| sagemaker | ml.trn1.32xlarge for training warm pool usage | L-36F422F7 | 0.0 | None | False | True | 
| sagemaker | ml.r6g.large for endpoint usage | L-D7FE33BF | 4.0 | None | False | True | 
| sagemaker | ml.m4.2xlarge for spot training job usage | L-FE159C34 | 20.0 | None | False | True | 
| sagemaker | RSessionGateway Apps running on ml.m5.8xlarge instance | L-2BEE7665 | 2.0 | None | False | True | 
| sagemaker | RSessionGateway Apps running on ml.m5d.8xlarge instance | L-2D4C4A2D | 2.0 | None | False | True | 
| sagemaker | RSessionGateway Apps running on ml.m5.xlarge instance | L-8442D925 | 11.0 | None | False | True | 
| sagemaker | ml.c6gd.16xlarge for endpoint usage | L-018036DB | 1.0 | None | False | True | 
| sagemaker | ml.p4d.24xlarge for spot training job usage | L-09D56C4F | 0.0 | None | False | True | 
| sagemaker | ml.r5n.4xlarge for endpoint usage | L-3070F0B4 | 2.0 | None | False | True | 
| sagemaker | ml.c7g.4xlarge for endpoint usage | L-52FB7989 | 0.0 | None | False | True | 
| sagemaker | ml.c5n.xlarge for training warm pool usage | L-8A72B806 | 0.0 | None | False | True | 
| sagemaker | Studio KernelGateway Apps running on ml.r5.16xlarge instance | L-2524EF35 | 2.0 | None | False | True | 
| sagemaker | ml.p2.xlarge for training job usage | L-5585E645 | 1.0 | None | False | True | 
| sagemaker | ml.m5.12xlarge for training warm pool usage | L-34594662 | 0.0 | None | False | True | 
| sagemaker | Maximum number of parallel compilation jobs | L-F0067944 | 20.0 | None | False | True | 
| sagemaker | ml.c6i.24xlarge for endpoint usage | L-9A32E51C | 1.0 | None | False | True | 
| sagemaker | ml.g5.2xlarge for endpoint usage | L-9614C779 | 2.0 | None | False | True | 
| sagemaker | ml.r5d.xlarge for endpoint usage | L-37CA4776 | 4.0 | None | False | True | 
| sagemaker | ml.p3.8xlarge for transform job usage | L-F93088C1 | 0.0 | None | False | True | 
| sagemaker | Maximum dataset size AutoML job can be run on | L-A663541C | 100.0 | None | False | False | 
| sagemaker | Rate of ListNotebookInstanceLifecycleConfigs requests | L-A3AA2757 | 2.0 | None | False | False | 
| sagemaker | ml.m5.large for processing job usage | L-8541302D | 16.0 | None | False | True | 
| sagemaker | ml.r5.8xlarge for notebook instance usage | L-DAE78A2A | 4.0 | None | False | True | 
| sagemaker | ml.g4dn.16xlarge for transform job usage | L-D79647DB | 0.0 | None | False | True | 
| sagemaker | ml.g5.xlarge for training warm pool usage | L-8E6F4665 | 0.0 | None | False | True | 
| sagemaker | ml.c5.9xlarge for training job usage | L-2BE095E2 | 8.0 | None | False | True | 
| sagemaker | Studio KernelGateway Apps running on ml.r5.24xlarge instance | L-7FFAF4CB | 2.0 | None | False | True | 
| sagemaker | ml.m5d.16xlarge for notebook instance usage | L-26EB4EC7 | 2.0 | None | False | True | 
| sagemaker | Maximum number of training jobs that each hyperparameter tuning job can create | L-EAC49F53 | 500.0 | None | False | False | 
| sagemaker | ml.c6i.2xlarge for endpoint usage | L-4FDB33AC | 4.0 | None | False | True | 
| sagemaker | ml.m4.16xlarge for training job usage | L-D7CE983F | 8.0 | None | False | True | 
| sagemaker | ml.m5.4xlarge for transform job usage | L-3E1C9273 | 2.0 | None | False | True | 
| sagemaker | RSessionGateway Apps running on ml.g4dn.8xlarge instance | L-A9165189 | 0.0 | None | False | True | 
| sagemaker | ml.g4dn.2xlarge for endpoint usage | L-EA346344 | 2.0 | None | False | True | 
| sagemaker | ml.t2.xlarge for notebook instance usage | L-9EFE4FAD | 30.0 | None | False | True | 
| sagemaker | ml.m5dn.large for endpoint usage | L-7597F90B | 16.0 | None | False | True | 
| sagemaker | ml.r6g.8xlarge for endpoint usage | L-BB73F76A | 1.0 | None | False | True | 
| sagemaker | ml.r5d.16xlarge for endpoint usage | L-CC329F7E | 0.0 | None | False | True | 
| sagemaker | ml.p2.16xlarge for endpoint usage | L-B638D452 | 0.0 | None | False | True | 
| sagemaker | Studio KernelGateway Apps running on ml.t3.medium instance | L-EAC6F82B | 30.0 | None | False | True | 
| sagemaker | ml.p3dn.24xlarge for training warm pool usage | L-D27958C4 | 0.0 | None | False | True | 
| sagemaker | RSessionGateway Apps running on ml.m5.24xlarge instance | L-B7EB1FFD | 2.0 | None | False | True | 
| sagemaker | ml.c7g.16xlarge for endpoint usage | L-A7E8B111 | 0.0 | None | False | True | 
| sagemaker | ml.r5.4xlarge for endpoint usage | L-DD362E80 | 2.0 | None | False | True | 
| sagemaker | ml.c5d.9xlarge for endpoint usage | L-50755EC1 | 1.0 | None | False | True | 
| sagemaker | ml.m5n.12xlarge for endpoint usage | L-DEF2CD40 | 2.0 | None | False | True | 
| sagemaker | ml.c5n.18xlarge for endpoint usage | L-14AB3D09 | 1.0 | None | False | True | 
| sagemaker | Studio KernelGateway Apps running on ml.c5.4xlarge instance | L-6C5791AF | 4.0 | None | False | True | 
| sagemaker | ml.g5.16xlarge for notebook instance usage | L-001EDCEF | 5.0 | None | False | True | 
| sagemaker | ml.c4.2xlarge for spot training job usage | L-978CD7EC | 20.0 | None | False | True | 
| sagemaker | Studio KernelGateway Apps running on ml.c5.large instance | L-1476E09A | 11.0 | None | False | True | 
| sagemaker | Studio KernelGateway Apps running on ml.m5d.4xlarge instance | L-9F3B1F91 | 6.0 | None | False | True | 
| sagemaker | ml.g4dn.2xlarge for spot training job usage | L-0496610F | 1.0 | None | False | True | 
| sagemaker | ml.trn1.2xlarge for spot training job usage | L-AA22B8B9 | 0.0 | None | False | True | 
| sagemaker | Rate of DescribeNotebookInstanceLifecycleConfig requests | L-B1CE7499 | 5.0 | None | False | False | 
| sagemaker | ml.r5n.24xlarge for endpoint usage | L-944A1241 | 0.0 | None | False | True | 
| sagemaker | RSessionGateway Apps running on ml.p4d.24xlarge instance | L-DCCEDB7D | 0.0 | None | False | True | 
| sagemaker | ml.c6gn.xlarge for endpoint usage | L-754870FD | 0.0 | None | False | True | 
| sagemaker | Maximum number of Studio user profiles per domain | L-AC46C40F | 60.0 | None | False | True | 
| sagemaker | ml.c5.xlarge for training warm pool usage | L-F978BE20 | 0.0 | None | False | True | 
| sagemaker | Maximum number of instances per processing job | L-A5D63399 | 20.0 | None | False | False | 
| sagemaker | Total domains | L-B683BCB0 | 2.0 | None | False | True | 
| sagemaker | Studio KernelGateway Apps running on ml.g4dn.8xlarge instance | L-D267F635 | 0.0 | None | False | True | 
| sagemaker | ml.m5.2xlarge for training job usage | L-AD0A282D | 30.0 | None | False | True | 
| sagemaker | Rate of ListTrainingJobs requests | L-DE587792 | 2.0 | None | False | False | 
| sagemaker | ml.c4.xlarge for endpoint usage | L-F8C60E1D | 8.0 | None | False | True | 
| sagemaker | ml.p2.8xlarge for processing job usage | L-CA14F686 | 0.0 | None | False | True | 
| sagemaker | ml.r6gd.16xlarge for endpoint usage | L-6995701D | 0.0 | None | False | True | 
| sagemaker | ml.c6gn.16xlarge for endpoint usage | L-E9BB87E2 | 1.0 | None | False | True | 
| sagemaker | ml.c5n.9xlarge for training warm pool usage | L-FDD19E2A | 0.0 | None | False | True | 
| sagemaker | Studio KernelGateway Apps running on ml.r5.4xlarge instance | L-D5D3B1E5 | 2.0 | None | False | True | 
| sagemaker | ml.m4.4xlarge for spot training job usage | L-D7D166A0 | 10.0 | None | False | True | 
| sagemaker | ml.m5n.16xlarge for endpoint usage | L-2B921E27 | 2.0 | None | False | True | 
| sagemaker | ml.m4.10xlarge for notebook instance usage | L-CEEF9A6E | 8.0 | None | False | True | 
| sagemaker | RSessionGateway Apps running on ml.r5.8xlarge instance | L-F49350C0 | 2.0 | None | False | True | 
| sagemaker | RSessionGateway Apps running on ml.m5d.xlarge instance | L-A3C7A675 | 11.0 | None | False | True | 
| sagemaker | ml.g5.48xlarge for spot training job usage | L-C87FF004 | 0.0 | None | False | True | 
| sagemaker | ml.c5.2xlarge for transform job usage | L-9215A13F | 8.0 | None | False | True | 
| sagemaker | ml.r5.24xlarge for endpoint usage | L-B03C553E | 0.0 | None | False | True | 
| sagemaker | ml.m5d.large for endpoint usage | L-98F45D48 | 16.0 | None | False | True | 
| sagemaker | Rate of UpdateEndpoint requests | L-E6623D00 | 1.0 | None | False | False | 
| sagemaker | RStudioServerPro Apps running on ml.c5.4xlarge instances | L-FEC35D99 | 1.0 | None | False | True | 
| sagemaker | ml.m4.10xlarge for training job usage | L-D35E48B2 | 8.0 | None | False | True | 
| sagemaker | ml.p2.xlarge for endpoint usage | L-FD469689 | 2.0 | None | False | True | 
| sagemaker | ml.m4.2xlarge for endpoint usage | L-6198DF25 | 16.0 | None | False | True | 
| sagemaker | ml.p3.8xlarge for training job usage | L-558F1246 | 0.0 | None | False | True | 
| sagemaker | ml.m5.12xlarge for endpoint usage | L-A9F2A8B3 | 2.0 | None | False | True | 
| sagemaker | ml.c4.4xlarge for training warm pool usage | L-FBB7E9CB | 0.0 | None | False | True | 
| sagemaker | ml.c5n.4xlarge for endpoint usage | L-2693C7B9 | 2.0 | None | False | True | 
| sagemaker | ml.m5.xlarge for spot training job usage | L-4CEE6BA6 | 20.0 | None | False | True | 
| sagemaker | ml.p3.16xlarge for spot training job usage | L-D58A90BB | 0.0 | None | False | True | 
| sagemaker | ml.p3.2xlarge for spot training job usage | L-2D4C6493 | 1.0 | None | False | True | 
| sagemaker | ml.g4dn.8xlarge for notebook instance usage | L-C2F8103D | 2.0 | None | False | True | 
| sagemaker | Rate of UpdateNotebookInstance requests | L-A29549DE | 1.0 | None | False | False | 
| sagemaker | Maximum number of concurrent AutoML Jobs | L-CFC2D5B6 | 4.0 | None | False | True | 
| sagemaker | Maximum number of Studio spaces per domain | L-8E5333B4 | 2.0 | None | False | True | 
| sagemaker | ml.c6gd.xlarge for endpoint usage | L-EDFF07E7 | 8.0 | None | False | True | 
| sagemaker | ml.m5.4xlarge for notebook instance usage | L-862C1E14 | 6.0 | None | False | True | 
| sagemaker | ml.g5.48xlarge for training warm pool usage | L-7D217E5D | 0.0 | None | False | True | 
| sagemaker | ml.r6g.16xlarge for endpoint usage | L-42EAE6FA | 0.0 | None | False | True | 
| sagemaker | ml.m5.16xlarge for endpoint usage | L-54462FCC | 2.0 | None | False | True | 
| sagemaker | Rate of DescribeTransformJob requests | L-5FDD3816 | 5.0 | None | False | False | 
| sagemaker | ml.c5.4xlarge for notebook instance usage | L-96B75525 | 4.0 | None | False | True | 
| sagemaker | RSessionGateway Apps running on ml.c5.xlarge instance | L-F3F4F82A | 11.0 | None | False | True | 
| sagemaker | ml.c5n.4xlarge for training warm pool usage | L-4A423436 | 0.0 | None | False | True | 
| sagemaker | ml.g4dn.16xlarge for training job usage | L-57998C77 | 1.0 | None | False | True | 
| sagemaker | ml.g4dn.xlarge for processing job usage | L-2F1EB012 | 0.0 | None | False | True | 
| sagemaker | ml.t3.2xlarge for notebook instance usage | L-FB715320 | 30.0 | None | False | True | 
| sagemaker | RSessionGateway Apps running on ml.p3.8xlarge instance | L-73887D5F | 0.0 | None | False | True | 
| sagemaker | ml.g4dn.8xlarge for training job usage | L-3118B7E1 | 1.0 | None | False | True | 
| sagemaker | Rate of DescribeStudioLifecycleConfig requests | L-9D3B2C53 | 5.0 | None | False | False | 
| schemas | Registries | L-85663EFB | 10.0 | None | False | True | 
| schemas | SchemaVersions | L-3C443A2A | 100.0 | None | False | True | 
| schemas | Schemas | L-EE9E5FA9 | 100.0 | None | False | True | 
| schemas | DiscoveredSchemas | L-1738102F | 200.0 | None | False | True | 
| schemas | Discoverers | L-037FC7C4 | 10.0 | None | False | True | 
| servicecatalog | Service actions per region | L-BEE0DD19 | 200.0 | None | False | False | 
| servicecatalog | Service action associations per provisioning artifact | L-58FC5582 | 25.0 | None | False | False | 
| servicecatalog | Products per portfolio | L-AB79E48B | 150.0 | None | False | True | 
| servicecatalog | Applications per attribute group | L-223F4C54 | 1000.0 | None | False | True | 
| servicecatalog | Product versions per product | L-A5846085 | 100.0 | None | False | True | 
| servicecatalog | Products per region | L-764CF6A1 | 350.0 | None | False | True | 
| servicecatalog | Shared accounts per portfolio | L-A2FB1BD2 | 5000.0 | None | False | False | 
| servicecatalog | Tags per product | L-CC0BF186 | 20.0 | None | False | False | 
| servicecatalog | Attribute groups per region | L-1639038A | 2000.0 | None | False | True | 
| servicecatalog | Users groups and roles per portfolio | L-E8959660 | 100.0 | None | False | True | 
| servicecatalog | Tags per portfolio | L-77FEF8C5 | 20.0 | None | False | False | 
| servicecatalog | Applications per region | L-7C3CEC2B | 2000.0 | None | False | True | 
| servicecatalog | Portfolios per region | L-C6458716 | 100.0 | None | False | True | 
| servicecatalog | Attribute groups per application | L-C533FF9A | 1000.0 | None | False | True | 
| servicecatalog | Users groups and roles per product | L-3BC91705 | 200.0 | None | False | True | 
| servicecatalog | Resources per application | L-360CDF2E | 1000.0 | None | False | True | 
| servicecatalog | Tags per provisioned product | L-2B360974 | 50.0 | None | False | False | 
| servicequotas | Active requests per quota | L-36BDD542 | 1.0 | None | False | False | 
| servicequotas | Throttle rate for ListAWSDefaultServiceQuotas | L-71DCD22A | 10.0 | None | False | False | 
| servicequotas | Throttle rate for GetRequestedServiceQuotaChange | L-027D2B0A | 5.0 | None | False | False | 
| servicequotas | Throttle rate for ListRequestedServiceQuotaChangeHistoryByQuota | L-0E18483E | 5.0 | None | False | False | 
| servicequotas | Throttle rate for ListServiceQuotas | L-65470577 | 10.0 | None | False | False | 
| servicequotas | Throttle rate for GetServiceQuota | L-09C84CC6 | 5.0 | None | False | False | 
| servicequotas | Throttle rate for GetAWSDefaultServiceQuota | L-A53F603E | 5.0 | None | False | False | 
| servicequotas | Throttle rate for ListRequestedServiceQuotaChangeHistory | L-C7624166 | 5.0 | None | False | False | 
| servicequotas | Throttle rate for RequestServiceQuotaIncrease | L-61010047 | 3.0 | None | False | False | 
| servicequotas | Throttle rate for ListServices | L-E3924FE5 | 10.0 | None | False | False | 
| servicequotas | Throttle rate for UntagResource | L-BF40C7E2 | 10.0 | None | False | False | 
| servicequotas | Throttle rate for ListTagsForResource | L-6120A68B | 10.0 | None | False | False | 
| servicequotas | Throttle rate for TagResource | L-86127B31 | 10.0 | None | False | False | 
| ses | Sending rate | L-CDEF9B6B | 14.0 | None | False | True | 
| ses | Sending quota | L-804C8AE8 | 50000.0 | None | False | True | 
| sms | Duration of service usage per VM in days | L-3290AB9E | 90.0 | None | False | True | 
| sms | Concurrent VM migrations | L-AFABDADD | 50.0 | None | False | True | 
| sns | CreatePlatformApplication Transactions per Second | L-4738DDCE | 900.0 | None | False | True | 
| sns | ConfirmSubscription Transactions per Second | L-FF07E5EA | 900.0 | None | False | True | 
| sns | ListSubscriptionsByTopic Transactions per Second | L-390AADBE | 30.0 | None | False | False | 
| sns | SetSubscriptionAttributes Transactions per Second | L-B6107771 | 900.0 | None | False | True | 
| sns | Pending Subscriptions per Account | L-1A43D3DB | 5000.0 | None | False | True | 
| sns | GetSubscriptionAttributes Transactions per Second | L-876E1222 | 900.0 | None | False | True | 
| sns | SetSMSAttributes Transactions per Second | L-154ECCA7 | 1.0 | None | False | False | 
| sns | CreateTopic Transactions per Second | L-AB928142 | 900.0 | None | False | True | 
| sns | Messages Published per Second | L-F8E2BA85 | 9000.0 | None | False | True | 
| sns | Unsubscribe Transactions per Second | L-93308085 | 100.0 | None | False | False | 
| sns | SetEndpointAttributes Transactions per Second | L-4EE37BC0 | 900.0 | None | False | True | 
| sns | DeleteTopic Transactions per Second | L-B98ECD3E | 900.0 | None | False | True | 
| sns | VerifySMSSandboxPhoneNumber Transactions per Second | L-B3509C67 | 1.0 | None | False | False | 
| sns | CreatePlatformEndpoint Transactions per Second | L-E1E48E53 | 900.0 | None | False | True | 
| sns | OptInPhoneNumber Transactions per Second | L-856966E8 | 20.0 | None | False | False | 
| sns | GetPlatformApplicationAttributes Transactions per Second | L-F35E8445 | 900.0 | None | False | True | 
| sns | Topics per Account | L-61103206 | 100000.0 | None | False | True | 
| sns | Subscribe Transactions per Second | L-BBD4D2FF | 100.0 | None | False | False | 
| sns | ListTagsForResource Transactions per Second | L-93CEC191 | 10.0 | None | False | False | 
| sns | RemovePermission Transactions per Second | L-6A04D1EB | 10.0 | None | False | False | 
| sns | ListPlatformApplications Transactions per Second | L-41B81227 | 15.0 | None | False | False | 
| sns | ListEndpointsByPlatformApplication Transactions per Second | L-4659BFC2 | 30.0 | None | False | False | 
| sns | GetEndpointAttributes Transactions per Second | L-038DA0E0 | 900.0 | None | False | True | 
| sns | Filter Policies per Account | L-4126E74A | 10000.0 | None | False | True | 
| sns | SetTopicAttributes Transactions per Second | L-F514C636 | 900.0 | None | False | True | 
| sns | ListOriginationNumbers Transactions per Second | L-6521CF3A | 1.0 | None | False | False | 
| sns | ListTopics Transactions per Second | L-039289D5 | 30.0 | None | False | False | 
| sns | SetPlatformApplicationAttributes Transactions per Second | L-A228E0EB | 900.0 | None | False | True | 
| sns | Filter Policies per Topic | L-B96EDA7D | 200.0 | None | False | True | 
| sns | AddPermission Transactions per Second | L-A05852B7 | 10.0 | None | False | False | 
| sns | ListSMSSandboxPhoneNumbers Transactions per Second | L-C1E19420 | 1.0 | None | False | False | 
| sns | CreateSMSSandboxPhoneNumber Transactions per Second | L-7B7E3FB8 | 1.0 | None | False | False | 
| sns | GetTopicAttributes Transactions per Second | L-820458B0 | 900.0 | None | False | True | 
| sns | GetSMSSandboxAccountStatus Transactions per Second | L-2EE2434F | 10.0 | None | False | False | 
| sns | TagResource Transactions per Second | L-BF824DE9 | 10.0 | None | False | False | 
| sns | DeleteEndpoint Transactions per Second | L-2FE42A3E | 900.0 | None | False | True | 
| sns | ListPhoneNumbersOptedOut Transactions per Second | L-19F66BE5 | 10.0 | None | False | False | 
| sns | CheckIfPhoneNumberIsOptedOut Transactions per Second | L-01EACE54 | 50.0 | None | False | False | 
| sns | DeleteSMSSandboxPhoneNumber Transactions per Second | L-F6A3071A | 1.0 | None | False | False | 
| sns | ListSubscriptions Transactions per Second | L-21C7FFA6 | 30.0 | None | False | False | 
| sns | UntagResource Transactions per Second | L-A30AD1BE | 10.0 | None | False | False | 
| sns | Subscriptions per Topic | L-A4340BCD | 12500000.0 | None | False | False | 
| sns | GetSMSAttributes Transactions per Second | L-9A72FF33 | 20.0 | None | False | False | 
| sns | DeletePlatformApplication Transactions per Second | L-9D5EC8F7 | 900.0 | None | False | True | 
| ssm | Additional Automation executions that can be queued | L-67DAE0B3 | 5000.0 | None | False | True | 
| ssm | Targets per Maintenance Window | L-B1A84B8B | 100.0 | None | False | True | 
| ssm | Maintenance Windows | L-7727CE5B | 50.0 | None | False | True | 
| ssm | Maintenance Window execution history retention | L-00E10A78 | 30.0 | None | False | False | 
| ssm | Patch groups per patch baseline | L-F4012070 | 25.0 | None | False | True | 
| ssm | Concurrently executing rate control automation | L-44746CFE | 25.0 | None | False | True | 
| ssm | Target groups per Maintenance Window target or task | L-038D7E0A | 5.0 | None | False | False | 
| ssm | Instances per target | L-F03CADDF | 50.0 | None | False | False | 
| ssm | Patch baselines | L-218CDBD4 | 50.0 | None | False | True | 
| ssm | Single Maintenance Window concurrent executions | L-22ADA421 | 1.0 | None | False | False | 
| ssm | Concurrently executing Automations | L-09101E66 | 100.0 | None | False | True | 
| ssm | Number of levels of nested automation | L-BDECE436 | 5.0 | None | False | False | 
| ssm | Tasks per Maintenance Window | L-3D9CCA6E | 20.0 | None | False | True | 
| ssm | Additional rate control automation executions that can be queued | L-CE4D78FF | 1000.0 | None | False | True | 
| ssm | Maintenance Window concurrent executions | L-26BF3FE6 | 5.0 | None | False | True | 
| ssm-contacts | ListEngagements API throttle quota | L-8F6873DD | 2.0 | None | False | True | 
| ssm-contacts | Contact channels per stage | L-F338226A | 10.0 | None | False | True | 
| ssm-contacts | ListPagesByEngagement API throttle quota | L-70D46058 | 2.0 | None | False | True | 
| ssm-contacts | Voice engagement throttle quota | L-28BF1B5E | 0.01 | None | False | False | 
| ssm-contacts | AcceptPage API throttle quota | L-D35B01ED | 20.0 | None | False | True | 
| ssm-contacts | SMS engagement throttle quota | L-73C3F2C3 | 0.05 | None | False | False | 
| ssm-contacts | StartEngagement API throttle quota | L-254D300C | 20.0 | None | False | True | 
| ssm-contacts | DescribeEngagement API throttle quota | L-0C2999E2 | 5.0 | None | False | True | 
| ssm-contacts | StopEngagement API throttle quota | L-F890E288 | 10.0 | None | False | True | 
| ssm-contacts | ListPagesByContact API throttle quota | L-05EEDCEB | 1.0 | None | False | True | 
| ssm-contacts | DescribePage API throttle quota | L-977ABCD7 | 5.0 | None | False | True | 
| ssm-contacts | Contacts per account | L-7DD2017D | 1000.0 | None | False | True | 
| ssm-contacts | All other operations API throttle quota | L-53EDA07E | 20.0 | None | False | True | 
| ssm-contacts | ListPageReceipts API throttle quota | L-E25E885A | 1.0 | None | False | True | 
| ssm-contacts | Stages per plan | L-5AE11799 | 5.0 | None | False | False | 
| ssm-contacts | Email engagement throttle quota | L-F3345603 | 0.05 | None | False | False | 
| ssm-guiconnect | Concurrent Remote Desktop connections | L-64419857 | 5.0 | None | False | True | 
| ssm-sap | Databases per component | L-5B34AA09 | 20.0 | None | False | True | 
| ssm-sap | SAP applications per Region in account | L-C8103580 | 10.0 | None | False | True | 
| ssm-sap | Components per SAP application | L-458E2EE3 | 5.0 | None | False | True | 
| textract | StartDocumentTextDetection throttle limit in transactions per second | L-AE9E2453 | 15.0 | None | False | True | 
| textract | StartDocumentAnalysis throttle limit in transactions per second | L-5E3A5D59 | 10.0 | None | False | True | 
| textract | AnalyzeExpense throttle limit in transactions per second | L-80A81B07 | 5.0 | None | False | True | 
| textract | StartExpenseAnalysis throttle limit in transactions per second | L-E31D91C2 | 5.0 | None | False | True | 
| textract | DetectDocumentText throttle limit in transactions per second | L-75788A8B | 25.0 | None | False | True | 
| textract | GetExpenseAnalysis throttle limit in transactions per second | L-FA2C35B5 | 5.0 | None | False | True | 
| textract | Async DocumentAnalysis throttle limit for max number of concurrent jobs | L-5CF3B0DF | 600.0 | None | False | True | 
| textract | AnalyzeID throttle limit in transactions per second | L-7C2E8C8C | 5.0 | None | False | True | 
| textract | Async ExpenseAnalysis throttle limit for max number of concurrent jobs | L-25F2C897 | 600.0 | None | False | True | 
| textract | Async DocumentTextDetection throttle limit for max number of concurrent jobs | L-5B33D1C3 | 600.0 | None | False | True | 
| textract | AnalyzeDocument throttle limit in transactions per second | L-B83AD6FF | 10.0 | None | False | True | 
| textract | GetDocumentAnalysis throttle limit in transactions per second | L-9ACAE5E4 | 10.0 | None | False | True | 
| textract | GetDocumentTextDetection throttle limit in transactions per second | L-94C8FE3F | 25.0 | None | False | True | 
| vpc | VPCs per Region | L-F678F1CE | 20.0 | None | False | True | 
| vpc | Egress-only internet gateways per Region | L-45FE3B85 | 20.0 | None | False | True | 
| vpc | VPC peering connection request expiry hours | L-8312C5BB | 168.0 | None | False | False | 
| vpc | Internet gateways per Region | L-A4707A72 | 20.0 | None | False | True | 
| vpc | VPC security groups per Region | L-E79EC296 | 2500.0 | None | False | True | 
| vpc | Network interfaces per Region | L-DF5E4CA3 | 5000.0 | None | False | True | 
| vpc | Gateway VPC endpoints per Region | L-1B52E74A | 20.0 | None | False | True | 
| vpc | Active VPC peering connections per VPC | L-7E9ECCDB | 50.0 | None | False | True | 
| vpc | Subnets per VPC | L-407747CB | 200.0 | None | False | True | 
| vpc | NAT gateways per Availability Zone | L-FE5A380F | 5.0 | None | False | True | 
| vpc | Subnets that can be shared with an account | L-44499CD2 | 100.0 | None | False | True | 
| vpc | IPv4 CIDR blocks per VPC | L-83CA0A9D | 5.0 | None | False | True | 
| vpc | Security groups per network interface | L-2AFB9258 | 5.0 | None | False | True | 
| vpc | Route tables per VPC | L-589F43AA | 200.0 | None | False | True | 
| vpc | Interface VPC endpoints per VPC | L-29B6F2EB | 50.0 | None | False | True | 
| vpc | Routes per route table | L-93826ACB | 50.0 | None | False | True | 
| vpc | Inbound or outbound rules per security group | L-0EA8095F | 200.0 | None | False | True | 
| vpc | Rules per network ACL | L-2AEEBF1A | 20.0 | None | False | True | 
| vpc | Participant accounts per VPC | L-2C462E13 | 100.0 | None | False | True | 
| vpc | Network ACLs per VPC | L-B4A6D682 | 200.0 | None | False | True | 
| vpc | Outstanding VPC peering connection requests | L-DC9F7029 | 25.0 | None | False | True | 
| workspaces | Standby WorkSpaces | L-9A67B5CB | 0.0 | None | False | True | 
| workspaces | IP access control groups per directory | L-F61D0B79 | 25.0 | None | False | False | 
| workspaces | Graphics WorkSpaces | L-84611756 | 0.0 | None | False | True | 
| workspaces | GraphicsPro WorkSpaces | L-254B485B | 0.0 | None | False | True | 
| workspaces | Rules per IP access control group | L-5782CB4D | 10.0 | None | False | False | 
| workspaces | Directories | L-EEB759DE | 50.0 | None | False | False | 
| workspaces | WorkSpaces | L-34278094 | 200.0 | None | False | True | 
| workspaces | GraphicsPro.g4dn WorkSpaces | L-BE9A8466 | 0.0 | None | False | True | 
| workspaces | IP access control groups | L-0E312A12 | 100.0 | None | False | False | 
| workspaces | Bundles | L-843E43DA | 50.0 | None | False | False | 
| workspaces | Connection aliases | L-0798A2C9 | 20.0 | None | False | False | 
| workspaces | Images | L-18CE281C | 40.0 | None | False | True | 
| workspaces | Graphics.g4dn WorkSpaces | L-BCACAEBC | 0.0 | None | False | True | 
| workspaces-web | Number of BrowserSettings | L-36965BD1 | 3.0 | None | False | True | 
| workspaces-web | Number of Certificates per TrustStore | L-B30615E2 | 100.0 | None | False | True | 
| workspaces-web | Number of NetworkSettings | L-787608AB | 3.0 | None | False | True | 
| workspaces-web | Number of TrustStores | L-3A76276F | 3.0 | None | False | True | 
| workspaces-web | Number of Web Portals | L-149BA3AD | 1.0 | None | False | True | 
| workspaces-web | Number of IdentityProviders per Portal | L-DFC864EF | 1.0 | None | False | True | 
| workspaces-web | Number of UserAccessLoggingSettings | L-8BD59015 | 3.0 | None | False | True | 
| workspaces-web | Number of UserSettings | L-3A62D5A9 | 3.0 | None | False | True | 
```

\
