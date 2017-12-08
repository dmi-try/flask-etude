pipeline {
  agent any
  stages {
    stage('run tests') {
      steps {
        sh 'tox'
      }
    }
    stage('build image') {
      steps {
        def image = docker.build("flask-dev:${env.BUILD_ID}")
      }
    }
    stage('publish image') {
      steps {
        image.push()
      }
    }
  }
}
