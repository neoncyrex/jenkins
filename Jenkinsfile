#!groovy
 
node('build') {
  stage('Checkout Source') {
    checkout scm
  }
  stage("Lint test") {
    echo "Custom testing"
    input "Run custom testingn?"
    sh "true"
  }
  stage("Neon testing") {
    echo "Neon testing"
    sh "true"
  }
}

