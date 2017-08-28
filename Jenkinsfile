#!groovy
 
node('build') {
  stage('Checkout Source') {
    checkout scm
  }
  stage("Lint test") {
    echo "Running lint application testing"
    sh "pylint -E test.py"
  }
  stage("Unit test") {
    echo "Running unit tests"
    sh "pytest"
  }
}

