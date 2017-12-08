pipeline {
  agent {
    docker {
      image 'ubuntu'
    }
    
  }
  stages {
    stage('prepare env') {
      steps {
        sh 'sudo apt-get install tox'
      }
    }
    stage('run tests') {
      steps {
        sh 'tox'
      }
    }
  }
}