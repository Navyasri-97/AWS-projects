Use the commands


Install Using Fargate
               
                eksctl create cluster --name demo-cluster --region us-east-1 --fargate

Delete the Cluster
              
                eksctl delete cluster --name demo-cluster --region us-east-1

To install eksctl 

Create file nano eksctl.sh and save the following commands

              # for ARM systems, set ARCH to: `arm64`, `armv6` or `armv7`
              ARCH=amd64
              PLATFORM=$(uname -s)_$ARCH

              curl -sLO "https://github.com/eksctl-io/eksctl/releases/latest/download/eksctl_$PLATFORM.tar.gz"

              # (Optional) Verify checksum
              curl -sL "https://github.com/eksctl-io/eksctl/releases/latest/download/eksctl_checksums.txt" | grep $PLATFORM | sha256sum --check

              tar -xzf eksctl_$PLATFORM.tar.gz -C /tmp && rm eksctl_$PLATFORM.tar.gz

              sudo mv /tmp/eksctl /usr/local/bin

  Then, run chmod +x eksctl.sh and sudo sh eksctl.sh
