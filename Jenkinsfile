#!groovy
 
node('build') {
  stage('Checkout Source') {
    checkout scm
  }
  stage("Lint test") {
    echo "Custom testing"
    sh "pylint -E test.py"
  }
}

