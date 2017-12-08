pipeline {
  agent {
    docker {
      image 'ubuntu'
    }
    
  }
  stages {
    stage('ls') {
      steps {
        sh '''pwd
ls -la
id
uname -a'''
      }
    }
  }
}