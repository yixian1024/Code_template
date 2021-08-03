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
                    yum install python3 -y
        			python3 --version
        			pip3 install pyyaml
				pip3 install git
        			pip3 list
		        """
            }
        }
        stage('Pull from Gitlab') {
            steps {
                git branch: 'master',
                    credentialsId: 'gitlab',
                    url: 'http://localhost/code_template.git'
                    
            }
        }
        stage('Build Quick Assemble Kit') {
            steps {
                sh "python3 main.py"
            }
        }
        stage('Return') {
            steps {
                archiveArtifacts artifacts: 'text.txt' 
            }
        }
    }
}
