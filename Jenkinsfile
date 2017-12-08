pipeline {
  agent {
    docker {
      image 'ubuntu'
    }
    
  }
  stages {
    stage('run tests') {
      steps {
        sh 'tox'
      }
    }
  }
}