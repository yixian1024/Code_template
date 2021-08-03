pipeline {
    agent{
        label 'centos8'
    }
    stages {
        stage('Setup environment') {
            steps {
                sh """
                    yum install git -y
                    yum install wget -y
                    yum install squashfs-tools -y
                    yum install mkisofs -y
                    yum install python3 -y
        			python3 --version
        			pip3 install wget
        			pip3 install shortuuid
        			pip3 install pyyaml
        			pip3 list
		        """
            }
        }
        stage('Pull from Gitlab') {
            steps {
                git branch: 'master',
                    credentialsId: 'gitlab',
                    url: 'http://10.102.49.26:8098/ironman/quick_assemble_kit.git'
                    
            }
        }
        stage('Build Quick Assemble Kit') {
            steps {
                sh "python3 bundle_manager.py"
            }
        }
        stage('Return') {
            steps {
                archiveArtifacts artifacts: '*.iso' 
            }
        }
    }
}