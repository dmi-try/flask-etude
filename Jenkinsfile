pipeline {
  agent any
  stages {
    stage('run tests') {
      steps {
        sh 'tox'
      }
    }
    stage('publish image') {
      steps {
        script {
          def image = docker.build("flask-dev:${env.BUILD_ID}")
          image.push()
        }
      }
    }
    stage('some debug') {
      steps {
        sh 'set'
      }
    }
  }
}
