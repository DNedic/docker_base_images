# AWS Command Line Interface Docker Image ([Dockerfile](Dockerfile))
[![](https://images.microbadger.com/badges/image/vladgh/awscli.svg)](https://microbadger.com/images/vladgh/awscli "Get your own image badge on microbadger.com")
[![](https://images.microbadger.com/badges/version/vladgh/awscli.svg)](https://microbadger.com/images/vladgh/awscli "Get your own version badge on microbadger.com")
[![](https://images.microbadger.com/badges/commit/vladgh/awscli.svg)](https://microbadger.com/images/vladgh/awscli "Get your own commit badge on microbadger.com")
[![](https://images.microbadger.com/badges/license/vladgh/awscli.svg)](https://microbadger.com/images/vladgh/awscli "Get your own license badge on microbadger.com")

## **⚠️ This project is no longer supported!**

Docker image with the AWS Command Line Interface installed.

Optional variables :
- `AWS_ACCESS_KEY_ID` (or functional IAM profile)
- `AWS_SECRET_ACCESS_KEY` (or functional IAM profile)
- `AWS_DEFAULT_REGION` (defaults to 'us-east-1')

## Run command examples:

- Simple
```
docker run -it \
  -e AWS_ACCESS_KEY_ID=1234 \
  -e AWS_SECRET_ACCESS_KEY=5678 \
  -e AWS_DEFAULT_REGION=us-west-2 \
  vladgh/awscli
```

- Provide the .aws config folder
```
docker run -it \
  -v ~/.aws:/root/.aws \
  vladgh/awscli
```

- Describe an EC2 instance
```
docker run \
  -e AWS_ACCESS_KEY_ID=1234 \
  -e AWS_SECRET_ACCESS_KEY=5678 \
  -e AWS_DEFAULT_REGION=us-west-2 \
  vladgh/awscli \
  aws ec2 describe-instances --instance-ids i-1234
```

## AWS Command Line Reference
http://docs.aws.amazon.com/cli/latest/reference/
