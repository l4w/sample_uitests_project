node {
   checkout scm

    try {
        stage('clearing the environment') {
            sh 'rm -rf screenshot/*'
            sh 'rm -rf logs/*'
        }
        stage('installing packages') {
            sh 'pipenv install'
        }
        stage('running tests') {
            sh 'pipenv run pytest tests -n=4'
        }
    }
    finally {
        archiveArtifacts allowEmptyArchive: true, artifacts: 'screenshot/**/*.png'
        archiveArtifacts allowEmptyArchive: true, artifacts: 'logs/**/*.log'
    }
}